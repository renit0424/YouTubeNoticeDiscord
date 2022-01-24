import time
import webbrowser
import datetime
import schedule
from googleapiclient.discovery import build
from discordwebhook import Discord
from config import youtube_api_key, channel_id ,webhookurl ,calltime

live_videos = []
live_videos2 = []
videoid = ""
b = ""
def get_live_videos():
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    search_response = youtube.search().list(
        part='id,snippet,brandingSettings',
        channelId=channel_id,
        maxResults='100',
        order='date',
        eventType="live",
        type='video',
    ).execute()
    totalResults = search_response.get("pageInfo").get("totalResults")
    if totalResults == 0:
        live_videos.append({"totalResults":totalResults})
    for video in search_response.get("items",[]):
        if video["snippet"].get("liveBroadcastContent") == "live":
            live_videos.append({"totalResults":totalResults,"live":video["snippet"].get("liveBroadcastContent"),"id":video["id"].get("videoId"),"title":video["snippet"].get("title"),"time":(datetime.datetime.strptime(video["snippet"].get("publishedAt"),"%Y-%m-%dT%H:%M:%SZ")+datetime.timedelta(hours=9))})
            videoid = video["id"].get("videoId")
    return live_videos
def liveStreaming():
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    search_response = youtube.videos().list(
        part='liveStreamingDetails,snippet',
        id=live_videos[0].get("id")
    ).execute()
    for video2 in search_response.get("items",[]):
        live_videos2.append({"starttime":(datetime.datetime.strptime(video2["liveStreamingDetails"].get("actualStartTime"),"%Y-%m-%dT%H:%M:%SZ")+datetime.timedelta(hours=9))})
    return live_videos2
def loop():
    a = ""
    dt = datetime.datetime.now()
    dt = datetime.datetime(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second)
    get_live_videos()
    if int(live_videos[0].get("totalResults")) == 0:
        print("ライブ配信がみつかりません")
    else:
        liveStreaming()
        if live_videos2[0].get("starttime") < dt:
            global b
            a = live_videos2[0]["starttime"].strftime('%Y-%m-%d %H:%M:%S')
            if a == b:
                return
            b = a
            print("ライブ配信を通知します。\n\t" + live_videos[0].get("title") + "\n\tライブ配信開始時間 " + live_videos2[0]["starttime"].strftime('%Y-%m-%d %H:%M:%S'))
            webhook_url = webhookurl
            discord = Discord(url=webhook_url)
            discord.post(
                content="ライブ配信中\n開始時間 "+live_videos2[0]["starttime"].strftime('%Y-%m-%d %H:%M:%S') +"\n"+live_videos[0].get("title") + "\n" + "https://www.youtube.com/watch?v="+ live_videos[0].get("id"),
                username="【ライブ配信通知】"+live_videos[0].get("channelTitle"),
                avatar_url="https://yt3.ggpht.com/IhCrx3NlPelAN_eXEXChNEgvIOI4NS6Q1ld2lzTYKCyv-FFks6vdmcfo5y0Co6cp8rGhZvS6ow=s88-c-k-c0x00ffffff-no-rj"
            )
            webbrowser.open("https://www.youtube.com/watch?v="+ live_videos[0].get("id"), new=1, autoraise=True)
        else:
            print("配信時間は過ぎてないです。")
schedule.every(calltime).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

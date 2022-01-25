# 【YouTube】YouTube Notice Discord
通称ようつべ配信開始通知Bot君(適当)

[YouTube](https://youtube.com/)で気になるあの子の配信開始通知をdiscordに投げてくれるプログラム。

言語はPythonで書いてます。

クッソ雑に作ってあるので手直ししたい人は勝手にしてください()
# 使い方
- google-api-python-clientを使用するのでインストール
```
pip install google-api-python-client
```

- 自動更新のために[schedule](https://github.com/dbader/schedule)を使うのでインストール
```
pip install schedule
```
# YouTube Data API v3でAPIを発行
  1.近いうちに記載します。
  
  2.後で使うので`ClientID`,`ClientSecret`をメモしておくか設定のconfig.pyに記載しておく。
# discordのWebhookURLを発行する。
  [こっから](https://support.discord.com/hc/ja/articles/228383668-%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB-Webhooks%E3%81%B8%E3%81%AE%E5%BA%8F%E7%AB%A0)サイト見ながら発行する。
# 設定
  config.pyにさっき取得したものたちを記載する。
  ```
#YouTubeAPIKey
youtube_api_key = '***'
#channelID
channel_id = '***'
#discord_webhookURL
webhookurl = 'https://discordapp.com/api/webhooks/***'
#呼び出す時間(分)
calltime = 20
  ```
あとはmain.pyを実行。
多分動く。

from requests_oauthlib import OAuth1Session
import urllib.request
import json


hinichi=input("東京の天気、今日なら0,明日なら1,明後日なら2と入力:")
twitter = OAuth1Session({TWITTER_SECRET},
{TWITTER_SECRET},
{TWITTER_SECRET},
{TWITTER_SECRET})

#東京の天気のjsonデータ取得
url="http://weather.livedoor.com/forecast/webservice/json/v1?city=130010"
response=urllib.request.urlopen(url)
content=json.loads(response.read().decode('utf8'))

if (hinichi is "0"):
  hinichikanji="今日"
elif(hinichi is "1"):
  hinichikanji="明日"
else:
  hinichikanji="明後日"

#投稿文作成
toukoubun='pythonからの投稿テスト:{0}の東京の天気は{1}です。'.format(hinichikanji,content["forecasts"][int(hinichi)]["telop"])
print(toukoubun)

#投稿
params={"status":toukoubun}
url2='https://api.twitter.com/1.1/statuses/update.json'
print(url2)
req = twitter.post(url2, params = params)

#成否確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)

# ツイッター投稿
from requests_oauthlib import OAuth1Session
import config
import random
import json
import os
import requests

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

year = random.randint(2006,2018)
with open('/virtual/hudosan/src/tokyo_tika_{0}.json'.format(str(year))) as f:
    d = json.load(f)
    targ = random.choice(d)
    
    while "BuildingYear" not in targ.keys():
        print("建築年が入っていない")
        targ = random.choice(d)

    tweet = "{}年 - 種類: {} 場所: {} 種別: {} 建築年: {} 取引価格: {} 面積: {}㎡ 1㎡価格: {}万円".format(year,targ["Type"],targ['Municipality']+targ['DistrictName'],
                                                                               targ["CityPlanning"]
                                                                               ,targ['BuildingYear'],
                                                                                str(int(targ['TradePrice'])/100000000)+'億円' if int(targ['TradePrice'])>100000000 else str(int(targ['TradePrice'])//10000)+"万円"
                                                                 ,targ["Area"], int(targ['TradePrice'])/int(targ["Area"])//10000)
    print(tweet)

url = "https://api.twitter.com/1.1/statuses/update.json"
params = {"status": tweet}

res = twitter.post(url,params=params)
if res.status_code == 200: #正常投稿出来た場合
    print("Success.")
else: #正常投稿出来なかった場合
    print("Failed. : %d"% res.status_code)

# fws
在FWS中自動創建子網域的機器人

# 設定

1. 修改`example_setting.json`為`setting.json`
2. 更改`setting.json`設定
 
- setting.json
```json
{
    "token":"", //機器人token

    "ip":"", //dns A記錄導向的ip
    "domains":{ //所有網域
        "hans0805.me":{
            "id":"", //該網域id(如圖)
            "key":"" //帳戶api key(如圖)
        },
        "dripweb.cf":{
            "id":"",
            "key":""
        }
    }
}
```

![圖一](https://raw.githubusercontent.com/HansHans135/fws/main/1.png)
<br>
![圖二](https://raw.githubusercontent.com/HansHans135/fws/main/2.png)
3. `bot.py`中第54行修改成紀錄頻道ID
4. 運行`bot.py`

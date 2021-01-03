from requests_oauthlib import OAuth1Session
import json
import datetime
import time

CK = '************************'
CS = '************************'
AT = '************************'
AS = '************************'
token=OAuth1Session(CK,CS,AT,AS)

get_DM_LIST = []

def get_DM(prmList):
    tmpList = prmList
    if tmpList == [] :
        pastList = [0, 0]
    else :
        pastList = tmpList
        tmpList = []
    tmpList.clear()
    params={("count",10)}
    getlist=token.get("https://api.twitter.com/1.1/direct_messages/events/list.json",params=params)
    dmlist=json.loads(getlist.text)

    for line in range(2):
        tmpId = dmlist['events'][line]['message_create']['sender_id']
        tmpText = dmlist['events'][line]['message_create']['message_data']['text']
        print(tmpId)
        print(tmpText)
        tmpList.append([tmpId, tmpText])
        #print("\n")
    # print(tmpList)
    # print(pastList)
    # print("mpList = " + tmpList[0][0])
    # print(tmpList)
    # print(pastList)
    if tmpList != pastList :
        #最後が自分からの送信ならTrueを返す
        if tmpList[0][0] == '******************' : #自分のrecipientIDに置き換える
            return True
        else :
            return tmpList[0] #tmpListとpastListが異なる
    else :
        return True #同じ

def send_DM(prmId, prmText) :
    payload = {"event":
                {"type": "message_create",
                    "message_create": {
                        "target": {"recipient_id": prmId },
                            "message_data": {"text": prmText}
                    }
                }
            }
    headers = {'content-type': 'application/json'}
    payload = json.dumps(payload)
    res = token.post('https://api.twitter.com/1.1/direct_messages/events/new.json', headers=headers, data=payload)
    # print("送信完了")

#引数にIDを指定してそのIDのtweetをcountの数だけ取得してリストの形で返す
def get_TL(prmName) :
    list_TL = []
    params ={
         'count'   : 200,        # 取得するtweet数
         'screen_name' : prmName,  # twitterアカウント名
    }
    req = token.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params = params)
    res = json.loads(req.text)
    for line in res:
        list_TL.append(line['text'])
    return list_TL

def make_Date(prmYear, prmMonth, prmDate) :
    try :
        d = datetime.date(prmYear, prmMonth, prmDate)
        return d
    except :
        return

#リストを受け取ると出力すべき形にして返す
def make_SendText(prmList) :
    s = ""
    for i in range(len(prmList)) :
        s += prmList[i] + "\n"
        print(s)
    return s


def main() :
    nowList = []
    while True :
        try :
            textList = []
            key = get_DM(nowList)
            print(key)
            if key != True :
                TL = get_TL(key[1])
                print(len(TL))
                for i in range(2010, 2030) :
                    for j in range(1, 13) :
                        for k in range(1, 32) :
                            for m in range(len(TL)) :
                                if (str(make_Date(i, j, k)) in TL[m]) == True :
                                    textList.append(TL[m])
                send_DM(key[0], make_SendText(textList))
                textList.clear()
        except Exception as e:
            # print("error")

        time.sleep(60)

main()

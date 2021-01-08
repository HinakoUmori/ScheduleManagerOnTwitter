# Schedule manager on Twitter

## Overview
Schedule manager on Twitter is program to collect tweet with yyyy-MM-dd. If you send twitterID without  "@"  as DM to account under this program, 
this program send collected tweet.

## Description
This program is needed to be executed always. This collect own DM once every 60 seconds. 
This interval is needed by limitation number of access to TwitterAPI. If account receves twitterID without "@" as DM, program collects 200 tweets on this account. 
If there are tweets including string yyyy-MM-dd, program returns these as DM. 

There is time lag from users send twitterID to this account to this program reply is about 90 seconds.
This program doesn't  suppose to be accessed by multiple users at the same time. If there are multiple accesses, this program can't be executed correctly.

## Requirement
python 3.7 Series

requests-oauthlib 1.3.0

## Usage
Change these two parts to yours
```
CK = '************************'
CS = '************************'
AT = '************************'
AS = '************************'
```
```
if tmpList != pastList :
        #最後が自分からの送信ならTrueを返す
        if tmpList[0][0] == '******************' : #自分のrecipientIDに置き換える
            return True
```
Execute this command
```
python3  schedule_management.py
```
## License
MIT

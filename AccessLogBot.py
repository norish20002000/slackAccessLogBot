#!/usr/local/pyenv/shims/python
# coding:utf-8

import time
import datetime
from slackclient import SlackClient
import AppConf

class AccessLogBot:
    sc = SlackClient(AppConf.token)

    def __init__(self):
        if AccessLogBot.sc.rtm_connect():

            while True:

                logData = AccessLogBot.sc.api_call("team.accessLogs", count=20)

                for i, log in enumerate(logData["logins"]):
                    log["date_last"] = datetime.datetime.fromtimestamp(log["date_last"])
                    log["date_first"] = datetime.datetime.fromtimestamp(log["date_first"])
                
                    print(log)
                    # print("\n")

                print("\n")
                time.sleep(5)

sbm = AccessLogBot()
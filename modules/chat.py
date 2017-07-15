
# -*- coding: utf8 -*-

import telegram
from telegram.bot import Bot
from member import member
from config import config

class Chat:
    def __init__(self):
        self.token = config.tg_token
        self.chat_id = config.tg_chat_id
        self.bot = Bot(token=self.token)
        pass

    def send_member_info(self):
        member.get_cur_member()
        text = "<b>人數統計</b>\n"
        
        for  k,v in member.resp.iteritems():
            text += config.name_list[k] + ":  "
            text += v + "\n"
        self.bot.send_message(chat_id=self.chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

chat = Chat()

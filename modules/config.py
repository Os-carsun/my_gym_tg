import ConfigParser

class Config:
    def __init__(self):
        """ Read all confg from app.cfg at once """
        config = ConfigParser.ConfigParser()
        config.read('app.cfg')

        self.url_list = config.get('GYM','list').split(',')
        self.name_list = dict()
        for pair in config.get('GYM','name_list').split(','):
            kv = pair.split(':')
            self.name_list[kv[0]]=kv[1]

        self.tg_token = config.get('TG','token')
        self.tg_chat_id = config.get('TG','chat_id')

config = Config()

#-----------------------------------------
#-  Copyright (c) 2023. Lazovikov Illia  -
#-----------------------------------------

import os

class Constants(object):
    version ="(v1.0.4)"

    botToken = os.environ['BOT_TOKEN']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    baseLink = os.environ['BASE_LINK']


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Constants, cls).__new__(cls)
        return cls.instance

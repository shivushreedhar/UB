import os
from os import environ, getcwd

import logging 
from logging import error as log_error

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

user_data = {}


AUTHORIZED_CHATS = environ.get("AUTHORIZED_CHATS", "")
if len(AUTHORIZED_CHATS) != 0:
    aid = AUTHORIZED_CHATS.split()
    for id_ in aid:
        user_data[int(id_.strip())] = {"is_auth": True}


SUDO_USERS = environ.get("SUDO_USERS", "6697298553")
if len(SUDO_USERS) != 0:
    aid = SUDO_USERS.split()
    for id_ in aid:
        user_data[int(id_.strip())] = {"is_sudo": True}


OWNER_ID = environ.get("OWNER_ID", "6697298553")
if len(OWNER_ID) == 0:
    log_error("OWNER_ID variable is missing! Exiting now")
    exit(1)
else:
    OWNER_ID = int(OWNER_ID)


config_dict = {'SUDO_USERS':SUDO_USERS,
               'AUTHORIZED_CHATS':AUTHORIZED_CHATS,
               'OWNER_ID':OWNER_ID}


class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6788872246:AAGtIALCc1c5_zsxERbGrnDWuBT3ZqJzASc")
    
    API_ID = int(os.environ.get("API_ID", "16073849"))
    
    API_HASH = os.environ.get("API_HASH", "e84dd69cd0504b8b45b2fd6a4e19068d")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://viratfilter:virat123@cluster0.0ug4o4o.mongodb.net/?retryWrites=true&w=majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002070783301"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001728957833")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5536032493"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Bshegdeuploader_bot")
                                  

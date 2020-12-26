import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "1400450496:AAGpZvH95-n_KQ7x1RvuOGFK5wNepwbyoJw"
    # The Telegram API things
    APP_ID = 2119350
    API_HASH ="8610b2e5dc11380f8b8005c9fcf8b3ed"
    OWNER_ID = 1422265105
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001241558511, -1001470368690]
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    SP_LIT_ALGO_RITH_M = os.environ.get(
        "SP_LIT_ALGO_RITH_M",
        "hjs"
    )
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 5))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 5))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@DSP_LEECHY_ROBOT")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@DSP_LEECHY_ROBOT")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "Mirror Bot")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@DSP_LEECHY_ROBOT")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech@DSP_LEECHY_ROBOT")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel@DSP_LEECHY_ROBOT")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize@DSP_LEECHY_ROBOT")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@DSP_LEECHY_ROBOT")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail@DSP_LEECHY_ROBOT")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail@DSP_LEECHY_ROBOT")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "True")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl@DSP_LEECHY_ROBOT")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone@DSP_LEECHY_ROBOT")
    UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload")
    RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme")

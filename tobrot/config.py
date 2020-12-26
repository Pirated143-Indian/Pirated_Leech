import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "1370072830:AAH-rifBIsiW3sPyTHtWdUjXPa-aWdFhHs4"
    # The Telegram API things
    APP_ID = 1468557
    API_HASH ="c05a1fff8d688c198d4665f4c08016a2"
    OWNER_ID = 1268206396
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001253546382, -1001331815943, -1001386365453, -1001493702344]
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
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@BG_Torrent_Leecher_Robot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@BG_Torrent_Leecher_Robot")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "Mirror Bot")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@BG_Torrent_Leecher_Robot")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech@BG_Torrent_Leecher_Robot")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel@BG_Torrent_Leecher_Robot")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize@BG_Torrent_Leecher_Robot")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@@BG_Torrent_Leecher_Robot")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail@BG_Torrent_Leecher_Robot")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail@BG_Torrent_Leecher_Robot")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "True")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl@BG_Torrent_Leecher_Robot")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone@BG_Torrent_Leecher_Robot")
    UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload")
    RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme")

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME", "untold_coder4")
BOT_USERNAME = getenv("BOT_USERNAME", "AnnieMusicRobot")
BOT_NAME = getenv("BOT_NAME", "˹ 𝗬𝗢𝗥 𝗫 𝗠𝗨𝗦𝗜𝗖 ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "YorXAssistant")
EVALOP = list(map(int, getenv("EVALOP", "6209871909").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", -1002014167331))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
DEEP_API = getenv("DEEP_API")
OWNER_ID = int(getenv("OWNER_ID", 6209871909))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PRIVATE-REPO4/MOONLIGHT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/world_friend_chatting_zone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sunlight_world")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# Telegram file size limits - Set these according to your requirements
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Pyrogram session strings - You need to generate these yourself
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AYUV = [ "<b>нєу</b> {0}, 💗\n\n๏ ᴛʜɪs ɪs {1} !\n\n➻ {1} ɪs ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴍᴜsɪᴄ ᴄᴏᴍᴘᴀɴɪᴏɴ, ʜᴇʀᴇ ᴛᴏ ʙʀɪɴɢ ʜᴀʀᴍᴏɴʏ ᴛᴏ ʏᴏᴜʀ ᴅᴀʏ. EɴJᴏʏ sᴇᴀᴍʟᴇss ᴍᴜsɪᴄ ᴘʟᴀʏʙᴀᴄᴋ, ᴄᴜʀᴀᴛᴇᴅ ᴘʟᴀʏʟɪsᴛs, ᴀɴᴅ ᴇғғᴏʀᴛʟᴇss ᴄᴏɴᴛʀᴏʟ, ᴀʟʟ ᴀᴛ ʏᴏᴜʀ ғɪɴɢᴇʀᴛɪᴘs. Lᴇᴛ {1} ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟɪsᴛᴇɴɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴇᴀsᴇ ᴀɴᴅ sᴛʏʟᴇ.\n\n<b><u>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs :</b></u> ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n──────────────────\n<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs🦋.</b> "  ,
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/24d982891899cfe9bd41a.jpg"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://telegra.ph/file/b9d32416c96e3051d126d.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/46758636cac7fed64d1c8.jpg"
STATS_VID_URL = "https://telegra.ph/file/8cf37f9fb1ba2b54df5e2.mp4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/46758636cac7fed64d1c8.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/98453c327134f8918f908.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/98453c327134f8918f908.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/98453c327134f8918f908.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/c28268e126572fa70c1b1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/c28268e126572fa70c1b1.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/5682767d9429b565f612e.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/8f95c335f16b84e43459d.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)

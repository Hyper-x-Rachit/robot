from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "15469484"))
    API_HASH = getenv("API_HASH", "a4e47ac121ccd896f52fc815a9a10a8e")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    STRING_SESSION = getenv("STRING_SESSION", None)
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "5980016986:AAG1mUJbgvpwNKMFdEtgRFGBAaWUGAAOiLg")
    OWNER_ID = int(getenv("OWNER_ID", "5824231649"))  # sᴛᴀʀᴛ @Exon_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "HYPER_X_RACHIT")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Shona_AI")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001962386072"))
    MONGO_URI = getenv("MONGO_DB_URI", "mongodb+srv://Rachit:Rachit@cluster0.hzww9ra.mongodb.net/?retryWrites=true&w=majority")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("mongodb+srv://Rachit:Rachit@cluster0.hzww9ra.mongodb.net/?retryWrites=true&w=majority"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

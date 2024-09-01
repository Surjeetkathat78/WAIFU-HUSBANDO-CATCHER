class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    
    OWNER_ID = "7089408502"
    sudo_users = "7089408502","6135328276"
    GROUP_ID = -1001529779762
    TOKEN = "7458352911:AAFEog08d7AOzd6gVKnc-bNBXQHWiv99Sl0"
    mongo_url = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL =["https://telegra.ph/file/44abc724240ff3cfc2d84.jpg"]
    SUPPORT_CHAT = "ZTX_MAIN_CHATS"
    UPDATE_CHAT = "ZTX_ORG"
    BOT_USERNAME = "UtopiaSmartBot"
    CHARA_CHANNEL_ID = "-1002202172045"
    api_id = 23028479
    api_hash = "c1e6a93b04c0810a5c282d8d8d44ea6f"
    

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

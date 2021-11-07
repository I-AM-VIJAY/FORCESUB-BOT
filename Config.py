import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "VkTgBotz")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", )
  API_HASH = os.environ.get("API_HASH", "")
  # Sudo users( goto @PRO_VK_ROBOT and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "2075923551").split()))
  SUDO_USERS.append(2075923551)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**🏷️FORCE SUBSCRIBE BOT**\n**🎖️ FORCE GROUP MEMBERS TO JOIN A SPECIFIC CHANNEL BEFORE SENDING MESSAGES IN THE GROUP.\n🎖️I wiYll MUTE MEMBERS IF THEY NOT JOINED YOUR CHANNEL AND TELL THEM TO JOIN THE CHANNEL AND UNMUTEING THEMSELF BY PRESSING A BUTTON.**",
        
        "**🏷️SETUP**\n**FIRST OF ALL ADD ME IN THE GROUP AS ADMIN WITH BAN USERS PERMISSION AND IN THE CHANNEL AS ADMIN.\n⚠️NOTE: ONLY  OF THE GROUP CAN SETUP ME AND I WILL LEAVE THE CHAT IF I AM NOT AN ADMIN IN THE CHAT.**",
        
        "**✅COMMANDS**\n__/ForceSubscribe = TO GET THE CURRENT SETTINGS.\n/ForceSubscribe no/off/disable = TO TURN OF FORCESUBSCRIBE.\n/ForceSubscribe {channel username or channel ID} = TO TURN ON AND SETUP THE CHANNEL.\n/ForceSubscribe clear = TO UNMUTE ALL MEMBERS WHO MUTED BY ME.\n/source_code = TO GET BOT SOURCE CODE😍\n\nNote: /FSub IS AN ALIAS OF /ForceSubscribe__",
        
       "**🤖I AM [FORCESUB-BOT](http://t.me/FSUB_VKTGBOT) \n🎖️ DEVELOPER = @vijay1142 \nDEVELOPED BY = @VKTGBOTZ \nSupport GROUP = @VKTGBOTSUPPORT**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n**I CAN FORCE MEMBERS TO JOIN A SPECIFIC CHANNEL BEFORE WRITING MESSAGES IN THE GROUP.\nCLICK HERE >> /help**"
   

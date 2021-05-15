from userbot import topfunc
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd
from var import Var

idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "4.0"
telever = "5.0"

if issudousing:
    amiusingsudo = "فعال✅"
else:
    amiusingsudo = "غير فعال ❌"

if islogokay:
    logchat = "متصل✅"
else:
    logchat = "غير متصل ❌"

if isherokuokay:
    riplife = "متصل ✅"
else:
    riplife = "غير متصل ❌"

if gdriveisshit:
    wearenoob = "فعال ✅"
else:
    wearenoob = "غير فعال ❌"

if rmbg:
    gendu = "مضاف  ✅"
else:
    gendu = "غير مضاف❌"

if wttrapi:
    starknoobs = "مضاف  ✅"
else:
    starknoobs = "غير مضاف ❌"

if hmmok:
    meiko = "مضاف ✅"
else:
    meiko = "غير مضاف ❌"

if isdbfine:
    dbstats = "بحالة جيده ✅"
else:
    dbstats = "سيء❌"

if Config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
if Var.LIGHTNING_PRO.lower() == "NO":
    light_pr = "NO"
else:
    lightning_pr = "YES"

lightning_status = (
    f"آسف يا سيدي في بعض الاضافات تسبب  خلل في Telegram\n"
    f"من فضلك حاول أن تفهم\n"
    f"بدلا من ذلك `.help` <اسم الاضافة>\n\n"
    f"الاصدار = {currentversion} \n"
    f"قاعدة البيانات = {dbstats} \n"
    f"المالك = {amiusingsudo} \n"
    f"سجل الاحداث = {logchat} \n"
    f"السيرفر= {riplife} \n"
    f"تخزين الدرايف= {wearenoob}"
)

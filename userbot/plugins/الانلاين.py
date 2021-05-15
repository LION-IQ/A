#    Copyright (C) 2021 KeinShin

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



"""Thanks To 
@Midhun_xD
@keinshin
@Shivam_Patel
@NOOBIzBack
"""


"""Only friday and DC (Can Use Without Credits) Can Use This Inline WithOut Copyright (Just Give The Credits Pls)
Thanks"""




import os

import re
import json
from math import ceil
from userbot.thunderconfig import Config

from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, DETAIL_CMD_HELP, bot

from var import Var


LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 
lightning_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import lightning_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "الكلاوات"
LIGHTNINGBOT = Var.TG_BOT_TOKEN_BF_HER






@borg.on(lightning_cmd(pattern=r"unload (?P<krish_blac>\w+)$"))
async def unload(lightning):
    if lightning.fwd_from:
        return
    krish_blac = lightning.pattern_match["krish_blac"]
    try:
        remove_plugin(krish_blac)
        await lightning.edit(f"تم الازالة بنجاح✅ {krish_blac}")
    except Exception as e:
        await lightning.edit(
            "تم الازالة بنجاح✅ {krish_blac}\n{}".format(krish_blac, str(e))
        )


@borg.on(lightning_cmd(pattern=r"load (?P<krish_blac>\w+)$"))
async def load(lightning):
    if lightning.fwd_from:
        return
    krish_blac = lightning.pattern_match["krish_blac"]
    try:
        try:
            remove_plugin(krish_blac)
        except BaseException:
            pass
        load_module(krish_blac)
        await lightning.edit(f"تم التحميل بنجاح✅ {krish_blac}")
    except Exception as e:
        await lightning.edit(
            f"Sorry,{krish_blac} can not be loaded\nbecause of the following error.\n{str(e)}"
        )



BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_LIT = f"Hello Sir MySelf Here For  {LIGHTNINGUSER}'s Protection "
else:
    BOT_LIT = BOT_MSG   


LIGHTNING_WARN = os.environ.get("LIGHTNING_WARN", None)
if LIGHTNING_WARN is None:
    WARNING = (
    f"**{BOT_LIT}**"
    f"** حبيبي انا بوت حماية {LIGHTNINGUSER}   **\n\n"
    f"**سيدي {LIGHTNINGUSER} مشغول الآن!** \n"
    f"{LIGHTNINGUSER}ما سبب المحادثة"
    f"**اذا اخترت ازعاج  سوف اقوم بحضرك تلقائيا** 😂 \n\n"
    f"**اختر سبب و اترك رسالة واحده  سيدي مشغول الان**\n"
)
else:
    WARNING = LIGHTNING_WARN










@tgbot.on(events.InlineQuery)
async def inline_handler(lightning):
    builder = lightning.builder
    result = None
    query = lightning.text
    if lightning.query.user_id == bot.uid and query.startswith("**Black") or query.startswith("Black"):
        rev_text = query[::-1]
        buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
        result = builder.article(
            f"قائمة المساعدة",
            text="\n{}\n`Plugins`: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await lightning.answer([result])
    elif lightning.query.user_id == bot.uid and query == "*رائع*":
        result = builder.article(
            title="رائع",
            text=f"**اذا عندك مشكلة  \n{LIGHTNINGUSER}** \nاختر نوعها حتى نساعدك ",
            buttons=[
                [custom.Button.inline("مساعدة", data="what?")],
                [Button.url("اوامر لاتعمل🥺", "https://t.me/KLTHON")],
                [Button.url("الدعم 🤓", "https://t.me/KLTHON")],
                [
                    Button.url(
                
                    "Want To Learn CMDS😅",
                    "https://t.me/KLTHON" ,
                    )
                ], 
            ],
        )
        await lightning.answer([result])
    elif lightning.query.user_id == bot.uid and query.startswith("**هلا سيدي**"):
        result = builder.photo(
            file=LIGHTNING_WARNING,
            text=WARNING,
            buttons=[
                [custom.Button.inline("ازعاج?😉", data="lightning_is_here_cant_spam")],
                [
                    custom.Button.inline(
                        "صديقك❤️❤️",
                        data="he_sucks",
                    )
                ],
                [custom.Button.inline("عندك طلب🙏", data="fck_ask")],
                
            ],
            )
        await lightning.answer([result] if result else None)
    else:
        return
    


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page + 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "حبيبي ما تكدر  لا تحاول !"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)


@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_lightning_plugins_(.*)")
   )
) # Thanks To Friday Userbot
async def lightning_pugins_query_hndlr(lightning):
    if not lightning.query.user_id == bot.uid:
        how = "حبيبي هاي مو الك لا تعبث "
        await lightning.answer(how, cache_time=0, alert=True)
        return
    light_pulu_name = lightning.data_match.group(1).decode("UTF-8")
   
    try:
        if light_pulu_name in CMD_HELP:
           
           lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_HELP[light_pulu_name]}"
           lightning_is_best = lightning_help_strin 
           lightning_is_best += "\n\n**اذا كان هنالك خطاء راسلنا @klthon** ".format(light_pulu_name)
        
        else:
            lightning_help_strin = "الاوامر الموجوده {}:\n".format(light_pulu_name)
            for i in CMD_HELP:
                lightning_help_strin += "ℹ️ " + i + "\n"
                for iter_list in CMD_HELP[i]:
                    lightning_help_strin += "    `" + str(iter_list) + "`"
                    lightning_help_strin += "\n"
                    lightning_help_strin += "\n"
    except BaseException:
         pass
   
    if light_pulu_name in CMD_LIST:
                lightning_help_strin = "الاوامر الموجوده{}:\n".format(light_pulu_name)
                for i in CMD_LIST[light_pulu_name]:
                    lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_LIST[light_pulu_name]}\n`**Details**- @KLTHON"
                    lightning_help_strin += "\n    " + i
                    lightning_help_strin += "\n"
                
    else:
           lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n**Details** - @KLTHON"
           lightning_is_best = lightning_help_strin 
           lightning_is_best += "\n\n**اذا كان هنالك خطاء راسلنا @klthon** ".format(light_pulu_name)
    lightning_help_strin = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n**Details** - @KLTHON"
    lightning_is_best = lightning_help_strin 
    lightning_is_best += "\n\n**اذا كان هنالك خطاء راسلنا @klthon** ".format(light_pulu_name)    
    if len(lightning_is_best) >= 4096:
          keinshin = "`انتظر حبيبي`"
          await lightning.answer(keinshin, cache_time=0, alert=True)
          out_file = lightning_is_best
          lig_url = "https://del.dog/documents"
          r = requests.post(lig_url, data=out_file.encode("UTF-8")).json()
          lig_url = f"https://del.dog/{r['key']}"
          await lightning.edit(
               f"Pasted {light_pulu_name} to {lig_url}",
               link_preview=False,
               buttons=[
                [custom.Button.inline("خاصة", data="krish")],
                [custom.Button.inline("رجوع💢", data="lghtback")]],
         )
    else:
           await lightning.edit(
            message=lightning_is_best,
            buttons=[
                [custom.Button.inline("خاصة‌", data="krish")],
                [custom.Button.inline("رجوع💢", data="lghtback")],
            ],
        )


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"helpme_prev\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "حبيبي ما تكدر  لا تعبث!"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def what(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"{LIGHTNINGUSER} استخدم الأزرار التالية "
        await lightning.answer(fck_bit, alert=True)
    else:
        txt = f" تعتقد أن هذا لك?\n راح اشتكي عليك عند القائد {LIGHTNINGUSER}👀👀"
        await lightning.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_is_here_cant_spam")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"  اهلا سيدي {LIGHTNINGUSER} 😂انا احاول التخلص من هذا المزعج"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f" **تعتقد راح تكدر؟؟**😂😂\n\n**[klawat](tg://user?id={lightning_id}) راح تبلع بلووك **😂😂"
    await lightning.edit("بايييييييي")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await lightning.edit("😂😂😂👋🏻👋🏻")
    await bot.send_message(
        LIGHT_LOGS,
        f"مرحبا سيدي هذا النوب[النوب](tg://user?id={lightning_id})حاول ارسال رسائل مزعجه 😂\n\n**بلع بلووك**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"اهلا سيدي {LIGHTNINGUSER} انا احاول التخلص من هذا المزعج"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"أنت تعتقد أنه يمكنك ذلك😂😂\nروح وانتظر الموافقة😂😂"
    await lightning.edit("بايييييييي")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"  مرحبا سيدي هذا النوب[النوب](tg://user?id={lightning_id}) يريد يراسل بدون موافقة😂 \n.",
    )





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"اهلا سيدي {LIGHTNINGUSER}احاول اتخلص من هذا اللزكة"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("تريد التحدث مع سيدي \n\nعليك الانتظار عزيزي \n\n**فقط** **يمكنك انتظار سيدي**")
    await asyncio.sleep(2)
    await lightning.edit(
        "ما نوع  الصداقة", buttons= [
        [Button.inline("زميل الدراسة", data="school")],
        [Button.inline("صديق على التلكرام", data="tg_okay")],
        ], 
    )
    light_text = "`تحذير`- ❗️⚠️لا تحاول أي شيء غبي ، انتظر بلطف!!!❗️⚠️"
    await bot.send_message(lightning.query.user_id, light_text)
    
    
    
    
    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            fck_bit = f"حسننا هيا يا سيدي {LIGHTNINGUSER} "
            await lightning.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**اذا انت صديق على التلكرام** حسننا انتظر ثواني"
        lightning_id = lightning.query.user_id
        await asyncio.sleep(2)
        await lightning.edit(f"`جاري اخبار سيدي بذالك{LIGHTNINGUSER}`")
        await asyncio.sleep(2)
        await lightning.edit("`تم✅`")
        await bot.send_message(lightning.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"مرحبا سيدي [Friend](tg://user?id={lightning_id}). صديقك على التلكرام له هنا للدردشة انظر الرسالة [Tg Friend](tg://user?id={lightning_id}) هو ينتظر.",
    
    )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            fck_bit = f"حسننا هيا يا سيدي {LIGHTNINGUSER} "
            await lightning.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**اذا انت صديق** حسننا انتظر"
        lightning_id = lightning.query.user_id
        await asyncio.sleep(2)
        await lightning.edit(f"`جاري اخبار سيدي بذالك {LIGHTNINGUSER}`")
        await asyncio.sleep(2)
        await lightning.edit("`تم✅`")
        await bot.send_message(lightning.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"مرجبا سيدي [Friend](tg://user?id={lightning_id}). صديقك على التلكرام له هنا للدردشة انظر الرسالة  [Tg Friend](tg://user?id={lightning_id})هو الان ينتظر.",
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"حسننا سيدي{LIGHTNINGUSER} اني احاول طرد  هذا اللزكة"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("حسناا خليني شوي افكر🤫")
    await asyncio.sleep(2)
    await lightning.edit("راح انطيك جنص(فرصة)🤨")
    await asyncio.sleep(2)
    await lightning.edit(
        "هل تحاول الازعاج هنا?", buttons= [
        [Button.inline("نعم", data="lemme_ban")],
        [Button.inline("لاء", data="hmm")],
        ],
    )

    
    reqws = "`تحذير`- ❗️⚠️لا تحاول أي شيء غبي ، انتظر بلطف!!!❗️⚠️"


    await bot.send_message(lightning.query.user_id, reqws)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"مرحبا سيدي هذا العطل [العطل ](tg://user?id={lightning_id}).عندة طلب  ماعرف شيريد.",
        buttons=[Button.url("تواصل معة", f"tg://user?id={lightning_id}")],
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "جييد👮🏻‍♀️"
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return          
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("عليك ان تنتظر ")
    hmmmmm = "حسنا ، يرجى الانتظار وسوف اخبر سيدي انك تنتظره"
    await bot.send_message(
              lightning.query.user_id, hmmmmm)
          
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "جييد👮🏻‍♀️"
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return    
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("اخترت نعم وتعترف انت مزعج ")
    ban = "ابلع بلووك" 
    await bot.send_message(
         lightning.query.user_id, ban)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))
async def hmm(lightning):
    if lightning.query.user_id == bot.uid:
        text = "🇲‌🇾‌ 🇭‌🇪‌🇱‌🇵‌ 🇸‌🇹‌🇦‌🇹‌🇸‌\n\nالاضافات-- الكل جيد ✔️\nالسيرفر--متصل✔️\nالسجل --جيد✔️:/\nاجمالي الاضافات: {}".format(len(CMD_LIST))
        await lightning.answer(text, alert=True)
    else:
        txt = f"الاحصائات{LIGHTNINGUSER}ليست لك :)"
        await lightning.answer(txt, alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"krish")))
async def hmm(lightning):
    if lightning.query.user_id == bot.uid:
        text = "\nامر الكلاوات \n`.كلاوات`\n🙄🙄🙄🙄"
        await lightning.answer(text, alert=True)
    else:
        txt = f"لل {LIGHTNINGUSER} ليست لك :)"
        await lightning.answer(txt, alert=True)        


"""
Thanks To Friday Userbot and @Midhun_xD For This idea

"""
import requests




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback")))
async def ho(event):
    if event.query.user_id != bot.uid:
        how = "ليست لك ."
        await event.answer(how, cache_time=0, alert=True)
        return
    await event.answer("( ͡🔥 ͜ʖ ͡🔥)", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
    ho = f"""تيلثون الكلاوات \n
اذا كان هنالك خطاء راسلنا @klthon \nمجموع الاضافات: {len(CMD_LIST)}"""
    await event.edit(message=ho, buttons=buttons)



        


    
def lightnings_menu_for_help(b_lac_krish, lightning_plugs, lightning_lol):
    lightning_no_rows = 10
    lightning_no_coulmns = 3
    lightning_plugins = []
    for p in lightning_plugs:
        if not p.startswith("_"):
            lightning_plugins.append(p)
    lightning_plugins = sorted(lightning_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("🇮🇶", x, "🇮🇶"), data="_lightning_plugins_{}".format(x)
        )
        for x in lightning_plugins
    ]
    pairs = list(zip(plugins[::lightning_no_coulmns], plugins[1::lightning_no_coulmns]))
    if len(plugins) % lightning_no_coulmns == 1:
        pairs.append((plugins[-1],))
    max_fix = ceil(len(pairs) / lightning_no_rows)
    lightning_plugins_pages = b_lac_krish % max_fix
    if len(pairs) > lightning_no_rows:
        pairs = pairs[
            lightning_plugins_pages * lightning_no_rows : lightning_no_rows * (lightning_plugins_pages + 1)
        ] + [
            (
                custom.Button.inline(
                    "➡️التالي", data="{}_prev({})".format(lightning_lol, lightning_plugins_pages)
                ),
               # Thanks To Friday For This Idea
               custom.Button.inline("〽️الاحصائات〽️", data="stta"
               ),
               custom.Button.inline(
                    "السابق↩️ ", data="{}_next({})".format(lightning_lol, lightning_plugins_pages)
                ),
                
            )
        ]
    return pairs

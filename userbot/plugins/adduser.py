"""Add the user(s) to the current chat
الامر: `.edd` <User(s)>"""

from telethon import functions

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="edd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.edd`الامر يستخدم في الجموعات فقط")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("تم اضافة  المستخدم")
        else:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("تمت إضافة المستخدم إلى الدردشة بنجاح.")

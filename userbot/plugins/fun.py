
import asyncio
import random
import re
import time
from random import choice, randint
from collections import deque
from telethon import events
import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


from userbot import CMD_HELP
from userbot.utils import register, admin_cmd


# ================= CONSTANT =================


GAMBAR_TITIT = """
šš
ššš
  ššš
    ššš
     ššš
       ššš
        ššš
         ššš
          ššš
          ššš
      šššš
 šššššš
 ššš  ššš
    šš       šš
"""

# ===========================================

#@register(outgoing=True, pattern="^.(yes|no|maybe|decide)$")
@borg.on(admin_cmd(pattern=r"(yes|no|maybe|decide)$"))
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(event.chat_id,
                                    str(r["answer"]).upper(),
                                    reply_to=message_id,
                                    file=r["image"])



@borg.on(admin_cmd(pattern=r"fp$"))
async def facepalm(e):
    """ Facepalm  š¤¦āā """
    await e.edit("š¤¦āā")

@borg.on(admin_cmd(pattern=r"corona$"))
async def iqless(e):
    await e.edit("Antivirus scan was completed \nā ļø Warning! This  donkey has Corona Virus")


@borg.on(admin_cmd(pattern=r"ggl (.*)"))
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Tap this blue, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@borg.on(admin_cmd(pattern=r"scam(?: |$)(.*)", outgoing=True))
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    options = [
        'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
        'photo', 'document', 'cancel'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if (scam_time > 0):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(outgoing=True, pattern="^.fail$")
async def fail(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nāāāāāāāāāāāāāāāā `" 
                     "`\nāāāāāāāāāāāāāāāā `"    
                     "`\nāāāāāāāāāāāāāāāā `"       
                     "`\nāāāāāāāāāāāāāāāā `")    


@register(outgoing=True, pattern="^.lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nā±āāā±ā±ā±ā­āāāā®āāā±ā±ā±ā± `" 
                     "`\nā±āāā±ā±ā±āā­āā®āāāā±ā±ā±ā± `"       
                     "`\nā±āāāāāāā°āāÆāāāāāāā± `" 
                     "`\nā±āāāāāā°āāāāÆāāāāāā± `") 
 
 
                                                                                   
@register(outgoing=True, pattern="^.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nā­ā­āāāā®ā®āāāāāāāāāā\nāāā­āāāÆāāāāāā²āāā±āā\nāāāā±āāāāāāāāā±āāā®ā`"
                     "`\nāāā°āāā±ā­ā®āā±ā±āā±ā±āāā\nāā°āāāāā°āÆāāā±ā±ā±ā°ā»ā«ā\nāāāāāā³āāāāāāā³āāāÆā`"
                     "`\nāāāāāāāāāāāāāāāāā `")
                     



@register(outgoing=True, pattern="^.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n(\_/)`"
                     "`\n(ā¢_ā¢)`"
                     "`\n >š¹ *`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(ā¢_ā¢)`"
                     "`\nš¹<\ *`")


@register(outgoing=True, pattern="^.hoi$")  
async def gtfo(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nāāāāāāāāā`" 
                     "`\nāāāāāāāāā`"    
                     "`\nāā¼ā¼ā¼ā¼ā¼`"       
                     "`\nā  Hello Man`"
                     "`\nāā²ā²ā²ā²ā²`"
                     "`\nāāāāāāāāā`"
                    "`\n āā   āā`")               


@register(outgoing=True, pattern="^.ml(?: |$)(.*)")
async def gtfo(e):
   message = e.pattern_match.group(1)
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nāāāāāāāāā`" 
                     "`\nāāāāāāāāā`"    
                     "`\nāā¼ā¼ā¼ā¼ā¼`"       
                     f"`\nā  {message}`"
                     "`\nāā²ā²ā²ā²ā²`"
                     "`\nāāāāāāāāā`"
                    "`\n āā   āā`")               


@register(outgoing=True, pattern="^.taco$")  
async def taco(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\__/}"
                     "\n(ā_ā)"
                     "\n( >š® Want a taco?")


@register(outgoing=True, pattern="^.paw$")  
async def paw(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`(=āĻā=)")


@register(outgoing=True, pattern="^.tf$")  
async def tf(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(ĢæāĢæāĢæÄ¹ĢÆĢæĢæāĢæ Ģæ)Ģ  ")  
      

@register(outgoing=True, pattern="^.gay$")            
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nāāāā­āāāāāā®āāāāā\nāāāāāāāāāāāāāāā`"
                     "`\nāāāāāāā­āā®ā»ā®āāāā\nāāāā±ā²āāāāāāāāāā\nāāā­ā»āāā°āā»āā®āāāā`"
                     "`\nāāā°ā³āā­āāāā³āÆāāāā\nāāāāāāā°āāā«āU GAY`"
                    "\nāāāāāāāāāāāāāāā")    


@register(outgoing=True, pattern="^.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ā²ā²ā­āāāāā® \nā­ā®āāāāāāā­ā® \nāā°ā«ā½ā½ā½ā£āÆā \nā°āā«ā³ā³ā³ā£āāÆ`"
                     "`\nā²ā²āāāāāā  \nā²ā²āāāāāā `")


@register(outgoing=True, pattern="^.hai$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\nāāāā±āāāāā²āā­āāāāā\nāāāāāāāāāāāHELLO!āš`"
                     "`\nāāāāāāāā³āāā°ā³ā®HELLO!ā\nāāāā­āā°āÆāā®āāāÆā°āāā\nā±āāāāāāāāāāā²āāāā`"
                     "`\nāāāā²āāāāā±āāāāāāā`")


@register(outgoing=True, pattern="^.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nāā­ā®ā­ā®\nāāāāā\nā­ā»āā»āā®`"
                     "`\nāāāāāā\nāāā­āāā®āā®\nāāāā­ā°āÆā°āÆā®`"
                     "`\nā«āā  NoU\nāāā°ā°āāāāāÆ`"
                     "`\nāāāā»āā`")



@register(outgoing=True, pattern="^.mf$")  
async def gtfo(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
"\n......................................../Ā“ĀÆ/) "
"\n......................................,/ĀÆ../ "
"\n...................................../..../ "
"\n..................................../Ā“.ĀÆ/"
"\n..................................../Ā“ĀÆ/"
"\n..................................,/ĀÆ../ "
"\n................................../..../ "
"\n................................./Ā“ĀÆ./"
"\n................................/Ā“ĀÆ./"
"\n..............................,/ĀÆ../ "
"\n............................./..../ "
"\n............................/Ā“ĀÆ/"
"\n........................../Ā“ĀÆ./"
"\n........................,/ĀÆ../ "
"\n......................./..../ "
"\n....................../Ā“ĀÆ/"
"\n....................,/ĀÆ../ "
"\n.................../..../ "
"\n............./Ā“ĀÆ/'...'/Ā“ĀÆĀÆ`Ā·Āø "
"\n........../'/.../..../......./ĀØĀÆ\ "
"\n........('(...Ā“...Ā“.... ĀÆ~/'...') "
"\n.........\.................'...../ "
"\n..........''...\.......... _.Ā·Ā“ "
"\n............\..............( "
"\n..............\.............\...")



@register(outgoing=True, pattern="^.sayhi$")
async def shalom(e):
    await e.edit(
        "\nššššššššš"
        "\nšš·š·š·š·š·š·š·š"
        "\nššššš·šššš"
        "\nššššš·šššš"
        "\nššššš·šššš"
        "\nšš·š·š·š·ļøš·š·š·š"
        "\nššššššššš"
        "\nššššššššš"
        "\nšš·ššļøšššš·š"
        "\nšš·š·š·š·š·š·š·š"
        "\nšš·š·š·š·š·š·ļøš·š"
        "\nšš·ššššļøšš·š"
        "\nššššššššš")

@register(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace('š', emoji)
    await e.edit(titid)


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [

            "8āļø===D",

            "8=āļø==D",

            "8==āļø=D",

            "8===āļøD",

            "8==āļø=D",

            "8=āļø==D",

            "8āļø===D",

            "8===āļøDš¦",

            "8==āļø=Dš¦š¦",

            "8=āļø==Dš¦š¦š¦"

        ]

        for i in animation_ttl:
        
            await asyncio.sleep(animation_interval)
        
            await event.edit(animation_chars[i % 8])

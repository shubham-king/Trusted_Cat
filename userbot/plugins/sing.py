""" Sing a Malayalam song... 
    Command .sing 
    By @Deonnn """



# BY @Deonnn

from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.sing", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Singing...")

    await asyncio.sleep(2)

    x=(random.randrange(1,67))
    
    if x==1:

        await event.edit("`๐ถ Put your wings on me, wings on me \n When I was so heavy \n Pour on a symphony \n When I'm low, low, low, low \n Ah, oh-ah, oh-ah \nGot me feeling drunk and high \n So high, so high๐ถ`")

    if x==2:

        await event.edit("๐ถ I know it breaks your heart \n Moved to the city in a broke down car \n And four years, no calls \n Now you're looking pretty in a hotel bar... ๐ถ")

    if x==3:

        await event.edit("๐ถ If we go down then we go down together... \n They'll say you could do anything... \n They'll say that I was clever๐ถ")

    if x==4:

        await event.edit("๐ถ You were the shadow to my light \n Did you feel us? \n Another star,You fade away... ๐ถ")

    if x==5:

        await event.edit("๐ถ Lately, I've been, I've been thinking \n I want you to be happier, I want you to be happier....  ๐ถ")

    if x==6:

        await event.edit("๐ถ You say you love me, I say you crazy \n We're nothing more than friends \n You're not my lover, more like a brother \n I known you since we were like ten, yeah...๐ถ")

    if x==7:

        await event.edit("๐ถ  Oh won't you stay for a while \n I'll take you on a ride \n If you can keep a secret\n Oh won't you stay for a while\n Show me darkness baby, show me deepness...๐ถ")    

    if x==8:

        await event.edit("๐ถ Take me through the night \n Fall into the dark side \n We don't need the light\n We'll live on the dark side...๐ถ")

    if x==9:

        await event.edit("๐ถI'm so alone \n Nothing feels like home \n I'm so alone \n Trying to find my way back home to you...  ๐ถ")

    if x==10:

        await event.edit("๐ถ I'm not looking for somebody \n With some superhuman gifts \n Some superhero\n Some fairytale bliss\n Just something I can turn to \n Somebody I can kiss... ๐ถ")
     
    if x==11:

        await event.edit("๐ถ What you don't understand is I'd catch a grenade for ya,yeah...yeah...\n Throw my hand on a blade for ya...yeah...yeah... \n I'd jump in front of a train for ya...yeah...yeah... \n You know I'd do anything for ya...yeah...yeah...๐ถ")

    if x==12:

        await event.edit("๐ถ He said, One day you'll leave this world behind So live a life you will remember \n My father told me when I was just a child \n These are the nights that never die \n My father told me...๐ถ")
    
    if x==13:

        await event.edit("๐ถ So wake me up when it's all over \n When I'm wiser and I'm older \n All this time I was finding myself \n And I didn't know I was lost ๐ถ")

    if x==14:

        await event.edit("๐ถMonday left me broken \n Tuesday, I was through with hoping \n Wednesday, my empty arms were open \n Thursday, waiting for love, waiting for love... ๐ถ")
        
    if x==15:

        await event.edit("๐ถ Yeah, I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more \n I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more... ๐ถ")

    if x==16:

        await event.edit("๐ถ Then you're left in the dust \n Unless I stuck by ya \n You're a sunflower \n I think your love would be too much \n Or you'll be left in the dust \n Unless I stuck by ya \n You're the sunflower \n You're the sunflower ๐ถ")
     
    if x==17:

        await event.edit("๐ถ I love it when you call me seรฑorita \n I wish I could pretend I didn't need ya \n But every touch is ooh la la la \n It's true, la la la \n Ooh, I should be running \n Ooh, you keep me coming for ya... ๐ถ")

    if x==18:

        await event.edit("๐ถ Your sugar \n Yes, please \n Won't you come and put it down on me \n I'm right here, 'cause I need \n Little love and little sympathy...๐ถ")

    if x==19:

        await event.edit("๐ถ Lately I been, I been losing sleep \n Dreaming about the things that we could be \n But baby I been, I been prayin' hard \n Said no more counting dollars \n We'll be counting stars \n Yeah, we'll be counting stars... ๐ถ")

    if x==20:

        await event.edit("๐ถI've been running through the jungle \n I've been running with the wolves \n To get to you, to get to you \n I've been down the darkest alleys \n Saw the dark side of the moon \n To get to you, to get to you... ๐ถ")

    if x==21:
        
        await event.edit("๐ถ Hypnotized, this love out of me \n Without your air I can't even breathe \n Lead my way out into the light \n Sing your lu-lu-lu-lullaby... ๐ถ")
        
    if x==22:
        
        await event.edit("๐ถI can feel your love pullin' me up from the underground, and \n I don't need my drugs, we could be more than just part-time lovers...๐ถ")
       
    if x==23:

        await event.edit("๐ถ Maybe we're perfect strangers \n Maybe it's not forever \n Maybe the night will change us \n Maybe we'll stay together \n Maybe we'll walk away \n Maybe we'll realize \n We're only human \n Maybe we don't need no reason...๐ถ")

    if x==24:

        await event.edit("๐ถ Hey, I just met you and this is crazy \n But here's my number, so call me maybe \n It's hard to look right at you baby \n But here's my number, so call me maybe... ๐ถ")

    if x==25:
        
        await event.edit("๐ถ You just want attention, you don't want my heart \n Maybe you just hate the thought of me with someone new \n Yeah, you just want attention, I knew from the start \n You're just making sure I'm never gettin' over you...๐ถ")
        
    if x==26:
        
        await event.edit("๐ถ We don't talk anymore, we don't talk anymore \n We don't talk anymore, like we used to do \n We don't love anymore \n What was all of it for? \n oh, we don't talk anymore, like we used to do...๐ถ")
    if x==27:
        
        await event.edit("๐ถ So love me like you do, lo-lo-love me like you do \n Love me like you do, lo-lo-love me like you do \n Touch me like you do, to-to-touch me like you do \n What are you waiting for?...๐ถ")
        
    if x==28:
        
        await event.edit("๐ถ I've become so numb, I can't feel you there \n Become so tired, so much more aware \n By becoming this all I want to do \n Is be more like me and be less like you... ๐ถ")

    if x==29:
        
        await event.edit("๐ถ Cause girls like you \n Run around with guys like me \n Til sundown, when I come through \n I need a girl like you, yeah yeah... ๐ถ")
        
    if x==30:
        
        await event.edit("๐ถCold enough to chill my bones \n It feels like I don't know you anymore \n I don't understand why you're so cold to me \n With every breath you breathe \n I see there's something going on \n I don't understand why you're so cold... ๐ถ")
    
    if x==31:
        
        await event.edit("๐ถ And if you feel you're sinking, I will jump right over \n Into cold, cold water for you \n And although time may take us into different places \n I will still be patient with you... ๐ถ")
        
    if x==32:
        
        await event.edit("๐ถ I know I can treat you better \n Than he can... \n And any girl like you deserves a gentleman \n Tell me why are we wasting time \n On all your wasted cryin, When you should be with me instead \n I know I can treat you better \n Better than he can...๐ถ")
        
    if x==33:
        
        await event.edit("๐ถI'm in love with the shape of you \n We push and pull like a magnet do \n Although my heart is falling too \n I'm in love with your body...๐ถ")
                         
    if x==34:
        
        await event.edit("๐ถYoungblood \n Say you want me, Say you want me \n Back in your life \n So I'm just a dead man crawling tonight \n 'Cause I need it, yeah, I need it \n All of the time \n Yeah, ooh ooh ooh...๐ถ")

    if x==35:

        await event.edit("๐ถ เดเดฐเตเดจเดพเตพ เดคเดฐเดณเดฎเดฟเดตเดจเดฟเตฝ... เดชเดเดฐเต เดตเดจเดฒเดคเดฟเดเดฏเดพเดฏเต... เดฎเตเดฑเตเดเต... เดฎเดคเดฟเดตเดฐเตเดตเตเดณเด เดธเดเต... ๐ถ")

    if x==36:

        await event.edit("๐ถ เดเดดเดฒเดฟเดจเตเดฑเต เดเดดเดเตเดเดณเดฟเตฝ เดเดตเตพ เดฎเดพเดเตเดเตเดชเตเดฏเต... เดจเตเดตเดฟเดจเตเดฑเต เดคเตเดฐเดเตเดเดณเดฟเตฝ เดเดพเตป เดฎเดพเดคเตเดฐเดฎเดพเดฏเต... ๐ถ")

    if x==37:

        await event.edit("๐ถ เดเดตเดฃเดฟเดชเตเดชเตเดจเตเดจเตเดเตเดเดพเดฒเดพเดเดฟเดเตเดเดพเด เดจเดฟเดจเตเดจเต เดเดพเตป... เดเดฏเดฟเดฒเตเดฒเตเดฏเด เดเดพเดตเดฟเดฒเต เดตเตเดฃเตเดฃเดฟเดฒเดพเดตเต... ๐ถ")

    if x==38:

        await event.edit("๐ถ เดเดจเตเดฆเตเดฐเดจเตเดฒเดฟเดฎเดฏเตเดฒเตเด เด เดฎเดฟเดดเดฟ เดชเตเดฏเตเดเดเดณเดฟเตฝ... เดเดจเตเดจเดฒเต เดจเดฟเตป เดฎเตเดเด เดจเต เดจเตเดเตเดเดฟ เดจเดฟเดจเตเดจเต... ๐ถ")

    if x==39:

        await event.edit("๐ถ เดฎเดฏเดฟเดฒเดพเดฏเต เดชเดฑเดจเตเดจเตเดตเดพ เดฎเดดเดตเดฟเดฒเตเดฒเต เดคเตเตฝเดเตเดเตเดฎเตเดจเตเดจเดดเดเต... ๐ถ")

    if x==40:

        await event.edit("๐ถ เดจเดฟเดฒเดพเดตเดฟเดจเตเดฑเต เดจเตเดฒเดญเดธเตเดฎ เดเตเดฑเดฟเดฏเดฃเดฟเดเตเดเดตเดณเต... เดเดพเดคเดฟเดฒเตเดฒเดเตเดเดฎเตเดฎเดฒเดฟเดเตเดเต เดเตเดฃเตเดเตเดเดฟ เดจเดฟเดจเตเดจเดตเดณเต... ๐ถ")

    if x==41:

        await event.edit("๐ถ เดจเตเดฏเตเดฐเต เดชเตเดดเดฏเดพเดฏเต เดคเดดเตเดเตเดฎเตเดชเตเตพ เดเดพเตป เดชเตเดฐเดฃเดฏเด เดตเดฟเดเดฐเตเด เดเดฐเดฏเดพเดตเตเด... ๐ถ")    

    if x==42:

        await event.edit("๐ถ เดเดฐเดฟเดเดฟเตฝ เดจเตเดฏเตเดฃเตเดเดพเดฏเดฟเดฐเตเดจเตเดจเตเดเตเดเดฟเดฒเตเดจเตเดจเต เดเดพเตป... เดเดฐเตเดฎเดพเดคเตเดฐ เดตเตเดฑเตเดคเต เดจเดฟเดจเดเตเดเตเดชเตเดฏเดฟ... ๐ถ")

    if x==43:

        await event.edit("๐ถ เดเดคเตเดฐเดฏเต เดเดจเตเดฎเดฎเดพเดฏเต เดจเดฟเดจเตเดจเตเดเดพเตป เดคเตเดเตเดจเตเดจเต... เดเดคเตเดฐเดฎเตเตฝ เดเดทเตเดเดฎเดพเดฏเต เดจเดฟเดจเตเดจเตเดฏเตเตป เดชเตเดฃเตเดฏเดฎเต... ๐ถ")

    if x==44:

        await event.edit("๐ถ เดฎเดดเดคเตเดคเตเดณเตเดณเดฟเดเตพ เดชเตเดดเดฟเดเตเดเตเดเตเดฎเต เดจเดพเดเตป เดตเดดเดฟ... เดจเดจเดเตเดเตเดเดฟเดฏเตเตป เดเตเดเดเตเดเตเดดเดฟเตฝ เดจเต เดตเดจเตเดจ เดจเดพเตพ... ๐ถ")
     
    if x==45:

        await event.edit("๐ถ เดเดฐเดณเต เดจเดฟเตป เดเต เดชเดฟเดเดฟเดเตเดเดพเตฝ, เดเดเดฒเตเดณเด เดตเตเดฃเตเดฃเดฟเดฒเดพเดตเต... เดเตพเดเตเดเดฃเตเดฃเดฟเตป เดเดพเดดเตเดเดฏเดฟเตฝ เดจเต, เดเตเดฑเตเดเตเดจเตเดจเตเดฐเต เดตเตเตบเดชเดฟเดฑเดพเดตเต... ๐ถ")

    if x==46:

        await event.edit("๐ถ เดฎเดฑเดจเตเดจเดฟเดเตเดเตเดฎเตเดจเตเดคเดฟเดจเต เดฎเดจเดธเตเดธเดฟเตฝ เดคเตเดณเตเดฎเตเดชเตเดจเตเดจเต เดฎเตเดจเดพเดจเตเดฐเดพเดเดคเตเดคเดฟเตป เดฒเตเดฒเดญเดพเดตเด... ๐ถ")
    
    if x==47:

        await event.edit("๐ถ เดฎเดดเดเตเดเดพเดฒเด เดเดจเดฟเดเตเดเดพเดฏเดฟ เดฎเดฏเดฟเตฝ เดเตเดฒเตเดณเตเดณ เดชเตเดฃเตเดฃเต เดจเดฟเดจเตเดจเตเดคเตเดคเดจเตเดจเต... ๐ถ")

    if x==48:

        await event.edit("๐ถ เดฎเดฟเดดเดฟเดฏเดฑเดฟเดฏเดพเดคเต เดตเดจเตเดจเต เดจเต เดฎเดฟเดดเดฟเดฏเตเดเตเดเดพเดฒเดฟเตฝ... เดเดจเดตเดฑเดฟเดฏเดพเดคเตเดฏเตเดคเต เดเดฟเดจเดพเดตเต เดชเตเดฒเต... ๐ถ")
        
    if x==49:

        await event.edit("๐ถ เดเดจเตเดฆเดจเดเตเดเตเดฒเดฏเดฟเตฝ เดฎเตเดเตเดเดฟเดจเตเดฐเดพเดเดฟเดฏเตเตป เดเดณเดฎเดพเตป เดเดฟเดเดพเดตเต เดเดฑเดเตเดเดฎเดพเดฏเต... ๐ถ")

    if x==50:

        await event.edit("๐ถ เดเดฑเตเดคเตเดคเดชเตเดฃเตเดฃเต เดจเดฟเดจเตเดจเต เดเดพเดฃเดพเดเตเดเดฟเดเตเดเตเดฐเต เดจเดพเดณเตเดฃเตเดเต... ๐ถ")
     
    if x==51:

        await event.edit("๐ถ เดคเดพเดฎเดฐเดชเตเดชเตเดตเดฟเตฝ เดตเดพเดดเตเด เดฆเตเดตเดฟเดฏเดฒเตเดฒเต เดจเต... เดชเตเดจเดฟเดฒเดพเดเตเดเดเดตเดฟเตฝ เดชเตเดเตเดเตเด เดชเตเดฃเตเดฏเดฎเดฒเตเดฒเต เดจเต... ๐ถ")

    if x==52:

        await event.edit("๐ถ เดชเดพเดเด เดชเตเดคเตเดคเดเดพเดฒเด เดชเดพเดเดพเตป เดตเดจเตเดจเต เดจเตเดฏเตเด... ๐ถ")

    if x==53:

        await event.edit("๐ถ เดฐเดพเดเดนเดเดธเดฎเต เดฎเดดเดตเดฟเตฝ เดเตเดเดฟเดฒเดฟเตฝ... เดธเตเดจเตเดนเดฆเตเดคเตเดฎเดพเดฏเต เดตเดฐเตเดฎเต... ๐ถ")

    if x==54:

        await event.edit("๐ถ เดชเดคเตเดคเตเดตเตเดณเตเดชเตเดชเดฟเดจเต เดฎเตเดฑเตเดฑเดคเตเดคเต เดจเดฟเดเตเดเดฃ เดเดธเตเดคเตเดฐเดฟ เดฎเตเดฒเตเดฒเดฏเตเดเตเดเต เดเดพเดคเตเดคเตเดเตเดคเตเดคเต... เดเดจเตเดฑเต เดเดธเตเดคเตเดฐเดฟ เดฎเตเดฒเตเดฒเดฏเตเดเตเดเต เดเดพเดคเตเดคเตเดเตเดคเตเดคเต... ๐ถ")

    if x==55:
        
        await event.edit("๐ถ เดฎเดเตเดเตพ เดชเตเดฐเดธเดพเดฆเดตเตเด เดจเตเดฑเตเดฑเดฟเดฏเดฟเตฝ เดเดพเตผเดคเตเดคเดฟ... เดฎเดเตเดเดเตเดเตเดฑเดฟเดฎเตเดฃเตเดเต เดเตเดฑเตเดฑเดฟ... ๐ถ")
        
    if x==56:
        
        await event.edit("๐ถ เดเดจเตเดคเดฟเดชเตเดชเตเตปเดตเตเดเตเดเด เดเดเดฒเดฟเตฝ เดฎเตเดฒเตเดฒเตเดคเตเดคเดพเดดเตเดฎเตเดชเตเตพ... เดฎเดพเดจเดคเตเดคเต เดฎเตเดฒเตเดฒเดคเตเดคเดฑเดฏเดฟเดฒเต เดฎเดพเดฃเดฟเดเตเดฏเดเตเดเตเดชเตเดชเต... ๐ถ")
       
    if x==57:

        await event.edit("๐ถ เดเดฎเตเดชเดฒเดชเตเดชเตเดดเต เดเดฃเตเดฃเดฟเดเตเดเดฃเตเดฃเดจเตเดเต เดจเต... เดเดจเตเดคเตเดชเดฐเดฟเดญเดตเด เดฎเตเดฒเตเดฒเตเดฏเตเดคเดฟเดตเดจเตเดจเตเดตเต... ๐ถ")

    if x==58:

        await event.edit("๐ถ เดเตเดเดเดพเดฆเตเดฐเดฟเดฏเดฟเตฝ เดเตเดเดเตเดเตเดฎเดพ เดเตเดเดฎเดเตเดเตเดชเตเดฒเตเดฏเต เดชเตเดฐเดฃเดฏเด... เดคเดดเตเดเตเดจเตเดจเต, เดเดจเตเดจเต เดชเตเดฃเดฐเตเดจเตเดจเต... ๐ถ")

    if x==59:
        
        await event.edit("๐ถ เดถเตเดฏเดพเดฎเดพเดเดฌเดฐเด เดชเตเตฝเดเตเดจเตเดจเตเดฐเดพ เดตเตเตบเดเดจเตเดฆเตเดฐเดจเดพเดฏเต เดจเดฟเตป เดชเตเดฎเตเดเด... ๐ถ")
        
    if x==60:
        
        await event.edit("๐ถ เดถเตเดฐเตเดฐเดพเดเดฎเต เดคเตเดเตเดจเตเดจเดฟเดคเตเตป เดตเตเดฃเดคเตป เดชเตเตป เดคเดจเตเดคเตเดฐเดฟเดฏเดฟเตฝ... ๐ถ")
        
    if x==61:
        
        await event.edit("๐ถ เดเดจเตเดคเดฟเดจเต เดตเตเดฑเตเดฐเต เดธเตเดฐเตเดฏเตเดฆเดฏเด... เดจเตเดฏเตเตป เดชเตเดจเตเดจเตเดทเดธเตเดธเดจเตเดงเตเดฏเดฏเดฒเตเดฒเต... ๐ถ")
        
    if x==62:
        
        await event.edit("๐ถ เดเดจเตเดฐเดพเดเดฟเดฃเต เดเดคเดพเดฏเตเตป เดเดฐเดณเดฟเตฝ เดตเดฟเดฐเดฟเดเตเด เดชเตเดเตเดเตพ... ๐ถ")

    if x==63:
        
        await event.edit("๐ถ เดชเดพเดเดพเด เดจเดฎเตเดเตเดเต เดชเดพเดเดพเด... เดตเตเดฃเตเดเตเดฎเตเดฐเต เดชเตเดฐเตเดฎเดเดพเดจเด... ๐ถ")
        
    if x==64:
        
        await event.edit("๐ถ เดเดฒเตเดฒเดฟเดฎเดฒเตผ เดเดพเดตเดฟเตฝ เดชเตเดฐเด เดเดพเดฃเดพเตป... เดเดจเตเดจเต เดจเดฎเตเดฎเตพ เดชเตเดฏเดฟ เดฐเดพเดตเดฟเตฝ เดจเดฟเดฒเดพเดตเดฟเตฝ... ๐ถ")
    
    if x==65:
        
        await event.edit("๐ถ เดเดฑเตเดเดตเดฏเตฝ เดเตเดฐเตเดตเต... เดฎเตเดฑเดฟเดตเดพเดฒเตป เดเตเดฐเตเดตเต... เดคเดณเดฟเตผ เดตเตเดฑเตเดฑเดฟเดฒเดฏเตเดฃเตเดเต... เดตเดฐเดฆเดเตเดทเดฟเดฃ เดตเตเดเตเดเดพเตป... ๐ถ")
        
    if x==66:
        
        await event.edit("๐ถ เดเตเดจเตเดจเดฟเดฎเดฃเดฟเดเตเดเตเดชเตเดชเต เดคเตเดฑเดจเตเดจเตเดฃเตเดฃเดฟ เดจเตเดเตเดเตเด เดจเตเดฐเด, เดชเดฟเดจเตเดจเดฟเตฝเดตเดจเตเดจเต เดเดฃเตเดฃเต เดชเตเดคเตเดคเตเด เดเดณเตเดณเดจเตเดเตเดเต เดชเตเดฏเดฟ... ๐ถ")
        
    if x==67:
        
        await event.edit("Not in a mood to sing. Sorry!")

# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"lul"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐๐คฃ๐๐คฃ๐๐คฃ"))
	for _ in range(999):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern=r"candy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐ฆ๐ง๐ฉ๐ช๐๐ฐ๐ง๐ซ๐ฌ๐ญ"))
	for _ in range(999):
		await asyncio.sleep(0.4)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐โน๏ธ๐โน๏ธ๐โน๏ธ๐"))
	for _ in range(999):
		await asyncio.sleep(0.4)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern=r"tlol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐ค๐ง๐คจ๐ค๐ง๐คจ"))
	for _ in range(999):
		await asyncio.sleep(0.4)
		await event.edit("".join(deq))
		deq.rotate(1)		

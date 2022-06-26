import discord
from discord.ext import commands
import asyncio
import requests
import threading
import random

#ใส่token ตัวเอง
token = "ss"

client = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True)
@client.event
async def on_ready():
	print("--------")
	print("")
	print(" Command : !run")
	print(" ลบเซิร์ฟทั้งหมดแล้วสร้างใหม่ ")
	print(client.user)
	print("")
	print("--------")
	
	
@client.command()
async def run(ctx):
	for s in client.guilds:
		def delete():
			requests.post(f"https://discord.com/api/v9/guilds/{s.id}/delete",headers={"authorization": token})
		def out():
			requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{s.id}",headers={"authorization": token})
		threading.Thread(target=delete).start()
		threading.Thread(target=out).start()
	asyncio.sleep(1)
	while True:
		def c():
			n = ['はじめまして！','私の名前は......です。','...... と呼んでください','私の名前はタナカミキコです。','...... から来ました。']
			name = random.choice(n)
			requests.post("https://discord.com/api/v9/guilds",headers={"authorization": token},json={"channels":[],"name":name,"system_channel_id":11})
		threading.Thread(target=c).start()
		
		
client.run(token, bot=False)
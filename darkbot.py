import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


prefix = "-"
bot = commands.Bot(command_prefix=prefix)

chat_filter = ["CUNT", "BITCH", "FOTZE", "NIGGER", "JUDE", "SS", "HITLER", "ADOLF", "ADOLF HITLER", "NIGGA", "SLAVE", "SKLAVE", "JEWS", "KZ"]
bypass_list = []

@bot.event
async def on_ready():
    print("ONLINE")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Member")
    await bot.add_roles(member, role)
    
@bot.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await bot.delete_message(message)
                    await bot.send_message(message.channel, "**YOU ARE CUTE**")
                except discord.errors.NotFound:
                    return 
    

bot.run("NTQxMDE1NzA0OTg0NjE3MDEx.DzZUTA.pTnYdTKkRPxs78clH8s52W81y54")


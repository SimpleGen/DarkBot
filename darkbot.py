import discord
from discord.ext.commands import Bot
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = "NTgxODA5ODU1OTU0NjgxODc2.XOmTnA.PRpqxPuMCQzHT-SqJES7lsZhMcQ"
client = commands.Bot(command_prefix="-")

Client = discord.client
Clientdiscord = discord.Client()

testmsgid = None
testmsguser = None
botmsg = None
msg = None

@client.event
async def on_ready():
    print ("I am running on")
    await client.change_presence(activity=discord.Game(name="-<service> @name | 7sek"))

#MINECRAFT
#MINECRAFT
#MINECRAFT
#MINECRAFT

@client.command()
@commands.has_permissions(add_reactions=True)
async def minecraft(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type your name! -minecraft @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a Minecraft account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "jeason3bb@gmail.com:baba6635",
        "monterojalysa@yahoo.com:jalysa23",
        "nickpilotte7@live.com:ilygussyyes7",
        "jeason3bb@gmail.com:baba6635",
        "monterojalysa@yahoo.com:jalysa23",
        "sennabravenboer@gmail.com:braaf206",
        "thebadster@hotmail.com:Clippers11",
        "stefanpaccaud@gmail.com:Stefan0122",
        "monterojalysa@yahoo.com:jalysa23",
        "kingneeso99@gmail.com:Kingslayer99",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    emb = (discord.Embed(title="SimpleGenerator", description="Bot by 7sek", color=0x2DF270))
    emb.add_field(name="Have fun with the account", value="you got muted for 30m", inline=False)
    await ctx.author.send(embed=emb)
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.remove_roles(role)
    await asyncio.sleep(1800)
    await member.add_roles(role)

@minecraft.error
async def minecraft_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

#VPN
#VPN
#VPN

@client.command()
@commands.has_permissions(add_reactions=True)
async def nordvpn(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type your name! -minecraft @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a Minecraft account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "acapurias@gmail.com:nelson12",
        "n.hoffmann987@gmx.de:callecam22",
        "ricetcx@gmail.com:sapigoreng",
        "jdanajlovski@gmx.de:jankowitsch1991",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    emb = (discord.Embed(title="SimpleGenerator", description="Bot by 7sek", color=0x2DF270))
    emb.add_field(name="Have fun with the account", value="you got muted for 30m", inline=False)
    await ctx.author.send(embed=emb)
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.remove_roles(role)
    await asyncio.sleep(1800)
    await member.add_roles(role)

@minecraft.error
async def minecraft_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

#Spotify
#Spotify
#Spotify
#Spotify

@client.command()
@commands.has_permissions(add_reactions=True)
async def spotify(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type your name! -spotify @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a Spotify account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "bradleyf644@gmail.com:Brad7878",
        "niclaslitzius@hotmail.de:Dortmund09",
        "alperanisilak@gmail.com:Narepla20",
        "sauntegames@gmail.com:Nng69dxv",
        "jason70still@gmail.com:Jaystill70",
        "frank.vosmer@gmail.com:Philips92",
        "abdul.rafay.aziz@gmail.com:Lahore123",
        "tony55442@gmail.com:Earlobe1",
        "amf505@gmail.com:Buddy12",
        "nortor@live.com:Tiur1000",
        "bigfella13_4@hotmail.com:Harvey27",
        "guatavovictor22@gmail.com:Gugu101010",
        "icejustin123@gmail.com:Dudeitup23",
        "hector2348@yahoo.com:Bulldog1",
        "osaydt@gmail.com:Crazy-911",
        "laneosmun@gmail.com:Apple240",
        "guillaume.ribas@hotmail.fr:Toulouse9731",
        "henrik.peters.1@gmx.de:POPcorn123",
        "flufie3@gmail.com:Kerstmis1234",
        "naya.steffensen@gmail.com:Sba32tyd",
        "gonzaleta@gmail.com:11juanpo",
        "haydon.cowan@gmail.com:Bluered1993",
        "sophie.horseman@hotmail.com:Scruffy123",
        "chris_lorusso@yahoo.com:Laxbro24",
        "grikschat@googlemail.com:Januar1984",
        "heine1505@gmail.com:Greyfox1505",
        "a.kugelstadt@outlook.de:Jualci50r",
        "vulvabean@gmail.com:Rhianna1",
        "hesham199600@hotmail.com:Spdf1996",
        "hallerarne@web.de:Toggotv19",
        "lucaskayrouz@gmail.com:Georgelibby1968",
        "andrewquick55@gmail.com:Andrewquick5",
        "gmeforentrie@gmail.com:Yuktipada79",
        "phillip.basi@gmail.com:Coconut22",
        "davidhunter2@gmail.com:Scrabble62",
        "graysonduncan@gmail.com:Grayson123",
        "lucas.brashears@yahoo.com:Woodland1",
        "kaliberus@gmail.com:Fwk4xvew",
        "ryan_figueroa114@yahoo.com:Jeannette1",
        "simeonconway@live.co.uk:Daft5lag",
        "cazi112@hotmail.co.uk:Speedtouch95",
        "lukepodobinski@yahoo.com:Crosby2006",
        "hsuhihhong@gmail.com:12341234",
        "shiyikokoko@ymail.com:9629935d",
        "hegedus.zsolt2001@gmail.com:Quad2001",
        "hamoline.gautier@gmail.com:Motdepasse1",
        "robin-nordsten96@hotmail.com:P0ledix5",
        "griffinheller@gmail.com:Bobisfred1",
        "cypherm211@yahoo.com:Michael1",
        "infernal1995@op.pl:11gunio11",
        "emil8aslund@gmail.com:Axel1234",
        "bengals0619@gmail.com:Twoface12",
        "hntrday@gmail.com:Iulca1213",
        "typtich@gmail.com:9801077mike",
        "greenmt@g.cofc.edu:Scruffy1",
        "mikhaelds@gmail.com:Desouza88",
        "cjhannaganjr@googlemail.com:Skyrim2001",
        "slowbar@gmail.com:Gobills666",
        "h8tbit@hotmail.com:Otheam81",
        "hbowler120@hotmail.com:Hockey17",
        "sebas_lp_22@hotmail.com:3425sebas",
        "ilanlavin@gmail.com:Il753951",
        "dr3way@yahoo.com:Csaszar94",
        "celia@robinhill.be:Games007!",
        "iliesberdal@yahoo.fr:19941996i",
        "2016mormauj1@gmail.com:Skater12",
        "samuel.enomoto@yahoo.com:Sonic077",
        "jakieg@hotmail.co.uk:Kingy010",
        "zurahh@outlook.com:Facupwinners1202",
        "myto0721@gmail.com:Rlxogks12",
        "huskie2014@gmail.com:CKirbs95",
        "aldair9sp@gmail.com:Aldair123",
        "gytukas20@gmail.com:Pucis123",
        "tonho.98.asm@gmail.com:Contrasenha1",
        "kataja.noah@gmail.com:Kataja123",
        "back2backmvp13@hotmail.com:Backyard13",
        "harrith.sivalingam@gmail.com:Sanjay02",
        "jackdholt@hotmail.co.uk:Puppybob1",
        "guitronivan@gmail.com:Google56",
        "grzestrzonkowski@gmail.com:Gregory99",
        "brad@allstar.com.au:Emily2003",
        "h.o.tuncel@hotmail.com:Hotmail4582.",
        "4tenhiphop@gmail.com:Exporta11",
        "paulkley98@googlemail.com:Helsing97",
        "danielbradshaw@live.com.au:Mason123",
        "ruffn3ck1986@googlemail.com:Bigmac1986",
        "pjrod_28@hotmail.com:El112887",
        "rodrigues_j@web.de:Joey1995",
        "cameronhensel145@gmail.com:Soccerboy123",
        "zadnikar.glenn@hotmail.com:Hiska007",
        "victor360vip@gmail.com:01310131hd",
        "valentinaho@hotmail.fr:Garfield974",
        "liam.strickland96@gmail.com:Z1gzou96",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    emb = (discord.Embed(title="SimpleGenerator", description="Bot by 7sek", color=0x2DF270))
    emb.add_field(name="Have fun with the account", value="you got muted for 30m", inline=False)
    await ctx.author.send(embed=emb)
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.remove_roles(role)
    await asyncio.sleep(1800)
    await member.add_roles(role)

@spotify.error
async def spotify_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

#Uplay
#Uplay
#Uplay
#Uplay

@client.command()
@commands.has_permissions(change_nickname=True)
async def uplay(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type your name! -uplay @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a Uplay account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "Sorry, we dont have uplay for the first time.",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)

@uplay.error
async def uplay_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
@commands.has_permissions(change_nickname=True)
async def pmute(ctx, member: discord.Member = None):
    await ctx.author.send("insult, advertising, provocation, spamming")
    if not member:
        await ctx.send("Please enter a name!")
        await ctx.author.send("If its not a Reason you got kicked or banned!")
        return
    await ctx.send(f"{member.mention}, got muted for 1 0min!")
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    await asyncio.sleep(5000)
    await member.add_roles(role)

@client.command()
async def apply(ctx):
    await ctx.send("Check your DMs!")
    await ctx.author.send("You want the helper oder refiller rank? Write @7sek#5813 or @lzxvai.#0701")
    
async def gen(ctx):
    emb = (discord.Embed(description="SimpleGenerator Help", color=0x2DF270))
    emb.set_author(name="7sek")
    emb.add_field(name="-spotify", value="generate a spotify account", inline=False)
    emb.add_field(name="-fortnite", value="generate a fortnite account", inline=False)
    emb.add_field(name="-roblox", value="generate a roblox account", inline=False)
    emb.add_field(name="-minecraft", value="generate a minecraft account", inline=False)
    emb.add_field(name="-uplay", value="generate a uplay account", inline=False)
    emb.set_thumbnail(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    await ctx.send(embed=emb)

@client.command()
async def report(ctx, member: discord.Member = None):
    channel = discord.utils.get(member.guild.channels, name="support")
    emb = (discord.Embed(description="Report", color=0x2DF270))
    emb.add_field(name=f"The member {member.mention} was reported.", value="------------------", inline=False)
    await channel.send(embed=emb)
    await channel.send(f"{member.mention}")
    if not member:
        await ctx.send("Spectify a member")
        return
    await ctx.send(f"{member.mention} reported")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} kicked")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
@commands.has_permissions(administrator=True)
async def ocase(ctx, member: discord.Member = None):
    await ctx.send("I open the case, please wait")
    await asyncio.sleep(3)
    choices = ['You won -> `Legend`',
               'You won -> `Legend`',
               'You won -> `Nothing`',
               'You won -> `Nothing`',
               'You won -> `Nothing`',
               'You won -> `Nothing`',
               'You won -> `Nothing`',
               'You won -> `Hero`',
               'You won -> `Simple`',
               'You won -> `Simple`',
               'You won -> `Simple`',]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@ocase.error
async def ocase_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")


@client.command()
@commands.has_permissions(administrator=True)
async def caseadmin(ctx, member: discord.Member = None):
    await ctx.send("Only the guys with the permission instant invite can open the case so create a role with the permission instant invite and user will open it with /ocase")


@caseadmin.error
async def caseadmin_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
async def case(ctx, member: discord.Member = None):
    emb = (discord.Embed(description="Case Info", color=0x2DF270))
    emb.add_field(name="-casei", value="see the case information!", inline=False)
    emb.add_field(name="-ocase", value="open the case!", inline=False)
    emb.add_field(name="-case_admin", value="only for administrator", inline=False)
    emb.set_thumbnail(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} got ban")

@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
async def verify(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("How is your Name? -verify @name")
        return
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)
    await ctx.author.send(f"I verified User: {member.mention} with the ID: {member.id}")
    await ctx.channel.send(f"{member.mention} Check your DMs!")

@verify.error
async def verify_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
async def id(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type your name")
        return
    await ctx.send(f"ID: {member.id}")

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"You do not have enough permissions {member.mention}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def iclear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

@iclear.error
async def iclear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
async def cf(ctx, member: discord.Member = None):
    await ctx.send("I start the CoinFlip")
    await asyncio.sleep(3)
    choices = ['💰 `WIN`', '😢 `LOSE`']
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def bot(ctx):
    await ctx.send("https://www.youtube.com/channel/UCDtcgX8sCmNS8_CKeJJpnzw?view_as=subscriber")
    await ctx.send("https://discord.gg/eSYMFhw")

@client.command()
async def friend(ctx):
    await ctx.send("https://www.youtube.com/channel/UCNT3gMwV8WSL5NCinBc4GxA")

@client.command()
async def spend(ctx):
    emb = (discord.Embed(description="Donate / PayPal", color=0x2DF270))
    emb.add_field(name="PayPal", value="simplebuildnetzwerk@gmail.com", inline=False)
    await ctx.author.send(embed=emb)

@client.command()
@commands.has_permissions(send_messages=True)
async def ping(ctx, member: discord.Member = None):
    await ctx.send("I check your ping, please wait!")
    await asyncio.sleep(3)
    emb = (discord.Embed(description="SupportBot", color=0x2DF270))
    emb.add_field(name="You have a:", value=f"{round(client.latency * 1000)}ms")
    await ctx.send(embed=emb)

@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
async def shelp(ctx):
    emb = (discord.Embed(description="SupportBot Help", color=0x2DF270))
    emb.set_author(name="7sek")
    emb.add_field(name="-kick", value="to kick people", inline=False)
    emb.add_field(name="-ban", value="to ban people", inline=False)
    emb.add_field(name="-mute", value="to mute people", inline=False)
    emb.add_field(name="-mute1", value="to mute people 1hour", inline=False)
    emb.add_field(name="-unmute", value="to unmute people", inline=False)
    emb.add_field(name="-clear 0-100", value="clear the chat", inline=False)
    emb.add_field(name="-iclear", value="instant chat clear", inline=False)
    emb.add_field(name="-bot", value="send the youtube channel link and the discord invite link", inline=False)
    emb.add_field(name="-friend", value="send the youtube channel from the friend of the developer", inline=False)
    emb.add_field(name="-spend", value="get the spend email (paypal)", inline=False)
    emb.add_field(name="-userinfo", value="get the userinfo", inline=False)
    emb.add_field(name="-id", value="get the user id", inline=False)
    emb.add_field(name="-cf", value="coins flip", inline=False)
    emb.add_field(name="-case", value="open a rang case (only on Events)", inline=False)
    emb.add_field(name="-ping", value="you can see your ms", inline=False)
    emb.add_field(name="-verify (your name)", value="if you not have the user rank", inline=False)
    emb.add_field(name="Create a rule User", value="new user will get this rule", inline=False)
    emb.add_field(name="Create a log channel", value="to send a welcome message", inline=False)
    emb.set_image(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    emb.set_thumbnail(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    await ctx.send(embed=emb)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))
    embed.add_field(name="Joined at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))

    embed.add_field(name=f"Roles {(len(roles))}", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot by 7sek", value="/bot")

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def crackerm(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -crackerm @name")
        return
    await ctx.send("You will get the rank the next secounds")
    await asyncio.sleep(3)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.add_roles(role)
    await asyncio.sleep(2592000)
    await member.remove_roles(role)

@client.command()
@commands.has_permissions(administrator=True)
async def test(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -test @name")
        return
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.add_roles(role)
    await ctx.send("Test")
    role = discord.utils.get(ctx.guild.roles, name="Access")
    await member.remove_roles(role)
    await asyncio.sleep(10)
    await member.add_roles(role)

@client.command()
@commands.has_permissions(administrator=True)
async def cracker1(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -crackerm @name")
        return
    await ctx.send("You will get the rank the next secounds")
    await asyncio.sleep(3)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.add_roles(role)
    await asyncio.sleep(604800)
    await member.remove_roles(role)

@client.command()
@commands.has_permissions(administrator=True)
async def cracker2(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -crackerm @name")
        return
    await ctx.send("You will get the rank the next secounds")
    await asyncio.sleep(3)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.add_roles(role)
    await asyncio.sleep(1209600)
    await member.remove_roles(role)

@client.command()
@commands.has_permissions(administrator=True)
async def rankhelp(ctx):
    emb = (discord.Embed(title="SupportBot Help", color=0x2DF270))
    emb.set_author(name="7sek")
    emb.add_field(name="-crackerm", value="cracker lite one month", inline=False)
    emb.add_field(name="-cracker2", value="cracker lite two week", inline=False)
    emb.add_field(name="-cracker1", value="cracker lite one week", inline=False)
    emb.set_thumbnail(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    await ctx.send(embed=emb)

@client.command()
@commands.has_permissions(administrator=True)
async def time(ctx):
    await ctx.send("3€ Cracker Lite and 5€ Cracker only two weeks. Use -advantages")
    await asyncio.sleep(3600)
    await ctx.send("3€ Cracker Lite and 5€ Cracker only two weeks. Use -advantages")
    await asyncio.sleep(3600)
    await ctx.send("3€ Cracker Lite and 5€ Cracker only two weeks. Use -advantages")
    await asyncio.sleep(3600)
    await ctx.send("3€ Cracker Lite and 5€ Cracker only two weeks. Use -advantages")
    await asyncio.sleep(3600)
    await ctx.send("3€ Cracker Lite and 5€ Cracker only two weeks. Use -advantages")
    await asyncio.sleep(3600)
    await ctx.send("3€ Cracker Lite and 5€ Cracker only two weeks. Use -advantages")

@client.command()
async def advantages(ctx):
    emb = (discord.Embed(title="advantages", description="Bot by 7sek", color=0x2DF270))
    emb.add_field(name="Cracker rank", value="Lifetime rank. With the rank you can generate Fortnite, roblox, uplay", inline=False)
    emb.add_field(name="Cracker Lite rank", value="One month rank. With the rank you can generate Fortnite, roblox, uplay", inline=False)
    emb.set_thumbnail(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    await ctx.author.send(embed=emb)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="log")
    emb = (discord.Embed(description="SupportBot", color=0x2DF270))
    emb.add_field(name=f"Welcome on our discord server", value=member.display_name)
    await channel.send(embed=emb)
    role = discord.utils.get(member.guild.roles, name="Access")
    await member.add_roles(role)
    role = discord.utils.get(member.guild.roles, name="User")
    await member.add_roles(role)

client.run("NTgzMjg1NzM1MDQ2NTEyNjYw.XO6OdQ.6wbf1XObMT7Dt82Buy1DACYDBdo")

import discord

client = discord.Client()
testmsgid = None
testmsguser = None


@client.event
async def on_ready():
    print(client.user.name)
    print("========")

    if message.content.lower().startswith("coder"):
        await client.send_message(message.channel, "SimpleGen")

    if message.content.lower().startswith("!member"):
        botmsg = await client.send_message(message.channel, "YES👍 NO👎")

        await client.add_reaction(botmsg, "👍")
        await client.add_reaction(botmsg, "👎")

        global testmsgid
        testmsgid = botmsg.id

        global testmsguser
        testmsguser = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    chat = reaction.message.channel

    if reaction.emoji == "👍" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "member", msg.server.roles)
        await client.add_roles(user, role)
        await client.send_message(chat, "Member")

    if reaction.emoji == "👎" and msg.id == testmsgid and user == testmsguser:
        await client.send_message(chat, "Not a Member")

client.run('NTAwNzQxMjU1MjgyNjg4MDEw.Dv_DOw.6SjIDG5TkvfnOFD4_OG82l_dfKA')

import discord
import random
from discord.ext import commands

# Prefix .
client = commands.Bot(command_prefix = ".")

# Bot ready
@client.event
async def on_ready():
	# Status
	await client.change_presence(status=discord.Status.online, activity=discord.Game(".help"))
	print("Bot is ready.")

# Auto roll



#Clear text
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

# Kick
@client.command()
@commands.has_permissions(administrator=True)

async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)


# Ban
@client.command()
@commands.has_permissions(administrator=True)

async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)



# Token
client.run('ODM1MTc1MTQzMjg2Mzc0NDEw.YILndg.Jj4Sh2p5IyMO3vqq9yeTrJhcy5M')

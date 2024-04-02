# importing discord.py
import discord
from discord import app_commands
from discord.ext import commands
from discordtoken import TOKEN
from bible import *

# use default intents
intents = discord.Intents.default()
# command_prefix is useless here
bot = commands.Bot(intents=intents, command_prefix=';')
# create groups for bibles
bible_group = app_commands.Group(name='bible', description='A group of commands for Bible verses')
bible_pt_group = app_commands.Group(name='bíblia', description='Um grupo de comandos para versículos Bíblicos')


# set up our on_ready bot event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # attempt the sync the bot commands
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)


# define our random command
@bible_group.command(name='random', description='Retrieves a random Bible verse')
async def random_verse(ctx: discord.Interaction):
    # tell the user we've got the command
    await ctx.response.defer()
    # retrieve our bible quote
    text, reference, translation = await get_random_verse()
    # send our plain text message
    verse_embed: discord.Embed = discord.Embed(
        title=reference,
        description=text,
        color=0x5c5c5c
    )
    verse_embed.set_author(name=translation)
    verse_embed.set_footer(
        text='Verse from bible-api.com',
        icon_url='https://wallpapers.com/images/hd/holy-bible-clipart-zttvmfha6lc31xl4.png'
    )
    await ctx.followup.send(embed=verse_embed)


# define our random command
@bible_group.command(name='verse', description='Retrieves a Bible verse')
@app_commands.describe(verse='The verse to retrieve')
async def verse_get(ctx: discord.Interaction, verse: str):
    # tell the user we've got the command
    await ctx.response.defer()
    # retrieve our bible quote
    text, reference, translation = await get_verse(verse)
    # send our plain text message
    verse_embed: discord.Embed = discord.Embed(
        title=reference,
        description=text,
        color=0x5c5c5c
    )
    verse_embed.set_author(name=translation)
    verse_embed.set_footer(
        text='Verse from bible-api.com',
        icon_url='https://wallpapers.com/images/hd/holy-bible-clipart-zttvmfha6lc31xl4.png'
    )
    await ctx.followup.send(embed=verse_embed)


# define our random command
@bible_pt_group.command(name='aleatório', description='Manda um versículo Bíblico aleatório')
async def random_verse_pt(ctx: discord.Interaction):
    # tell the user we've got the command
    await ctx.response.defer()
    # retrieve our bible quote
    text, reference, translation = await get_random_verse_pt()
    # send our plain text message
    verse_embed: discord.Embed = discord.Embed(
        title=reference,
        description=text,
        color=0x5c5c5c
    )
    verse_embed.set_author(name=translation)
    verse_embed.set_footer(
        text='Versículo de bible-api.com',
        icon_url='https://wallpapers.com/images/hd/holy-bible-clipart-zttvmfha6lc31xl4.png'
    )
    await ctx.followup.send(embed=verse_embed)


# define our random command
@bible_pt_group.command(name='versículo', description='Manda um versículo da Bíblia')
@app_commands.describe(verse='The verse to retrieve')
async def verse_pt(ctx: discord.Interaction, verse: str):
    # tell the user we've got the command
    await ctx.response.defer()
    # retrieve our bible quote
    text, reference, translation = await get_verse_pt(verse)
    # send our plain text message
    verse_embed: discord.Embed = discord.Embed(
        title=reference,
        description=text,
        color=0x5c5c5c
    )
    verse_embed.set_author(name=translation)
    verse_embed.set_footer(
        text='Versículo de bible-api.com',
        icon_url='https://wallpapers.com/images/hd/holy-bible-clipart-zttvmfha6lc31xl4.png'
    )
    await ctx.followup.send(embed=verse_embed)


@bot.tree.command(name='help', description='Lists all the commands you can use')
async def help_command(ctx: discord.Interaction):
    # tell the user we've got the command
    await ctx.response.defer()
    help_embed: discord.Embed = discord.Embed(
        title='Command List:',
        color=0x5c5c5c
    ).set_author(name='Help')
    help_embed.add_field(
        name='/bible verse: {verse}',
        value='Returns the specified Bible verse'
    )
    help_embed.add_field(
        name='/bible random',
        value='Returns a random Bible verse'
    )
    help_embed.add_field(
        name='/bíblia versículo: {versículo}',
        value='Retorna o versículo Bíblico especificado'
    )
    help_embed.add_field(
        name='/bíblia aleatório',
        value='Retorna um versículo Bíblico aleatório'
    )
    await ctx.followup.send(embed=help_embed)


# add the bible group to our bot commands
bot.tree.add_command(bible_group)
bot.tree.add_command(bible_pt_group)


# run the bot
bot.run(TOKEN)
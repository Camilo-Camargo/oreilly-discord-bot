import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from account import read_user_account
from book import safaribook
from convertor import download_and_convert

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command('book')
async def hello(ctx, arg):
    book_id = arg
    account = read_user_account()
    output_path = safaribook(account[0], account[1], book_id)
    await ctx.send(file=discord.File(output_path))

@bot.command('convert')
async def convert(ctx, url: str):
    name_file_pdf = download_and_convert(url)
    await ctx.send(f'Archivo {name_file_pdf} creado.', file=discord.File(name_file_pdf))

bot.run(TOKEN)

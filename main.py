import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from account import read_user_account
from book import safaribook

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

bot.run(TOKEN)

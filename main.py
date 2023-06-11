import os
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
from book import safaribook

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command('book')
async def hello(ctx, arg):
    book_id = arg
    output_path = await asyncio.to_thread(safaribook, book_id)
    await ctx.send(file=discord.File(output_path))

bot.run(TOKEN)

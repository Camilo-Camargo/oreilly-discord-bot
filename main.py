import os
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
    print(f'Retrieving book {book_id}')
    output_path = await safaribook(book_id)
    print(output_path)
    await ctx.send(file=discord.File(output_path))

bot.run(TOKEN)

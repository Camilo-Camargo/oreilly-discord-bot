import asyncio
import os
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
from book import safaribook
from convertor import download_and_convert, convert_pdf_to_word

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


"""@bot.command('book')
async def hello(ctx, arg):
    book_id = arg
    output_path = await asyncio.to_thread(safaribook, book_id)
    await ctx.send(file=discord.File(output_path))
"""
@bot.command('convert')
async def convert(ctx, url: str):
    try:
        await ctx.send("Downloading and converting the file... This may take some time.")

        name_file_pdf = await asyncio.to_thread(download_and_convert, url)

        await asyncio.sleep(1)

        await ctx.send(f'File {name_file_pdf} created.', file=discord.File(name_file_pdf))
    except Exception as e:
        await ctx.send("An error occurred during file conversion.")
        print(f"Error during conversion: {str(e)}")
        
@bot.command('doc')
async def convert(ctx, url: str):
    try:
        await ctx.send("Downloading and converting the file... This may take some time.")

        name_file_docx = await asyncio.to_thread(convert_pdf_to_word, url)

        await asyncio.sleep(1)

        await ctx.send(f'File {name_file_docx} created.', file=discord.File(name_file_docx))
    except Exception as e:
        await ctx.send("An error occurred during conversion to Word format.")
        print(f"Error during conversion: {str(e)}")
bot.run(TOKEN)
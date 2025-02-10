import discord
from discord.ext import commands
import asyncio

with open("tk.txt", "r") as file:
    TOKEN = file.read().strip()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def delete_messages(ctx):
    await ctx.message.delete()
    user = ctx.author
    channel = ctx.channel

    confirmation = await channel.send(f"{user.mention}, je vais supprimer tous vos messages. Confirmez avec ✅.")
    await confirmation.add_reaction("✅")

    def check(reaction, user_react):
        return user_react == user and str(reaction.emoji) == "✅"

    try:
        await bot.wait_for("reaction_add", timeout=30.0, check=check)
        await confirmation.delete()
    except asyncio.TimeoutError:
        await confirmation.edit(content="⏳ Temps écoulé. Annulation de la suppression.")
        return

    deleted = 0
    async for message in channel.history(limit=1000):
        if message.author == user:
            await message.delete()
            deleted += 1

    await channel.send(f"✅ {user.mention}, j'ai supprimé {deleted} de vos messages.", delete_after=5)

bot.run(TOKEN)

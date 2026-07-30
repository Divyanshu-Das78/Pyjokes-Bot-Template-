import discord
import pyjokes
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print (f"Logged on as {self.user}")
        # Sync slash commands
        await self.tree.sync()

    async def on_message(self,message):
        if message.author==self.user:
           return
        if message.content.startswith("!joke"):  #responds when u use !joke
           await message.channel.send(pyjokes.get_joke())
        if self.user.mentioned_in(message):      #responds when u ping bot
            await message.channel.send(pyjokes.get_joke())


intents=discord.Intents.default()
intents.message_content=True

client =Client(command_prefix="!",intents=intents)

#/command

@client.tree.command(name="joke",description="tells you a nerd joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.send_message(pyjokes.get_joke())

client.run("YOUR-BOT-TOKEN-GOES-HERE")
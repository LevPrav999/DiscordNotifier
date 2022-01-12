from Utils.alerter import send
from Utils.urlShortener import short

import discord
from discord.ext import commands

import config


class AntiCaps(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.title = "Anti-Caps System"

        self.type = config.CAPS_TYPE
        if self.type == 1:
            self.maximum = config.MAXIMUM_CAPS_LETTERS
        elif self.type == 2:
            self.maximum = config.MAXIMUM_CAPS_WORDS

    async def send_alert(self, message: discord.Message) -> None:
        send(
            self.title,
            f"Author: {message.author}" +
            f"\nChannel: {message.channel.name}" +
            f"\nLink to message: {short(message.jump_url)}"
        )

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.guild.id != config.GUILD_TO_LISTEN:
            return
        if message.channel.id in config.ALLOWED_CHANNELS_IDS:
            return

        count = 0
        if self.type == 1:
            for word in message.content.split(" "):
                for letter in word:
                    if letter.isupper():
                        count += 1
                    if count == self.maximum:
                        await self.send_alert(message)
                count = 0
        elif self.type == 2:
            for word in message.content.split(" "):
                if word.isupper():
                    count += 1
                if count == self.maximum:
                    await self.send_alert(message)


def setup(client):
    client.add_cog(AntiCaps(client))

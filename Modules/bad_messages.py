from discord.ext import commands

import config
from Utils.alerter import send
from Utils.urlShortener import short


async def make_it_normal(text):
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace("/", "")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace("'", "")
    text = text.replace("\"", "")
    text = text.replace("\\", "")
    text = text.replace("?", "")
    text = text.replace(" ", "")
    return text


class BadMessagesFinder(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.words = config.BAD_WORDS
        self.title = "Anti Bad Words System"

    @commands.Cog.listener()
    async def on_message(self, message) -> None:
        if message.guild.id != config.GUILD_TO_LISTEN:
            return
        if message.channel.id in config.ALLOWED_CHANNELS_IDS:
            return
        content = await make_it_normal(message.content)
        for word in self.words:
            if word.lower() in content.lower():
                send(
                    self.title,
                    f"Author: {message.author}" +
                    f"\nBad word: {word}" +
                    f"\nChannel: {message.channel.name}" +
                    f"\nLink to message: {short(message.jump_url)}"
                )


def setup(client):
    client.add_cog(BadMessagesFinder(client))

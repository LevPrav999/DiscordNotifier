from Utils.alerter import send

import discord
from discord.ext import commands, tasks

import config


class AntiSpam(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.title = "Anti-Spam System"

        self.delay = config.SPAM_DELAY

        self.spam_array = {}
        self.check_time.start()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.guild.id != config.GUILD_TO_LISTEN:
            return
        if message.channel.id in config.ALLOWED_CHANNELS_IDS:
            return

        if message.author.id not in self.spam_array.keys():
            self.spam_array[message.author.id] = {}
            self.spam_array[message.author.id]['message'] = 0
            self.spam_array[message.author.id]['time'] = 60

        self.spam_array[message.author.id]['message'] += 1

        if self.spam_array[message.author.id]['message'] >= self.delay:
            send(
                self.title,
                f"Member: {message.author}\nChannel: {message.channel.name}"
            )
            self.spam_array[message.author.id]['message'] = 0

    @tasks.loop(seconds=1.0)
    async def check_time(self) -> None:
        if len(self.spam_array):
            for member in self.spam_array.keys():
                if self.spam_array[member]['time'] != 0:
                    self.spam_array[member]['time'] -= 1
                else:
                    self.spam_array.pop(member)


def setup(client):
    client.add_cog(AntiSpam(client))

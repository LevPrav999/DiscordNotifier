import os
import discord
from discord.ext import commands
from colorama import Fore, Style, init

import config

TOKEN = config.TOKEN

client = commands.Bot(
    command_prefix="!",
    self_bot=True,
    chunk_guilds_at_startup=False
)
client.remove_command('help')
init()


@client.event
async def on_command_error(ctx, error) -> None:
    return print(Fore.RED + "[ERROR] " + Style.RESET_ALL + str(error))


for filename in os.listdir('./Modules'):
    if filename.endswith('.py'):
        client.load_extension(f'Modules.{filename[:-3]}')
        print(
            Fore.YELLOW + "[LOG] "
            + Style.RESET_ALL + f"Модуль {filename[:-3]} успешно загружен!"
        )


print(Fore.GREEN + "===================================" + Style.RESET_ALL)
print(
    Fore.CYAN + '|' +
    Style.RESET_ALL +
    '        Бот активирован!         ' + Fore.CYAN + '|'
    + Style.RESET_ALL
)
print(Fore.CYAN + "===================================" + Style.RESET_ALL)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure:
    print(Fore.RED + "[ERROR] " + Style.RESET_ALL + "Invalid token")

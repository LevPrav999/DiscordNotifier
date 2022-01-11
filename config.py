TOKEN = ""  # Your account token
BAD_WORDS = ["Привет", "Пока"]  # List of bad words
GUILD_TO_LISTEN = 0  # Guild's ID to listen

# The number of messages per minute from a user that will be considered spam
SPAM_DELAY = 15

ALLOWED_CHANNELS_IDS = []  # IDs of channels, where spam is allowed

"""
Caps Type
------
The type of message verification for the presence of caps.
If the parameter is 1, the number of letters written in caps
in words will be checked.
If the parameter is 2, the number of words completely written by caps
in the message will be checked.
------
If the parameter is set to 1, 
you don't have to specify the MAXIMUM_CAPS_WORDS value.

If the parameter is set as 2, 
you can omit the MAXIMUM_CAPS_LETTERS parameter
"""
CAPS_TYPE = 1
MAXIMUM_CAPS_WORDS = 2
MAXIMUM_CAPS_LETTERS = 5

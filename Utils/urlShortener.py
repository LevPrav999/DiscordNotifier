import pyshorteners


def short(link: str) -> str:
    shortener = pyshorteners.Shortener()
    link_shorted = shortener.tinyurl.short(link)
    return link_shorted

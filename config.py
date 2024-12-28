from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21335208"))
API_HASH = getenv("API_HASH", "4cb201499c03fe54f817617d27b336aa")

BOT_TOKEN = getenv("BOT_TOKEN", "7785413630:AAEW8JLe2Kpo8tWbPzV1RhZV-5FYEXHISnE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6626261440"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "-1002351224070")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "-1002398548749")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7252639965 1577166444").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

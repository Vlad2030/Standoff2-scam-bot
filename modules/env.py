# SO2 SCAM BOT BY github.com/Vlad2030

# Your bot ID t.me/BotFather
from environs import Env

env = Env()
env.read_env()

TOKEN: str = env.str("TOKEN")
DONATE_LINK: str = env.str("DONATE_LINK")

import os
API_ID = int(os.getenv("29008048"))
API_HASH = os.getenv("1b6ac0b75aa562970d3f3d66438bf650")
BOT_TOKEN = os.getenv("5839518492:AAFCI9SbzBlJ4cL-ZiSMx-6HGWgbhtLVpAc")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("5875452400", "").split()})

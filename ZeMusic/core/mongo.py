from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("يتم رفع البيانات...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Elhyba
    LOGGER(__name__).info("تم رفع البيانات.")
except:
    LOGGER(__name__).error("خطاء.  لم يتم رفع البيانات")
    exit()

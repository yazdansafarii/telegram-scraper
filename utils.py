import logging

# تنظیمات لاگ‌گیری (برای اینکه بفهمیم ربات چه می‌کند)
logging.basicConfig(
    format='[%(levelname)s] %(asctime)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def clean_message(text):
    """
    این تابع می‌تواند در آینده برای حذف لینک‌ها یا ایموجی‌ها توسعه یابد.
    فعلا فقط فضاهای خالی اضافه را حذف می‌کند.
    """
    if not text:
        return ""
    return text.strip()

def contains_keyword(text, keywords):
    """بررسی وجود کلمه کلیدی در متن"""
    if not text:
        return False
    text_lower = text.lower() # تبدیل به حروف کوچک برای جستجوی بهتر
    return any(k.lower() in text_lower for k in keywords)
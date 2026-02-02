import os
from dotenv import load_dotenv

# بارگذاری متغیرها از فایل .env
load_dotenv()

# اطلاعات اتصال
# مستقیم مقدار را جایگزین کنید
API_ID = 33220805
API_HASH = '45e921eeb6dd50e233b50d1761bebc91'

SESSION_NAME = os.getenv('SESSION_NAME')

# لیست کانال‌هایی که باید رصد شوند (یوزرنیم یا آیدی عددی)
SOURCE_CHANNELS = [
    '@varzesh3',
    '@khabarfouri',
    '@yazadntestbot'
    # -100123456789,  # مثال برای کانال خصوصی
]

# کلمات کلیدی (حساس به حروف کوچک و بزرگ نیست چون در کد هندل می‌کنیم)
KEYWORDS = [
    'دلار',
    
]

# تنظیمات ضد اسپم (ثانیه)
MIN_DELAY = 5
MAX_DELAY = 15
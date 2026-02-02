# 🚀 Telegram Keyword Monitor (Telethon Userbot)

A powerful, modular, and anti-spam Telegram userbot built with **Telethon**. It monitors specific channels (public or private) for certain keywords and saves matching messages directly to your **Saved Messages**.



## ✨ Features
* **Keyword Filtering:** Only captures messages you actually care about.
* **Private Channel Support:** Works with private channels using Peer IDs.
* **Anti-Spam System:** Randomized delays and FloodWait handling to prevent account bans.
* **Clean Architecture:** Separated config, utils, and main logic for easy scalability.
* **Environment Variables:** Keeps your API credentials safe.

## 🛠 Installation

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/yazdansafarii/telegram-monitor-bot.git](https://github.com/yazdansafarii/telegram-monitor-bot.git)
    cd telegram-monitor-bot
    ```

2.  **Set up Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install telethon python-dotenv python-socks
    ```

4.  **Configuration:**
    * Create a `.env` file and add your `API_ID` and `API_HASH`.
    * Edit `config.py` to add your target channels and keywords.

5.  **Run:**
    ```bash
    python main.py
    ```

---

# 🚀 ربات مانیتورینگ کلمات کلیدی تلگرام

این یک یوزربات تلگرام حرفه‌ای و ماژولار است که با کتابخانه **Telethon** نوشته شده. این ربات کانال‌های هدف (عمومی یا خصوصی) را رصد کرده و در صورت پیدا کردن کلمات کلیدی، پیام را در **Saved Messages** شما کپی می‌کند.

## ✨ قابلیت‌ها
* **فیلتر کلمات کلیدی:** فقط پیام‌هایی که برای شما مهم هستند ذخیره می‌شوند.
* **پشتیبانی از کانال‌های خصوصی:** قابلیت کار با کانال‌های بدون یوزرنیم از طریق ID.
* **سیستم ضد اسپم:** استفاده از وقفه تصادفی و مدیریت خطای FloodWait برای جلوگیری از مسدود شدن اکانت.
* **ساختار تمیز:** تفکیک فایل‌های تنظیمات و توابع کمکی برای توسعه آسان در آینده.
* **امنیت بالا:** استفاده از فایل محیطی برای مخفی نگه داشتن اطلاعات حساس.

## 🛠 نصب و راه‌اندازی

۱. **کلون کردن مخزن:**
```bash
git clone [https://github.com/yazdansafarii/telegram-monitor-bot.git](https://github.com/yazdansafarii/telegram-monitor-bot.git)
cd telegram-monitor-bot

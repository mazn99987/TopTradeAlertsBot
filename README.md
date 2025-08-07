
# Telegram Bot (aiogram v3) — Render Background Worker

## المتطلبات محليًا (اختياري)
- Python 3.10+
- إنشاء بيئة ثم تثبيت المتطلبات:
  ```bash
  python -m venv venv
  source venv/bin/activate  # ويندوز: venv\Scripts\activate
  pip install -r requirements.txt
  export TG_TOKEN=ضع_التوكن_هنا
  python bot.py
  ```

## النشر على Render (مُفضّل)
1) أنشئ Repo على GitHub وارفع هذه الملفات كما هي.
2) في Render: New -> Background Worker -> اختر المستودع.
3) لا تغيّر "startCommand" (هو: `python bot.py`).
4) بعد إنشاء الخدمة، افتح Settings -> Environment -> Add Variable:
   - Key: `TG_TOKEN`
   - Value: التوكن من BotFather
5) Deploy. عند اكتمال التشغيل سترى Logs تفيد بأن البوت بدأ يستقبل رسائل.

## أوامر البوت
- /start
- /help
- /news (مثال — سنربطه لاحقًا بمصادر السوق)

> ملاحظة: لا تحتاج Webhook على Render في وضع الـ Worker؛ البوت يعمل بالـ Polling 24/7 على الخطة المجانية.

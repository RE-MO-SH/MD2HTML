# Markdown to HTML Converter

A simple Python GUI application that converts Markdown text into an HTML document. It supports **RTL/LTR** direction, uses **B Nazanin** font for Persian text and **Times New Roman** for English, and provides an easy way to preview, save, or open the result in a browser.

---

## English

### Features
- Real‑time Markdown → HTML conversion
- Choose between **RTL** (right‑to‑left) and **LTR** (left‑to‑right) direction
- Beautiful default styling with Persian and English fonts
- Support for tables, fenced code blocks, and extra Markdown features
- Save the generated HTML to a `.html` file
- Open the output directly in your default browser (uses a temporary file if not saved)
- Handles `\n` as a literal newline (replace `\n` with actual line breaks)

### Requirements
- Python 3.6+
- [markdown](https://pypi.org/project/Markdown/) library

### Installation
1. Clone or download this repository.
2. Install the required package:
   ```bash
   pip install markdown

    Run the application:
    bash

    python converter.py

Usage

    Enter your Markdown text in the upper text area.

    Select the desired text direction (RTL or LTR).

    Click Convert – the HTML output appears in the lower text area.

    Use Save to HTML file to store the output permanently.

    Click Open in browser to view the rendered page.

Notes

    The font stack is set to 'B Nazanin', 'Times New Roman', serif – this gives priority to Persian text while falling back to Times New Roman for English characters.

    If you include \n in your input, it will be replaced with an actual newline (line break).

License

This project is open‑source and available under the MIT License.
فارسی
توضیحات

یک برنامهٔ سادهٔ گرافیکی با Tkinter که متن مارک‌دان را به اچ‌تی‌ام‌ال تبدیل می‌کند. این برنامه از جهت‌های RTL و LTR پشتیبانی کرده، برای متن فارسی از فونت «بی نازنین» و برای انگلیسی از «تایمز نیو رومن» استفاده می‌کند و امکان پیش‌نمایش، ذخیره و باز کردن خروجی در مرورگر را فراهم می‌آورد.
ویژگی‌ها

    تبدیل لحظه‌ای مارک‌دان به اچ‌تی‌ام‌ال

    انتخاب جهت RTL (راست‌به‌چپ) یا LTR (چپ‌به‌راست)

    استایل زیبا با فونت‌های مناسب فارسی و انگلیسی

    پشتیبانی از جداول، بلوک‌های کد و ویژگی‌های اضافی مارک‌دان

    ذخیرهٔ خروجی به فایل .html

    باز کردن خروجی در مرورگر پیش‌فرض (در صورت عدم ذخیره، از فایل موقت استفاده می‌شود)

    تبدیل \n به خط جدید واقعی

نیازمندی‌ها

    پایتون نسخهٔ ۳٫۶ یا بالاتر

    کتابخانهٔ markdown

نصب و اجرا

۱. مخزن را کلون یا دانلود کنید.
۲. کتابخانهٔ مورد نیاز را نصب کنید:
bash

pip install markdown

۳. برنامه را اجرا کنید:
bash

python converter.py

طریقهٔ استفاده

۱. متن مارک‌دان خود را در بخش بالایی وارد کنید.
۲. جهت متن مورد نظر (RTL یا LTR) را انتخاب کنید.
۳. روی دکمهٔ Convert کلیک کنید – خروجی اچ‌تی‌ام‌ال در بخش پایینی نمایش داده می‌شود.
۴. با دکمهٔ Save to HTML file می‌توانید فایل را ذخیره کنید.
۵. با دکمهٔ Open in browser خروجی را در مرورگر مشاهده کنید.
نکات

    ترتیب فونت‌ها به صورت 'B Nazanin', 'Times New Roman', serif است که اولویت با فونت فارسی بوده و برای کاراکترهای انگلیسی از تایمز نیو رومن استفاده می‌شود.

    اگر در ورودی از \n استفاده کنید، به خط جدید واقعی تبدیل خواهد شد.

مجوز

این پروژه متن‌باز بوده و تحت مجوز MIT در دسترس است.

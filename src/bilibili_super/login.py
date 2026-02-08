import base64
import json
import os
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import COOKIE_FILE, EDGE_UA


class BilibiliLogin:

    def __init__(self):
        self.login_url = f'https://passport.bilibili.com/login'
        options = Options()
        options.add_argument(f'--user-agent={EDGE_UA}')
        options.add_argument(f'--disable-blink-features=AutomationControlled')
        options.add_experimental_option('detach', False)  # 测试时使用
        options.add_argument("--headless=new")
        service = Service()
        self.driver = webdriver.Edge(service = service, options = options)
        self.wait = WebDriverWait(self.driver, 30)

    def _save_cookies(self):
        with open(COOKIE_FILE, 'w', encoding = 'utf-8') as f:
            json.dump(self.driver.get_cookies(), f, indent = 4)
        print('💾 Cookie saved')

    def _login_cookie(self):
        if not os.path.exists(COOKIE_FILE):
            print('❌ Cookie 不存在，需要扫码')
            return False

        with open(COOKIE_FILE, 'r', encoding='utf-8') as f:
            cookies = json.load(f)

        self.driver.get('https://www.bilibili.com')
        for c in cookies:
            if 'sameSite' in c and c['sameSite'] == 'None':
                c['sameSite'] = 'Strict'
            self.driver.add_cookie(c)

        self.driver.refresh()
        print('✅ Cookie 登录成功')
        return True

    def _login_qrcode(self):
        self.driver.get(self.login_url)

        qrcode_src = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="login-scan__qrcode"]//img')
            )
        ).get_attribute('src')

        img_bytes = base64.b64decode(qrcode_src.split(',')[1])
        qrcode = Image.open(BytesIO(img_bytes)).convert('RGBA')
        qrcode.show()
        print('📱 请扫码')
        if self.wait.until(lambda d: d.current_url.startswith('https://www.bilibili.com')):
            print('🎉 扫码成功')
            self._save_cookies()
            return True
        else:
            print('❌ 扫码失败')
            return False

    def login(self):
        # 1.尝试cookie登录
        if self._login_cookie():
            return self.driver, True

        # 2.qrcode登录
        elif self._login_qrcode():
            return self.driver, True

        else:
            print('❌ 登录失败')
            return self.driver, False
import base64
import json

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from .config import COOKIE_FILE, EDGE_UA


def load_cookies_and_uid():
    with open(COOKIE_FILE, 'r', encoding = 'utf-8') as f:
        cookies = json.load(f)

    uid = next(
        (c['value'] for c in cookies if c['name'] == 'DedeUserID'),
        None
    )

    if not uid:
        raise RuntimeError('DedeUserID not found in cookie file')
    cookies = '; '.join(f'{c["name"]}={c["value"]}' for c in cookies)
    return cookies, uid


def load_cookies():
    with open(COOKIE_FILE, 'r', encoding = 'utf-8') as f:
        cookies = json.load(f)
    return '; '.join(f'{c["name"]}={c["value"]}' for c in cookies)


def generate_dm_params():
    options = Options()
    options.add_argument(f"--user-agent={EDGE_UA}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless=new")

    driver = webdriver.Edge(service=Service(), options=options)

    try:
        driver.get("https://www.bilibili.com")

        js = """
        function getWebGLInfo() {
            const canvas = document.createElement("canvas");
            const gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");

            if (!gl) return null;

            const debugInfo = gl.getExtension("WEBGL_debug_renderer_info");

            const version = gl.getParameter(gl.VERSION);
            const renderer = debugInfo
                ? gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL)
                : gl.getParameter(gl.RENDERER);

            return [version, renderer];
        }
        return getWebGLInfo();
        """

        version, renderer = driver.execute_script(js)

        def to_base64(s: str):
            return base64.b64encode(s.encode()).decode()

        return {
            "DM_IMG_STR": to_base64(version)[:-2],
            "DM_COVER_IMG_STR": to_base64(renderer)[:-2],
        }

    finally:
        driver.quit()
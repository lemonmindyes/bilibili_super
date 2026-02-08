import asyncio
import json
import hashlib
import math
import time
from urllib.parse import quote

import httpx

from src.bilibili_super import DM_COVER_IMG_STR, DM_IMG_STR
from .config import *
from .utils import load_cookies, load_cookies_and_uid


class BilibiliUser:

    def __init__(self):
        self.cookies, self.uid = load_cookies_and_uid()
        self.headers = {
            'User-Agent': EDGE_UA,
            'Cookie': self.cookies,
        }

    def _build_following_urls(self, total: int, page_size: int = 24):
        total_pages = math.ceil(total / page_size)
        return [
            (
                "https://api.bilibili.com/x/relation/followings"
                f"?order=desc"
                f"&order_type="
                f"&vmid={self.uid}"
                f"&pn={i}"
                f"&ps={page_size}"
                f"&gaia_source=main_web"
                f"&web_location=333.1387"
            )
            for i in range(1, total_pages + 1)
        ]

    @staticmethod
    async def _fetch_page(client: httpx.AsyncClient, url: str):
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

    async def _get_all_followings(self):
        async with httpx.AsyncClient(headers = self.headers, timeout = 10.0) as client:
            # 1. 获取关注数
            total = self.get_following_count()
            total = total['data']['following']

            # 2. 构造分页 URL
            urls = self._build_following_urls(total)

            # 3. 并发抓取
            tasks = [self._fetch_page(client, url) for url in urls]
            pages = await asyncio.gather(*tasks)

        # 4. 汇总数据
        all_followings = []
        for page in pages:
            items = page.get('data', {}).get('list', [])
            all_followings.extend(items)
        with open('followings.json', 'w', encoding = 'utf-8') as f:
            json.dump(all_followings, f, ensure_ascii = False, indent = 4)
        return all_followings

    def get_following_count(self):
        with httpx.Client(headers = self.headers, timeout = 10.0) as client:
            url = f'https://api.bilibili.com/x/relation/stat'
            params = {'vmid': self.uid}
            response = client.get(url, params = params)
            response.raise_for_status()
            return response.json()

    def get_all_followings(self):
        return asyncio.run(self._get_all_followings())


class BilibiliUp:

    def __init__(self):
        self.cookies = load_cookies()
        self.headers = {
            'User-Agent': EDGE_UA,
            'Cookie': self.cookies,
        }

    @staticmethod
    def _sign(raw_query: str):
        sign_str = raw_query + MIXIN_KEY
        md5 = hashlib.md5()
        md5.update(sign_str.encode('utf-8'))
        return md5.hexdigest()

    async def _fetch_video_page(self, client, mid, pn):
        url = 'https://api.bilibili.com/x/space/wbi/arc/search'

        wts = int(time.time())

        params = {
            'pn': pn,
            'ps': 40,
            'tid': 0,
            'special_type': '',
            'order': 'pubdate',
            'mid': mid,
            'index': 0,
            'keyword': '',
            'order_avoided': 'true',
            'platform': 'web',
            'web_location': '333.1387',
            'dm_img_list': DM_IMG_LIST,
            'dm_img_str': DM_IMG_STR,
            'dm_cover_img_str': DM_COVER_IMG_STR,
            'dm_img_inter': DM_IMG_INTER,
            'wts': wts
        }

        # 构造签名字符串
        base_query = (
            f'dm_cover_img_str={DM_COVER_IMG_STR}&'
            f'dm_img_inter={quote(DM_IMG_INTER, safe="")}&'
            f'dm_img_list={quote(DM_IMG_LIST, safe="")}&'
            f'dm_img_str={DM_IMG_STR}&'
            f'index=0&keyword=&mid={mid}&'
            f'order=pubdate&order_avoided=true&'
            f'platform=web&pn={pn}&ps=40&'
            f'special_type=&tid=0&'
            f'web_location=333.1387&wts={wts}'
        )
        params['w_rid'] = self._sign(base_query)

        resp = await client.get(url, params = params)
        resp.raise_for_status()
        return resp.json()

    async def _get_up_video_list(self, up_name: str):
        up_info = self.get_up_info(up_name)
        mid = up_info['mid']
        videos = up_info['videos']

        ps = 40
        total_pages = math.ceil(videos / ps)

        async with httpx.AsyncClient(headers = self.headers, timeout = 10.0) as client:
            tasks = [
                self._fetch_video_page(client, mid, pn)
                for pn in range(1, total_pages + 1)
            ]
            results = await asyncio.gather(*tasks)

        all_videos = []
        for r in results:
            vlist = r['data']['list']['vlist']
            all_videos.extend(vlist)
        with open(f'{up_name}_video_list.json', 'w', encoding = 'utf-8') as f:
            json.dump(all_videos, f, ensure_ascii = False, indent = 4)
        return all_videos

    def get_up_info(self, up_name: str):
        wts = int(time.time())

        base_query = (
            f'__refresh__=true&_extra=&'
            f'ad_resource=5646&category_id=&'
            f'context=&duration=&'
            f'dynamic_offset=0&from_source=&'
            f'from_spmid=333.337&gaia_vtoken=&'
            f'highlight=1&keyword={up_name}&'
            f'order=&order_sort=0&'
            f'page=1&page_size=36&'
            f'platform=pc&pubtime_begin_s=0&'
            f'pubtime_end_s=0&qv_id=GMGeuAPZk7exW8ZwU4tarBMlgQYPqN71&'
            f'search_type=bili_user&single_column=0&'
            f'source_tag=3&user_type=0&'
            f'web_location=1430654&wts={wts}'
        )
        w_rid = self._sign(base_query)

        url = 'https://api.bilibili.com/x/web-interface/wbi/search/type'
        params = {
            'category_id': '',
            'search_type': 'bili_user',
            'ad_resource': '5646',
            '__refresh__': 'true',
            '_extra': '',
            'context': '',
            'page': '1',
            'page_size': '36',
            'order': '',
            'pubtime_begin_s': '0',
            'pubtime_end_s': '0',
            'duration': '',
            'from_source': '',
            'from_spmid': '333.337',
            'platform': 'pc',
            'highlight': '1',
            'single_column': '0',
            'keyword': up_name,
            'qv_id': 'GMGeuAPZk7exW8ZwU4tarBMlgQYPqN71',
            'source_tag': '3',
            'gaia_vtoken': '',
            'order_sort': '0',
            'user_type': '0',
            'dynamic_offset': '0',
            'web_location': '1430654',
            'w_rid': w_rid,
            'wts': wts,
        }

        with httpx.Client(timeout = 10.0) as client:
            resp = client.get(url, params = params, headers = self.headers)
            resp.raise_for_status()
            result = resp.json()['data']['result'][0]
            with open(f'{up_name}.json', 'w', encoding = 'utf-8') as f:
                json.dump(result, f, ensure_ascii = False, indent = 4)
            return result

    def get_up_video_list(self, up_name: str):
        return asyncio.run(self._get_up_video_list(up_name))

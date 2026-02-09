import asyncio
import json
import hashlib
import time
from urllib.parse import quote

import httpx

from .config import EDGE_UA, MIXIN_KEY
from .utils import load_cookies


class BilibiliVideo:

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

    async def _fetch_video_page(self, client: httpx.AsyncClient, query: str, pn: int):
        url = f'https://api.bilibili.com/x/web-interface/wbi/search/type'

        wts = int(time.time())
        base_query = (
            f'__refresh__=true&_extra=&'
            f'ad_resource=5654&category_id=&'
            f'context=&dynamic_offset=24&from_source=&'
            f'from_spmid=333.337&gaia_vtoken=&'
            f'highlight=1&keyword={quote("王者荣耀", safe="")}&'
            f'page={pn}&page_size=42&'
            f'platform=pc&pubtime_begin_s=0&'
            f'pubtime_end_s=0&qv_id=QUtrGkD6JWU8pRQqT4o5wTZ6uXvh7TSu&'
            f'search_type=video&single_column=0&'
            f'source_tag=3&web_location=1430654&'
            f'web_roll_page=1&wts={wts}'
        )
        w_rid = self._sign(base_query)

        params = {
            'category_id': '',
            'search_type': 'video',
            'ad_resource': '5654',
            '__refresh__': 'true',
            '_extra': '',
            'context': '',
            'page': f'{pn}',
            'page_size': 42,
            'pubtime_begin_s': '0',
            'pubtime_end_s': '0',
            'from_source': '',
            'from_spmid': '333.337',
            'platform': 'pc',
            'highlight': '1',
            'single_column': '0',
            'keyword': query,
            'qv_id': 'QUtrGkD6JWU8pRQqT4o5wTZ6uXvh7TSu',
            'source_tag': '3',
            'gaia_vtoken': '',
            'dynamic_offset': (pn - 1) * 24,
            'web_roll_page': 1,
            'web_location': '1430654',
            'w_rid': w_rid,
            'wts': wts,
        }

        resp = await client.get(url, params = params)
        resp.raise_for_status()
        return resp.json()

    async def _search_video(self, query: str, max_page: int = 5):
        async with httpx.AsyncClient(headers = self.headers, timeout = 10.0) as client:
            tasks = [
                self._fetch_video_page(client, query, pn)
                for pn in range(1, max_page + 1)
            ]
            results = await asyncio.gather(*tasks)

        all_videos = []
        for r in results:
            vlist = r['data']['result']
            all_videos.extend(vlist)
        with open(f'{query}_video_list.json', 'w', encoding = 'utf-8') as f:
            json.dump(all_videos, f, ensure_ascii = False, indent = 4)
        return all_videos

    def search_video(self, query: str, max_page: int = 5):
        return asyncio.run(self._search_video(query, max_page))

    def get_video_info(self, aid: int = None, bvid: str = None):
        with httpx.Client(headers = self.headers, timeout = 10.0) as client:
            url = f'https://uapis.cn/api/v1/social/bilibili/videoinfo'
            if aid is not None:
                params = {'aid': aid}
            else:
                params = {'bvid': bvid}
            resp = client.get(url, params = params)
            resp.raise_for_status()
            if aid is not None:
                with open(f'{aid}_video_info.json', 'w', encoding = 'utf-8') as f:
                    json.dump(resp.json(), f, ensure_ascii = False, indent = 4)
            else:
                with open(f'{bvid}_video_info.json', 'w', encoding = 'utf-8') as f:
                    json.dump(resp.json(), f, ensure_ascii = False, indent = 4)
            return resp.json()
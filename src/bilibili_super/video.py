import asyncio
import json
import hashlib
import math
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

    @staticmethod
    async def _fetch_json(client: httpx.AsyncClient, url: str):
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()

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

    async def _fetch_second_comment(self, oid: int | str, root: int | str, count: int):
        pages = math.ceil(count / 10) + 1

        reply_urls = [
            f'https://api.bilibili.com/x/v2/reply/reply?'
            f'oid={oid}&'
            f'type=1&'
            f'root={root}&'
            f'ps=10&'
            f'pn={i}&'
            f'web_location=333.788'
            for i in range(1, pages)
        ]

        async with httpx.AsyncClient(headers = self.headers, timeout = 10.0) as client:
            tasks = [
                self._fetch_json(client, url)
                for url in reply_urls
            ]
            results = await asyncio.gather(*tasks)
        replies = []
        for r in results:
            replies.extend(r['data']['replies'])
        return replies

    async def _fetch_popular_page(self, client: httpx.AsyncClient, pn: int):
        url = f'https://api.bilibili.com/x/web-interface/popular'
        wts = int(time.time())
        params = {
            'ps': 20,
            'pn': pn,
            'web_location': 333.934,
            'wts': wts
        }
        base_query = (
            f'pn={pn}&ps=20&'
            f'web_location=333.934&wts={wts}'
        )
        w_rid = self._sign(base_query)
        params['w_rid'] = w_rid
        resp = await client.get(url, params = params)
        resp.raise_for_status()
        return resp.json()

    async def _fetch_popular_video(self, max_page: int = 5):
        async with httpx.AsyncClient(headers = self.headers, timeout = 10.0) as client:
            tasks = [
                self._fetch_popular_page(client, i)
                for i in range(1, max_page + 1)
            ]
            results = await asyncio.gather(*tasks)

        popular_videos = []
        for r in results:
            popular_videos.extend(r['data']['list'])
        with open(f'popular_video_list.json', 'w', encoding = 'utf-8') as f:
            json.dump(popular_videos, f, ensure_ascii = False, indent = 4)
        return popular_videos

    # 根据关键词搜索视频并获取信息
    def search_video(self, query: str, max_page: int = 5):
        return asyncio.run(self._search_video(query, max_page))

    # 根据aid或bvid获取视频元数据
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

    # 根据oid或bvid获取视频评论(包括二级评论)
    def get_video_comment(self, oid: int | str, max_page: int = 50):
        result = []
        page = 1
        with httpx.Client(headers = self.headers, timeout = 10.0) as client:
            pagination_str = '{"offset":""}'
            while True and page <= max_page:
                url = 'https://api.bilibili.com/x/v2/reply/wbi/main'
                wts = int(time.time())
                params = {
                    'oid': oid,
                    'type': 1,
                    'mode': 3,
                    'pagination_str': pagination_str,
                    'plat': 1,
                    'seek_rpid': '',
                    'web_location': 1315875,
                    'wts': wts,
                }
                base_query = (
                    f'mode=3&oid={oid}&'
                    f'pagination_str={quote(pagination_str, safe = "")}&plat=1&seek_rpid=&'
                    f'type=1&web_location=1315875&wts={wts}'
                )
                w_rid = self._sign(base_query)
                params['w_rid'] = w_rid

                resp = client.get(url, params = params)
                resp.raise_for_status()
                tmp = []
                if resp.json()['data']['top_replies']:
                    tmp.extend(resp.json()['data']['top_replies'])
                tmp.extend(resp.json()['data']['replies'])
                # 获取二级评论
                for v in tmp:
                    if v['count'] > 0:
                        second_replies = asyncio.run(self._fetch_second_comment(oid, v['rpid'], v['rcount']))
                        v['replies'] = second_replies
                    else:
                        continue
                result.extend(tmp)
                if not resp.json()['data']['cursor']['pagination_reply']:
                    break
                next_offset = resp.json()['data']['cursor']['pagination_reply']['next_offset']
                pagination_str = json.dumps({'offset': next_offset})
                page += 1
                if page == 2:
                    del params['seek_rpid']

        with open(f'{oid}_video_comment.json', 'w', encoding = 'utf-8') as f:
            json.dump(result, f, ensure_ascii = False, indent = 4)
        return result

    # 获取热门视频(https://www.bilibili.com/v/popular/all)
    def get_popular_video(self, max_page: int = 5):
        return asyncio.run(self._fetch_popular_video(max_page))

    # 获取每周必看(https://www.bilibili.com/v/popular/weekly)
    def get_popular_weekly_video(self, number: int):
        # 1.获取总期数
        url = f'https://api.bilibili.com/x/web-interface/popular/series/list'
        wts = int(time.time())
        params = {
            'web_location': '333.934',
            'wts': wts
        }
        base_query = (
            f'web_location=333.934&wts={wts}'
        )
        w_rid = self._sign(base_query)
        params['w_rid'] = w_rid
        with httpx.Client(headers = self.headers, timeout = 10.0) as client:
            resp = client.get(url, params = params)
            resp.raise_for_status()
            max_number = resp.json()['data']['list'][0]['number']
            if number > max_number:
                raise ValueError(f'每周必看第 {number} 期不存在')
        # 2.获取当期每周必看视频
        url = f'https://api.bilibili.com/x/web-interface/popular/series/one'
        wts = int(time.time())
        params = {
            'number': number,
            'web_location': '333.934',
            'wts': wts
        }
        base_query = (
            f'number={number}&web_location=333.934&wts={wts}'
        )
        w_rid = self._sign(base_query)
        params['w_rid'] = w_rid
        with httpx.Client(headers = self.headers, timeout = 10.0) as client:
            resp = client.get(url, params = params)
            resp.raise_for_status()
            result = resp.json()['data']['list']
        with open(f'{number}_weekly_video_list.json', 'w', encoding = 'utf-8') as f:
            json.dump(result, f, ensure_ascii = False, indent = 4)
        return result


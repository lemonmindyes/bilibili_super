# bilibili-super

个人学习，bilibili信息获取(纯接口形式直接调用)，不要传播

## Install
```bash
pip install bilibili_super
```

## Usage

### login
使用 `BilibiliLogin.login()` 登录，如果没登陆过则会弹出二维码，扫码登录。
登录过则会有一个bilibili_cookies.json文件保存cookies，后续不需要二次登录。

```python
from bilibili_super import BilibiliLogin

Blogin = BilibiliLogin()
Blogin.login()
```

### user
#### 1.获取当前用户关注数
使用 `BilibiliUser.get_following_count()` 获取当前用户关注数
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
count = user.get_following_count()['data']['following']
print(count)
```

#### 2.获取当前用户关注up列表详细信息
使用 `BilibiliUser.get_all_followings()` 获取当前用户关注up列表详细信息
运行完毕会自动生成一个followings.json文件，里面包含所有关注的up详细信息
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
up_list = user.get_all_followings()
print(f'关注的up列表条数为：{len(up_list)}')
```

#### 3.获取当前用户动态信息
使用 `BilibiliUser.get_user_dynamic(max_page = 5)` 获取当前用户动态信息
运行完毕会自动生成一个dynamic.json文件，里面包含当前用户动态信息，爬取页数，默认为5
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
dynamic = user.get_user_dynamic(max_page = 5)
print(f'关注的up动态条数为：{len(dynamic)}')
```

#### 4.获取任意up信息
使用 `BilibiliUp.get_up_info(upname)` 获取任意up信息
运行完毕会自动生成一个upname.json文件，里面包含该up信息
```python
from bilibili_super import BilibiliUp

up = BilibiliUp()
result = up.get_up_info('金可鱼')
print(result)
```

#### 5.获取任意up的投稿视频列表信息
使用 `BilibiliUp.get_up_video_list(upname)` 获取任意up的投稿视频列表信息
运行完毕会自动生成一个upname_video_list.json文件，里面包含该up的投稿视频列表信息
```python
from bilibili_super import BilibiliUp

up = BilibiliUp()
result = up.get_up_video_list('金可鱼')
print(f'视频列表数为：{len(result)}')
```

### video
#### 1.根据关键词搜索视频并获取信息
使用 `BilibiliVideo.search_video(query, max_page = 5)` 根据关键词搜索视频并获取信息
运行完毕会自动生成一个query_video_list.json文件，里面包含搜索结果，可以修改
爬取页数，默认为5
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.search_video('金可鱼', max_page = 5)
print(f'获取到 {len(result)} 个视频')
```

#### 2.根据aid或bvid获取视频元数据
使用 `BilibiliVideo.get_video_info(aid | bvid)` 根据aid或bvid获取视频元数据
运行完毕会自动生成一个(aid | bvid)_video_info.json文件，里面包含视频元数据
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.get_video_info(bvid = 'BV1D7cwzkEFG')
print(result)
```
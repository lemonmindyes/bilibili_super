# 🔍 bilibili-super

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=lemonmindyes.bilibili_super)

个人学习，bilibili信息获取(纯接口形式直接调用)，不要传播

🎯 **简洁易用** • 🔧 **功能丰富** • 🚀 **高效稳定**

</div>

## 📦 安装

```bash
pip install bilibili_super
```

> 💡 **提示**: 需要 Python 3.10 或更高版本

## ⚠️ 注意事项

第一次使用请先运行login部分代码，会自动生成 `bilibili_cookies.json` 文件和
`dm_params.json` 文件，后续任何操作都不需要再次登录。

🔒 **安全提醒**: 请妥善保管生成的配置文件，避免泄露个人信息。

## Usage

### 🔐 登录认证

使用 `BilibiliLogin.login()` 登录，如果没登录过则会弹出二维码，扫码登录。
登录成功后会自动生成 `bilibili_cookies.json` 文件保存cookies，后续不需要二次登录。

✨ **特性**: 
- 📱 手机扫码登录
- 🍪 自动保存Cookie
- 🔐 安全可靠

```python
from bilibili_super import BilibiliLogin

Blogin = BilibiliLogin()
Blogin.login()
```

### user
#### 1️⃣ 获取当前用户关注数
使用 `BilibiliUser.get_following_count()` 获取当前用户关注数
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
count = user.get_following_count()['data']['following']
print(count)
```

#### 2️⃣ 获取当前用户关注UP列表详细信息
使用 `BilibiliUser.get_all_followings(is_save = True)` 获取当前用户关注UP列表详细信息，
is_save为True时，会自动生成一个 `followings.json` 文件，里面包含所有关注的UP详细信息，
否则不生成。
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
up_list = user.get_all_followings(is_save = True)
print(f'关注的up列表条数为：{len(up_list)}')
```

#### 3️⃣ 获取当前用户动态信息
使用 `BilibiliUser.get_user_dynamic(max_page = 5, is_save = True)` 获取当前用户动态信息
is_save为True时，会自动生成一个 `dynamic.json` 文件，里面包含当前用户动态信息，
否则不生成。默认爬取5页，可以修改。
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
dynamic = user.get_user_dynamic(max_page = 5, is_save = True)
print(f'关注的up动态条数为：{len(dynamic)}')
```

#### 4️⃣ 获取用户的关注数和粉丝数
使用 `BilibiliUser.get_relation_state()` 获取当前用户关注数和粉丝数
```python
from bilibili_super import BilibiliUser

user = BilibiliUser()
relation_state = user.get_relation_state()
print(relation_state)
```

#### 5️⃣ 获取任意UP信息
使用 `BilibiliUp.get_up_info(upname, is_save = True)` 获取任意UP信息，
is_save为True时，运行完毕会自动生成一个 `{upname}.json` 文件，里面包含该UP信息，
否则不生成。
```python
from bilibili_super import BilibiliUp

up = BilibiliUp()
result = up.get_up_info('金可鱼', is_save = True)
print(result)
```

#### 6️⃣ 获取任意UP的投稿视频列表信息
使用 `BilibiliUp.get_up_video_list(upname, is_save = True)` 获取任意UP的投稿视频列表信息，
is_save为True时，运行完毕会自动生成一个 `{upname}_video_list.json` 文件，里面包含该UP的投稿视频列表信息，
否则不生成。
```python
from bilibili_super import BilibiliUp

up = BilibiliUp()
result = up.get_up_video_list('金可鱼', is_save = True)
print(f'视频列表数为：{len(result)}')
```

### video
#### 1️⃣ 根据关键词搜索视频并获取信息
使用 `BilibiliVideo.search_video(query, max_page = 5, is_save = True)`根据关键词搜索视频并获取信息
is_save为True时，运行完毕会自动生成一个 `{query}_video_list.json` 文件，里面包含搜索结果，
否则不生成。默认爬取5页，可以修改。
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.search_video('金可鱼', max_page = 5, is_save = True)
print(f'获取到 {len(result)} 个视频')
```

#### 2️⃣ 根据aid或bvid获取视频元数据
使用 `BilibiliVideo.get_video_info(aid | bvid, is_save = True)` 根据aid或bvid获取视频元数据
is_save为True时，运行完毕会自动生成一个 `{aid|bvid}_video_info.json` 文件，里面包含视频元数据，
否则不生成。
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.get_video_info(bvid = 'BV1D7cwzkEFG', is_save = True)
print(result)
```

#### 3️⃣ 根据oid或bvid获取视频评论(包括二级评论)
使用 `BilibiliVideo.get_video_comment(oid | bvid, max_page = 50, is_save = True)` 
根据oid或bvid获取视频评论(包括二级评论)，is_save为True，运行完毕会自动生成一个
`{oid|bvid}_video_comment.json` 文件，里面包含视频评论，否则不生成。
爬取页数，默认为最大50，可以修改，如果不满50页，爬取完毕会自动退出。
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.get_video_comment(oid = 'BV1KMfoBnESY', max_page = 50, is_save = True)
count = 0
for v in result:
    count += 1
    if v['replies']:
        count += len(v['replies'])
print(count)
```

#### 4️⃣ 获取热门视频
使用 `BilibiliVideo.get_popular_video(max_page = 5, is_save = True)` 获取热门视频
is_save为True时，运行完毕会自动生成一个popular_video_list.json文件，否则不生成。
里面包含热门视频列表，爬取页数，默认为5，可以修改
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.get_popular_video(max_page = 5, is_save = True)
print(f'获取到 {len(result)} 个热门视频')
```

#### 5️⃣ 根据期数获取每周必看
使用 `BilibiliVideo.get_popular_weekly_video(number = 359, is_save = True)` 
根据期数获取每周必看，接口会自动分析当前最大期数，如果超出则会报错，is_save为True时，
运行完毕会自动生成一个 `{number}_weekly_video_list.json` 文件，否则不生成。
里面包含每周必看视频列表
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.get_popular_weekly_video(number = 359, is_save = True)
print(f'获取到 {len(result)} 个每周必看视频')
```

#### 6️⃣ 获取入站必刷视频
使用 `BilibiliVideo.get_popular_history_video(is_save = True)` 获取入站必刷视频
is_save为True时，运行完毕会自动生成一个popular_history_video_list.json文件，否则不生成。
里面包含入站必刷视频列表
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
result = video.get_popular_history_video(is_save = True)
print(f'获取到 {len(result)} 个入站必刷视频')
```

#### 7️⃣ 获取排行榜视频
使用 `BilibiliVideo.get_popular_rank(query = 'all', is_save = True)` 获取排行榜视频
is_save为True时，运行完毕会自动生成一个 `{query}_rank_list.json` 文件，否则不生成。
query参数可以参考`https://www.bilibili.com/v/popular/rank/all`
和`https://www.bilibili.com/v/popular/rank/anime`
的末尾参数，也可以用ctrl查看函数有参数介绍
```python
from bilibili_super import BilibiliVideo

video = BilibiliVideo()
query = 'all'
result = video.get_popular_rank(query = query, is_save = True)
print(f'获取到 {len(result)} 个{query}排行榜视频')
```

# 免责声明
<div id="disclaimer"> 

## 1. 项目目的与性质
本项目（以下简称“本项目”）是作为一个技术研究与学习工具而创建的，旨在探索和学习网络数据采集技术。本项目专注于自媒体平台的数据爬取技术研究，旨在提供给学习者和研究者作为技术交流之用。

## 2. 法律合规性声明
本项目开发者（以下简称“开发者”）郑重提醒用户在下载、安装和使用本项目时，严格遵守中华人民共和国相关法律法规，包括但不限于《中华人民共和国网络安全法》、《中华人民共和国反间谍法》等所有适用的国家法律和政策。用户应自行承担一切因使用本项目而可能引起的法律责任。

## 3. 使用目的限制
本项目严禁用于任何非法目的或非学习、非研究的商业行为。本项目不得用于任何形式的非法侵入他人计算机系统，不得用于任何侵犯他人知识产权或其他合法权益的行为。用户应保证其使用本项目的目的纯属个人学习和技术研究，不得用于任何形式的非法活动。

## 4. 免责声明
开发者已尽最大努力确保本项目的正当性及安全性，但不对用户使用本项目可能引起的任何形式的直接或间接损失承担责任。包括但不限于由于使用本项目而导致的任何数据丢失、设备损坏、法律诉讼等。

## 5. 知识产权声明
本项目的知识产权归开发者所有。本项目受到著作权法和国际著作权条约以及其他知识产权法律和条约的保护。用户在遵守本声明及相关法律法规的前提下，可以下载和使用本项目。

## 6. 最终解释权
关于本项目的最终解释权归开发者所有。开发者保留随时更改或更新本免责声明的权利，恕不另行通知。
</div>
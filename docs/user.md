# user接口文档

## 1.获取当前用户关注数
### 接口基本信息
```text
接口名称：获取当前用户关注数
请求方式：GET
请求地址：https://api.bilibili.com/x/relation/stat
库中接口：BilibiliUser().get_following_count()
```

### 请求参数
#### Query参数

| 参数名 |     类型      | 必填 | 默认值 |  描述  |
| :----: | :-----------: | :--: | :----: | :----: |
|  vmid  | int \| string |  是  |   无   | 用户ID |

#### Header参数

|   参数名   |  类型  | 必填 |    描述    |
| :--------: | :----: | :--: | :--------: |
| User-Agent | string |  是  |  用户代理  |
|   Cookie   | string |  是  | 用户Cookie |

### 返回参数说明

```json
{
    "code": 0, // 状态码，0表示成功
    "message": "0", // 提示信息
    "ttl": 1, // 缓存时间
    "data": { // 关键数据
        "mid": 628904447, // ⭐用户ID
        "following": 169, // ⭐关注数
        "whisper": 0, //
        "black": 1, // 黑名单数量
        "follower": 8, // ⭐粉丝数
        "fans_medal_toast": null, //
        "fans_effect": null //
    }
}
```

## 2.获取当前用户关注up列表详细信息

### 接口基本信息

```text
接口名称：获取当前用户关注up列表详细信息
请求方式：GET
请求地址：https://api.bilibili.com/x/relation/followings
库中接口：BilibiliUser().get_all_followings(is_save = True)
```

## 请求参数

#### Query参数

|    参数名    |     类型      | 必填 |  默认值  |             描述             |
| :----------: | :-----------: | :--: | :------: | :--------------------------: |
|    order     |    string     |  是  |   desc   |           排序方式           |
|  order_type  |               |  否  |    空    |           排序类型           |
|     vmid     | int \| string |  是  |    无    |            用户ID            |
|      pn      | int \| string |  是  |    1     |       第几页，从1开始        |
|      ps      | int \| string |  是  |    24    | 每页多少关注数（建议不调整） |
| gaia_source  |    string     |  是  | main_web |         请求来源标识         |
| web_location |    string     |  是  | 333.1387 |         页面位置编号         |

#### Header参数

|   参数名   |  类型  | 必填 |    描述    |
| :--------: | :----: | :--: | :--------: |
| User-Agent | string |  是  |  用户代理  |
|   Cookie   | string |  是  | 用户Cookie |

### 返回参数说明(本接口只提取了所有list数据，有多少个关注，就有多少个{})

```json
{
    "code": 0, // 状态码，0表示成功
    "message": "0", // 提示信息
    "ttl": 1, // 缓存时间
    "data": { // 关键数据
        "list": [ // ⭐当前页的用户关注列表，有ps默认24个，只展开一个讲解
            {
                "mid": 383115030, // ⭐用户ID
                "attribute": 2, // 关注关系类型
                "mtime": 1770737860, // ⭐最近关注时间（秒级时间戳）
                "tag": null,
                "special": 0,
                "contract_info": {},
                "uname": "工科博士小魔女", // ⭐用户名
                "face": "https://i0.hdslb.com/bfs/face/609646f2d4391cda0c9d747f2766162aa0366249.jpg", // ⭐头像URL
                "sign": "卡牌爱好者。\n2026重点更新科研小知识系列。\n鹅群：1058179702。", // ⭐个性签名
                "face_nft": 0, // 是否NFT头像（0为普通头像）
                "handle": "",
                "official_verify": { // ⭐官方认证字段
                    "type": -1, // 认证类型（-1：无认证、0：个人认证、1、机构认证）
                    "desc": "" // 认证说明
                },
                "vip": { // vip会员字段
                    "vipType": 2, // 会员类型（2：年度大会员）
                    "vipDueDate": 1772294400000,
                    "dueRemark": "",
                    "accessStatus": 0,
                    "vipStatus": 1, // 是否是有效会员（0：不是会员，1：会员）
                    "vipStatusWarn": "",
                    "themeType": 0, // 主题类型
                    "label": { // UI标签信息
                        "path": "http://i0.hdslb.com/bfs/vip/label_annual.png",
                        "text": "年度大会员",
                        "label_theme": "annual_vip",
                        "text_color": "#FFFFFF",
                        "bg_style": 1,
                        "bg_color": "#FB7299",
                        "border_color": ""
                    },
                    "avatar_subscript": 1,
                    "nickname_color": "#FB7299", // 昵称颜色
                    "avatar_subscript_url": ""
                },
                "name_render": {},
                "nft_icon": "",
                "rec_reason": "",
                "track_id": "",
                "follow_time": "" // 关注时间（空）
            },
        ],
        "re_version": 0, // 
        "total": 169 // 总关注人数
    }
}
```

## 3.获取当前用户动态信息（只列出主要字段信息，代码接口只将items中的元素全部放入列表中返回）

### 接口基本信息

```text
接口名称：获取当前用户动态信息
请求方式：GET
请求地址：https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all
库中接口：BilibiliUser().get_user_dynamic(max_page = 5, is_save = True)
```

## 请求参数

|         参数名         |  类型  | 必填 |  默认值  |            描述            |
| :--------------------: | :----: | :--: | :------: | :------------------------: |
|    timezone_offset     |  int   |  是  |   -480   |         时区偏移量         |
|          type          | string |  是  |   all    |          全部动态          |
|        platform        | sting  |  是  |   web    |          平台类型          |
|         offset         |  int   |  是  |   None   | 分页游标（page = 1：None） |
|          page          |  int   |  是  |    1     |      页码（从1开始）       |
|        features        | string |  是  |          |          功能开关          |
|      web_location      | string |  是  | 333.1365 |        页面来源标识        |
| x-bili-device-req-json | string |  是  |          |        设备指纹参数        |

#### Header参数

|   参数名   |  类型  | 必填 |    描述    |
| :--------: | :----: | :--: | :--------: |
| User-Agent | string |  是  |  用户代理  |
|   Cookie   | string |  是  | 用户Cookie |

### 返回参数说明

| 字段名  |  类型  |      描述       |
| :-----: | :----: | :-------------: |
|  code   |  int   |  基础索引信息   |
|  data   | object |  动态自身的 ID  |
| message | string | ⭐动态的主体数据 |
|   ttl   |  int   |    缓存时间     |

#### data字段

|     字段名      |  类型  |      描述      |
| :-------------: | :----: | :------------: |
|    has_more     |  bool  | 是否还有下一页 |
|      items      | object | ⭐动态主体数据  |
|     offset      | string |  ⭐下一页游标   |
| update_baseline | string |                |
|   update_num    |  int   |                |

#### items字段

| 字段名  |  类型  |                            描述                             |
| :-----: | :----: | :---------------------------------------------------------: |
|  basic  | object |                          基础信息                           |
| id_str  | string |                         动态唯一ID                          |
| modules | object |                        ⭐动态内容主体                        |
|  orig   | object | ⭐被转发的原始动态（只有动态里有转发别人的动态才有这个字段） |
|  type   | string |                          动态类型                           |
| visible |  bool  |                          是否可见                           |

#### basic字段

```json
"basic": {
    "comment_id_str": "116049143923097", // 评论ID
    "comment_type": 1, // 评论类型，1：视频
    "like_icon": {
        "action_url": "",
        "end_url": "",
        "id": 0,
        "start_url": ""
    },
    "rid_str": "116049143923097" // 动态唯一ID的另一种名字
},
```

#### modules字段

|     字段名     |  类型  |     描述      |
| :------------: | :----: | :-----------: |
| module_author  | object | ⭐作者信息模块 |
| module_dynamic | object | ⭐动态内容主体 |
|  module_more   | object | 更多操作模块  |
|  module_stat   | object | ⭐互动统计模块 |

#### module_author字段

|      字段名       |  类型  |            描述             |
| :---------------: | :----: | :-------------------------: |
|      avatar       | object |   头像容器信息（UI字段）    |
|       face        | string |        ⭐用户头像URL         |
|     face_nft      |  bool  |         是否NFT头像         |
|     following     |  bool  |      是否已关注该用户       |
|     jump_url      | string |        用户空间链接         |
|       label       | string |      标签（通常为空）       |
|        mid        |  int   |     ⭐用户ID（唯一标识）     |
|       name        | string |           ⭐用户名           |
|  official_verify  | object |        ⭐官方认证信息        |
|      pendant      | object |   头像挂件信息（UI字段）    |
|    pub_action     | string |        发布动作描述         |
| pub_location_text | string |        发布位置文本         |
|     pub_time      | string | 相对发布时间（如“5分钟前”） |
|      pub_ts       |  int   |       ⭐发布时间戳（秒       |
|       type        | string |          作者类型           |

#### official_verify & vip字段

```json
"official_verify": { // ⭐官方认证字段
    "type": -1, // 认证类型（-1：无认证、0：个人认证、1、机构认证）
    "desc": "" // 认证说明
},
"vip": { // vip会员字段
    "vipType": 2, // 会员类型（2：年度大会员）
    "vipDueDate": 1772294400000,
    "dueRemark": "",
    "accessStatus": 0,
    "vipStatus": 1, // 是否是有效会员（0：不是会员，1：会员）
    "vipStatusWarn": "",
    "themeType": 0, // 主题类型
    "label": { // UI标签信息
        "path": "http://i0.hdslb.com/bfs/vip/label_annual.png",
        "text": "年度大会员",
        "label_theme": "annual_vip",
        "text_color": "#FFFFFF",
        "bg_style": 1,
        "bg_color": "#FB7299",
        "border_color": ""
    },
    "avatar_subscript": 1,
    "nickname_color": "#FB7299", // 昵称颜色
    "avatar_subscript_url": ""
},
```

#### module_dynamic字段

```json
"module_dynamic": { // ⭐动态内容主体模块
    "additional": null, // 附加内容模块（如投票、商品卡片等，当前为空）
    "desc": null, // 动态文本描述（纯文字或视频附带文案，此处为空）
    "major": { // ⭐主要内容模块（决定动态的核心类型）
        "archive": { // ⭐视频内容对象
            "aid": "116046207915999", // 视频AV号（旧版视频ID）
            "badge": { //
                "bg_color": "#FB7299", //
                "color": "#FFFFFF", //
                "icon_url": "https://i0.hdslb.com/bfs/activity-plat/static/20230112/3b3c5705bda98d50983f6f47df360fef/qcRJ6sJU91.png",
                "text": "充电专属" // 角标文字（投稿视频、充电专属）
            },
            "bvid": "BV1JpFQzbEQP", // ⭐视频BV号（当前主流视频ID）
            "cover": "http://i1.hdslb.com/bfs/archive/e2d9560e29847cdf8300b6581abd62723fd4dee9.jpg", // 视频封面图
            "desc": "", // 视频简介（简略版）
            "disable_preview": 1, //
            "duration_text": "05:24", // 视频时长文本
            "jump_url": "//www.bilibili.com/video/BV1JpFQzbEQP/", // ⭐视频跳转链接
            "stat": { // 视频统计信息
                "danmaku": "0", // 弹幕数
                "play": "139" // 播放量
            },
            "title": "第366集（s）", // ⭐视频标题
            "type": 1 // 视频类型（通常1=普通视频）
        },
        "type": "MAJOR_TYPE_ARCHIVE" // ⭐主要内容类型（视频动态）
    },
    "topic": null // 动态话题信息（如#话题#，当前为空）
}
```


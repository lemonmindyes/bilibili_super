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

#### Query

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
|  code   |  int   |     状态码      |
|  data   | object | ⭐动态的主体数据 |
| message | string |    提示信息     |
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

## 4.获取任意UP信息

### 接口基本信息

```text
接口名称：获取任意UP信息
请求方式：GET
请求地址：https://api.bilibili.com/x/web-interface/wbi/search/type
库中接口：BilibiliUp().get_up_info('金可鱼', is_save = True)
```

## 请求参数

#### Query参数

|     参数名      |  类型  | 必填 |  默认值   |                         描述                         |
| :-------------: | :----: | :--: | :-------: | :--------------------------------------------------: |
|   category_id   | string |  是  |           |              分类ID（用户搜索一般为空）              |
|   search_type   | string |  是  | bili_user |                 搜索类型（用户搜索）                 |
|   ad_resource   | string |  是  |   5646    |                                                      |
|   __refresh__   | string |  是  |   true    |                   是否刷新请求标识                   |
|     _extra      | string |  是  |           |                                                      |
|     context     | string |  是  |           |                                                      |
|      page       |  int   |  是  |     1     |            ⭐页码（这个场景下请不要修改）             |
|    page_size    |  int   |  是  |    36     |        ⭐每页返回数量（这个场景下请不要修改）         |
|      order      | string |  是  |           |                 排序方式（默认综合）                 |
| pubtime_begin_s |  int   |  是  |     0     |                                                      |
|  pubtime_end_s  |  int   |  是  |     0     |                                                      |
|    duration     | string |  是  |           |                                                      |
|   from_source   | string |  是  |           |                                                      |
|   from_spmid    | string |  是  |  333.337  |                                                      |
|    platform     | string |  是  |    pc     |                    客户端平台类型                    |
|    highlight    |  int   |  是  |     1     |                                                      |
|  single_column  |  int   |  是  |           |                                                      |
|     keyword     | string |  是  |           |                ⭐搜索关键词（用户名）                 |
|      qv_id      | string |  是  |  随机值   | 查询追踪ID（默认：GMGeuAPZk7exW8ZwU4tarBMlgQYPqN71） |
|   source_tag    | string |  是  |     3     |                                                      |
|   gaia_vtoken   | string |  是  |           |                                                      |
|   order_sort    |  int   |  是  |     0     |                                                      |
|    user_type    |  int   |  是  |     0     |                                                      |
| dynamic_offset  |  int   |  是  |     0     |                                                      |
|  web_location   | string |  是  |  1430654  |                                                      |
|      w_rid      | string |  是  |           |                 ⭐签名参数（WBI签名）                 |
|       wts       |  int   |  是  | 当前时间  |                  ⭐时间戳（签名用）                   |

#### Header参数

|   参数名   |  类型  | 必填 |    描述    |
| :--------: | :----: | :--: | :--------: |
| User-Agent | string |  是  |  用户代理  |
|   Cookie   | string |  是  | 用户Cookie |

### 返回参数说明

| 字段名  |  类型  |      描述       |
| :-----: | :----: | :-------------: |
|  code   |  int   |     状态码      |
|  data   | object | ⭐动态的主体数据 |
| message | string |    提示信息     |
|   ttl   |  int   |    缓存时间     |

#### data字段

|     字段名      |  类型  |        描述         |
| :-------------: | :----: | :-----------------: |
|      seid       | string |     搜索会话ID      |
|      page       |  int   |      ⭐当前页码      |
|    pagesize     |  int   | ⭐每页返回的结果数量 |
|   numResults    |  int   |    搜索结果总数     |
|    numPages     |  int   |       总页数        |
| suggest_keyword | string |                     |
|    rqt_type     | string |      请求类型       |
|    exp_list     | object |  实验参数（忽略）   |
|     egg_hit     |  int   |      彩蛋标识       |
|     result      | object |    ⭐搜索结果列表    |
|   show_column   |  int   |      展示模式       |
|  in_black_key   |  int   |                     |
|  in_white_key   |  int   |                     |

#### result字段

```json
{
    "type": "bili_user", // 结果类型（固定为用户搜索结果）
    "mid": 588753764, // ⭐用户ID（唯一标识）
    "uname": "金可鱼", // ⭐用户名
    "usign": "忍耐到底，必然得救。\n微博：-金可鱼-  \n商务2663616010@qq.com ", // ⭐用户个性签名
    "fans": 227097, // ⭐粉丝数
    "videos": 173, // ⭐投稿视频数量
    "upic": "//i0.hdslb.com/bfs/face/5273b00710f6abf2ea7b7603ed6539f40cbfc781.jpg", // ⭐用户头像URL
    "face_nft": 0,
    "face_nft_type": 0,
    "verify_info": "",
    "level": 6, // 用户等级（1~6级）
    "gender": 2, // 性别（1=男，2=女）
    "is_upuser": 1, // 是否为UP主（0=不是，1=是）
    "is_live": 0, // 是否正在直播（0=不在直播中，1=直播中）
    "room_id": 24479157, // 直播间ID（若存在）
    "res": [ // ⭐代表性视频列表（通常为最近或热门投稿）只展示三个
      {
        "aid": 116041023889041, // ⭐视频AV号
        "bvid": "BV1sNcgz9E4p", // ⭐视频BV号
        "title": "青春的感觉", // ⭐视频标题
        "pubdate": 1770646076, // ⭐发布时间戳（秒）
        "arcurl": "http://www.bilibili.com/video/av116041023889041", // ⭐视频跳转链接
        "pic": "//i1.hdslb.com/bfs/archive/54394bd64a7bc73fb6d99fb04c35f173c5c73dec.jpg", // ⭐视频封面
        "play": "24790", // ⭐播放量
        "dm": 26, // ⭐弹幕数
        "coin": 119, // ⭐投币数
        "fav": 231, // ⭐收藏数
        "desc": "-", // ⭐视频简介
        "duration": "2:43", // ⭐视频时长
        "is_pay": 0,
        "is_union_video": 0,
        "is_charge_video": 0,
        "vt": 0,
        "enable_vt": 0,
        "vt_display": ""
      },
      {
        "aid": 115983142360244,
        "bvid": "BV11C6vB3EBN",
        "title": "狐主任：原来你也好这口…",
        "pubdate": 1770386400,
        "arcurl": "http://www.bilibili.com/video/av115983142360244",
        "pic": "//i2.hdslb.com/bfs/archive/590b3d3813823528c84c290dea89b2eb31ab276a.jpg",
        "play": "35659",
        "dm": 32,
        "coin": 131,
        "fav": 222,
        "desc": "-",
        "duration": "2:47",
        "is_pay": 0,
        "is_union_video": 0,
        "is_charge_video": 0,
        "vt": 0,
        "enable_vt": 0,
        "vt_display": ""
      },
      {
        "aid": 115984518157684,
        "bvid": "BV13z6zBhEiB",
        "title": "我也妹眨眼啊",
        "pubdate": 1769783449,
        "arcurl": "http://www.bilibili.com/video/av115984518157684",
        "pic": "//i2.hdslb.com/bfs/archive/434e1bf7bde151fce911dd14cdf9b7abd784535c.jpg",
        "play": "34925",
        "dm": 16,
        "coin": 220,
        "fav": 271,
        "desc": "-",
        "duration": "1:57",
        "is_pay": 0,
        "is_union_video": 0,
        "is_charge_video": 0,
        "vt": 0,
        "enable_vt": 0,
        "vt_display": ""
      }
    ],
    "official_verify": { // ⭐官方认证字段
      "type": 0, // 认证类型（-1：无认证、0：个人认证、1、机构认证）
      "desc": "bilibili 知名UP主" // 认证说明
    },
    "hit_columns": [

    ],
    "is_senior_member": 0
},
```

## 5.获取任意up的投稿视频列表信息（只整合vlist数据进行返回）

### 接口基本信息

```text
接口名称：获取任意up的投稿视频列表信息
请求方式：GET
请求地址：https://api.bilibili.com/x/space/wbi/arc/search
库中接口：BilibiliUp().get_up_video_list('金可鱼', is_save = True)
```

## 请求参数

#### Query参数

|      参数名      |  类型  | 必填 |   默认值   |               描述                |
| :--------------: | :----: | :--: | :--------: | :-------------------------------: |
|        pn        |  int   |  是  |     1      |               ⭐页码               |
|        ps        |  int   |  是  |     40     |           ⭐每页返回数量           |
|       tid        |  int   |  是  |     0      |                                   |
|   special_type   | string |  是  |            |                                   |
|      order       | string |  是  |  pubdate   | 排序方式，如：pubdate（发布时间） |
|       mid        |  int   |  是  |            |        ⭐用户ID（唯一标识）        |
|      index       |  int   |  是  |     0      |                                   |
|     keyword      | string |  是  |            |                                   |
|  order_avoided   |  bool  |  是  |    true    |       是否避免默认排序策略        |
|     platform     | string |  是  |    web     |             平台类型              |
|   web_location   | string |  是  |  333.1387  |                                   |
|   dm_img_list    | string |  是  |            |      浏览器指纹轨迹数据列表       |
|    dm_img_str    | string |  是  |            |        WebGL 渲染信息指纹         |
| dm_cover_img_str | string |  是  |            |         GPU/显卡相关指纹          |
|   dm_img_inter   | string |  是  |            |         页面交互行为数据          |
|      w_rid       | string |  是  |            |          ⭐WBI 签名校验值          |
|       wts        |  int   |  是  | 当前时间戳 |          ⭐WBI 时间戳参数          |

#### Header参数

|   参数名   |  类型  | 必填 |    描述    |
| :--------: | :----: | :--: | :--------: |
| User-Agent | string |  是  |  用户代理  |
|   Cookie   | string |  是  | 用户Cookie |

### 返回参数说明

| 字段名  |  类型  |   描述    |
| :-----: | :----: | :-------: |
|  code   |  int   |  状态码   |
|  data   | object | ⭐主体数据 |
| message | string | 提示信息  |
|   ttl   |  int   | 缓存时间  |

#### data字段

|     字段名      |  类型  |               描述                |
| :-------------: | :----: | :-------------------------------: |
| episodic_button | object |                                   |
|    gaia_data    |  null  |                                   |
|  gaia_res_type  |  int   | Gaia 风控响应类型，0 表示正常状态 |
|     is_risk     |  bool  |       是否被判定为风险请求        |
|      list       | object |           ⭐投稿信息列表           |
|      page       | object | ⭐分页信息（页码、每页数量、总数） |

#### list字段

| 字段名 |  类型  |                  描述                   |
| :----: | :----: | :-------------------------------------: |
| slist  |  list  |                                         |
| tlist  | object |  ⭐分区统计信息，表示各分区下的视频数量  |
| vlist  |  list  | ⭐实际的视频详细列表数据（核心数据字段） |

#### tlist

```json
"tlist": {
    "155": {
        "tid": 155, // B站视频所属的分区（内容分类）ID
        "count": 6,
        "name": "时尚"
    },
    "160": {
        "tid": 160,
        "count": 151,
        "name": "生活"
    },
    "188": {
        "tid": 188,
        "count": 5,
        "name": "科技"
    },
    "223": {
        "tid": 223,
        "count": 1,
        "name": "汽车"
    },
    "36": {
        "tid": 36,
        "count": 6,
        "name": "知识"
    },
    "4": {
        "tid": 4,
        "count": 4,
        "name": "游戏"
    }
},
```

#### vlist(list里面有同样的很多object，介绍其中一个)

```json
{
    "comment": 495, // ⭐ 评论数量
    "typeid": 21, // ⭐ 视频子分区ID
    "play": 353826, // ⭐ 播放量
    "pic": "http://i0.hdslb.com/bfs/archive/5b5cd650b9e3c6cb46bd252746f0ee49ed32a69f.jpg", // ⭐ 视频封面URL
    "subtitle": "",
    "description": "谢谢这位宝子！好看！喜欢！", // ⭐ 视频描述
    "copyright": "1", // ⭐ 版权类型（1=自制，2=转载）
    "title": "粉丝寄啥我穿啥挑战！有点意思…", // ⭐ 视频标题
    "review": 0,
    "author": "金可鱼", // ⭐ UP主名称
    "mid": 588753764, // ⭐用户ID（唯一标识）
    "created": 1749477592, // ⭐ 发布时间戳（秒）
    "length": "01:17", // ⭐ 视频时长
    "video_review": 135, // ⭐ 弹幕数量
    "aid": 114653749318583, // ⭐ 视频AV号
    "bvid": "BV1PNTiz3EqG", // ⭐ 视频BV号
    "hide_click": false,
    "is_pay": 0,
    "is_union_video": 0,
    "is_steins_gate": 0,
    "is_live_playback": 0,
    "is_lesson_video": 0,
    "is_lesson_finished": 0,
    "lesson_update_info": "",
    "jump_url": "",
    "meta": null,
    "is_avoided": 0,
    "season_id": 0,
    "attribute": 8405376,
    "is_charging_arc": false,
    "elec_arc_type": 0,
    "elec_arc_badge": "",
    "vt": 0,
    "enable_vt": 0,
    "vt_display": "",
    "playback_position": 0,
    "is_self_view": false,
    "view_self_type": 0
},
```


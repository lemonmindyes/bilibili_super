import os

BASE_DIR = os.getcwd()
COOKIE_FILE = os.path.join(BASE_DIR, "bilibili_cookies.json")
DM_PARAM_FILE = os.path.join(BASE_DIR, "dm_params.json")
EDGE_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
)

# 加密
MIXIN_KEY = 'ea1db124af3c7062474693fa704f4ff8'

DM_IMG_INTER = '{"ds":[{"t":7,"c":"dnVpX2J1dHRvbiB2dWlfYnV0dG9uLS1hY3RpdmUgdnVpX2J1dHRvbi0tYWN0aXZlLWJsdWUgdnVpX2J1dHRvbi0tbm8tdHJhbnNpdGlvbiB2dWlfcGFnZW5hdGlvbi0tYnRuIHZ1aV9wYWdlbmF0aW9uLS1idG4tbn","p":[6107,83,9149],"s":[337,507,674]}],"wh":[3274,2358,10],"of":[5253,7146,213]}'
DM_IMG_LIST = '[{"x":2628,"y":-2200,"z":0,"timestamp":23363,"k":60,"type":0},{"x":2720,"y":-2083,"z":86,"timestamp":23464,"k":109,"type":0},{"x":2717,"y":-2021,"z":49,"timestamp":23564,"k":120,"type":0},{"x":2870,"y":-1868,"z":202,"timestamp":23664,"k":79,"type":0},{"x":2701,"y":-2037,"z":33,"timestamp":23769,"k":77,"type":1},{"x":3135,"y":-1503,"z":443,"timestamp":23870,"k":76,"type":0},{"x":3595,"y":354,"z":392,"timestamp":23992,"k":84,"type":0},{"x":3777,"y":1114,"z":427,"timestamp":24096,"k":84,"type":0},{"x":3907,"y":1050,"z":495,"timestamp":41009,"k":102,"type":0},{"x":3667,"y":609,"z":352,"timestamp":41110,"k":83,"type":0},{"x":4000,"y":818,"z":781,"timestamp":41210,"k":101,"type":0},{"x":3765,"y":582,"z":549,"timestamp":41311,"k":108,"type":0},{"x":3555,"y":364,"z":340,"timestamp":41412,"k":126,"type":0},{"x":3662,"y":447,"z":450,"timestamp":41513,"k":112,"type":0},{"x":4386,"y":1164,"z":1172,"timestamp":41627,"k":112,"type":0},{"x":4534,"y":1253,"z":1313,"timestamp":41728,"k":81,"type":0},{"x":3377,"y":89,"z":154,"timestamp":41860,"k":85,"type":0},{"x":5041,"y":1746,"z":1816,"timestamp":41968,"k":116,"type":0},{"x":4757,"y":1347,"z":1509,"timestamp":42070,"k":96,"type":0},{"x":4169,"y":477,"z":985,"timestamp":42171,"k":80,"type":0},{"x":4403,"y":382,"z":1332,"timestamp":42271,"k":62,"type":0},{"x":4441,"y":198,"z":1415,"timestamp":42371,"k":103,"type":0},{"x":4682,"y":271,"z":1608,"timestamp":42472,"k":100,"type":0},{"x":4715,"y":193,"z":1629,"timestamp":42572,"k":108,"type":0},{"x":4522,"y":-91,"z":1525,"timestamp":42672,"k":107,"type":0},{"x":3526,"y":-1110,"z":552,"timestamp":42774,"k":65,"type":0},{"x":3968,"y":-675,"z":992,"timestamp":407204,"k":72,"type":1},{"x":4245,"y":1894,"z":994,"timestamp":407735,"k":75,"type":0},{"x":5911,"y":2870,"z":2913,"timestamp":407835,"k":94,"type":0},{"x":5696,"y":2559,"z":2756,"timestamp":407941,"k":114,"type":0},{"x":3290,"y":584,"z":322,"timestamp":408041,"k":120,"type":0},{"x":4113,"y":1545,"z":1145,"timestamp":408141,"k":115,"type":0},{"x":4761,"y":2190,"z":1802,"timestamp":408243,"k":73,"type":0},{"x":5663,"y":3085,"z":2702,"timestamp":408595,"k":70,"type":0},{"x":5939,"y":3354,"z":2976,"timestamp":408696,"k":106,"type":0},{"x":6703,"y":4111,"z":3738,"timestamp":408937,"k":115,"type":0},{"x":5271,"y":2645,"z":2293,"timestamp":409039,"k":104,"type":0},{"x":4644,"y":2011,"z":1664,"timestamp":409148,"k":89,"type":0},{"x":6674,"y":4034,"z":3692,"timestamp":409290,"k":79,"type":0},{"x":5519,"y":2866,"z":2530,"timestamp":409398,"k":81,"type":0},{"x":4462,"y":1937,"z":1434,"timestamp":409498,"k":118,"type":0},{"x":5546,"y":3518,"z":2430,"timestamp":409600,"k":71,"type":0},{"x":5779,"y":2247,"z":2253,"timestamp":415159,"k":99,"type":0},{"x":6436,"y":1883,"z":3236,"timestamp":415259,"k":124,"type":0},{"x":4355,"y":-536,"z":996,"timestamp":415359,"k":73,"type":0},{"x":4514,"y":-576,"z":1039,"timestamp":415459,"k":65,"type":0},{"x":6608,"y":1865,"z":3380,"timestamp":415560,"k":70,"type":0},{"x":5665,"y":977,"z":2479,"timestamp":415660,"k":77,"type":0},{"x":4293,"y":-371,"z":1127,"timestamp":415761,"k":86,"type":0},{"x":4204,"y":-397,"z":1079,"timestamp":415862,"k":69,"type":0}]'

# user
DYNAMIC_FEATURES = 'itemOpusStyle,listOnlyfans,opusBigCover,onlyfansVote,decorationCard,onlyfansAssetsV2,forwardListHidden,ugcDelete,onlyfansQaCard,commentsNewVersion,avatarAutoTheme,sunflowerStyle,cardsEnhance,eva3CardOpus,eva3CardVideo,eva3CardComment,eva3CardVote,eva3CardUser'

# video
RANK_MAP = {
    'all': 0,
    'anime': 1,
    'movie': 2,
    'documentary': 3,
    'guochuang': 4,
    'tv': 5,
    'variety': 7,
    'cinephile': 1001,
    'ent': 1002,
    'music': 1003,
    'dance': 1004,
    'douga': 1005,
    'kichiku': 1007,
    'game': 1008,
    'knowledge': 1010,
    'tech': 1012,
    'car': 1013,
    'fashion': 1014,
    'sports': 1018,
    'food': 1020,
    'animal': 1024
}

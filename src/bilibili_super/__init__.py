import os
import json

from .config import DM_PARAM_FILE
from .utils import generate_dm_params


def _load_or_init_dm_params():
    if os.path.exists(DM_PARAM_FILE):
        with open(DM_PARAM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    # 不存在则生成
    print("[bilibili_super] Generating DM parameters (one-time setup)...")
    params = generate_dm_params()

    with open(DM_PARAM_FILE, "w", encoding="utf-8") as f:
        json.dump(params, f, indent=4)

    return params


DM_PARAMS = _load_or_init_dm_params()
DM_IMG_STR = DM_PARAMS['DM_IMG_STR']
DM_COVER_IMG_STR = DM_PARAMS['DM_COVER_IMG_STR']

from .login import BilibiliLogin
from .user import BilibiliUser, BilibiliUp
from .video import BilibiliVideo

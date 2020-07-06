# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("mari", "真里", "由月,真里", 17,(1,1), "female", "高校生", "me:わたし"),
        ("negi", "根岸", "根岸,博明", 17,(1,1), "male", "高校生", "me:俺"),
        ## sub
        ## school
        ## univ
        ## others
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("Kyoto", "京都市", 13546,3500),
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("highschool", "高校", "Kyoto"),
        ("univ", "大学", "Kyoto"),
        ("myhome", "由月家", "Kyoto"),
        ("hishome", "根岸家", "Kyoto"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("current", "current", 1,1,2020),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )


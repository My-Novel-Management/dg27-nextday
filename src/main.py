# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## assets
from storybuilder.assets import basic, accessory
## local files
from src.chapter1.main import ch_point_and_line
from src.chapter2.main import ch_thin_world
from src.chapter3.main import ch_real_world
from src.chapter4.main import ch_warp_world

## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   1.一次元「点と線で繋がる世界」
#   2.二次元「薄っぺらなこの世界」
#   3.三次元「形を持ち始めた、現実世界」
#   4.四次元「歪んでいく、幾つもの世界」
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("明日の向こう側――End of The World")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2018)
    w.setBaseArea("Tokyo")
    w.setColumnRow(42,34)
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("高校二年の真里は失踪した同級生の根岸を探し、彼の父の研究に行き当たる。それは「時間」についての研究だった。真里と根岸の次元を超えた交流が始まる")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_point_and_line(w),
            ch_thin_world(w),
            ch_real_world(w),
            ch_warp_world(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())


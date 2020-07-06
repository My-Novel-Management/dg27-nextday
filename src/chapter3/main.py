# -*- coding: utf-8 -*-
"""Chapter 3: 第三次元「形を持ち始めた、現実」
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()

## scenes
def sc_tmp(w: World):
    return w.scene("Sc: xxx",
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_tmp(w: World):
    return w.episode("Ep: xxx",
            sc_tmp(w),
            )

## chapter
def ch_real_world(w: World):
    return w.chapter("第三次元　形を持ち始めた、現実",
            ep_tmp(w),
            note="＜あとで＞")

# -*- coding: utf-8 -*-
"""Chapter 1: 第一次元　点と線の、繋がり
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
def ch_point_and_line(w: World):
    return w.chapter("第一次元　点と線の、繋がり",
            ep_tmp(w),
            note="$mariは火曜日から同じ暮らすの$negiがいないことを不思議に感じていた。一方$negiは$mariが不在なことを妙に感じていた")

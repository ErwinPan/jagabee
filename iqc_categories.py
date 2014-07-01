# -*- coding: utf-8 -*-
import urllib
import os
import sys, getopt


all_categories = [
    {
        'main_cat': '飲品零食',
        'sub_cats': [
            {
                'sub_cat':  '水',       
                'url':      '/List/0/1/54'
            },
            {
                'sub_cat':  '茶飲料',
                'url':      '/List/0/1/57'
            }, 
            {
                'sub_cat':  '咖啡',
                'url':      '/List/0/1/60'
            }, 
            {
                'sub_cat':  '汽水',
                'url':      '/List/0/1/61'
            }, 
            {
                'sub_cat':  '醋(飲料)',
                'url':      '/List/0/1/59'
            }, 
            {
                'sub_cat':  '穀糧飲料',
                'url':      '/List/0/1/56'
            }, 
            {
                'sub_cat':  '乳酸飲料',
                'url':      '/List/0/1/119'
            }, 
            {
                'sub_cat':  '運動飲料',
                'url':      '/List/0/1/120'
            }, 
            {
                'sub_cat':  '其他飲料',
                'url':      '/List/0/1/63'
            }, 
            {
                'sub_cat':  '酒',
                'url':      '/List/0/1/58'
            }, 
            {
                'sub_cat':  '乳製品',
                'url':      '/List/0/1/122'
            }, 
            {
                'sub_cat':  '冰品',
                'url':      '/List/0/1/64'
            }, 
            {
                'sub_cat':  '餅乾',
                'url':      '/List/0/1/65'
            }, 
            {
                'sub_cat':  '糖果',
                'url':      '/List/0/1/66'
            }, 
            {
                'sub_cat':  '布丁果凍',
                'url':      '/List/0/1/67'
            }, 
            {
                'sub_cat':  '其它零食',
                'url':      '/List/0/1/68'
            }, 
            {
                'sub_cat':  '麵包糕餅',
                'url':      '/List/0/1/69'
            }, 
        ], # sub_cats
    }, # main_cat



    {
        'main_cat': '雜糧蔬果',
        'sub_cats': [
            {
                'sub_cat':  '米類',
                'url':      '/List/0/3/78'
            },
            {
                'sub_cat':  '麥類',
                'url':      '/List/0/3/79'
            },
            {
                'sub_cat':  '雜糧類',
                'url':      '/List/0/3/82'
            },
            {
                'sub_cat':  '堅果類',
                'url':      '/List/0/3/84'
            },
            {
                'sub_cat':  '豆類及豆菜類',
                'url':      '/List/0/3/127'
            },
            {
                'sub_cat':  '蔬菜類',
                'url':      '/List/0/3/128'
            },
            {
                'sub_cat':  '水果類',
                'url':      '/List/0/3/129'
            },
            {
                'sub_cat':  '茶葉',
                'url':      '/List/0/3/130'
            },
            {
                'sub_cat':  '菇類',
                'url':      '/List/0/3/131'
            },
            {
                'sub_cat':  '米類',
                'url':      '/List/0/3/78'
            },
        ], # sub_cats
    }, # main_cat



    {
        'main_cat': '加工食品',
        'sub_cats': [
            {
                'sub_cat':  '順丁烯二酸專區',
                'url':      '/List/0/4/169'
            },
            {
                'sub_cat':  '罐頭食品',
                'url':      '/List/0/4/89'
            },
            {
                'sub_cat':  '真空包裝食品',
                'url':      '/List/0/4/90'
            },
            {
                'sub_cat':  '冷凍食品',
                'url':      '/List/0/4/91'
            },
            {
                'sub_cat':  '果醬餡料',
                'url':      '/List/0/4/92'
            },
            {
                'sub_cat':  '素食',
                'url':      '/List/0/4/142'
            },
            {
                'sub_cat':  '蜂製品',
                'url':      '/List/0/4/94'
            },
            {
                'sub_cat':  '加工蔬果雜糧',
                'url':      '/List/0/4/93'
            },
            {
                'sub_cat':  '加工蛋製品',
                'url':      '/List/0/4/95'
            },
            {
                'sub_cat':  '加工肉製品',
                'url':      '/List/0/4/96'
            },
            {
                'sub_cat':  '加工水產品',
                'url':      '/List/0/4/97'
            },
            {
                'sub_cat':  '加工豆類食品',
                'url':      '/List/0/4/98'
            },
            {
                'sub_cat':  '其他加工食品',
                'url':      '/List/0/4/99'
            },
            {
                'sub_cat':  '麵粉及麵製品',
                'url':      '/List/0/4/100'
            },
            {
                'sub_cat':  '其他粉類及粉製品',
                'url':      '/List/0/4/101'
            },
            {
                'sub_cat':  '油脂',
                'url':      '/List/0/4/102'
            },
            {
                'sub_cat':  '鹽類',
                'url':      '/List/0/4/103'
            },
            {
                'sub_cat':  '糖類',
                'url':      '/List/0/4/104'
            },
            {
                'sub_cat':  '調味料與醬料',
                'url':      '/List/0/4/143'
            },
            {
                'sub_cat':  '其他食品原料',
                'url':      '/List/0/4/144'
            },
            {
                'sub_cat':  '中藥材',
                'url':      '/List/0/4/146'
            },
            {
                'sub_cat':  '食品添加物',
                'url':      '/List/0/4/145'
            },
        ], # sub_cats
    }, # main_cat


    {
        'main_cat': '機能食品',
        'sub_cats': [
            {
                'sub_cat':  '嬰兒食品',
                'url':      '/List/0/5/132'
            },
            {
                'sub_cat':  '膠囊食品',
                'url':      '/List/0/5/133'
            },
            {
                'sub_cat':  '錠狀食品',
                'url':      '/List/0/5/134'
            },
            {
                'sub_cat':  '粉狀食品',
                'url':      '/List/0/5/135'
            },
            {
                'sub_cat':  '特殊營養食品',
                'url':      '/List/0/5/136'
            },
            {
                'sub_cat':  '藻類製品',
                'url':      '/List/0/5/137'
            },
            {
                'sub_cat':  '紅麴製品',
                'url':      '/List/0/5/138'
            },
            {
                'sub_cat':  '魚油製品',
                'url':      '/List/0/5/139'
            },
            {
                'sub_cat':  '卵磷脂製品',
                'url':      '/List/0/5/140'
            },
            {
                'sub_cat':  '其他機能食品',
                'url':      '/List/0/5/141'
            },
        ], # sub_cats
    }, # main_cat
]

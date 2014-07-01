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
]

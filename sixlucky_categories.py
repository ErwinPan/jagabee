# -*- coding: utf-8 -*-
import urllib
import os
import sys, getopt

all_categories = [
    {
        'main_cat': '身體保養清潔',
        'sub_cats': [
            {
                'sub_cat':  '頸部保養',       
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30426&TNm=%E9%A0%B8%E9%83%A8%E4%BF%9D%E9%A4%8A'
            },
            {
                'sub_cat':  '手部保養/清潔',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30427&TNm=%E6%89%8B%E9%83%A8%E4%BF%9D%E9%A4%8A%2F%E6%B8%85%E6%BD%94'
            },
            {
                'sub_cat':  '美胸 / 豐胸',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30430&TNm=%E7%BE%8E%E8%83%B8%2F%E8%B1%90%E8%83%B8'
            },
            {
                'sub_cat':  '美體去角質',
                    'url':  'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30431&TNm=%E7%BE%8E%E9%AB%94%E5%8E%BB%E8%A7%92%E8%B3%AA'
            },
            {
                'sub_cat':  '沐浴澡巾 / 浴帽',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30598&TNm=%E6%B2%90%E6%B5%B4%E6%BE%A1%E5%B7%BE%20%2F%20%E6%B5%B4%E5%B8%BD'
            },
            {
                'sub_cat':  '美體沐浴乳/膠',
                    'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30432&TNm=%E7%BE%8E%E9%AB%94%E6%B2%90%E6%B5%B4%E4%B9%B3%2F%E8%86%A0'
            },
            {
                'sub_cat':  '美體潤膚乳液 / 香氛噴霧',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30433&TNm=%E7%BE%8E%E9%AB%94%E6%BD%A4%E8%86%9A%E4%B9%B3%E6%B6%B2%2F%E9%A6%99%E6%B0%9B%E5%99%B4%E9%9C%A7'
            },
            {
                'sub_cat':  '美臀保養',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30435&TNm=%E7%BE%8E%E8%87%80%E4%BF%9D%E9%A4%8A'
            },
            {
                'sub_cat':  '美體瘦身',
                    'url':  'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30434&TNm=%E7%BE%8E%E9%AB%94%E7%98%A6%E8%BA%AB'
            },
            {
                'sub_cat':  '美腿美足護理 / 清潔',
                    'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30436&TNm=%E7%BE%8E%E8%85%BF%E7%BE%8E%E8%B6%B3%E8%AD%B7%E7%90%86%2F%E6%B8%85%E6%BD%94'
            },
            {
                'sub_cat':  '除毛用品',
                    'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30437&TNm=%E9%99%A4%E6%AF%9B%E7%94%A8%E5%93%81'
            },
            {
                'sub_cat':  '美體防曬',
                    'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12473&Nm=%E8%BA%AB%E9%AB%94%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30573&TNm=%E7%BE%8E%E9%AB%94%E9%98%B2%E6%9B%AC'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '臉部保養清潔',
        'sub_cats': [
            {
                'sub_cat':  '化妝水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30411&TNm=%E5%8C%96%E5%A6%9D%E6%B0%B4'
            },
            {
                'sub_cat':  '乳液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30412&TNm=%E4%B9%B3%E6%B6%B2'
            },
            {
                'sub_cat':  '保濕霜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30413&TNm=%E4%BF%9D%E6%BF%95%E9%9C%9C'
            },
            {
                'sub_cat':  '日晚霜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30414&TNm=%E6%97%A5%E6%99%9A%E9%9C%9C'
            },
            {
                'sub_cat':  '精華液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30415&TNm=%E7%B2%BE%E8%8F%AF%E6%B6%B2'
            },
            {
                'sub_cat':  '防晒隔離霜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30416&TNm=%E9%98%B2%E6%99%92%E9%9A%94%E9%9B%A2%E9%9C%9C'
            },
            {
                'sub_cat':  '面膜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30417&TNm=%E9%9D%A2%E8%86%9C'
            },
            {
                'sub_cat':  '卸妝乳/油/液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30418&TNm=%E5%8D%B8%E5%A6%9D%E4%B9%B3%2F%E6%B2%B9%2F%E6%B6%B2'
            },
            {
                'sub_cat':  '去角質 / 抗痘系列',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30419&TNm=%E5%8E%BB%E8%A7%92%E8%B3%AA%20%2F%20%E6%8A%97%E7%97%98%E7%B3%BB%E5%88%97'
            },
            {
                'sub_cat':  '按摩霜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30420&TNm=%E6%8C%89%E6%91%A9%E9%9C%9C'
            },
            {
                'sub_cat':  '洗面乳',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30421&TNm=%E6%B4%97%E9%9D%A2%E4%B9%B3'
            },
            {
                'sub_cat':  '眼部/眉毛/睫毛保養/清潔',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30422&TNm=%E7%9C%BC%E9%83%A8%2F%E7%9C%89%E6%AF%9B%2F%E7%9D%AB%E6%AF%9B%E4%BF%9D%E9%A4%8A%2F%E6%B8%85%E6%BD%94'
            },
            {
                'sub_cat':  '美唇保養 / 清潔',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30423&TNm=%E7%BE%8E%E5%94%87%E4%BF%9D%E9%A4%8A%2F%E6%B8%85%E6%BD%94'
            },
            {
                'sub_cat':  '美齒保養 / 清潔',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30424&TNm=%E7%BE%8E%E9%BD%92%E4%BF%9D%E9%A4%8A%2F%E6%B8%85%E6%BD%94'
            },
            {
                'sub_cat':  '鼻部保養 / 清潔',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12502&Nm=%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A%E6%B8%85%E6%BD%94&TO=30425&TNm=%E9%BC%BB%E9%83%A8%E4%BF%9D%E9%A4%8A%2F%E6%B8%85%E6%BD%94'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '男仕保養',
        'sub_cats': [
            {
                'sub_cat':  '洗面乳',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12474&Nm=%E7%94%B7%E4%BB%95%E4%BF%9D%E9%A4%8A&TO=30438&TNm=%E6%B4%97%E9%9D%A2%E4%B9%B3'
            },
            {
                'sub_cat':  '化粧水/收歛水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12474&Nm=%E7%94%B7%E4%BB%95%E4%BF%9D%E9%A4%8A&TO=30439&TNm=%E5%8C%96%E7%B2%A7%E6%B0%B4%2F%E6%94%B6%E6%AD%9B%E6%B0%B4'
            },
            {
                'sub_cat':  '控油/抗痘系列',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12474&Nm=%E7%94%B7%E4%BB%95%E4%BF%9D%E9%A4%8A&TO=29518&TNm=%E6%8E%A7%E6%B2%B9%2F%E6%8A%97%E7%97%98%E7%B3%BB%E5%88%97'
            },
            {
                'sub_cat':  '乳液/保濕',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12474&Nm=%E7%94%B7%E4%BB%95%E4%BF%9D%E9%A4%8A&TO=30440&TNm=%E4%B9%B3%E6%B6%B2%2F%E4%BF%9D%E6%BF%95'
            },
            {
                'sub_cat':  '去角質/磨砂霜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12474&Nm=%E7%94%B7%E4%BB%95%E4%BF%9D%E9%A4%8A&TO=30441&TNm=%E5%8E%BB%E8%A7%92%E8%B3%AA%2F%E7%A3%A8%E7%A0%82%E9%9C%9C'
            },
            {
                'sub_cat':  '清潔面膜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12474&Nm=%E7%94%B7%E4%BB%95%E4%BF%9D%E9%A4%8A&TO=30442&TNm=%E6%B8%85%E6%BD%94%E9%9D%A2%E8%86%9C'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '香水',
        'sub_cats': [
            {
                'sub_cat':  '女用香水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30319&TNm=%E5%A5%B3%E7%94%A8%E9%A6%99%E6%B0%B4'
            },
            {
                'sub_cat':  '男用香水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30320&TNm=%E7%94%B7%E7%94%A8%E9%A6%99%E6%B0%B4'
            },
            {
                'sub_cat':  '小香水（女）',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30323&TNm=%E5%B0%8F%E9%A6%99%E6%B0%B4%28%E5%A5%B3%29'
            },
            {
                'sub_cat':  '小香水（男）',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30321&TNm=%E5%B0%8F%E9%A6%99%E6%B0%B4%28%E7%94%B7%29'
            },
            {
                'sub_cat':  'TESTER 女用香水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30324&TNm=TESTER%E5%A5%B3%E7%94%A8%E9%A6%99%E6%B0%B4'
            },
            {
                'sub_cat':  'TESTER 男用香水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30325&TNm=TESTER%E7%94%B7%E7%94%A8%E9%A6%99%E6%B0%B4'
            },
            {
                'sub_cat':  '香水禮盒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30326&TNm=%E9%A6%99%E6%B0%B4%E7%A6%AE%E7%9B%92'
            },
            {
                'sub_cat':  '香膏香粉 / 體香劑',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12470&Nm=%E9%A6%99%E6%B0%B4&TO=30327&TNm=%E9%A6%99%E8%86%8F%E9%A6%99%E7%B2%89%20%2F%20%E9%AB%94%E9%A6%99%E5%8A%91'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '彩粧',
        'sub_cats': [
            {
                'sub_cat':  '眉筆　/　眉餅　/　眉刷',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30444&TNm=%E7%9C%89%E7%AD%86%2F%E7%9C%89%E9%A4%85%2F%E7%9C%89%E5%88%B7'
            },
            {
                'sub_cat':  '眼影',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30445&TNm=%E7%9C%BC%E5%BD%B1'
            },
            {
                'sub_cat':  '眼影筆',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30446&TNm=%E7%9C%BC%E5%BD%B1%E7%AD%86'
            },
            {
                'sub_cat':  '眼蜜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30447&TNm=%E7%9C%BC%E8%9C%9C'
            },
            {
                'sub_cat':  '睫毛定型液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30448&TNm=%E7%9D%AB%E6%AF%9B%E5%AE%9A%E5%9E%8B%E6%B6%B2'
            },
            {
                'sub_cat':  '睫毛膏',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30449&TNm=%E7%9D%AB%E6%AF%9B%E8%86%8F'
            },
            {
                'sub_cat':  '腮紅',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30550&TNm=%E8%85%AE%E7%B4%85'
            },
            {
                'sub_cat':  '眼線液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30521&TNm=%E7%9C%BC%E7%B7%9A%E6%B6%B2'
            },
            {
                'sub_cat':  '眼線筆',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30450&TNm=%E7%9C%BC%E7%B7%9A%E7%AD%86'
            },
            {
                'sub_cat':  '蓋斑　/　遮瑕膏',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30451&TNm=%E8%93%8B%E6%96%91%2F%E9%81%AE%E7%91%95%E8%86%8F'
            },
            {
                'sub_cat':  'B B CREAM',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30452&TNm=B%20B%20CREAM'
            },
            {
                'sub_cat':  '粉底液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30453&TNm=%E7%B2%89%E5%BA%95%E6%B6%B2'
            },
            {
                'sub_cat':  '粉條',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30454&TNm=%E7%B2%89%E6%A2%9D'
            },
            {
                'sub_cat':  '蜜粉',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30455&TNm=%E8%9C%9C%E7%B2%89'
            },
            {
                'sub_cat':  '蜜粉餅',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30456&TNm=%E8%9C%9C%E7%B2%89%E9%A4%85'
            },
            {
                'sub_cat':  '兩用粉餅',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30457&TNm=%E5%85%A9%E7%94%A8%E7%B2%89%E9%A4%85'
            },
            {
                'sub_cat':  '蜜粉　/　閃亮蜜粉',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30458&TNm=%E8%9C%9C%E7%B2%89%2F%E9%96%83%E4%BA%AE%E8%9C%9C%E7%B2%89'
            },
            {
                'sub_cat':  '造型水粉餅　/　粉露',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30459&TNm=%E9%80%A0%E5%9E%8B%E6%B0%B4%E7%B2%89%E9%A4%85%2F%E7%B2%89%E9%9C%B2'
            },
            {
                'sub_cat':  '口紅　/　唇蜜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30460&TNm=%E5%8F%A3%E7%B4%85%2F%E5%94%87%E8%9C%9C'
            },
            {
                'sub_cat':  '唇線筆',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12475&Nm=%E5%BD%A9%E7%B2%A7&TO=30462&TNm=%E5%94%87%E7%B7%9A%E7%AD%86'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '彩粧配件',
        'sub_cats': [
            {
                'sub_cat':  '睫毛夾',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29497&TNm=%E7%9D%AB%E6%AF%9B%E5%A4%BE'
            },
            {
                'sub_cat':  '睫毛夾補充蕊',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29498&TNm=%E7%9D%AB%E6%AF%9B%E5%A4%BE%E8%A3%9C%E5%85%85%E8%95%8A'
            },
            {
                'sub_cat':  '睫毛鋼梳',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29506&TNm=%E7%9D%AB%E6%AF%9B%E9%8B%BC%E6%A2%B3'
            },
            {
                'sub_cat':  '假睫毛',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29494&TNm=%E5%81%87%E7%9D%AB%E6%AF%9B'
            },
            {
                'sub_cat':  '假睫毛輔助器',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29495&TNm=%E5%81%87%E7%9D%AB%E6%AF%9B%E8%BC%94%E5%8A%A9%E5%99%A8'
            },
            {
                'sub_cat':  '睫毛黏膠',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29496&TNm=%E7%9D%AB%E6%AF%9B%E9%BB%8F%E8%86%A0'
            },
            {
                'sub_cat':  '修眉刀',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29508&TNm=%E4%BF%AE%E7%9C%89%E5%88%80'
            },
            {
                'sub_cat':  '刷具組',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29504&TNm=%E5%88%B7%E5%85%B7%E7%B5%84'
            },
            {
                'sub_cat':  '吸油面紙 /濕紙巾',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29503&TNm=%E5%90%B8%E6%B2%B9%E9%9D%A2%E7%B4%99%20%2F%E6%BF%95%E7%B4%99%E5%B7%BE'
            },
            {
                'sub_cat':  '唇筆',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29501&TNm=%E5%94%87%E7%AD%86'
            },
            {
                'sub_cat':  '單入刷具',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29505&TNm=%E5%96%AE%E5%85%A5%E5%88%B7%E5%85%B7'
            },
            {
                'sub_cat':  '棉花棒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29512&TNm=%E6%A3%89%E8%8A%B1%E6%A3%92'
            },
            {
                'sub_cat':  '海棉粉撲',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29492&TNm=%E6%B5%B7%E6%A3%89%E7%B2%89%E6%92%B2'
            },
            {
                'sub_cat':  '眼影棒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29500&TNm=%E7%9C%BC%E5%BD%B1%E6%A3%92'
            },
            {
                'sub_cat':  '睫毛膏輔助器',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29510&TNm=%E7%9D%AB%E6%AF%9B%E8%86%8F%E8%BC%94%E5%8A%A9%E5%99%A8'
            },
            {
                'sub_cat':  '粉紙',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29502&TNm=%E7%B2%89%E7%B4%99'
            },
            {
                'sub_cat':  '美容鏡',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29507&TNm=%E7%BE%8E%E5%AE%B9%E9%8F%A1'
            },
            {
                'sub_cat':  '雙眼皮貼',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12476&Nm=%E5%BD%A9%E7%B2%A7%E9%85%8D%E4%BB%B6&TO=29493&TNm=%E9%9B%99%E7%9C%BC%E7%9A%AE%E8%B2%BC'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '美髮護理',
        'sub_cats': [
            {
                'sub_cat':  '洗髮乳',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30487&TNm=%E6%B4%97%E9%AB%AE%E4%B9%B3'
            },
            {
                'sub_cat':  '潤髮乳',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30486&TNm=%E6%BD%A4%E9%AB%AE%E4%B9%B3'
            },
            {
                'sub_cat':  '護髮乳/霜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30485&TNm=%E8%AD%B7%E9%AB%AE%E4%B9%B3%2F%E9%9C%9C'
            },
            {
                'sub_cat':  '護髮液/膜',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30482&TNm=%E8%AD%B7%E9%AB%AE%E6%B6%B2%2F%E8%86%9C'
            },
            {
                'sub_cat':  '泡沫膠',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30574&TNm=%E6%B3%A1%E6%B2%AB%E8%86%A0'
            },
            {
                'sub_cat':  '造型髮腊/髮膠/髮泥',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30469&TNm=%E9%80%A0%E5%9E%8B%E9%AB%AE%E8%85%8A%2F%E9%AB%AE%E8%86%A0%2F%E9%AB%AE%E6%B3%A5'
            },
            {
                'sub_cat':  '髮利香/定型液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30471&TNm=%E9%AB%AE%E5%88%A9%E9%A6%99%2F%E5%AE%9A%E5%9E%8B%E6%B6%B2'
            },
            {
                'sub_cat':  '髮雕',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30474&TNm=%E9%AB%AE%E9%9B%95'
            },
            {
                'sub_cat':  '吹風機',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30464&TNm=%E5%90%B9%E9%A2%A8%E6%A9%9F'
            },
            {
                'sub_cat':  '染髮',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30467&TNm=%E6%9F%93%E9%AB%AE'
            },
            {
                'sub_cat':  '梳子',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30465&TNm=%E6%A2%B3%E5%AD%90'
            },
            {
                'sub_cat':  '美髮造型用具',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30575&TNm=%E7%BE%8E%E9%AB%AE%E9%80%A0%E5%9E%8B%E7%94%A8%E5%85%B7'
            },
            {
                'sub_cat':  '髮捲(髮夾)',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12477&Nm=%E7%BE%8E%E9%AB%AE%E8%AD%B7%E7%90%86&TO=30463&TNm=%E9%AB%AE%E6%8D%B2%28%E9%AB%AE%E5%A4%BE%29'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '美甲護理',
        'sub_cats': [
            {
                'sub_cat':  '去光水',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12528&Nm=%E7%BE%8E%E7%94%B2%E8%AD%B7%E7%90%86&TO=29477&TNm=%E5%8E%BB%E5%85%89%E6%B0%B4'
            },
            {
                'sub_cat':  '指甲油',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12528&Nm=%E7%BE%8E%E7%94%B2%E8%AD%B7%E7%90%86&TO=29478&TNm=%E6%8C%87%E7%94%B2%E6%B2%B9'
            },
            {
                'sub_cat':  '指甲剪',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12528&Nm=%E7%BE%8E%E7%94%B2%E8%AD%B7%E7%90%86&TO=29479&TNm=%E6%8C%87%E7%94%B2%E5%89%AA'
            },
            {
                'sub_cat':  '指甲保養液',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12528&Nm=%E7%BE%8E%E7%94%B2%E8%AD%B7%E7%90%86&TO=29480&TNm=%E6%8C%87%E7%94%B2%E4%BF%9D%E9%A4%8A%E6%B6%B2'
            },
            {
                'sub_cat':  '指甲彩繪迼型',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12528&Nm=%E7%BE%8E%E7%94%B2%E8%AD%B7%E7%90%86&TO=29481&TNm=%E6%8C%87%E7%94%B2%E5%BD%A9%E7%B9%AA%E8%BF%BC%E5%9E%8B'
            },
            {
                'sub_cat':  '指甲調和劑',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12528&Nm=%E7%BE%8E%E7%94%B2%E8%AD%B7%E7%90%86&TO=29491&TNm=%E6%8C%87%E7%94%B2%E8%AA%BF%E5%92%8C%E5%8A%91'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '美容用品',
        'sub_cats': [
            {
                'sub_cat':  '粉刺夾',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29482&TNm=%E7%B2%89%E5%88%BA%E5%A4%BE'
            },
            {
                'sub_cat':  '青春棒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29483&TNm=%E9%9D%92%E6%98%A5%E6%A3%92'
            },
            {
                'sub_cat':  '眉扒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29484&TNm=%E7%9C%89%E6%89%92'
            },
            {
                'sub_cat':  '剪刀 / 修容刀',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29485&TNm=%E5%89%AA%E5%88%80%2F%E4%BF%AE%E5%AE%B9%E5%88%80'
            },
            {
                'sub_cat':  '鼻毛剪',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29486&TNm=%E9%BC%BB%E6%AF%9B%E5%89%AA'
            },
            {
                'sub_cat':  '洗臉刷',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29488&TNm=%E6%B4%97%E8%87%89%E5%88%B7'
            },
            {
                'sub_cat':  '臉部按摩棒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29487&TNm=%E8%87%89%E9%83%A8%E6%8C%89%E6%91%A9%E6%A3%92'
            },
            {
                'sub_cat':  '美體清潔用品',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=30260&TNm=%E7%BE%8E%E9%AB%94%E6%B8%85%E6%BD%94%E7%94%A8%E5%93%81'
            },
            {
                'sub_cat':  '身體按摩棒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29489&TNm=%E8%BA%AB%E9%AB%94%E6%8C%89%E6%91%A9%E6%A3%92'
            },
            {
                'sub_cat':  '美容小物',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=29490&TNm=%E7%BE%8E%E5%AE%B9%E5%B0%8F%E7%89%A9'
            },
            {
                'sub_cat':  '化妝棉',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12479&Nm=%E7%BE%8E%E5%AE%B9%E7%94%A8%E5%93%81&TO=30554&TNm=%E5%8C%96%E5%A6%9D%E6%A3%89'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '美容考試用品',
        'sub_cats': [
            {
                'sub_cat':  '乙丙級考試口紅盤',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12478&Nm=%E7%BE%8E%E5%AE%B9%E8%80%83%E8%A9%A6%E7%94%A8%E5%93%81&TO=29259&TNm=%E4%B9%99%E4%B8%99%E7%B4%9A%E8%80%83%E8%A9%A6%E5%8F%A3%E7%B4%85%E7%9B%A4'
            },
            {
                'sub_cat':  '乙丙級考試眼影盤',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12478&Nm=%E7%BE%8E%E5%AE%B9%E8%80%83%E8%A9%A6%E7%94%A8%E5%93%81&TO=29258&TNm=%E4%B9%99%E4%B8%99%E7%B4%9A%E8%80%83%E8%A9%A6%E7%9C%BC%E5%BD%B1%E7%9B%A4'
            },
        ], # sub_cats
    }, # main_cat
    {
        'main_cat': '婦幼用品',
        'sub_cats': [
            {
                'sub_cat':  'EVE 舒摩兒',
                'url':      'http://www.6lucky.com.tw/showroom/mallset_u.php?SOB=12480&Nm=%E5%A9%A6%E5%B9%BC%E7%94%A8%E5%93%81&TO=52681&TNm=EVE%E8%88%92%E6%91%A9%E5%85%92'
            },
        ], # sub_cats
    }, # main_cat
]

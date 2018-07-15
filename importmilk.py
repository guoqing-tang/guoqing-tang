#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Python3 Author:Tang   Time: 2018/7/14


import re
import urllib.request
import pymysql


#  可以改为自己的数据库
connectDatabase = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="goodsbase")
#  可以加上更多的用户，构建用户代理池
#  也可以加上IP代理池
#  IP资源有很多免费的IP资源，可以直接爬取
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML\
, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

#  进口牛奶的网址
url = "https://list.jd.com/list.html?cat=1320,5019,12215"
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
match_urlitem = '"venderType":"."},(.*?):'
urlitem = re.compile(match_urlitem, re.S).findall(data)
# print(urlitem)

for i in urlitem:  # 遍历整个列表，获取到每一个具体商品相应的ID
    # print(i)
    url1 = "https://item.jd.com/" + str(i) + ".html"  # 每一个商品的具体页面网址
    # print(url1)
    data1 = urllib.request.urlopen(url1).read().decode("gbk", "ignore")

    url2 = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv&productId="+str(i)+"&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    # print(url2)
    data2 = urllib.request.urlopen(url2).read().decode("gbk", "ignore")

    match_goodCommentRate = '"goodRate":(.*?),"'  # 好评率
    match_goodComment = '"goodCount":(.*?),'  # 好评数
    match_middleComment = '"generalCount":(.*?),"'  # 中评数
    match_poorComment = '"poorCount":(.*?),"'  # 差评数

    match_name = '<title>(.*?)</title>'
    match_shopName = 'dianpuname1">(.*?)</a>'

    match_id = i
    match_link = url1
    match_vender = 'venderId:(\d.*?),'

    goodCommentRate = re.compile(match_goodCommentRate, re.S).findall(data2)
    if len(goodCommentRate) > 0:
        goodCommentRate = goodCommentRate[0]
    goodComment = re.compile(match_goodComment, re.S).findall(data2)
    if len(goodComment) > 0:
        goodComment = goodComment[0]
    middleComment = re.compile(match_middleComment, re.S).findall(data2)
    if len(middleComment) > 0:
        middleComment = middleComment[0]
    poorComment = re.compile(match_poorComment, re.S).findall(data2)
    if len(poorComment) > 0:
        poorComment = poorComment[0]

    name = re.compile(match_name, re.S).findall(data1)
    if len(name) > 0:
        name = name[0]
    shopName = re.compile(match_shopName, re.S).findall(data1)
    if len(shopName) > 0:
        shopName = shopName[0]
    print(goodCommentRate, goodComment, middleComment, poorComment, name, shopName)

    vender = re.compile(match_vender, re.S).findall(data1)
    venderID = vender[0]
    print(venderID)

    #  价格数据的网页地址，是需要利用商品ID和商品具体页的源代码venderID构建的
    url3 = "https://c0.3.cn/stock?skuId="+str(i)+"&area=1_72_2799_0&venderId="+str(venderID)+"&cat=1320,5019,12215&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=810313210&pdpin=&detailedAdd=null&callback=jQuery7348457"
    data3 = urllib.request.urlopen(url3).read().decode("utf-8", "ignore")
    print(url3)
    match_price = '"p":"(.*?)",'
    price = re.compile(match_price, re.S).findall(data3)
    price = price[0]
    print(price)
    # 写入数据库
    connectDatabase.query("insert into milkgoods(nameID,name,shopname,price,link,goodcommentrate,goodcomment,middlecomment,poorcomment) \
    values(' "+str(i)+"','"+str(name)+"','"+str(shopName)+"','"+str(price)+"','"+str(url1)+"','"+str(goodCommentRate)\
                          +"','"+str(goodComment)+"','"+str(middleComment)+"','"+str(poorComment)+"')")
    connectDatabase.commit()




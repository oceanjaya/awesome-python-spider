# awesome-python-spider
# Python数据爬取实战
这是一系列Python爬虫实战项目，从入门到精通，爬虫原来如此简单～

## 1. Unsplash Spider
一个基于[Requests](http://cn.python-requests.org/zh_CN/latest/index.html),[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/index.html)的简单单线程爬虫，用于爬取一个非常棒的图片分享网站[Unsplash](https://unsplash.com)上的图片。
使用了以下库
requests：发出GET请求和下载图片  
BeautifulSoup ：解析HTML 可以较为方便地取特定标签text
re ：正则表达式辅助提取信息
os ：保存图片

有待完善 :
 - [ ] 多线程
 - [ ] 下载完打包后用[bypy](https://github.com/houtianze/bypy)自动上传百度云
 
### 2. V2ex-coin 
[V2EX](http://www.v2ex.com/)自动登陆领取金币 :P
发现自从2016年4月22号以后V2EX登陆POST数据 username键和password键变成了随机值，也需要像once值那样从网页中提取。  
使用方法:把main中username,password改成自己的，然后run一遍就可以了。可以加到服务器crontab定时任务中实现每日自动登陆领取金币～
主要练习了使用Chrome开发者工具分析POST请求，并使用requests模拟请求登陆。

TODO:
 - [ ] 知乎BOT（自动点赞、评论、转发、自动提问“如何评价XXX”。。）
 - [ ] 微博BOT
 - [ ] 豆瓣BOT
 - [ ] twitterBOT
 ……




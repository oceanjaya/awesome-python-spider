#coding=utf-8

import  requests,re,datetime

Header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Referer': 'http://www.v2ex.com/signin',
}

class get_v2ex_coin:
    s=requests.session()
    def __init__(self,username,password):
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print "开始！"
        self.username=username
        self.password=password
        self.login()

    #处理登陆
    def login(self):
        #先发出GET请求拿到参数
        login_html=self.s.get("http://www.v2ex.com/signin",headers=Header).text
        #找到POST时用户名、密码的key
        keys=re.findall('class="sl" name="(.+)" value',login_html)
        #找到POST中once的值
        once=re.findall('value="(\d+)" name="once"',login_html)[0]
        username_key= keys[0]
        password_key= keys[1]
        #包装成字典
        post_data={
            username_key:self.username,
            password_key:self.password,
            'once':once,
            'next':'/'
        }
        #发出POST请求
        post_result=self.s.post("http://www.v2ex.com/signin",data=post_data,headers=Header)
        if post_result.text.find("signout")==-1:
            print self.username+" 登陆失败！"
        else:
            print self.username+" 登陆成功！"
            self.get_coin()

    def get_coin(self):
        if self.s.get("http://www.v2ex.com/mission/daily").text.find("fa-ok-sign")!=-1:
            print self.username+" 已领取过奖励!"
        else:
            try:
                daily=re.findall('(/mission/daily/redeem\?once=\d+)',self.s.get("http://www.v2ex.com/mission/daily").text)[0]
                a=self.s.get("http://www.v2ex.com"+daily,headers=Header)
                print self.username+" 签到成功！"
            except:
                print self.username+" 签到失败！"
        print "Good Bye!"

if __name__=="__main__":
    #请填入用户名和密码
    username=''
    password=''
    get_v2ex_coin(username,password)


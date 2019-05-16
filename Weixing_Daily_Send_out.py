# 2019年05月15日
# 源源源
# yuan梦项目
# 功能：1、每日定期给某人发送“早上好”问候消息
# 2019年05月15日下班后开始第一天测试
# 2019年05月16日，早上，代码测试成功，消息成功发送
import random
import re
import itchat
import time


class Weixing_Daily_Send_Out():
    def __init__(self):  # 初始化登录的方法
        itchat.auto_login()

    def get_weixing_name(self):
        users = itchat.search_friends("陈梦媛")  # 此处可以设置需要发送的指定人的名字
        userName = users[0]['UserName']  # 找到好友中第一个备注是某某某的人
        return userName

    def get_time(self):  # 获取当前时间的方法
        get_now_time = time.strftime('%H-%M', time.localtime(time.time()))
        return get_now_time

    def now_time(self, get_now_time):  # 将时间格式化提取时间的方法
        clean_now_time = re.sub('[-]', '', get_now_time)
        return clean_now_time

    def judge_time(self, images, userName):  # 判断获取的时间时候是相要的时间的的方法,同时发送对应的指定消息
        itchat.send_image(images, toUserName=userName)  # 此处设置的发送的一张图片
        itchat.send('Hello', toUserName=userName)  # 此处设置的需要发送的内容，此处是Hello

    def get_images_address(self):  # 随机获得图片地址的方法
        moring_00 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_00.jpg"
        moring_01 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_01.jpg"
        moring_02 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_02.jpg"
        moring_03 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_03.jpg"
        images = random.choice([moring_00, moring_01, moring_02, moring_03])  # 未避免被发现，此处采用随机数图片变换
        print(images)
        return images

    def run(self):  # 主函数
        images = self.get_images_address()
        userName = self.get_weixing_name()
        while True:  # 此处采用循环，一直获取时间，直到达到指定的时间点，跳出循环
            get_now_time = self.get_time()
            clean_now_time = self.now_time(get_now_time)
            if clean_now_time == str("0810"):  # 此处设置时间点
                self.judge_time(images, userName)
                print("每日消息发送完毕")
                break


if __name__ == '__main__':
    weixin_daily_send_out = Weixing_Daily_Send_Out()
    weixin_daily_send_out.run()

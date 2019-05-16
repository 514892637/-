# 2019年05月15日
# 源源源
# yuan梦项目
# 功能：1、每日定期给某人发送“早上好”问候消息，附带随机早安表情图
#       2、在关键时间节点，定期发送指定消息
# 2019年05月15日下班后开始第一天测试
# 2019年05月16日，早上，测试成功，消息成功发送
# 2019年05月16日，增加关键时间节点发送消息功能，例如在结婚纪念日，生日等
import random
import re
import itchat
import time


class Weixing_Daily_Send_Out():
    def __init__(self):  # 初始化登录的方法
        itchat.auto_login()

    def get_weixing_name(self):
        users = itchat.search_friends("陈梦媛")  # 此处可以设置需要发送的指定人的名字
        # users = itchat.search_friends("张帆（综合）")  # 此处可以设置需要发送的指定人的名字，此为测试人员
        userName = users[0]['UserName']  # 找到好友中第一个备注是某某某的人
        return userName

    def get_time(self):  # 获取当前时间的方法
        get_now_time = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        return get_now_time

    def now_time(self, get_now_time):  # 将时间格式化提取时间的方法
        clean_now_time_time = re.sub('[-]', '', get_now_time)
        clean_new_time = clean_now_time_time[4:8]
        clean_now_time = clean_now_time_time[8:12]
        return clean_new_time, clean_now_time

    def judge_time(self, images, userName):  # 判断获取的时间时候是相要的时间的的方法,同时发送对应的指定消息
        itchat.send_image(images, toUserName=userName)  # 此处设置的发送的一张图片
        itchat.send('Hello', toUserName=userName)  # 此处设置的需要发送的内容，此处是Hello

    def get_images_address(self):  # 随机获得图片地址的方法
        moring_00 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_00.jpg"
        moring_01 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_01.jpg"
        moring_02 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_02.jpg"
        moring_03 = "C:\\Users\\LSY\Desktop\\Good_moring\\moring_03.jpg"
        images = random.choice([moring_00, moring_01, moring_02, moring_03])  # 未避免被发现，此处采用随机数图片变换
        return images

    def judge_time_01(self, userName):  # 判断获取的时间时候是相要的时间的的方法,同时发送对应的指定消息
        itchat.send('祝你儿童节快乐！哈哈哈哈哈', toUserName=userName)  # 此处设置的需要发送的内容

    def judge_time_02(self, userName):  # 判断获取的时间时候是相要的时间的的方法,同时发送对应的指定消息
        itchat.send('还记得今天是什么日子吗？今天是我在茫茫人海中第一次遇见你的时间，感谢你的默默陪伴！爱你...',
                    toUserName=userName)  # 此处设置甜言蜜语，算了，不写了，我一个单身狗既然写的如此开心，默默的留下了伤心的泪水，算了还是new一个女朋友出来好了

    def judge_time_03(self, userName):  # 判断获取的时间时候是相要的时间的的方法,同时发送对应的指定消息
        itchat.send('祝你新年快乐！新的一年，要一直开心哈！', toUserName=userName)  # 此处设置的新年祝福语

    def run(self):  # 主函数
        images = self.get_images_address()
        userName = self.get_weixing_name()
        while True:  # 此处采用循环，一直获取时间，直到达到指定的时间点，跳出循环
            get_now_time = self.get_time()
            clean_new_time, clean_now_time = self.now_time(get_now_time)
            if clean_now_time == str("0810"):  # 此处设置时间点,因为是每天要发一句问候语，所以，直接采用判断即可，如果判断成功直接发送消息，并执行下面语句，不成功就不循环判断
                self.judge_time(images, userName)
                print("每日消息发送完毕")
                if clean_new_time == str("0601"):  # 此处设置儿童节时间点
                    self.judge_time_01(userName)
                    print("节假日消息发送完毕")
                elif clean_new_time == str("0511"):  # 此处设置在茫茫人海中第一次见到你的时间点
                    self.judge_time_02(userName)
                    print("特殊纪念日消息发送完毕")
                break


if __name__ == '__main__':
    weixin_daily_send_out = Weixing_Daily_Send_Out()
    weixin_daily_send_out.run()

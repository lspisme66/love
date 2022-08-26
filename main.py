from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]
template_id = os.environ["TEMPLATE_ID"]
template_id2 = os.environ["TEMPLATE_ID2"]
today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
city2 = os.environ['CITY2']
birthday = os.environ['BIRTHDAY']
birthday2 = os.environ['BIRTHDAY2']
astro = os.environ["ASTRO"]
astro2 = os.environ["ASTRO2"]
user_id = os.environ["USER_ID"]
user_id2 = os.environ["USER_ID2"]










def week(a):
    if a==0:data = "一"
    if a==1:data = "二"
    if a==2:data = "三"
    if a==3:data = "四"
    if a==4:data = "五"
    if a==5:data = "六"
    if a==6:data = "日"
    return data







#推送信息
def send_message(to_user, access_token, city_name, weather, max_temperature, min_temperature, pipi, lizhi, pop, tips, note_en, note_ch, health_tip, lucky_):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() % 7]
    # 获取在一起的日子的日期格式

def get_weather(): # 女方天气
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  dates = weather['date']
  return weather['weather'], math.floor(weather['temp']),math.floor(weather['low']),math.floor(weather['high']),dates,weather['wind']

def get_weather2(): #男方天气
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city2
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  dates = weather['date']
  return weather['weather'], math.floor(weather['temp']),math.floor(weather['low']),math.floor(weather['high']),dates,weather['wind']
 
def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days + 1

def get_birthday2():
  next = datetime.strptime(str(date.today().year) + "-" + birthday2, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days + 1

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea,temperature,low,high,dates,wind = get_weather()
wea2,temperature2,low2,high2,dates2,wind2 = get_weather2()
week_math = datetime.strptime(dates,"%Y-%m-%d").weekday()
data = {"city":{"value":city},
        "today":{"value":dates + " 星期" + week(week_math)}, #今天日期
        
        "weather":{"value":wea,"color":get_random_color()}, # 女方天气
        "wind":{"value":wind,"color":get_random_color()}, # 女方天气风级
        "temperature":{"value":temperature,"color":get_random_color()}, # 女方天气气温
        "low":{"value":low,"color":get_random_color()}, # 女方天气低温
        "high":{"value":high,"color":get_random_color()}, # 女方天气高温
        "lucky":{"value":lucky(),"color":get_random_color()}, # 女方星座
        "birthday_left":{"value":get_birthday(),"color":get_random_color()}, # 女方生日
         "birthday_left2":{"value":get_birthday2(),"color":get_random_color()}, # 男方生日

        "love_days":{"value":get_count(),"color":get_random_color()}, # 恋爱日
        "words":{"value":get_words(), "color":get_random_color()} #彩虹屁
}
data2 = {"city":{"value":city2},
        "today":{"value":dates + " 星期" + week(week_math)}, #今天日期
        

        
        "weather2":{"value":wea2,"color":get_random_color()}, # 男方天气
        "wind2":{"value":wind2,"color":get_random_color()}, # 男方天气风级
        "temperature2":{"value":temperature2,"color":get_random_color()}, # 男方天气气温
        "low2":{"value":low2,"color":get_random_color()}, # 男方天气低温
        "high2":{"value":high2,"color":get_random_color()}, # 男方天气高温
        "birthday_left2":{"value":get_birthday2(),"color":get_random_color()}, # 男方生日
         "birthday_left":{"value":get_birthday(),"color":get_random_color()}, # 女方生日
        "lucky2":{"value":lucky2(),"color":get_random_color()},  # 男方星座
        "love_days":{"value":get_count(),"color":get_random_color()}, # 恋爱日
        "words":{"value":get_words(), "color":get_random_color()} #彩虹屁
}


#res = wm.send_template(user_id, template_id, data)
res2 = wm.send_template(user_id2, template_id2, data2)
#print(res)
print(res2)

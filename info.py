#coding=utf-8
import sys
import datetime
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

d1 = datetime.datetime(2017, 1, 7)
d2 = datetime.datetime.now()
day = str((d2-d1).days)

def insert(str, add):
    str = str[:len(str)-1] + add
    return str
"""
天气
"""
res = requests.get("http://www.weather.com.cn/weather1d/101270101.shtml")
res.encoding = "utf-8"
sample = res.text
soup = BeautifulSoup(sample, 'html.parser')
ziwaixian = insert(soup.select('.li1')[0].p.text, "噢~")
ganmao = insert(soup.select('.li2')[0].p.text, "哟~")
tianqi = soup.select('.li3')[0].a.span.text
chuanyi = soup.select('.li3')[0].a.p.text
yundong = soup.select('.li5')[0].span.text + " 。所以" + insert(soup.select('.li5')[0].p.text, "噢~")
wuran = soup.select('.li6')[0].span.text
wuranjianyi = insert(soup.select('.li6')[0].p.text, "哟~")
#timeSource = soup.select('.time-source')[0].contents[0].strip()
temLow = soup.select('.tem')[0].find_all('span')[0].text + "℃。"
temHigh = soup.select('.tem')[1].find_all('span')[0].text + "℃"

"""
情话
"""
res1 = requests.get("http://www.binzz.com/yulu2/3588.html")
res1.encoding = "gbk"
sample1 = res1.text
soup1 = BeautifulSoup(sample1, 'html.parser')
qinghua = soup1.select('#content')[0].find_all("p")[(d2-d1).days - 65].text.split("：")[1]

"""
星座
"""
res2 = requests.get("http://astro.sina.com.cn/fate_day_Pisces/")
res2.encoding = "utf-8"
sample2 = res2.text
soup2 = BeautifulSoup(sample2, 'html.parser')
xingzuo = soup2.select('div.words')[0].find_all("p")[3].text


"""
笑话
"""

res3 = requests.get("http://www.jokeji.cn/jokehtml/ym/201703141340521.htm")
res3.encoding = "gbk"
sample3 = res3.text
soup3 = BeautifulSoup(sample3, 'html.parser')
xiaohua = soup3.select('#text110')[0].find_all("p")[(d2-d1).days - 91].text[2:]


"""
歌曲
"""

# sample4 = "<ul class='f-hide'><li>< a href=' '>Feeling Good</ a></li><li>< a href='/song?id=5048584'>All By Myself</ a></li><li>< a href='/song?id=2310010'>All by Myself</ a></li><li>< a href='/song?id=363488'>爱不爱我</ a></li><li>< a href='/song?id=299036'>多得他</ a></li><li>< a href='/song?id=445144811'>十点半的地铁</ a></li><li>< a href='/song?id=447280427'>灵魂歌手</ a></li><li>< a href='/song?id=453189433'>爱上一个不回家的人</ a></li><li>< a href='/song?id=437292675'>我要你</ a></li><li>< a href='/song?id=454711150'>胡桃夹子</ a></li><li>< a href='/song?id=410519574'>Against The Stream</ a></li><li>< a href='/song?id=29850094'>裂心</ a></li><li>< a href='/song?id=255588'>柿子</ a></li><li>< a href='/song?id=159416'>红豆曲</ a></li><li>< a href='/song?id=32785700'>一生所爱</ a></li><li>< a href='/song?id=36229054'>自己</ a></li><li>< a href='/song?id=428591531'>最后的请求</ a></li><li>< a href='/song?id=253042'>想你想疯了</ a></li><li>< a href='/song?id=27583497'>想你想疯了</ a></li><li>< a href='/song?id=28754846'>卷珠帘</ a></li><li>< a href='/song?id=1934618'>Scarborough Fair/Canticle</ a></li><li>< a href='/song?id=417250673'>父亲写的散文诗(时光版)</ a></li><li>< a href='/song?id=189215'>三天两夜</ a></li><li>< a href='/song?id=27904166'>三天两夜</ a></li><li>< a href='/song?id=432430074'>崇拜</ a></li><li>< a href='/song?id=238855'>天亮了</ a></li><li>< a href='/song?id=28668277'>你就不要想起我 (Instrumental)</ a></li><li>< a href='/song?id=449577226'>你就不要想起我 (cover田馥甄) </ a></li><li>< a href='/song?id=65126'>红玫瑰</ a></li><li>< a href='/song?id=399353382'>红玫瑰(Live)</ a></li><li>< a href='/song?id=168091'>蓝莲花</ a></li><li>< a href='/song?id=110236'>异乡人</ a></li><li>< a href='/song?id=454966185'>Daididau</ a></li><li>< a href='/song?id=399353367'>听不到(Live)</ a></li><li>< a href='/song?id=29011528'>御龙铭千古</ a></li><li>< a href='/song?id=306818'>突然想爱你</ a></li><li>< a href='/song?id=29822036'>时间有泪</ a></li><li>< a href='/song?id=28680438'>Thinking Out Loud</ a></li><li>< a href='/song?id=2924423'>Adagio</ a></li><li>< a href='/song?id=29803532'>盛夏光年</ a></li><li>< a href='/song?id=34922419'>Writing's On the Wall</ a></li><li>< a href='/song?id=186686'>用情</ a></li><li>< a href='/song?id=70074'>哥哥(Live) - live</ a></li><li>< a href='/song?id=27937869'>很想很想说再见</ a></li><li>< a href='/song?id=29567191'>三十岁的女人</ a></li><li>< a href='/song?id=77244'>阿瓦尔古丽</ a></li><li>< a href='/song?id=28196001'>克卜勒</ a></li><li>< a href='/song?id=31473269'>默</ a></li><li>< a href='/song?id=65198'>命硬</ a></li><li>< a href='/song?id=29722263'>Uptown Funk</ a></li><li>< a href='/song?id=3950546'>It's My Life</ a></li><li>< a href='/song?id=198477'>月亮粑粑</ a></li><li>< a href='/song?id=189285'>爱是永恒</ a></li><li>< a href='/song?id=31140355'>克卜勒</ a></li><li>< a href='/song?id=176355'>你是我最深爱的人</ a></li><li>< a href='/song?id=326784'>我最亲爱的</ a></li><li>< a href='/song?id=190473'>秋意浓</ a></li><li>< a href='/song?id=188703'>李香兰</ a></li><li>< a href='/song?id=524331'>行かないで</ a></li><li>< a href='/song?id=346075'>真的爱你</ a></li><li>< a href='/song?id=224993'>真的爱你</ a></li><li>< a href='/song?id=327944'>鲁冰花</ a></li><li>< a href='/song?id=22463223'>Better Man</ a></li><li>< a href='/song?id=26222114'>定风波</ a></li><li>< a href='/song?id=29567189'>理想</ a></li><li>< a href='/song?id=5103402'>Golden</ a></li><li>< a href='/song?id=284730'>Whispering Steppes</ a></li><li>< a href='/song?id=436514312'>成都</ a></li><li>< a href='/song?id=26857076'>The Show Must Go On</ a></li><li>< a href='/song?id=29932301'>很奇怪我爱你 - live</ a></li><li>< a href='/song?id=299650'>百年孤寂</ a></li><li>< a href='/song?id=21730469'>Run</ a></li><li>< a href='/song?id=2923244'>Run</ a></li><li>< a href='/song?id=1215678'>Vincent</ a></li><li>< a href='/song?id=225016'>Vincent</ a></li><li>< a href='/song?id=110207'>蒙娜丽莎的眼泪</ a></li><li>< a href='/song?id=29716090'>蒙娜丽莎的眼泪(Live)</ a></li><li>< a href='/song?id=259086'>请不要在别人肩上哭泣</ a></li><li>< a href='/song?id=19674656'>Opera 2</ a></li><li>< a href='/song?id=29739000'>九儿 (红高粱)</ a></li><li>< a href='/song?id=26390265'>无赖</ a></li><li>< a href='/song?id=4877329'>卡门</ a></li><li>< a href='/song?id=5273505'>卡门</ a></li><li>< a href='/song?id=155894'>你是我心爱的姑娘</ a></li><li>< a href='/song?id=19550156'>Love on Top</ a></li><li>< a href='/song?id=159264'>那一段日子</ a></li><li>< a href='/song?id=1777926'>S.o.s d'un terrien en detresse</ a></li><li>< a href='/song?id=407759451'>阿楚姑娘</ a></li><li>< a href='/song?id=407840732'>阿楚姑娘</ a></li><li>< a href='/song?id=85621'>第一次</ a></li><li>< a href='/song?id=1476106'>Imagine</ a></li><li>< a href='/song?id=412902921'>Lion</ a></li><li>< a href='/song?id=155897'>再见青春</ a></li><li>< a href='/song?id=257202'>不必在乎我是谁</ a></li></ul>"
# soup4 = BeautifulSoup(sample4, 'html.parser')
# songUrl = "http://music.163.com/#/" + soup4.select('a')[(d2-d1).days - 72]["href"]
# songName = soup4.select('a')[0].text

res6 = requests.get("http://www.lizhi.fm/233233/")
res6.encoding = "utf-8"
sample6 = res6.text
soup6 = BeautifulSoup(sample6, 'html.parser')
fmUrl = "http://www.lizhi.fm" + soup6.find_all("a", attrs={"data-band": "233233"})[0]["href"]
fmName = soup6.find_all("a", attrs={"data-band": "233233"})[0].select("p.audioName")[0].text

id_ = "music.163.com/#/song?id=37196629"
casablanca = "Casablanca"
content1= "亲爱的<b>李琳垚</b>:" + "<br>" +\
      "    早上好，今天是你跟<b>王清野</b>在一起的<b>第" + day +"天</b>噢~" + "<br><br>" +\
      "    今天他想对你说的话是：" + qinghua + "<br><br>" + \
      "<b>接下来为您播报今天成都的天气情况：</b>" + "<br>" + \
      "    整体温度：" + temHigh + "～" + temLow + tianqi + "噢~所以" + chuanyi + "不要忘记啦！" + "<br>" +\
      "    感冒指数：" + ganmao + "<br>" +  \
      "    运动指数：今天的运动情况是" + yundong + "<br>" + \
      "    空气污染：程度" + wuran + "。" + "所以" + wuranjianyi + "<br>" + \
      "    紫外线指数：" + ziwaixian + "<br><br>" + \
      "<b>今日双鱼座的星座运势是：</b>" + "<br>" + \
      "    " + xingzuo[2:] + "<br><br>" + \
      "<b>再送上笑话一则：</b>" + "<br>" + \
      "" + xiaohua + "<br><br>" + \
      "<b>今日歌曲一首</b>：<a href=http://music.163.com/#/song?id=29556039>Grapevine Valentine- Kingsfoil</a><br><br>" + \
      "<b>最后也是最重要的</b>：" + "<br>"


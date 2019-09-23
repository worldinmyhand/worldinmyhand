# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:41:01 2019

@author: user
"""


import jieba

import requests
from bs4 import BeautifulSoup
list_Country={'台灣':'Taiwan','阿爾巴尼亞':'Albania','阿爾及利亞':'Algeria','安哥拉':'Angola','安圭拉':'Anguilla','阿根廷':'Argentina','亞美尼亞':'Armenia','阿路巴':'Aruba','澳大利亞':'Australia','奧地利':'Austria','亞塞拜然':'Azerbaijan','巴林':'Bahrain','孟加拉':'Bangladesh','巴貝多':'Barbados','白俄羅斯':'Belarus','比利時':'Belgium','貝里斯':'Belize','貝南':'Benin','百慕達':'Bermuda','不丹':'Bhutan','玻利維亞':'Bolivia','波士尼亞與赫塞哥維納':'Bosnia and Herzegovina','波札那':'Botswana','巴西':'Brazil','汶萊':'Brunei','保加利亞':'Bulgaria','布吉納法索':'Burkina Faso','蒲隆地':'Burundi','柬埔寨':'Cambodia','喀麥隆':'Cameroon','加拿大':'Canada','維德角島':'Cape Verde','開曼群島':'Cayman Islands','中非共和國':'Central African Republic','查德':'Chad','智利':'Chile','中國':'China','哥倫比亞':'Colombia','剛果':'Republic of the Congo','科克群島':'Cook Islands','哥斯大黎加':'Costa Rica','象牙海岸':'Ivory Coast','克羅埃西亞':'Croatia','賽普勒斯':'Cyprus','捷克':'Czech Republic','丹麥':'Denmark','多明尼加':'Dominican Republic','多米尼克':'Dominica','厄瓜多':'Ecuador','埃及':'Egypt','厄利垂亞':'Eritrea','愛沙尼亞':'Estonia','衣索匹亞':'Ethiopia','斐濟':'Fiji','芬蘭':'Finland','法屬玻里尼西亞':'French Polynesia','法國':'France','加彭':'Gabon','喬治亞':'Georgia','德國':'Germany','迦納':'Ghana','直布羅陀':'Gibraltar','英國':'United Kingdom','希臘':'Greece','格瑞那達':'Grenada','瓜地馬拉':'Guatemala','幾內亞':'Guinea','蓋亞那':'Guyana','海地':'Haiti','宏都拉斯':'Honduras','香港':'Hong Kong','匈牙利':'Hungary','冰島':'Iceland','印度':'India','印尼':'Indonesia','伊拉克':'Iraq','愛爾蘭':'Ireland','以色列':'Israel','義大利':'Italy','牙買加':'Jamaica','日本':'Japan','約旦':'Jordan','肯亞':'Kenya','南韓':'South Korea','北韓':'North Korea','科威特':'Kuwait','寮國':"Laos",'衣索匹亞':'Ethiopia','衣索匹亞':'Ethiopia','盧森堡':'Luxembourg','澳門':'Macao','馬其頓':'Macedonia','馬達加斯加':'Madagascar','馬拉威':'Malawi','馬來西亞':'Malaysia','馬爾地夫':'Maldives','馬利':'Mali','馬爾他':'Malta','模里西斯':'Mauritius','茅利塔尼亞':'Mauritania','墨西哥':'Mexico','摩爾多瓦':'Moldova','蒙古':'Mongolia','摩洛哥':'Morocco','緬甸':'Myanmar','納米比亞':'Namibia','諾魯':'Nauru','尼泊爾':'Nepal','荷蘭':'Netherlands','新喀里多尼亞':'New Caledonia','紐西蘭':'New Zealand','尼日':'Niger','奈及利亞':'Nigeria','挪威':'Norway','阿曼':'Oman','巴基斯坦':'Pakistan','巴拿馬':'Panama','巴布亞紐幾內亞':'Papua New Guinea','巴拉圭':'Paraguay','秘魯':'Peru','菲律賓':'Philippines','波蘭':'Poland','葡萄牙':'Portugal','卡達':'Qatar','羅馬尼亞':'Romania','俄羅斯':'Russia','盧安達':'Rwanda','聖克里斯多福及尼維斯':'Saint Christopher and Nevis','聖露西亞':'Saint Lucia','聖文森及格瑞那丁':'Saint Vincent and the Grenadines','聖多美普林西比':'Sao Tome and Principe','沙烏地阿拉伯':'Saudi Arabia','塞內加爾':'Senegal','塞席爾':'Seychelles','獅子山':'Sierra Leone','新加坡':'Singapore','斯洛伐克':'Slovakia','斯洛維尼亞':'Slovenia','索羅門群島':'Solomon Islands','索馬利亞':'Somalia','南非':'South Africa','西班牙':'Spain','斯里蘭卡':'Sri Lanka','蘇丹':'Sudan','蘇利南':'Suriname','史瓦濟蘭':'Swaziland','瑞典':'Sweden','瑞士':'Switzerland','敘利亞':'Syria','泰國':'Thailand','多哥':'Togo','千里達及托巴哥':'Trinidad and Tobago','突尼西亞':'Tunisia','土耳其':'Turkey','烏干達':'Uganda','烏克蘭':'Ukraine','阿拉伯聯合大公國':'United Arab Emirates','美國':'United States of America','烏拉圭':'Uruguay','委內瑞拉':'Venezuela','越南':'Vietnam','薩摩亞':' Samoa','葉門':'Yemen','南斯拉夫':'Yugoslavia','尚比亞':'Zambia','辛巴威':'Zimbabwe','古巴共和國' :'Cuba','衣索比亞':'Ethiopia','法屬圭亞那':'French Guiana','古拉索':'Curacao','阿魯巴':'Aruba','吉里巴斯':' Kiribati','馬紹爾群島':'Marshall Islands','阿富汗':'Afghanistan','伊朗':'Iran','烏茲別克共和國':'Uzbekistan','葛摩聯盟':'Comoros','賴比瑞亞':'Liberia','利比亞':'Libya','馬約特島':'Mayotte','莫三比克':'Mozambique','留尼旺':'Reunion','甘比亞':'The Gambia','安道爾侯國':'Andorra','科索沃':'Kosovo','拉脫維亞':'Latvia','列支敦斯登':'Liechtenstein','立陶宛':'Lithuania','摩納哥':'Monaco','蒙特內哥羅':'Montenegro','尼加拉瓜共和國':'Nicaragua','東帝汶':'Timor Leste','萬那杜共和國':'Vanuatu','吉爾吉斯':'Kyrgyzstan','黎巴嫩':'Lebanon','塔吉克':'Tajikistan','吉布地':'Djibouti','賴索托':'Lesotho','約旦河西岸':'West Bank','坦尚尼亞':'United Republic of Tanzania','土庫曼':'Turkmenistan','塞爾維亞':'Republic of Serbia','薩爾瓦多':'El Salvador','南蘇丹':'South Sudan','西撒哈拉':'Western Sahara','波多黎各':'Puerto Rico','馬利':'Mali','哈薩克':'Kazakhstan','格陵蘭':'Greenland','赤道幾內亞':'Equatorial Guinea','幾內亞比索':'Guinea Bissau','福克蘭群島':'Falkland Islands','剛果民主共和國':'Democratic Republic of the Congo','巴哈馬':'The Bahamas','索馬里蘭':'Somaliland'}



def GoogleNews(url):
    response = requests.get(url)
    jieba.load_userdict("../jieba_dict/dict2.txt")
    #新增結巴辭意
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('a',class_='DY5T1d')
    Time= soup.find_all('time',class_='WW6dff uQIVzc Sksgp')   

    list_B=[]
    for x in range(20):
        list_A={'Time':'','Country':'','Title':'','Website':''}
        M=content[x].text
        words = jieba.cut(M, cut_all=False)
    
        for word in words:
            if word in list_Country:
                list_A['Country']=word
            else:
                continue
        if list_A['Country']=="":
            continue
    #過濾標題無國家名稱的訊息
        else:
            list_A['Time']=Time[x].get("datetime")
            list_A['Title']=content[x].text
            list_A['Website']='https://news.google.com'+content[x].get('href')[1:]
            list_B.append(list_A)
    return list_B

def Alert(url):
    r = requests.get(url,verify=False) 
    jieba.load_userdict("../jieba_dict/dict2.txt")
    
    if r.status_code == requests.codes.ok:
        # 以 BeautifulSoup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')   
        Country= soup.find_all(attrs={'data-title':'國家'})
        Color_Alert= soup.find_all(attrs={'data-title':"最新警示提醒"})
        list_B=[]    
        for s in range(len(Country)):
            list_A={'Country':'','Color_Alert':''}
            M=Country[s].text
            words = jieba.cut(M, cut_all=False)
            for word in words:
                if word in list_Country:
                    list_A['Country']=word
                else:
                    continue
            if list_A['Country']=="":
                continue
    #過濾標題無國家名稱的訊息
            else:
                list_A['Color_Alert']=Color_Alert[s].text
                list_B.append(list_A)
        return list_B

def TravelNews(url):
    r = requests.get('https://www.boca.gov.tw/lp-56-1-xCat-4.html',verify=False)
    jieba.load_userdict("../jieba_dict/dict2.txt")
    #新增結巴辭意
    if r.status_code==requests.codes.ok:
      # 以 BeautifulSoup 解析 HTML 程式碼
      
        soup = BeautifulSoup(r.text, 'html.parser')
        Time = soup.find_all(attrs={'data-title':"張貼日"})
        Mess = soup.find_all(attrs={'data-title':"標題"})
        Web=soup.select('tr > td > a')
      
        list_B=[]
        for s in range(len(Time)):
            list_A={'Time':'','Country':'','Title':'','Website':''}
    
            M=Mess[s].text
            words = jieba.cut(M, cut_all=False)
            for word in words:
                if word in list_Country:
                    list_A['Country']=word
                else:
                    continue
            if list_A['Country']=="":
                continue
        #過濾標題無國家名稱的訊息
            else:
                list_A['Time']=Time[s].text
                list_A['Title']=Mess[s].text
                list_A['Website']=Web[s].get('href')
                list_B.append(list_A)
        return list_B

list_7=GoogleNews('https://news.google.com/search?q=%E6%88%B0%E7%88%AD%20when%3A60d&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
#最新戰爭
list_6=GoogleNews('https://news.google.com/search?q=%E4%B9%BE%E6%97%B1%20when%3A60d&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
#最新乾旱
list_5=GoogleNews('https://news.google.com/search?q=%E5%9C%8B%E9%9A%9B%E6%81%90%E6%94%BB%20%22%E6%81%90%E6%94%BB%22&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
#最新恐攻
list_4=GoogleNews('https://news.google.com/search?q=%E5%9C%8B%E9%9A%9B%E6%8A%97%E8%AD%B0%20%22%E6%8A%97%E8%AD%B0%22&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
#最新抗議
list_3=GoogleNews('https://news.google.com/search?q=%E6%B0%B4%E7%81%BD%20when%3A60d&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
#最新水災

list_1=Alert('https://www.boca.gov.tw/sp-trwa-list-1.html')
list_2=TravelNews('https://www.boca.gov.tw/lp-56-1-xCat-4.html')   


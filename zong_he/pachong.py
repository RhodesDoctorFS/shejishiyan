#client(客户端)
"""
http请求
request
get 只获取
post 读入用户输入数据，然后返回数据

1 使用httprequest工具模拟请求，接受返回的文本
包：requests
2 对接受文本进行筛选，获取信息
包：bs4（筛选文本）,lxml(筛选规则,辅助bs4)
3 爬取与反爬取
    程序访问和浏览器访问不同，
    requset的handle的属性不同，如果不是浏览器访问会被反爬屏蔽

    user-angent是重要的识别手段
    其次还有referer
    记录了前一个网站的utl
4 bs4的原理是将html文本转化为标签树结构，整个库就是对树结构进行处理来提取有用信息
 """
import requests#模拟html请求的包
from bs4 import BeautifulSoup
import lxml
from tabulate import tabulate #制表

def get_content(utr:str):
    header ={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }#伪装为浏览器访问
    reponse=requests.get(url,headers=header)#使用方法get来获取相应网页的页面信息，附带header信息进行伪装
    reponse_text=reponse.content.decode("utf-8")#使用utf-8规则解析文本
    return reponse_text#文本返回


def get_info(content:str):#抓取关键信息
    soup=BeautifulSoup(content,'lxml')#实例化bs，将文本输入并采用lxml规则进行筛选
    first_filter =soup.find('tbody')#定位到储存信息的标签位置
    data=[] #用于储存数据
    for tag in first_filter.children:#使用children遍历器遍历子节点
        name=tag.find_all_next('a')#提取所有标签为a的数据
        tags=tag.find_all_next('p')#提取p
        others=tag.find_all_next('td')#提取td
        data.append([
            others[0].text.strip(),#将第一个td标签的元素中的文本信息进行去除空行后加入data
            name[0].text.strip(),#同上
            name[1].text.strip(),#
            tags[0].text.strip(),#
            others[2].text.strip(),#
            others[3].text.strip(),#
            others[4].text.strip(),#
            others[5].text.strip()#
            ])
    headers=["排名","中文名","英文名","级别类型","所在地","学校类型","总分","办学层次"]
    table= tabulate(data,headers,tablefmt='pipe')
    print(table)#将信息打印

    
if __name__ =='__main__':
    url="https://www.shanghairanking.cn/rankings/bcur/202311"
    firsttext=get_content(url)
    get_info(firsttext)

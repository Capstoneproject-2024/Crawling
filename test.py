from driver import Element

from selenium.webdriver.common.keys import Keys
from Crawler import Crawl
import csv

import time
# 

# url = "https://pedia.watcha.com/ko-KR/?domain=book"
# element.url(url)

# NUM = 1282
# #f = open('test.csv','w', newline='')

# #wr = csv.writer(f)
# count=1

# element = Element()
# url1 = "https://cau.dkyobobook.co.kr/content/contentList.ink?brcd=&sntnAuthCode=&contentAll=Y&cttsDvsnCode=001&ctgrId=&orderByKey=publDate&selViewCnt=20&pageIndex="
# url2 = "&recordCount=20"

# for i in range(1,NUM+1):
#     url = url1+str(i)+url2
#     element.url(url)
#     books = element.find_all(css_class = "tit")
#     writer = element.find_all(css_class  = "writer")
#     for j in range(20):
#         try:
#             #wr.writerow([count,books[j].find(tag ="a").text(), writer[j].text()[-10:-6]])
#             count+=1
#             print(books[j].find(tag ="a").text())
#             print(writer[j].text()[-10:-6])
#         except Exception as e:
#             print("오류 발생:", e)
#     print("page:"+str(i))

# element.url(url)
# e = element.find_all(css_class = "tit")

# for i in e:
#     j = i.find(tag="a")
#     print(j.text())
# e = e.find(tag="a")
# print(e)
# print(e.text())
# l = element.find_all(css_class = "tit")
# for i in l:
#     j = i. find(tag = "a")
#     #print (j.text)

# c8163d6897c44e00a656

# bf517d4e5ad926d3a46d // 책 찾아야 함

# //*[@id="gnb"]/ul/li[1]/a
# //*[@id="container"]/div/ul/li[1]/div[2]/ul/li[1]/a
# //*[@id="container"]/div/ul/li[2]/div[2]/ul/li[1]/a
# //*[@id="container"]/div/ul/li[20]/div[2]/ul/li[1]/a
# # c = Crawl("공공부문 ESG 전략")
# c = Crawl("나는 스타벅스에서 그리스신화를 마신다","2024")

f = open('test.csv',"r")
rdr = csv.reader(f)
f2 = open('write.csv','w', newline='')
wr = csv.writer(f2)




c = Crawl()

def run(keyword, year):
    c.set(keyword, year)
    s = c.find()
    if s=="no":
        print("검색결과 없음")
    elif s=="":
        print("no")
    else:
        print(s)
        wr.writerow([keyword,year,s])




for line in rdr:
    try:
        run(line[1],line[2])
    except Exception:
        print()

# c.set("공공부문 ESG 전략","2024")

# s=c.find()
# if s=="no":
#     print("검색결과 없음")
# elif s=="":
#     print("no")
# else:
#     print(s)
    

# c.set("1년 만에 교포로 오해받은 김아란의 영어 정복기","2023")
# s=c.find()
# if s=="no":
#     print("검색결과 없음")
# elif s=="":
#     print("no")
# else:
#     print(s)

# c.set("나는 스타벅스에서 그리스신화를 마신다","2024")
# print ("b")
# s=c.find()
# if s=="no":
#     print("검색결과 없음")
# elif s=="":
#     print("no")
# else:
#     print(s)



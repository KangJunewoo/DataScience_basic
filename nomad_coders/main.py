import requests
from bs4 import BeautifulSoup

indeed_result = requests.get('https://www.indeed.com/jobs?q=python&limit=50')

#아래 코드 실행하면 엄청난 html 데이터가 물밀듯이 들어온다.ㄷㄷ
#print(indeed_result.text)

indeed_soup=BeautifulSoup(indeed_result.text, 'html.parser')

#find 함수를 사용해보자. div이면서 class=pagination을 갖고있는거.
#여기부턴 f12 사용하며 웹사이트 직접 들어가 찾아야한다.
pagination = indeed_soup.find('div', {'class':'pagination'})


links=pagination.find_all('a')
#아래를 실행해서 보니까, span에 페이지값이 들어있음.
#print(links)

'''
요렇게 span태그만 추출 가능
for link in links:
  print(link.find('span'))
'''

pages=[]
#필요없는 마지막 태그 떼주기
for link in links[:-1]:
  #사실 a태그 안에 span 안에 메인텍스트 하나밖에 없어서, find('span') 빼줘도 무방.
  pages.append(int(link.find('span').string))

max_page=pages[-1]
#range를 활용해

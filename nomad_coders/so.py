import requests
from bs4 import BeautifulSoup



URL=f"https://stackoverflow.com/jobs?q=python&sort=1"

def get_last_page():
  result=requests.get(URL)
  soup=BeautifulSoup(result.text, 'html.parser')
  #find는 젤 위에것만, find_all은 모든 목록을 리턴해준다.
  pages=soup.find('div', {'class':'s-pagination'}).find_all('a')
  #pages=soup.find('div', {'class':'pagination'}).find_all('a')
  #마지막거 떨궈주고 보니까.. 페이지가 겁나 많고 next로 넘어가는 식.
  #그래서 아래명령으로 보니까 101페이지..
  last_page=pages[-2].get_text(strip=True)
  return int(last_page)

def extract_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    print(page+1)


def get_jobs():
  last_page=get_last_page()
  jobs=extract_jobs(last_page)
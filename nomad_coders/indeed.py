import requests
from bs4 import BeautifulSoup

LIMIT=50
#앞에 f를 붙이면 {} 안에 변수참조가능.
URL=f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def extract_indeed_pages():  
  result = requests.get(URL)

  soup=BeautifulSoup(result.text, 'html.parser')

  #find 함수를 사용해보자. div이면서 class=pagination을 갖고있는거.
  #여기부턴 f12 사용하며 웹사이트 직접 들어가 찾아야한다.
  pagination = soup.find('div', {'class':'pagination'})


  links=pagination.find_all('a')
  pages=[]

  for link in links[:-1]:
    pages.append(int(link.find('span').string))

  max_page=pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs=[]
  #어느페이지를 크롤링할지 구했으니, 이제 request만 남았다.
  for page in range(last_page):
    result=requests.get(f'{URL}&start={page*LIMIT}')
    print(result.status_code)
  return jobs
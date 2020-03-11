import requests
from bs4 import BeautifulSoup

LIMIT=50
#앞에 f를 붙이면 {} 안에 변수참조가능.
URL=f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def get_last_page():  
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

def extract_job(html):
  title=html.find('div', {'class':'title'}).find('a')['title']
  #링크가 있는 회사가 있고 없는 회사가 있다.
  company = html.find('span', {'class':'company'})
  if company:
    company_anchor=company.find('a')
    if company_anchor is not None:
      company=str(company_anchor.string)
    else:
      company=str(company.string)
    #빈칸을 해결하기 위해 strip을 사용하자.
    company=company.strip()
  else:
    company=None
  #location이 모두 있다면 아래코드를 쓰면 된다. 근데 가끔 None이 잡히므로..
  #location = html.find('span',{'class':'location'}).string
  #다음과 같은 클래스에선 항상 loc 값이 들어있는 걸 이용.
  location=html.find('div', {'class':'recJobLoc'})['data-rc-loc']
  job_id=html['data-jk']
  #항상 print를 해주면서 확인해주는거 잊지 말자.
  return {
    'title':title,
    'company':company,
    'location':location,
    'job_id':job_id
    }


def extract_jobs(last_page):
  jobs=[]
  
  #어느페이지를 크롤링할지 구했으니, 이제 request만 남았다.
  # for page in range(last_page):
  #코딩중에는 page=0으로 잡아서 단순하게.
  for page in range(last_page):
    print(f'Scrapping Indeed : page {page}')
    result=requests.get(f'{URL}&start={page*LIMIT}')
    soup=BeautifulSoup(result.text, 'html.parser')
    results=soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
    #a태그에서 title을 가져오도록 하자.
    for result in results:
      job=extract_job(result)
      jobs.append(job)
  return jobs

#조금만 가져오고 싶다면, 둘째줄에 1이나 2 넣자.
def get_jobs():
  '''
  이 코드가 오리지날. 시간관계상 두 페이지만 스크레이핑해보자.
  last_page=get_last_page()
  jobs=extract_jobs(last_page)
  '''
  jobs=extract_jobs(2)
  return jobs
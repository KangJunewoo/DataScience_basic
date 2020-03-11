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

def extract_job(html):
  job_info=[]
  #스택오버플로우 사이트가 강의때랑 달라져서, 직접 실습 ㄱㄱ.
  infos=html.find_all('div', {'class':'grid--cell fl1'})
  for info in infos:
    title=info.find('h2', {'class':'mb4'}).find('a', {'class':'s-link'})['title']
    comp_loc=info.find('h3').find_all('span')
    company=comp_loc[0].get_text().strip()
    location=comp_loc[1].get_text().strip()
    '''
    print({
      'title':title,
      'company':company,
      'location':location
    })
    return 0
    '''
    job={
      'title':title,
      'company':company,
      'location':location
    }
    #print(job)
    job_info.append(job)
  return job_info


def extract_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    print(f'Scrapping SO : Page {page}')
    result=requests.get(f'{URL}&pg{page+1}')
    soup = BeautifulSoup(result.text,'html.parser')
    results=soup.find_all('div', {'class':'listResults'})
    for result in results:
      job=extract_job(result)
      jobs+=job
  
  return jobs




def get_jobs():
  '''
  이 코드가 오리지날. 시간관계상 두 페이지만 스크레이핑해보자.
  last_page=get_last_page()
  
  jobs=extract_jobs(last_page)
  '''
  jobs=extract_jobs(2)
  return jobs
  #print(jobs)
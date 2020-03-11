from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file_indeed, save_to_file_so

indeed_jobs = get_indeed_jobs()
so_jobs=get_so_jobs()
#print(indeed_jobs)
#print(so_jobs)
save_to_file_indeed(indeed_jobs)
save_to_file_so(so_jobs)
myfile = open("jobs.txt", "r")
jobs = myfile.read().split('\n')
myfile.close()
job_list = []

for j in jobs[1: -1]:
	job = j.split()
	w, l = int(job[0]), int(job[1])
	job_list.append((w, l))

def comp(job1, job2):
	if float(job1[0]) / job1[1] == float(job2[0]) / job2[1]:
		return -cmp(job1[0], job2[0])
	else:
		return -cmp( float(job1[0]) / job1[1], float(job2[0]) / job2[1])

job_list.sort(comp)

s, t = 0, 0

for j in job_list:
	t += j[1]
	s += j[0] * t

print s
	
	
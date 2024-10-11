import os

def sorted_text():
	leen = {}
	tot = []
	lo = []

	for x in os.scandir('sorte'):
		result = os.path.split(x)
		with open(x, 'r', encoding='utf-8') as f:
			file = f.readlines()
			a = len(file)
			leen[a] = result[1]
			lo.append(len(file))
	sor = sorted(leen)
	for l in sor:
		tot.append(leen[l])
	lo_sort = sorted(lo)
	for long, name in zip(lo_sort, tot):
		with open(os.path.join('sorte', name), 'r', encoding='utf-8') as f:
			read = f.readlines()
		with open('res.txt', 'a',  encoding='utf-8') as wf:
			lk = str(long)
			wf.write(name)
			wf.write('\n')
			wf.write(lk)
			wf.write('\n')
			wf.writelines(read)
			wf.writelines('\n')

sorted_text()
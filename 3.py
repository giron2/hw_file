import os


def sort():
	text_1 = '1.txt'
	text_2 = '2.txt'
	text_3 = '3.txt'
	res = "res.txt"
	file1_path = os.path.join(os.getcwd(), text_1)
	file2_path = os.path.join(os.getcwd(), text_2)
	file3_path = os.path.join(os.getcwd(), text_3)
	with open(file1_path, 'r', encoding='utf-8') as f1:
		file1 = f1.readlines()
	with open(file2_path, 'r', encoding='utf-8') as f2:
		file2 = f2.readlines()
	with open(file3_path, 'r', encoding='utf-8') as f3:
		file3 = f3.readlines()
	with open(res, 'w', encoding='utf-8') as f:

		if len(file1) < len(file2) and len(file1) < len(file3):
			f.write(text_1 + '\n')
			f.write(str(len(file1)) + '\n')
			f.writelines(file1)
			f.write('\n')
		elif len(file2) < len(file1) and len(file2) < len(file3):
			f.write(text_2 + '\n')
			f.write(str(len(file2)) + '\n')
			f.writelines(file2)
			f.write('\n')
		elif len(file3) < len(file1) and len(file3) < len(file2):
			f.write(text_3 + '\n')
			f.write(str(len(file3)) + '\n')
			f.writelines(file3)
			f.write('\n')
		if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
				file3):
			f.write(text_1 + '\n')
			f.write(str(len(file1)) + '\n')
			f.writelines(file1)
			f.write('\n')
		elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
				file3):
			f.write(text_2 + '\n')
			f.write(str(len(file2)) + '\n')
			f.writelines(file2)
			f.write('\n')
		elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
				file2):
			f.write(text_3 + '\n')
			f.write(str(len(file3)) + '\n')
			f.writelines(file3)
			f.write('\n')
		if len(file1) > len(file2) and len(file1) > len(file3):
			f.write(text_1 + '\n')
			f.write(str(len(file1)) + '\n')
			f.writelines(file1)
		elif len(file2) > len(file1) and len(file2) > len(file3):
			f.write(text_2 + '\n')
			fl.write(str(len(file2)) + '\n')
			f.writelines(file2)
		elif len(file3) > len(file1) and len(file3) > len(file2):
			f.write(text_3 + '\n')
			f.write(str(len(file3)) + '\n')
			f.writelines(file3)
sort()
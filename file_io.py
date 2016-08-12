

class File_IO:


	def __init__(self):pass



	def  write_file(self,file_name,data):

		with open(file_name,'w') as f:

			for d in data:
				f.write(d+"\n")


	def getLines(self,file_name):

		try:

			lines=[]


			with open(file_name) as f:

			

				for line in f:
					lines.append(line)

		except FileNotFoundError as e:
			print(e)

		return lines





if __name__ == "__main__":

	

	f_io=File_IO()

	lines=f_io.getLines('pos.txt')

	if len(lines) == 0:
		print("There is no line in the file.")

	else:
		for line in lines:
			print(line,end='')





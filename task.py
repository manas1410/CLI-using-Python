import sys
import collections
from itertools import islice
import os 

parser =sys.argv 

f =  open('task.txt','a+')

dic = {}
dic_done = {}


def add_del(key, value):
	f =  open('task.txt','a+')
	f.write(value+" "+key+"\n")
	f.close()

def add(key, value):
	f =  open('task.txt','a+')
	f.write(value+" "+key+"\n")
	print("Added task: "+'"'+key+'"'+" with priority "+value)
	f.close()

def sort_dic(read_lines):
	#print(read_lines)
	for i in read_lines:
		for j in range(len(i)):
			if i[j] == ' ':
				value = i[0:j]
				break

		#for k in range(j+1,len(i)):
			#print(i[k]) 
		key = i[j+1:-1:]
		
		dic[key] = int(value)
	#print(dic)

	sorted_values = sorted(dic.items(), key=lambda kv: kv[1])
	return collections.OrderedDict(sorted_values)

def sort_dic_done(read_lines):
	#print(read_lines)
	for i in read_lines:
		for j in range(len(i)):
			if i[j] == ' ':
				value = i[0:j]
				break

		#for k in range(j+1,len(i)):
			#print(i[k]) 
		key = i[j+1:len(i):]
		dic_done[key] = int(value)
	#print(dic)

	sorted_values = sorted(dic_done.items(), key=lambda kv: kv[1])
	return collections.OrderedDict(sorted_values)


def ls():
	f =  open('task.txt','r')
	read_lines = f.readlines()
	sorted_dic = sort_dic(read_lines)

	c = 1
	if (len(sorted_dic)>0):
		for i in sorted_dic.keys():
			print(str(c)+". "+i+" ["+str(sorted_dic[i])+"]")
			c += 1
	else:
		print("There are no pending tasks!")
	f.close()


#def delete():
def done(done_no):
	if (int(done_no) == 0):
		print("Error: no incomplete item with index #0 exists.")
	elif (int(done_no) <0):
		print("Error: no incomplete item with index #"+done_no+" exists.")
	else:

		f =  open('task.txt','r')
		read_lines = f.readlines()
		sorted_dic = sort_dic(read_lines)
		f.close()
		if int(done_no)<=len(sorted_dic):
			f =  open('task.txt','w+')
			f_com = open('completed.txt','a+')
			c = 1
			for i in sorted_dic.keys():
				if c==int(done_no):
					f_com.write(str(sorted_dic[i])+" "+i+"\n")
				else:
					f.write(str(sorted_dic[i])+" "+i+"\n")
				c += 1
			f_com.close()
			f.close()
			print("Marked item as done.")
		else:
			print("Error: no incomplete item with index #"+done_no+" exists.")

def report():
	f =  open('task.txt','r')
	read_lines = f.readlines()
	sorted_dic = sort_dic(read_lines)

	print("Pending"+" : "+str(len(sorted_dic)))

	c = 1
	for i in sorted_dic.keys():
		print(str(c)+". "+i+" ["+str(sorted_dic[i])+"]")
		c += 1 
	f.close()


	f_com = open('completed.txt','r')
	read_lines = f_com.readlines()
	sorted_dic = sort_dic_done(read_lines)
	v=0
	for i in sorted_dic.keys():
		v += 1 

	print("\nCompleted"+" : "+str(v))
	c = 1
	for i in sorted_dic.keys():
		print(str(c)+". "+i[0:-1:])
		c += 1 
	f_com.close()

def delete(delete_no):
	f =  open('task.txt','r')
	read_lines = f.readlines()
	sorted_dic = sort_dic(read_lines)
	try:
		del sorted_dic[next(islice(sorted_dic, int(delete_no)-1, None))]
		v=0
		f.close()
		os.remove('task.txt')

		for i in sorted_dic.keys():
			add_del(i,str(sorted_dic[i]))

		print("Deleted task #"+str(delete_no))
	except:
		print("Error: task with index #"+delete_no+" does not exist. Nothing deleted.")

def help():
	print('Usage :-')
	print('$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list')
	print('$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order')
	print('$ ./task del INDEX            # Delete the incomplete item with the given index')
	print('$ ./task done INDEX           # Mark the incomplete item with the given index as complete')
	print('$ ./task help                 # Show usage')
	print('$ ./task report               # Statistics')

	

if len(parser) == 1:
	help()
elif parser[1] == 'add':
	if len(parser) <= 3:
		print('Error: Missing tasks string. Nothing added!')
	else:
		s=""
		for i in range(3,len(parser)):
			s+=parser[i]+" "
		add(s[0:-1:],parser[2])

elif parser[1] == 'ls':
	ls()
elif parser[1] == 'done':
	if len(parser) == 2:
		print('Error: Missing NUMBER for marking tasks as done.')
	else:
		done(parser[2])
elif parser[1] == 'report':
	report()
elif parser[1] == 'del':
	if len(parser) == 2:
		print('Error: Missing NUMBER for deleting tasks.')
	else:
		delete(parser[2])
elif parser[1] == 'help':
	help()
else:
	print("")





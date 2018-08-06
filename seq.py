from collections import OrderedDict
import itertools
list=[]
copylist=[]
leftmost={};
copies={};
i=0
f = open("input.txt")
for line in f:
   list.append(line)
   copylist.append(line)
for s in list:
	if s.split()[0].lower() in leftmost:
		leftmost[s.split()[0].lower()]=leftmost[s.split()[0].lower()]+1
	else:
		leftmost[s.split()[0].lower()]=1
		copies[s.split()[0].lower().lower()]=[]
	copies[s.split()[0].lower()].append(i);
	i=i+1
#sorted(leftmost.items(), key= ,reverse=True)
#print sorted(leftmost.values())
left=OrderedDict(sorted(leftmost.items(), key=lambda x:x[1],reverse=True))
delete=""
for key, value in left.iteritems():
	delete=key
#	print key, value
	break
super=OrderedDict()
super[delete]=[]
for i in copies[delete]:
    list[i]=list[i].split(' ',1)[1]
leftmost.pop(delete,"error")
s=[]
while delete:
	s=copies[delete]
	copies.pop(delete,"error")
	for i in s:
		if list[i]:
#			print i,":",list[i]
#			print "chopped:",list[i].split()[0]
			if (list[i].split()[0]).lower() in leftmost:
#				print "in leftmost:",list[i].split()[0]
				leftmost[(list[i].split()[0]).lower()]=leftmost[(list[i].split()[0]).lower()]+1
			else:
				leftmost[(list[i].split()[0]).lower()]=1
				copies[(list[i].split()[0]).lower()]=[]
			copies[(list[i].split()[0]).lower()].append(i)
#	for key, value in copies.iteritems():
#		print key,value
#	print "\n\n\n"
	left=OrderedDict(sorted(leftmost.items(), key=lambda x:x[1],reverse=True))
	delete=""
	for key, value in left.iteritems():
		delete=key
		#print "delete:",delete
		break
	#print "\n\n\n"
	leftmost.pop(delete,"error")
	if not delete in super:
		super[delete]=[]
	if delete:
		for i in copies[delete]:
			#print "i in delete",i,"/",delete
			if list[i]:
				#print "in if of delete",list[i]
				s=list[i].split(' ',1)
				#for t in s:
					#print "in if of delete :1t",t,"/"
				if len(s)>1:				
					list[i]=s[1]
				else:
					list[i]=""
				#print "in if of 1 after delete",list[i]
#for key,value in super.items():
#	print key,""
#print "\nmatrix:"
x=1
for s in copylist:
	#print "s:",s
	t=s.split()
	for word in t:
#		print "inword:",word
		super[word.lower()].append(word.lower())
	for key,value in super.items():
		while len(value)<x:
			super[key].append(None)
	x=x+1		
temptemplate={}
superorig=super.copy()
templist=[]
templist.append(" ")
for key,value in super.items():
	#print "key:",key
	templst=value
	super.pop(key,"error")
	if key in templist:
		continue
	temptemplate[key]=[]
	for tempky,tempval in super.items():
		#print "in inner loop: ",tempky
		val=0
		for val1,val2 in itertools.izip_longest(templst,tempval):
			if val1 is not None:
				if val2 is not None:
				    continue
			if val1 is None:
				if val2 is None:
					continue
			val=1
			break
		if val==0:
			temptemplate[key].append(tempky)
			templist.append(tempky)
			superorig.pop(tempky,"error")
joindict={}
for key,value in temptemplate.items():
	z=key
	for s in value:
		z=z+" "+s
	temptemplate[key]=z
templist=[]
templist.append(" ")
for key,value in superorig.items():
	#print "key:",key
	templst=value
	superorig.pop(key,"error")
	if key in templist:
		continue
	joindict[key]=[]
	for tempky,tempval in superorig.items():
		#print "in inner loop: ",tempky
		val=0
		for val1,val2 in itertools.izip_longest(templst,tempval):
			if val1 is not None:
				if val2 is None:
				    continue
			if val1 is None:
				if val2 is None:
					continue
			if val1 is None:
				if val2 is not None:
				    continue
			val=1
			break
		if val==0:
			joindict[key].append(tempky)
			templist.append(tempky)
			superorig.pop(tempky,"error")
templates=[]
for key,value in joindict.items():
	s=temptemplate[key]
	for val in value:
		s=s+" | "+temptemplate[val]
	templates.append(s)
for template in templates:
	print template
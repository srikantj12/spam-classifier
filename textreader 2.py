#from lxml import etree
#from io import StringIO, BytesIO
#import codecs
#f=codecs.open("E:\\final year project\\data\\dat\\html\\friends.htm", 'r')
#parser=etree.HTMLParser()
#z=f.read()
#tree   = etree.parse(BytesIO(z), parser)
#result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
#print(result)
import xlsxwriter
import sys
import os
def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r',encoding='utf-8', errors='ignore')
        a_list.append(f.read())
    f.close()
    return a_list
 
if __name__ == "__main__":
    # initialise the data
	spam = init_lists('enron1/spam/')
	ham = init_lists('enron1/ham/')
	workbook = xlsxwriter.Workbook('demo2.csv')
	worksheet = workbook.add_worksheet()
	worksheet.set_column('A:A', 20)
	worksheet.set_column('A:B', 20)
	worksheet.set_column('A:C', 20)
	bold = workbook.add_format({'bold': True})
	worksheet.write('A1', 'Sender',bold)
	worksheet.write('B1', 'Message',bold)
	worksheet.write('C1', 'spam/ham',bold)
	#reload(sys)  
	#sys.setdefaultencoding('utf8')
	"""f=open("E:\\final year project\\data\\sms\\SMSSpamCollection")
	i=0
	for line in f:
		print line
		line=line.strip()
		s=line.split(" ",1)
		t=s[0].split()
		print t
		if len(t)>1:
			if len(s)>1:
				print t[1]
				s[1]=t[1]+s[1]
			else:
				s.append(t[1])
		worksheet.write('A'+str(i),"user"+str(i))
		worksheet.write('B'+str(i),s[1])
		worksheet.write('C'+str(i),t[0])
		i=i+1"""
	i=0
	for line in spam:
		#line=line.encode('utf-8').strip()
		worksheet.write('B'+str(i),line)
		worksheet.write('C'+str(i),"spam")
		i=i+1
	for line in ham:
		#line=line.encode('utf-8').strip()
		worksheet.write('B'+str(i),line)
		worksheet.write('C'+str(i),"spam")
		i=i+1
	workbook.close()
from subprocess import check_output
from datetime import date
import sys

today = date.today()

persent_date = today.strftime('%Y-%m-%d')
print("Today's date:",persent_date)

date_string = check_output('git log -1 --pretty=format:"%ci"'.split()).decode()




#print(date_string)  #// get the log of date
data1 = date_string.split(' ',-1)
data = data1[0]
#print(data)
print(data[1:])


#print("Last Commited Date:",data[0])
print(data[0]==persent_date)
if (data[0] == persent_date):
    print("Validation successfull")
else:
    sys.exit(-1)
    


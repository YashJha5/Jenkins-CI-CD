from subprocess import check_output
from datetime import date

today = date.today()

taareekh = today.strftime('%Y-%m-%d')
print("Today's date:",taareekh)

date_string = check_output('git log -1 --pretty=format:"%ci"').decode()


#print(date_string)  // get the log of date
data = date_string.split()
#print(data)
#print(data[0])


#print("Last Commited Date:",data[0])
print(data[0]==taareekh)
if (data[0] == today):
    print("Yusss Now we can build the setup")
else: 
    False


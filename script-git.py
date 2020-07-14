from subprocess import check_output
from datetime import date

today = date.today()
print("Today's date:", today)

date_string = check_output('git log -1 --pretty=format:"%ci"').decode()


#print(date_string)  // get the log of date
data = date_string.split( )


print(data[0])
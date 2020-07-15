import subprocess
from datetime import date
import sys


cmd = subprocess.Popen(['git','log','-1','--pretty=format:"%ci"'], stdout=subprocess.PIPE)
output = cmd.communicate()[0]
#print cmd.returncode
print output

data1 = output.split(' ',-1)
data2 = data1[0]
data = data2[1:]


print(data)

today = date.today()
persent_date = today.strftime('%Y-%m-%d')
print("Today's date:",persent_date)

print(data==persent_date)

if (data == persent_date):
    print("Validation successfull")
else:
    sys.exit(-1)
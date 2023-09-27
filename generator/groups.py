import os
import getopt
import sys
from comtypes.client import CreateObject
from random import randrange


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file name"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 10
f = "data/groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
xl = CreateObject("Excel.Application")
xl.Visible = False
xl.DisplayAlerts = False

wb = xl.Workbooks.Add()
for i in range(n):
    group_name = "TestGroupName_" + str(randrange(100, 999))
    print("[" + str(i+1) + "]:" + group_name)
    xl.Range["A%s" % (i+1)].Value[()] = group_name

wb.SaveAs(os.path.join(project_dir, f))
wb.Close()
xl.Quit()

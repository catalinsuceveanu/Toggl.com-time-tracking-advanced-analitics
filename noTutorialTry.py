import requests
import xlsxwriter
import json

recievedData = requests.get ('https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')
workbook = xlsxwriter.Workbook("noTutorialTest.xlsx")
theWorkingSheet = workbook.add_worksheet('first_test')

theWorkingSheet.write ('A1', 'No.')
theWorkingSheet.write ('B1', 'Stack Overflow Question')
theWorkingSheet.write ('C1', 'Link')

index = 2
no = 1

for data in recievedData.json()['items']:
    theWorkingSheet.write ('A'+str(no), no)
    theWorkingSheet.write ('B'+str(index), data['title'])
    theWorkingSheet.write ('C'+str(index), data['link'])
    index +=1
    no +=1
workbook.close()
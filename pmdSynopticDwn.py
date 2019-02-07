# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:15:41 2016

@author: MuhammadAdilJaved
"""
import re
import time
from mechanize import Browser
br = Browser()
br.set_handle_robots(False)

br.open("http://www.pmd.gov.pk/cp/display.asp")
br.select_form(nr=0)
form = br.form #
controlDate = br.form.find_control("dat")
controlTime = br.form.find_control("Tim")
backdays = 1            #for how many days in back you want to download data, max. 15
start_time = time.time()
dateList = []
dateListPMD = []

timeList = ['0000', '0300', '0600', '0900', '1200', '1500', '1800', '2100']

#Visit "http://www.pmd.gov.pk/cp/display.asp" and put the available dates in List below
#dateList = ['5/10/2016','5/9/2016',\
#			'5/8/2016','5/7/2016',\
#			'5/6/2016','5/5/2016',\
#			'5/4/2016','5/3/2016',\
#			'5/2/2016','5/1/2016',\
#			'4/30/2016','4/29/2016',\
#			'4/28/2016','4/27/2016',\
#			'4/26/2016']

for item in controlDate.items:
        dateListPMD.append(item.name)
        
for date in dateListPMD[0:int(backdays)]:
    dateList.append(date)
    
print "**** Downloading data for following dates: ****"
print dateList
#short dateList for debugging
#dateList = ['5/10/2016','5/9/2016']
#dateList = ['5/10/2016']

i = 0   #for DATE Loop
ii = 0  #for TIME Loop
count = 0 #to calculate no of files Downloaded
for dt in dateList:
    br.open("http://www.pmd.gov.pk/cp/display.asp")
    br.select_form(nr=0)
    form = br.form #
    controlDate = br.form.find_control("dat")
    controlTime = br.form.find_control("Tim")
    for item in controlDate.items:
        if item.name == dt:
            item.selected = True
            dtFileName = dt.translate(None, '!@#$/')
            print "Required DATE found i.e "
            print item.name, dt
            print "DATE loop # ", i
            i = i+1
            for dti in timeList:
                br.open("http://www.pmd.gov.pk/cp/display.asp")
                br.select_form(nr=0)
                form = br.form #
                controlDate = br.form.find_control("dat")
                controlTime = br.form.find_control("Tim")

                for item in controlDate.items:  #
                    if item.name == dt:         #
                        for item2 in controlTime.items:
                            if item2.name == dti:
                                print "Require TIME found & Downloading File i.e "
                                print item2.name, dti
                                print "TIME loop # ", ii
                                ii = ii + 1
                                item.selected = True                        
                                item2.selected = True
                                synoptic = (br.submit()).read()
                                soup = re.sub('<[^>]*>', '', synoptic)            
                                textFile = open(str(dtFileName)+str(dti)+'.txt', 'wb')
                                textFile.write(soup)
                                textFile.close()
                                count = count + 1
                            else:
                                #print "Required TIME NOT found"
                                print item2.name, dti
        else:
            #print "Required DATE NOT found"
            print item.name, dt


elapsed_time = (time.time() - start_time)/60
print "*****************************"
print "Total Elapsed Time: ", round(elapsed_time,2), " Mins."
print "Total Files Downloaded: ", str(count)
print "*****  F I N I S H E D  *****"

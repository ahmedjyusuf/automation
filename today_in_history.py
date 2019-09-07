import os
import datetime

# get current date
mydate = datetime.datetime.now()
month = mydate.strftime("%B")
today = mydate.strftime("%d")
year_now = mydate.strftime("%Y")
print(month, today, year_now)

#I parsed and downloaded thousands of articles from Reuters
# arctiles are organized by years and months
# and the files names also start witht yy/mm/dd ie. 2014-09-05 Nigeria sends in warplanes...

def check_date(site):
    for year in range(2012, 2020):
        directory = f'/Users/ahmedyusuf/{site}/{year}/{month}'
        if os.path.exists(directory): 
            for f in os.listdir(directory):
                
                # now let's get the month and year from the file names
                f_date = f.split()
                f_date = f_date[0].split('-')
                f_year = f_date[0]
                f_date = f_date[2]
                
                # any article dated todays date from 2012 up to 2020
                if f_date == today: 
                    #print(f)
                    year_ago = int(year_now) - int(f_year)
                    print(f"on todays date {year_ago} year(s) ago \n{f}\n\n")
            else:
                pass

check_date('Reuters')

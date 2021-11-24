import csv
from datetime import datetime

#empty list
leads = []
file_path = r"C:\Users\olivi\source\repos\RegistrationMetrics\SimpleMetrics.csv"

input_file = csv.DictReader(open(file_path))

for row in input_file:
    leads.append(row)

#print(leads)

#Referral Metrics
    social_media_count = 0
    referral_count = 0
    flyer_count = 0
    other_count = 0

    for row in leads:
        if row['How did you hear about us'] == 'Social Media':
            social_media_count = social_media_count + 1

    social_percent = int(100*social_media_count/len(leads))

    for row in leads:
        if row['How did you hear about us'] == 'Referral':
            referral_count = referral_count + 1

    referral_percent = int(100*referral_count/len(leads))

    for row in leads:
        if row['How did you hear about us'] == 'Flyer':
            flyer_count = flyer_count + 1

    flyer_percent = int(100*flyer_count/len(leads))

    for row in leads:
        if row['How did you hear about us'] == 'Other':
            other_count = other_count + 1

    other_percent = int(100*other_count/len(leads))

#Class Selection Metrics
    beginner5_count = 0
    beginner14_count = 0
    trial_count = 0
    intermediate_count = 0
    subscribe_count = 0

    for row in leads:
        if row['Class Selection'] == 'Beginner (5+)':
            beginner5_count = beginner5_count + 1
        elif row['Class Selection'] == 'Beginner (14+)':
            beginner14_count = beginner14_count + 1
        elif row['Class Selection'] == 'Trial Class':
            trial_count = trial_count + 1
        elif row['Class Selection'] == 'Intermediate (Instructor approval required)':
            intermediate_count = intermediate_count + 1
        elif row['Class Selection'] == 'Subscribe for Updates':
            subscribe_count = subscribe_count + 1
        
        beginner5_percent = int(100*beginner5_count/len(leads))
        beginner14_percent = int(100*beginner14_count/len(leads))
        trial_percent = int(100*trial_count/len(leads))
        intermediate_percent = int(100*intermediate_count/len(leads))
        subscribe_percent = int(100*subscribe_count/len(leads))

 
print("Number of leads: ", len(leads))
print("Lead Source Breakdown:")
print("          Referral: ", referral_count, " (", referral_percent, "%)", sep="")
print("          Social Media: ", social_media_count, " (", social_percent, "%)", sep="")
print("          Flyer: ", flyer_count, " (", flyer_percent, "%)", sep="")
print("          Other: ", other_count, " (", other_percent, "%)", sep="")

print("Class Selection (Customer Type) Breakdown:")
print("          Beginners (ages 5-13): ", beginner5_count, " (", beginner5_percent, "%)", sep="")
print("          Beginners (ages 14+): ", beginner14_count, " (", beginner14_count, "%)", sep="")
print("          Intermediate (all ages, usually a transfer from another studio): ", intermediate_count, " (", intermediate_count, "%)", sep="")
print("          Trial (all ages): ", trial_count, " (", trial_percent, "%)", sep="")
print("          Subscribe for Updates: ", subscribe_count, " (", subscribe_percent, "%)", sep="")


#Calculate age of student

date_string = '10-26-1997'
date = datetime.strptime(date_string, '%m-%d-%Y')

age = (date.today().year - date.year)

print(age, " years old")


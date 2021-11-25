import csv
from datetime import datetime

import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
import urllib.parse

#empty list
leads = []
file_path = r"C:\Users\olivi\source\repos\RegistrationMetrics\MetricsSimple.csv"
input_file = csv.DictReader(open(file_path))

for row in input_file:
    leads.append(row)

print("Number of leads: ", len(leads))

#Referral Metrics
social_media_count = 0
referral_count = 0
flyer_count = 0
other_count = 0

for row in leads:
    if row['How did you hear about us'] == 'Social Media':
        social_media_count = social_media_count + 1
    elif row['How did you hear about us'] == 'Referral':
        referral_count = referral_count + 1
    elif row['How did you hear about us'] == 'Flyer':
        flyer_count = flyer_count + 1
    elif row['How did you hear about us'] == 'Other':
        other_count = other_count + 1

social_percent = int(100*social_media_count/len(leads))
referral_percent = int(100*referral_count/len(leads))
other_percent = int(100*other_count/len(leads))
flyer_percent = int(100*flyer_count/len(leads))

print("Lead Source Breakdown:")
print("          Referral: ", referral_count, " (", referral_percent, "%)", sep="")
print("          Social Media: ", social_media_count, " (", social_percent, "%)", sep="")
print("          Flyer: ", flyer_count, " (", flyer_percent, "%)", sep="")
print("          Other: ", other_count, " (", other_percent, "%)", sep="")

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
    elif row['Class Selection'] == 'Intermediate (Instructor approval required)':
        intermediate_count = intermediate_count + 1
    elif row['Class Selection'] == 'Trial Class':
        trial_count = trial_count + 1
    elif row['Class Selection'] == 'Subscribe for Updates':
        subscribe_count = subscribe_count + 1
    
beginner5_percent = int(100*beginner5_count/len(leads))
beginner14_percent = int(100*beginner14_count/len(leads))
intermediate_percent = int(100*intermediate_count/len(leads))
trial_percent = int(100*trial_count/len(leads))
subscribe_percent = int(100*subscribe_count/len(leads))

print("Class Selection (Customer Type) Breakdown:")
print("          Beginners (ages 5-13): ", beginner5_count, " (", beginner5_percent, "%)", sep="")
print("          Beginners (ages 14+): ", beginner14_count, " (", beginner14_count, "%)", sep="")
print("          Intermediate (all ages, usually a transfer from another studio): ", intermediate_count, " (", intermediate_count, "%)", sep="")
print("          Trial (all ages): ", trial_count, " (", trial_percent, "%)", sep="")
print("          Subscribe for Updates: ", subscribe_count, " (", subscribe_percent, "%)", sep="")

#Calculate age of each student

age_sum = 0

for row in leads:
    dob = row["Date of Birth"]
    date = datetime.strptime(dob, '%m/%d/%Y')
    row['age'] = (date.today().year - date.year)
    age_sum = row['age'] + age_sum

age_avg = age_sum / len(leads)

print('Demographics:')
print("          Average age: ", round(age_avg, 2))

#Use distance matrix API

API = input("Enter the API Key:/n")

import requests
import json

distance_sum = 0
duration_sum = 0

#Get the driving distance and duration for each lead from their given address to our business location

for row in leads:
    lead_address = row['Address']
    #print(lead_address)

    lead_address_URL = urllib.parse.quote(lead_address)

    #print(lead_address_URL)

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=420+E+8th+Street,+New+Albany,+IN&destinations=" + lead_address_URL + '&units=imperial&key=' + API
    #print(url) 

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)
    distance_value = (json.loads(response.text))["rows"][0]["elements"][0]["distance"]["value"]
    distance_sum = distance_sum + distance_value

    duration_text = (json.loads(response.text))["rows"][0]["elements"][0]["duration"]["text"]
    duration_value = (json.loads(response.text))["rows"][0]["elements"][0]["duration"]["value"]
    duration_sum = duration_sum + duration_value

#Convert meters to miles (distance) and seconds to hours (duration) and calculate average
distance_avg = round((distance_sum*0.000621371)/len(leads), 2)
duration_avg = round((duration_sum/60)/len(leads), 2)

print("          Average Driving Distance: ", distance_avg, "miles")
print("          Average Driving Time: ", duration_avg, "minutes")
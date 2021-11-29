import csv
from datetime import datetime

import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
import urllib.parse


import requests
import json


print("")
print("Welcome to Registration Metrics")
print("-------------------------------")

#empty list
leads = []
file_path = "./MetricsSimple.csv"
input_file = csv.DictReader(open(file_path))

#collect the API Key
API = input("Enter the API Key:")

for row in input_file:
    leads.append(row)

print("Number of leads: ", len(leads))

#Referral Metrics

#function to calculate distribution %
def calculate_percent(category, denominator, input):
    numerator = 0
    for row in leads:
            if row[category] == input:
                numerator  = numerator + 1 
            else: 
                numerator = numerator
    percent = int(100*(numerator/len(denominator)))
    return percent

#Call calculate_percent() and display Lead Source metrics
social_percent = calculate_percent("How did you hear about us", leads, "Social Media")
referral_percent = calculate_percent("How did you hear about us", leads, "Referral")
other_percent = calculate_percent("How did you hear about us", leads, "Other")
flyer_percent = calculate_percent("How did you hear about us", leads, "Flyer")

print("Lead Source Breakdown:")
print("                       Referral:", " ", referral_percent, "%", sep="")
print("                       Social Media:", " ", social_percent, "%", sep="")
print("                       Flyer:", " ", flyer_percent, "%", sep="")
print("                       Other:", " ", other_percent, "%", sep="")

#Call calculate_percent() and display Class Selection metrics

beginner5_percent = calculate_percent("Class Selection", leads, 'Beginner (5+)')
beginner14_percent = calculate_percent("Class Selection", leads, 'Beginner (14+)')
intermediate_percent = calculate_percent("Class Selection", leads, 'Intermediate (Instructor approval required)')
trial_percent = calculate_percent("Class Selection", leads, 'Trial Class')
subscribe_percent = calculate_percent("Class Selection", leads, 'Subscribe for Updates')

print("Class Selection Breakdown:")
print("                       Beginners (ages 5-13): ", beginner5_percent, "%", sep="")
print("                       Beginners (ages 14+): ", beginner14_percent, "%", sep="")
print("                       Intermediate: ", intermediate_percent, "%", sep="")
print("                       Trial (all ages): ",trial_percent, "%", sep="")
print("                       Subscribe for Updates: ",subscribe_percent, "%", sep="")

#Calculate age of each student

age_sum = 0

for row in leads:
    dob = row["Date of Birth"]
    date = datetime.strptime(dob, '%m/%d/%Y')
    row['age'] = (date.today().year - date.year)
    age_sum = row['age'] + age_sum

age_avg = age_sum / len(leads)

print('Demographics:')
print("                       Average age: ", round(age_avg, 2))

#Use Google Distance Matrix API
#Get the driving distance and duration for each lead from their given address to our business location

distance_sum = 0
duration_sum = 0

for row in leads:
    lead_address = row['Address']
    lead_address_URL = urllib.parse.quote(lead_address)

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=420+E+8th+Street,+New+Albany,+IN&destinations=" + lead_address_URL + '&units=imperial&key=' + API

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    distance_value = (json.loads(response.text))["rows"][0]["elements"][0]["distance"]["value"]
    distance_sum = distance_sum + distance_value

    duration_text = (json.loads(response.text))["rows"][0]["elements"][0]["duration"]["text"]
    duration_value = (json.loads(response.text))["rows"][0]["elements"][0]["duration"]["value"]
    duration_sum = duration_sum + duration_value

#Convert meters to miles (distance) and seconds to hours (duration) and calculate average
distance_avg = round((distance_sum*0.000621371)/len(leads), 2)
duration_avg = round((duration_sum/60)/len(leads), 2)

print("                       Average Driving Distance: ", distance_avg, "miles")
print("                       Average Driving Time: ", duration_avg, "minutes")
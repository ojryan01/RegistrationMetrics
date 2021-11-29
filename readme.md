REGISTRATION METRICS
===============================


CONTENTS OF THIS FILE
---------------------
1. QUICKSTART 
2. PROJECT DESCRIPTION
3. SPECIAL INSTRUCTIONS
4. FUTURE WORK
#

QUICKSTART
-------------------
Open terminal and enter the following commands:

    pip install -r requirements.txt
    python registration.py

You will be prompted to enter an API key in your console. Key will be provided upon request. 
The application will load the sample data file MetricsSimple.csv from the same directory as registration.py.

PROJECT DESCRIPTION
-------------------

This goal of this project is to demonstrate basic usage of Python. To get started I took a 1.5 hour PluralSight course "Practical Python for Beginners" and used a variety of online tutorials for the Google API. This is my first attempt at using this language to create a functional console application.

The data set used for this project is a subset of existing customer/leads data submitted through my small business website. My goal for the application was to import the data in CSV format and output some interesting metrics about the demographics of the form submitters ('Leads'). 

The application performs the following actions:

1. Lead Source Breakdown: Leads are asked to make a selection about how they heard about us (Social media, referral, etc). The program first displays the breakdown of these responses as a percentage of the total submissions.
2. Class Selection Breakdown: Leads can use this form to sign up for a free trial class, register for an ongoing class, or subscribe for updates. The program displays the breakdown of this selection as a percentage of the total submissions. 
3. Average Age: Leads are asked for their birthday. The program next calculates the age in years of each submission and provides an average age of all leads.
4. Distance: Leads are asked to provide a street address. For each lead, the program calls the Google Distance Matrix API to calculate the driving distance and duration from the business location to the lead address, and display the average of all data.
---------------------------------------------------------------
SPECIAL INSTRUCTIONS
---------------------------
The application will ask for an API Key to be entered. This is available upon request.

The sample data set MetricsSimple.csv is available upon request. The program opens the file from the current directory. 

---------------------------------------------------------------
FUTURE DEVELOPMENT AND LIMITATIONS
----------------------------------

1. Data management - I would like to learn more about current best practices for sharing API keys. Google recommends not including this information in a public repository so for now I'm planning to share it separately via email, but I'm sure there are better ways to handle it.

2. Age calculation - Right now the age calculation doesn't account for whether the persons birth date has already passed for this year or not. In future work I can add a check for this to increase the accuracy of this value.

3. Program flow - The application executes all of the calculations in order every time the program is run. To make it more user friendly, we can implement a master loop to allow the user to select which data calculation they would like to perform. 
----------------------------------------------------------------

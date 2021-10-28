'''
Name: Cathal Brolly
Description: Boarding pass file
Creating input to fill boarding pass
'''
import csv
import random
import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from boardingPassBanner import banner
from boardingPassAdvert import advert
from boardingPassPredictions import predictingDestination

boardingPass = "BOARDING PASS"
avios = 0
discount = "0%"
bpList = []

def boarding_pass(title, name, surname, passportNo, holiday_destination, location, gate, flightNo, date, seat, flightClass, discount,
                  baggage, extraBaggage, avios):
    filepath = os.path.join(newDirPath, f"{name}_{flightNo}.txt")
    print("The new file: " + filepath)
    newFile = open(filepath, "w")

    newFile.writelines("-------------------------------------------------------------------------------------------------------------------------\n")
    newFile.writelines(boardingPass.center(100, ' '))
    newFile.writelines("\n-------------------------------------------------------------------------------------------------------------------------\n")
    newFile.writelines(f"| Title: {title:<20} Firstname: {name:^20} Surname: {surname:>10} |\n")
    newFile.writelines(f"| Passport Number: {passportNo:<20} Flying from: {location:^10}   Flying to: {holiday_destination:>20}  |\n")
    newFile.writelines(f"| Gate: {gate:<20} Flight Number: {flightNo:<20} Date: {date:>15}  |\n")
    newFile.writelines(f"| Seat: {seat:<20} Class: {flightClass:^20}         Discount: {discount:>10}   |\n")
    newFile.writelines(f"| Bag: {baggage:<20}  Extra Bag: {extraBaggage:^20}     Avios: {avios:>13}   |\n")
    newFile.writelines("-------------------------------------------------------------------------------------------------------------------------\n")

    newFile.close()

    boardingFile = open(str(filepath), "r")

    print(boardingFile.read())

    boardingFile.close()



def boardingPassDictionary(title, name, surname, passportNo, holiday_destination, location, gate, flightNo, date, seat, flightClass, discount,
                  baggage, extraBaggage, avios):
    #boardingPassDictionary = {'Title': title, 'Name': name, 'Surname': surname, 'Passport Number': passportNo, 'Destination': holiday_destination,
                              #'Location': location, 'Gate': gate, 'Flight Number': flightNo, 'Date': date, 'Seat': seat,
                              #'Flight Class': flightClass, 'Discount': discount, 'Baggage': baggage, 'Extra Baggage': extraBaggage, 'Avios':avios}

    #dataframe = pd.DataFrame(boardingPassDictionary)
    #dataframe.to_csv('boardingPass.csv')


#def validAge(age, discount):
    #if age.isdigit() == False:
        #print("That's not an age!")
        #age = input("What age are you?\n")
    #elif int(age) >= 65:
        #discount is "20%"
    #elif int(age) < 18:
        #print("You cannot fly!")
        #discount is "0%"
        #sys.exit()
    #else:
        #discount is "0%"


    banner()
title = input("What is your title?\n")

while title == "":
    print("You have not entered in any data!")
    title = input("What is your title?\n")

name = input("What is your first name?\n")

while name == "":
    print("You have not entered in any data!")
    name = input("What is your name?\n")

surname = input("What is your surname?\n")
newDirPath = os.path.join(os.path.expanduser("~"), f"{name}_{surname}")
print("The new directory: " + newDirPath)
os.mkdir(newDirPath)

location = input("Where are you flying from?\n")
while name == "":
    print("You have not entered in any data!")
    name = input("What is your name?\n")

passportNo = input("What is your passport number?\n")
while passportNo.isdigit() == False:
    print("That's not a passport number!")
    gate = input("What is your passport number?\n")


while location == "":
    print("You have not entered in any data!")
    location = input("Where are you flying from?\n")

destinationFile = open("destinations.txt", "r")

holiday_destination = input("What is your destination? " + destinationFile.read() + "\n")

#print(destinationFile.read())

destinationFile.close()

ni = {
    "country": "UK",
    "city": "Belfast",
    "price": 50,
    "airports":[{"name": "Belfast International Airport"}, {"name": "George Best Belfast City Airport"}]
}

uk = {
    "country": "UK",
    "city": "London",
    "price": 100,
    "airports": [{"name": "Heathrow Airport"}, {"name": "Gatwick Airport"}, {"name": "London Stansted Airport"},
                 {"name": "London Luton Airport"}, {"name": "London City Airport"}]
}
france = {
    "country": "France",
    "city": "Paris",
    "price": 200,
    "airports": [{"name": "Charles de Gaulle Airport"}, {"name": "Orly Airport"}, {"name": "Beauvais-Tille Airport"}]
}

spain = {
    "country": "Spain",
    "city": "Madrid",
    "price": 250,
    "airports": [{"name": "Adolfo Suárez Madrid–Barajas Airport"}]
}
airports = []
destinations = [ni, uk, france, spain]
for destination in destinations:
    #print(destination)
    for airport in destination['airports']:
        #print(type)
        airports.append(airport['name'])
print(airports)

priceList = []
for destination in destinations:
    #print(destination["price"])
    priceList.append(destination["price"])
print(priceList)

destinationList = []
for destination in destinations:
    #print(destination["city"])
    destinationList.append(destination["city"])
print(destinationList)


while holiday_destination == "":
    print("You have not entered in any data!")
    destination = input("What is your destination?\n")

#origins = ["Belfast", "London", "Paris", "Madrid"]
#cities = []
#for origin in origins:
    #if name == origin["cities"]:
        #availableDestinations = []
        #for destination in origin["destinations"]:
            #availableDestinations.append(destination["name"])
        #travelDestination = input(f"Where are you flying to? {availableDestinations}")
        #print(f"This is the destination you are flying to {destinations}")
        #print(f"This is what is in origins {origins}")
    #cities.append(origin["cities"])
    #cities.append(origin[:])

#city_destination = input(f"Select your destination: {cities}\n")
#for origin in origins:
    #print(f"This is what is in {origins}")
    #if city_destination == origin["city"]:
    #if city_destination == origin[:]:
        #print(origin)
        #available_destinations = []
    #for destination in origin["destinations"]:
        #print(f"This is destination {destination}")
    #if destinations == destination["name"]:
        #flyingPrice = destination["price"]
        #print(f"This is the flight price: {price}")
        #for destination in origin[:]:
            #available_destinations.append(destination["name"])
            #available_destinations.append(destination[:])
        #holiday = input(f"Where do you want to fly to {available_destinations}?\n")
        #print(holiday)

gate = input("What is your gate?\n")
while gate.isdigit() == False:
    print("That's not a gate number!")
    gate = input("What is your gate?\n")

flightNo = input("What is your flight number?\n")

if flightNo.isdigit() == True:
    avios = avios + 10
elif flightNo.isdigit() == False:
    print("That's not a number!")
    flightNo = input("What is your flight number?\n")
if len(flightNo) != 6:
    print("That Flight Number is not the right length!")
    flightNo = input("What is your flight number?\n")

date = input("What date is your flight? [dd/mm/yy]\n")
if date == " ":
    print("That is not a valid date!")
else:
    while True:
        date = input("What date is your flight? [dd/mm/yy]\n")
        try:
            date = datetime.strptime(date, "%d/%m/%Y")

        except:
            print("This is not a valid date")
        else:
            date = datetime.strftime(date, "%d/%m/%Y")
        break

if len(date) < 8 and len(date) > 10:
    print("That isn't a proper date!\n")
    date = input("What date is your flight? [dd/mm/yy]\n")



#while date is not datetime.strptime(date, "%d/%m/%y"):
   # print("That is not a proper date!\n")
    #date = input("What date is your flight? [dd/mm/yy]\n")


flightDate = datetime.strptime(date, "%d/%m/%y")

returnDate = input("When will your return date be? [dd/mm/yy]\n")



flightClass = input("What class are you flying? Business or Economy?\n")
if flightClass == "Business":
    flightClass = "Business"
elif flightClass == "Economy":
    flightClass = "Economy"
else:
    print("That is not a class!")
    flightClass = input("What class are you flying? Business or Economy?\n")

seat = input("What is your seat number?\n")
if seat.isdigit() == False:
    print("That's not a number!")
    seat = input("What is your seat number?\n")

baggageList = ["12Kg", "18Kg", "23Kg"]
baggage = input(f"Please select your baggage size? {baggageList}\n")

while baggage not in baggageList:
    print(f"That is not a valid bag size!\n")
    baggage = input(f"Please select your baggage size? {baggageList}\n")

extraBaggage = input("Do you require extra baggage? Yes/No\n")
if extraBaggage.casefold() == "yes":
    extraBaggage = input(f"Please select your baggage size? {baggageList}\n")
    while extraBaggage not in baggageList:
        print(f"That is not a valid bag size!\n")
        extraBaggage = input(f"Please select your baggage size? {baggageList}\n")
else:
    extraBaggage = "no"
    advert(name, surname)


predictingDestination()
#age = input("What age are you?\n")
#validAge(age, discount)
#age = input("What age are you?\n")
#if age.isdigit() == False:
    #print("That's not an age!")
    #age = input("What age are you?\n")

#if int(age) >= 65:
    #discount = "20%"
#elif int(age) < 18:
    #print("You cannot fly!")
    #discount = "0%"
    #sys.exit()
#else:
    #discount = "0%"

connecting_flight = input("Do you have a connecting flight?\n")

if connecting_flight.casefold() == "yes":
    connecting_destination = input("Where is your connecting flight to?\n")
    avios = avios + 10

    boarding_pass(title, name, surname, passportNo, holiday_destination, connecting_destination, gate, flightNo, date, seat, flightClass,
                  discount, baggage, extraBaggage, avios)
    boardingPassDictionary(title, name, surname, passportNo, holiday_destination, connecting_destination, gate, flightNo, date, seat, flightClass,
                  discount, baggage, extraBaggage, avios)

    flightNo = random.randrange(100000, 999999)
    boarding_pass(title, name, surname, passportNo, connecting_destination, location, gate, flightNo, date, seat, flightClass,
                  discount, baggage, extraBaggage, avios)
    boardingPassDictionary(title, name, surname, passportNo, connecting_destination, location, gate, flightNo, date, seat, flightClass,
                  discount, baggage, extraBaggage, avios)


else:
    advert(name, surname)
    boarding_pass(title, name, surname, passportNo, location, holiday_destination, gate, flightNo, date, seat, flightClass, discount, baggage,
                  extraBaggage, avios)
    boardingPassDictionary(title, name, surname, passportNo, location, holiday_destination, gate, flightNo, date, seat, flightClass, discount, baggage,
                  extraBaggage, avios)


returnPass = input("Do you require a return boarding pass?\n")
if returnPass.casefold() == "yes":
    avios + 10
    flightNo = random.randrange(100000, 999999)
        #Printing return boarding pass
    boarding_pass(title, name, surname, passportNo, holiday_destination, location, gate, flightNo, returnDate.date(), seat, flightClass, discount, baggage,
                  extraBaggage, avios)
    boardingPassDictionary(title, name, surname, passportNo, holiday_destination, location, gate, flightNo, returnDate.date(), seat, flightClass, discount, baggage,
                  extraBaggage, avios)



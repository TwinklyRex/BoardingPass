'''
File Name:
Description:
Author: Cathal Brolly
Edited on: 27/09/2021
'''

import os

boardingPass = "BOARDING PASS"

newDirPath = os.path.join(os.path.expanduser("~"), f"{name}_{surname}")
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
'''
File Name: boarding_pass_file_and_directory
Description: Create a file and directory for the boarding passes
Author: Cathal Brolly
Edited on: 24/09/2021
'''

import os

boardingPass = "BOARDING PASS"

def boarding_pass(title, name, surname, passportNo, destination, location, gate, flightNo, date, seat, flightClass, discount,
                  baggage, extraBaggage, avios):
    newFile.writelines("-------------------------------------------------------------------------------------------------------------------------")
    newFile.writelines(boardingPass.center(100, ' '))
    newFile.writelines("-------------------------------------------------------------------------------------------------------------------------")
    newFile.writelines(f"| Title: {title:<20} Firstname: {name:^20} Surname: {surname:>10}")
    newFile.writelines(f"| Passport Number: {passportNo:<20} Flying from: {location:^10}   Flying to: {destination:>20}  |")
    newFile.writelines(f"| Gate: {gate:<20} Flight Number: {flightNo:<20} Date: {date:>15}  |")
    newFile.writelines(f"| Seat: {seat:<20} Class: {flightClass:^20}         Discount: {discount:>10}   |")
    newFile.writelines(f"| Bag: {baggage:<20}  Extra Bag: {extraBaggage:^20}     Avios: {avios:>13}   |")
    newFile.writelines("-------------------------------------------------------------------------------------------------------------------------")


newDirPath = os.path.join(os.path.expanduser("~"), f"{name}_{surname}")
print("The new directory: " + newDirPath)
os.mkdir(newDirPath)

filepath = os.path.join(newDirPath, f"{name}_returnPass.txt")
    print("The new file: " + filepath)
    newFile = open(filepath, "w")

    newFile.writelines(str(boarding_pass(title, name, surname, destination, location, gate, flightNo,
                        returnDate, seat, flightClass, discount, baggage, extraBaggage, avios)))

    newFile.close()
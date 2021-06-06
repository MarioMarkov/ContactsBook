import csv
import datetime
from enum import Enum
from datetime import date

class Melodies(Enum):
    SenTrope = 1
    Wagabunga = 2
    TrapLape = 3


class Company:
    name=''
    occupation=''
    address =''
    webpage =''

    def __init__(self, name='', occupation='', address='', webpage=''):
        self.name = name
        self.occupation = occupation
        self.address = address
        self.webpage = webpage



class Contact:
    name =''
    phone =''
    melody=''
    company = ''
    birthday= datetime.date.today()
    def __init__(self,name,phone,melody, birthday,company = ''):
        self.name = name
        self.phone = phone
        self.melody = melody
        self.company = company
        self.birthday = birthday


def drawMenu():
    print()
    print("         Contact Book - Menu            ")
    print()
    print("1 - Create new Contact")
    print("2 - Delete a Contact")
    print("3 - Update a Contact")
    print("4 - Print all contacts")
    print("5 - See birthday reminders")
    print("6 - Exit")
    menuItem = input("Choose Action: ")
    if menuItem not in "123456":
        print()
        print("Invalid input")
        drawMenu()
    handleInput(menuItem)


def handleInput(menuItem):
    if menuItem == "1":
        print("Add Personal details: ")
        name = input("Name: ")
        phone = input("Phone: ")

        print("Choose Melody: ")

        i=1
        for melody in Melodies:
            print(f"{i} - {Melodies(i).name}")
            i+=1


        melody = input("Melody: ")
        melodyName = Melodies(int(melody)).name
        birthday = input("Birthday? (in DD/MM/YYYY) ")
        birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()

        answertoCompany = input("Do you want to add Company? (Y/N): ")
        company = ''
        if answertoCompany.lower() == 'y' or answertoCompany.lower() == "yes":
            print("Add Company details: ")
            companyName = input("Name: ")
            occupation = input("Occupation: ")
            address = input("Address: ")
            webPage = input("Web Page: ")
            company = Company(companyName, occupation, address, webPage)
            print(
                f"New Company is added: Name: {company.name}, Occupation: {company.occupation}, Adress: {company.address}, WebPage: {company.webpage}")

        contact = Contact(name, phone, melodyName, birthdate,company )
        writeContactToFile(contact)
        print(f"New Contact is added: Name: {contact.name}, Phone: {contact.phone}, Melody: {contact.melody}")
        drawMenu()
    elif menuItem == "2":
        name = input("Name of contact to delete: ")
        deleteContact(name)
        drawMenu()
    elif menuItem == "3":
        name = input("Name of contact to update: ")
        print()
        print("1 - Update Name")
        print("2 - Update Phone")
        print("3 - Update Melody")
        print("7 - Exit")
        action = input("Choose Action: ")
        newValue =''
        if action=="1":
            newValue = input("Enter new name: ")
        elif action == "2":
            newValue = input("Enter new phone: ")
        if action == "3":
            newValue = input("Enter new melody: ")

        updateValueFromFile(name,int(action),newValue)
        drawMenu()
    elif menuItem == "4":
        printAllContacts()
    elif menuItem == "5":
        printBirthdayReminders()
    elif menuItem == "7":
        return

def printAllContacts():
    with open('contacts.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            print(row)
    readFile.close()

def  printBirthdayReminders():
    with open('contacts.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != []:
                birthday = datetime.datetime.strptime(row[3], "%Y-%m-%d").date()
                dateNow = datetime.date(datetime.datetime.now().year,datetime.datetime.now().month, datetime.datetime.now().day)
                res = datetime.date(dateNow.year ,birthday.month, birthday.day)
                if dateNow.day - res.day>=-10 and  dateNow.day - res.day<=0:
                    print(f"{row[0].capitalize()} has a birthday after {abs(dateNow.day - res.day)} days.")



    readFile.close()

def updateValueFromFile(name,action,newValue):

    lines = list()
    with open('contacts.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != [] and row[0] == name.lower():
                row[action-1] = newValue
            lines.append(row)
    readFile.close()

    with open('contacts.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        for line in lines:
            if not line:
                lines.remove(line)
        writer.writerows(lines)
    writeFile.close()

def deleteContact(name):
    lines = list()
    with open('contacts.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            if row != [] and row[0] == name:
                lines.remove(row)
    readFile.close()
    with open('contacts.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        for line in lines:
            if not line:
                lines.remove(line)
        writer.writerows(lines)
    writeFile.close()

def writeContactToFile(contact):
    f = open("contacts.csv","a", newline="")
    tup1 = (contact.name,contact.phone,contact.melody,contact.birthday,'' if contact.company == ''else contact.company.name)
    writer = csv.writer(f)
    writer.writerow(tup1)
    f.close()

def takeInput():
    while(1):
        answer = input("Do you wanna add new Contact? (Y/N): ")
        if answer.lower() == 'y' or answer.lower() == "yes":
            print("Add Personal details: ")
            name = input("Name: ")
            phone = input("Phone: ")
            melody = input("Melody: ")
            answertoCompany = input("Do you wanna add Company? (Y/N): ")
            if answertoCompany.lower() == 'y' or answertoCompany.lower() == "yes":
                print("Add Company details: ")
                name = input("Name: ")
                occupation = input("Occupation: ")
                address = input("Adress: ")
                webPage = input("Web Page: ")
                company = Company(name,occupation,address,webPage)
                print(f"New Company is added: Name: {company.name}, Occupation: {company.occupation}, Adress: {company.address}, WebPage: {company.webpage}")

            contact = Contact(name, phone, melody,company)
            writeContactToFile(contact)
            print(f"New Contact is added: Name: {contact.name}, Phone: {contact.phone}, Melody: {contact.melody}")
        elif answer.lower() == 'n':
            break;
        else:
            print("Invalid input")


drawMenu()


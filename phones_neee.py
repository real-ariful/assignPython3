#%%
# movies.py *- coding: utf-8 -*-
"""
There is a file of the top 1000 or so movie titles called movies.txt. For this
question you are to build a way of displaying a random movie title, finding
movies, and building and saving a list of movies you would like to watch.
The program first displays a menu (something like that shown below) and
carries out the appropriate action depending on which letter the user
types, and then redisplays the menu
"""
import os
import csv
import random


#phones = []
favourites = []
#name_pos = 0
#phone_pos = 1
#phone_header = [ 'Name', 'Phone Number']


#def reorder_phones():
#    global phones       # this insures that we use the one at the top
#    print("reorder_phones")
#
#def proper_menu_choice(which):
#    if not which.isdigit():
#        print ("'" + which + "' needs to be the number of a phone!")
#        return False
#    which = int(which)
#    if which < 1 or which > len(phones):
#        print ("'" + str(which) + "' needs to be the number of a phone!")
#        return False
#    return True
#    
#def delete_phone(which):
#    if not proper_menu_choice(which):
#        return
#    which = int(which)
#
#    del phones[which-1]
#    print( "Deleted phone #", which)
#
#def edit_phone(which):
#    if not proper_menu_choice(which):
#        return
#    which = int(which)
#        
#    phone = phones[which-1]
#    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
#    
#    print(phone[name_pos])
#    newname = input("Enter phone name to change or press return: ")
#    if newname == "":
#        newname = phone[name_pos]
#        
#    print(phone[phone_pos])    
#    newphone_num = input("Enter new phone number to change or press return: ")
#    if newphone_num == "":
#        newphone_num = phone[phone_pos]
#            
#    phone = [newname, newphone_num]
#    phones[which-1] = phone
#
#  
#def save_phone_list():
#
#    f = open("myphones.csv", 'w', newline='')
#    for item in phones:
#        csv.writer(f).writerow(item)
#    f.close()
#  
#def load_phone_list():
#    if os.access("myphones.csv",os.F_OK):
#        f = open("myphones.csv")
#        for row in csv.reader(f):
#            phones.append(row)
#        f.close()
#
#def show_phones():
#    show_phone(phone_header, "")
#    index = 1
#    for phone in phones:
#        show_phone(phone, index)
#        index = index + 1
#    print()
#
#def show_phone(phone, index):
#    outputstr = "{0:>3}  {1:<20}  {2:>16}"
#    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))
#
#def create_phone():
#    print("Enter the data for a new phone:")
#    newname = input("Enter name: ")
#    newphone_num = input("Enter phone number: ")
#    phone = [newname,newphone_num]
#    phones.append(phone)
    
def menu_choice():

    print("*** Movie Title Explorer ***")
    print("l - load file of movie titles")
    print("r - random movie")
    print("s - searching")
    print("sw - starts with")
    print("k - keep: save the last displayed movie title to your favourites")
    print("f - favourites display")
    print("c - clear favourites")
    print("q - quit")
    print("")
    print("command: ?")
    choice = input("Choice: ")    
    if choice.lower() in ['l','r', 's','sw','k', 'f', 'c','q']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None


def main_loop():
    
    #load_phone_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            print( "No choice selected")
            break     # jump out of while loop
        if choice == 'l':
            fchoice = input()
            if fchoice == '':
                filename="movies.txt"
                print( "loading from movies.txt")
                f= open(filename,'r')
            else:
                print("loading files of",filename)
                f= open(filename,'r')
                break     # jump out of while loop
        elif choice == 'r':
            #create_phone()
            print( "random movie loading: ")
            mv = f.readlines() 
            print(random.choice(mv))
        elif choice == 's':
            which = input("searching: ")
            which.lower()
            #f= open(filename,'r')
            for lines in f:
                if (which in lines) == True:
                    mv=lines.split("\n")
                    print(mv[0])
            #delete_phone(which)
        elif choice == 'sw':
            #show_phones()
            #print("starts with ")
            which = input("searching: ")
            which.lower()
            #f= open(filename,'r')
            for lines in f:
                if which in lines:
                    mv=lines.split("\n")
                    print(mv[0])
        elif choice == 'k':
            if mv not in favourites:
                    favourites.append(mv[0])
                    print("keep: save the last displayed movie title to your favourites")
            #reorder_phones()
            
        elif choice == 'f':
            #which = input("Which item do you want to edit? ")
            print("favourites display: ")
            print(favourites)
            #edit_phone(which)
        elif choice == 'c':
            #which = input("Which item do you want to edit? ")
            print("clear favourites")
            del favourites[:]
            #edit_phone(which)
        elif choice == 'q':
            print("quiting")
            break
            #edit_phone(which)
        else:
            print("Invalid choice.")
            
    #save_phone_list()
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
    
    
#%%
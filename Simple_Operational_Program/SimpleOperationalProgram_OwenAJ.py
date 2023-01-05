# DATABASE-------------------------------------------------------------------------------------------------------------------------------------------

# Initial value using list and dict, 5 columns, 1 == PK (ID)
# iv = {}

iv = {
    'id001' : {   
            'Name' : 'Owen',
            'Age' : 22,
            'Gender' : 'Male',
            'Title' : 'Data scientist'
    },
     'id002' : {   
            'Name' : 'Floren',
            'Age' : 20,
            'Gender' : 'Female',
            'Title' : 'Marketing'
    },
     'id003' : {   
            'Name' : 'Lisa',
            'Age' : 21,
            'Gender' : 'Female',
            'Title' : 'Business analyst'
    }
}

# SUBFUNCTIONS---------------------------------------------------------------------------------------------------------------------------------------

# Display the current dashboard, displaying every key-value pairs in dict in dict
def dashboard() :
    print(f'ID\t\t|Name\t\t|Age\t\t|Gender\t\t|Title')
    for key, values in iv.items() :
        row = ''
        row += f'{key}\t\t'
        for i in values :
            row += f'|{values[i]}\t\t'
        print(row)

# Display selected record data
def display(id) :
    print(f'ID\t\t|Name\t\t|Age\t\t|Gender\t\t|Title')
    print(f"{id}\t\t|{iv[id]['Name']}\t\t|{iv[id]['Age']}\t\t|{iv[id]['Gender']}\t\t|{iv[id]['Title']}\t\t\n")

# Update confirmation
def confirm() :
    while(True) :
        input2 = input('Do you want to update the record? (Y/N): ').capitalize()
        if input2 == 'Y' :
            break
        elif input2 == 'N' :
            print('Record is not updated')
            menu3()
        else :
            print('Incorrect input, please enter (Y/N)')

# Update database records
def update(field) :
    if field == 'Name' :
        name = input('Name: ').title()
        confirm()
        iv[id]['Name'] = name
        print('Data updated')
        dashboard()
        menu3()
    elif field == 'Age' :
        while(True) : 
            try :
                age = int(input('Age: '))
            except ValueError :
                print('Incorrect input, please enter a positive integer')
                continue
            else :
                if age <= 0 :
                    print('Incorrect input, please enter a positive integer')
                    continue
                else :
                    break
        confirm()
        iv[id]['Age'] = age
        print('Data updated')
        dashboard()
        menu3()
    elif field == 'Gender' :
        while(True) :
            gender = input('Gender: ').capitalize()
            if gender == 'Male' or gender == 'Female' :
                break
            else :
                print('Incorrect input, please enter Male/Female')
                continue
        confirm()
        iv[id]['Gender'] = gender
        print('Data updated')
        dashboard()
        menu3()
    elif field == 'Title' :
        title = input('Title: ').capitalize()
        confirm()
        iv[id]['Title'] = title
        print('Data updated')
        dashboard()
        menu3()

# MAIN FUNCTIONS-------------------------------------------------------------------------------------------------------------------------------------

# Main menu
def main() :
    while(True) :
        print('''
=============== Company Employee Data ===============

1. Employee data records
2. Add employee data
3. Update employee data
4. Delete employee data
5. Exit

''')
        # Asking for an integer input until it gives the correct input
        try :
            input1 = int(input('Please input menu [1-5]: '))
        except ValueError :
            print('Incorrect input, please enter [1-5]')
            continue
        else :
            if input1 == 1 :
                menu1()
            elif input1 == 2 :
                menu2()
            elif input1 == 3 :
                menu3()
            elif input1 == 4 :
                menu4()
            elif input1 == 5 :
                while(True) :
                    # No need for try and except since the expected result is str
                    input2 = input('Press Y to exit the program or N to cancel (Y/N): ').capitalize()
                    if input2 == 'Y' :
                        print('Program terminated!')
                        quit()
                    elif input2 == 'N' :
                        main()
                    else :
                        print('Incorrect input, please enter (Y/N)')
            else :
                print('Incorrect input, please enter [1-5]')
    
# Menu 1
def menu1() :
  while(True) :
    print('''
=============== Employee Data Records ===============

1. Report all data
2. Report selected data
3. Return to main menu

''')
    try :
        input1 = int(input('Please input menu [1-3]: '))
    except ValueError :
        print('Incorrect input, please enter [1-3]')
        continue
    else :
        if int(input1) == 1 :
            if len(iv) == 0 :
                print('There is no data')
                continue
            else :
                dashboard()
        elif int(input1) == 2 :
            if len(iv) == 0 :
                print('There is no data')
                continue
            else : 
                while(True) :
                    id = input('Input ID: ').lower()
                    if iv.get(id) is not None:
                        display(id)
                        break
                    else :
                        print('ID not found, please input accordingly [id###]')
                        continue
        elif int(input1) == 3 :
            main()
        else :
            print('Incorrect input, please enter [1-3]')

# Menu 2
def menu2() :
    while(True) :
        print('''
=============== Add Employee Data ===============

1. Add data
2. Return to main menu

''')
        try :
            input1 = int(input('Please input menu [1-2]: '))
        except ValueError :
            print('Incorrect input, please enter [1-2]')
            continue
        else :
            if input1 == 1 :
                while(True) : 
                    id = input('ID (id###): ').lower()
                    if (id[0:2] == 'id' and len(id) == 5) :
                        if iv.get(id) is not None :
                            print('Duplicated data, please input a different ID')
                            menu2()
                        else : 
                            break
                    else : 
                        print('Incorrect input, please enter using (id###) format')
                        continue
                name = input('Name: ').title()
                while(True) : 
                    try :
                        age = int(input('Age: '))
                    except ValueError :
                        print('Incorrect input, please enter a positive integer')
                        continue
                    else :
                        if age <= 0 :
                            print('Incorrect input, please enter a positive integer')
                            continue
                        else :
                            break
                while(True) :
                    gender = input('Gender: ').capitalize()
                    if gender == 'Male' or gender == 'Female' :
                        break
                    else :
                        print('Incorrect input, please enter Male/Female')
                        continue
                title = input('Title: ').capitalize()
                while(True) :
                    input2 = input('Do you want to save the record? (Y/N): ').capitalize()
                    if input2 == 'Y' :
                        break
                    elif input2 == 'N' :
                        print('Record is not saved')
                        menu2()
                    else :
                        print('Incorrect input, please enter (Y/N)')
                iv[id]= {'Name' : name, 'Age' : age, 'Gender' : gender, 'Title' : title}
                print('Record saving is successful')
                dashboard()
            elif input1 == 2 :
                main()
            else :
                print('Incorrect input, please enter [1-2]')

# Menu 3
def menu3() :
    global id # Declare global function as such update() function can access the inputted id
    while(True) :
        print('''
=============== Update Employee Data ===============

1. Update data
2. Return to main menu

''')
        try :
            input1 = int(input('Please input menu [1-2]: '))
        except ValueError :
            print('Incorrect input, please enter [1-2]')
            continue
        else :
            if input1 == 1 :
                if len(iv) == 0 :
                    print('There is no data')
                    continue
                else :
                    dashboard()
                    while(True) : 
                        id = input('ID (id###): ').lower()
                        if (id[0:2] == 'id' and len(id) == 5) :
                            if iv.get(id) is not None :
                                display(id)
                                while(True) :
                                    input2 = input('Do you want to edit the record? (Y/N): ').capitalize()
                                    if input2 == 'Y' :
                                        break
                                    elif input2 == 'N' :
                                        print('Record is not editted')
                                        menu3()
                                    else :
                                        print('Incorrect input, please enter (Y/N)')
                                break
                            else :
                                print('There is no such record, enter another ID')
                                continue
                        else : 
                            print('Incorrect input, please enter using (id###) format')
                            continue
                    while(True) :    
                        updateField = input('Enter the field you wish to be updated: ').capitalize()
                        if updateField not in ['Name', 'Age', 'Gender', 'Title'] :
                            print("Incorrect field, please enter ['Name', 'Age', 'Gender', 'Title']: ")
                            continue
                        else :
                            break
                    update(updateField)
            elif input1 == 2 :
                main()
            else :
                print('Incorrect input, please enter [1-2]')

# Menu 4
def menu4() :
    while(True) :
        print('''
=============== Delete Employee Data ===============

1. Delete data
2. Return to main menu

''')
        try :
            input1 = int(input('Please input menu [1-2]: '))
        except ValueError :
            print('Incorrect input, please enter [1-2]')
            continue
        else :
            if input1 == 1 :
                if len(iv) == 0 :
                    print('There is no data')
                    continue
                else :
                    dashboard()
                    while(True) : 
                        id = input('ID (id###): ').lower()
                        if (id[0:2] == 'id' and len(id) == 5) :
                            if iv.get(id) is not None :
                                display(id)
                                while(True) :
                                    input2 = input('Do you want to delete the record? (Y/N): ').capitalize()
                                    if input2 == 'Y' :
                                         break
                                    elif input2 == 'N' :
                                         print('Record is not deleted')
                                         menu4()
                                    else :
                                        print('Incorrect input, please enter (Y/N)')
                                del iv[id]
                                print('Record deletion is successful')
                                dashboard()
                                menu4()
                            else :
                                print('There is no such record, enter another ID')
                                continue
                        else : 
                            print('Incorrect input, please enter using (id###) format')
                            continue
            elif input1 == 2 :
                main()
            else :
                print('Incorrect input, please enter [1-2]')
#-----------------------------------------------------------------------------------------------------------------------------------------------------
main()
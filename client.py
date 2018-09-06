#Import Modules
import apartment
import apartment_db
import tenant
import tenant_database

#setup apartment database from file
aptDB = apartment_db.Apartment_db()
aptDB.loadApartments('apts.txt')
tenantDB = tenant_database.Tenant_db()

#clean-up
def float_input(prompt):
    while True:
        try:
            parsed = float(input(prompt))
            break
        except:
            print('Please enter numbers only.')
    return parsed

def int_input(prompt):
    while True:
        try:
            parsed = int(input(prompt))
            break
        except:
            print('Please enter numbers only.')
    return parsed


#Add menu for all client options
def aptMenu():
    print('\n1. Rent/Lease Apartment')
    print('2. Search Available Apartments')
    print('3. Make Apartment Available')
    print('4. List Available Apartments')
    print('5. List Rented Apartments')
    print('6. Display Tenant Information')
    print('7. Add New Apartment')
    print('8. Exit')



while True:
    aptMenu()
    choice = int_input('\nEnter your selection number: ')

    if choice == 1:
        #1. Rent/Lease Apartment
        availApts = aptDB.getAvailApartments()
        userMinBed = float_input('Enter the minimum number of bedrooms you need: ')
        userMinBath = float_input('Enter the minimum number of bathrooms you need: ')
        userMaxPrice = float_input('Enter the maximum rent amount you wish to pay: ')

        print('{:<10}{:<15}{:<15}{:<20}{:<10}'.format('Apt #', 'Bedrooms', 'Baths', 'Rent Amount', 'Availability \n'))
        flag = False
        for a in availApts:
            if (userMinBed <= a.getApt_bed()) and (userMinBath <= a.getApt_bath()) and (userMaxPrice >= a.getApt_rent()):
                print('{:<10}{:<15}{:<15}{:<20.2f}{:<10}'.format(str(a.getApt_num()), str(a.getApt_bed()), str(a.getApt_bath()), a.getApt_rent(), str(a.getApt_status())) + '\n')
                flag = True
        if flag == False:
            print('Sorry, no results were found matching your criteria. \n')
        else: 
            aptToLease = int_input('Enter the apartment number you wish to lease or enter -1 to return to main menu: ')
            if aptToLease == -1:
                continue
            elif aptDB.getApartment(aptToLease) == None:
                continue
            else:
                leaseFname = str(input('To finalize your lease, enter your first name: '))
                leaseLname = str(input('Please enter your last name: '))
                newTenant = tenant.Tenant(leaseFname, leaseLname, aptToLease) 
                tenantDB.addTenant(newTenant)
                aptDB.changeApartmentStatus(aptToLease, 'R')
                        
        
                
    elif choice == 2:
        #2. Search Available Apartments
        availApts = aptDB.getAvailApartments()
        userMinBed = float_input('Enter the minimum number of bedrooms you need: ')
        userMinBath = float_input('Enter the minimum number of bathrooms you need: ')
        userMaxPrice = float_input('Enter the maximum rent amount you wish to pay: ')

        print('{:<10}{:<15}{:<15}{:<20}{:<10}'.format('Apt #', 'Bedrooms', 'Baths', 'Rent Amount', 'Availability \n'))
        flag = False
        for a in availApts:
            if (userMinBed <= a.getApt_bed()) and (userMinBath <= a.getApt_bath()) and (userMaxPrice >= a.getApt_rent()):
                print('{:<10}{:<15}{:<15}{:<20.2f}{:<10}'.format(str(a.getApt_num()), str(a.getApt_bed()), str(a.getApt_bath()), a.getApt_rent(), str(a.getApt_status())) + '\n')
                flag = True
        if flag == False:
            print('Sorry, no results were found matching your criteria. \n')
            
                           
    elif choice == 3:
        #3. Make Apartment Available

        aptNumber = float_input('Enter an apartment number: ')
        getApt = aptDB.getApartment(aptNumber)
        if getApt != None:
            if getApt.getApt_status() == 'R':
                aptDB.changeApartmentStatus(aptNumber,'A')
                tenantDB.removeTenant(aptNumber)
            elif getApt.getApt_status() == 'A':
                print('The apartment is already available.')
        

        
    elif choice == 4:
        #4.  List Available Apartments
        availApts = aptDB.getAvailApartments()
        print('{:<10}{:<15}{:<15}{:<20}{:<10}'.format('Apt #', 'Bedrooms', 'Baths', 'Rent Amount', 'Availability \n'))
        if len(availApts) > 0:
            for av in availApts:
                print('{:<10}{:<15}{:<15}{:<20.2f}{:<10}'.format(str(av.getApt_num()), str(av.getApt_bed()), str(av.getApt_bath()), av.getApt_rent(), str(av.getApt_status())) + '\n')
        else:
            print('Sorry, no apartments are available.')
        
    elif choice == 5:
        #5. List Rented/Leased Apartments
        rentedApts = aptDB.getRentedApartments()
        print('{:<10}{:<15}{:<15}{:<20}{:<10}{:<15}{:<20}{:<20}'.format('Apt #', 'Bedrooms', 'Baths', 'Rent Amount', 'Avail', 'Tenant ID', 'Tenant First Name', 'Tenant Last Name\n'))
        if len(rentedApts) > 0:
            for re in rentedApts:
                getTenant = tenantDB.getTenant(re.getApt_num())
                print('{:<10}{:<15}{:<15}{:<20.2f}{:<10}{:<15}{:<20}{:<20}'.format(str(re.getApt_num()), str(re.getApt_bed()), str(re.getApt_bath()), re.getApt_rent(), str(re.getApt_status()), str(getTenant.getTenant_id()), str(getTenant.getTenant_fName()), str(getTenant.getTenant_lName())))
        else:
            print('Sorry, no apartments are available.')
            
    elif choice == 6:
        #6. Display Tenant Information

        try:
            aptTenant = int(input('Enter an apartment number: '))
        except:
            print('Please enter numbers only.')
            continue

        getTenant = tenantDB.getTenant(aptTenant)
        allApts = aptDB.getAvailApartments()
        print('{:<20}{:<20}{:<20}{:<20}'.format('\nFirst Name', 'Last Name', 'Tenant ID', 'Apartment # \n'))
    
        if aptDB.getApartment(aptTenant) != None:
            if getTenant != '':
                print('{:<20}{:<20}{:<20}{:<20}'.format(str(getTenant.getTenant_fName()), str(getTenant.getTenant_lName()), str(getTenant.getTenant_id()), str(getTenant.getTenant_aptNum())))
            else:
                print('Apartment #' + str(aptTenant) + ' is available. No tenant is associated with that apartment currently.')       
            
            
    elif choice == 7:
        #7. Add New Apartment
        a1 = int_input('Add new apartment number: ')
        a2 = int_input('Add number of bedrooms: ')
        a3 = int_input('Add number of bathrooms: ')
        a4 = int_input('Add price for new apartment: ')
        newAptInst = apartment.Apartment(a1, a2, a3, a4, 'A')
        aptDB.addApts(newAptInst)
        #Note: according to hw instruction, there is no check to see if new apartment num exists prior.
        #Thus, adding new apartment with existing apartment num, creates duplicate. 
        
    elif choice == 8:
        break
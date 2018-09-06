import apartment

class Apartment_db:
    def __init__(self):
        self.apartments  = list()
    def addApts(self, apt): 
        #adds apartment to list
        self.apartments.append(apt)
        #prints success message
        print('Apartment added successfully!')
    def getApartment(self, aptNum):
        #returns apartment details
        for oneApt in self.apartments:
            if aptNum == oneApt.getApt_num():
                return oneApt
                break
        print('Sorry, that apartment number is not in the database.')       
    def getAvailApartments(self): 
        #returns all 'A' apartment
        avlApts = []
        for anApt in self.apartments:
            if anApt.getApt_status() == 'A':
                avlApts.append(anApt)
        return avlApts
    def getRentedApartments(self): 
        #returns all 'R' apartments
        rentApts = []
        for apt in self.apartments:
            if apt.getApt_status() == 'R':
                rentApts.append(apt)
        return rentApts
    def changeApartmentStatus(self, aNum, status): 
        #changes 'R' to 'A'
        flag = 0
        for eachApt in self.apartments:
            if (eachApt.getApt_num() == aNum) and (eachApt.getApt_status() == 'A'):
                if eachApt.getApt_status() == status:
                    flag = 1
                    break
                else:
                    eachApt.setApt_status('R')
                    flag = 2
                    break
            elif (eachApt.getApt_num() == aNum) and (eachApt.getApt_status() == 'R'):
                if eachApt.getApt_status() == status:
                    flag = 1
                    break
                else:
                    eachApt.setApt_status('A')
                    flag = 3
                    break
                    #remember: delete tenant associated with formerly R
        if flag == 0:
            print('Sorry, the apartment number you entered was not found.')
        elif flag == 1:
            print('Apartment status has not changed.')
        elif flag == 2:
            print('Apartment status changed to rented.')
        else:
            print('Apartment status changed to available.')
            
    def getTotalApartments(self):
        #Returns count of all apartments in DB
        countDB = len(self.apartments)
        return countDB
    def getTotalAvailable(self):
        #Returns count of all available apartments in DB
        avlApts = []
        for anApt in self.apartments:
            if anApt.getApt_status() == 'A':
                avlApts.append(anApt)
        return len(avlApts)
    def getTotalRented(self):
        #Returns count of rented apartments in DB
        avlApts = []
        for anApt in self.apartments:
            if anApt.getApt_status() == 'R':
                avlApts.append(anApt)
        return len(avlApts)
    def loadApartments(self, file):
        #Loads apartments from txt file
        infile = open(file, 'r')
        aptData = infile.readlines()
        aptLst = list()
        for i in aptData:
            clean = i.strip('\n ').split(' ')
            aptTemp = apartment.Apartment(clean[0], clean [1], clean[2], clean[3], clean[4])
            aptLst.append(aptTemp)
        self.apartments = aptLst



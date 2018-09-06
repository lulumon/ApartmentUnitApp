class Apartment:
    def __init__(self, apt_num, apt_bedrm, apt_bath, apt_rent, apt_status):
        self.apt_num = int(apt_num)
        self.apt_bedrm = float(apt_bedrm)
        self.apt_bath = float(apt_bath)
        self.apt_rent = float(apt_rent)
        self.apt_status = str(apt_status)
    def setApt_num(self, aptNum):
        self.apt_num = int(aptNum)
    def setApt_bed(self, bedNum):
        self.apt_bedrm = float(bedNum)
    def setApt_bath(self, bathNum):
        self.apt_bath = float(bathNum)
    def setApt_rent(self, rent):
        self.apt_rent = float(rent)
    def setApt_status(self, aStatus):
        self.apt_status = str(aStatus)      
    def getApt_num(self):
        return self.apt_num
    def getApt_bed(self):
        return self.apt_bedrm
    def getApt_bath(self):
        return self.apt_bath
    def getApt_rent(self):
        return self.apt_rent
    def getApt_status(self):
        return self.apt_status       
        
        

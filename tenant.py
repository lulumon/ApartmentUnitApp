import random

class Tenant:
    def __init__(self, tenant_fName, tenant_lName, tenant_aptNum):
        self.tenant_fName = str(tenant_fName)
        self.tenant_lName = str(tenant_lName)
        self.tenant_aptNum = int(tenant_aptNum)
        self.tenant_id = random.randrange(10000,99999)
        #Note: per class, tenant id does not need to be checked if it exists. 
    def getTenant_id(self):
        return self.tenant_id
    def getTenant_fName(self):
        return self.tenant_fName
    def getTenant_lName(self):
        return self.tenant_lName
    def getTenant_aptNum(self):
        return self.tenant_aptNum
 
        

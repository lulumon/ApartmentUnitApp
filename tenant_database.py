import tenant
import apartment

class Tenant_db:
    def __init__(self):
        self.tenants  = list()
    def addTenant(self, tenant):
        self.tenants.append(tenant)
    def getTenant(self, aptNo):
        for tenant in self.tenants:
            if aptNo == tenant.getTenant_aptNum():
                return tenant
        return str()              
    def countTenants(self):
        tenantCount = len(self.tenants)
        return tenantCount
    def removeTenant(self, aptNum):
        temp = []
        flag = False
        for tenant in self.tenants:
            if aptNum == tenant.getTenant_aptNum():
                temp.append(tenant)
                self.tenants.remove(tenant)
                return temp
            else:
                flag = True
        if flag == True:
            return str()      

    def getAllTenants(self):
        return self.tenants 
    

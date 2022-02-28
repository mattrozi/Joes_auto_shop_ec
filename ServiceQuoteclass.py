class ServiceQuote:

    def __init__(self,pcharge,lcharge):
        self.__parts_charges=pcharge
        self.__labor_charges=lcharge
        self.__sales_tax=0.8
        self.__total_charges=0

    def set_parts_charges(self,pcharge):
        self.__parts_charges=pcharge

    def set_labor_charges(self,lcharge):
        self.__labor_charges=lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        self.__sales_tax=(self.__labor_charges+self.__parts_charges)*self.__sales_tax

    def get_total_charges(self):
        self.__total_charges=self.get_sales_tax()+self.__labor_charges+self.__parts_charges
        

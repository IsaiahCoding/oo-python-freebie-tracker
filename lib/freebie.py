


class Freebie:
    all = []
    
    def __init__(self, dev, compmany, item_name, value):
        self.dev = dev
        self.compmany = compmany
        self.item_name = item_name
        self.value = value
        
        self.__class__.all.append(self)
    
    @property
    def dev(self):
        return self._dev
    
    @dev.setter
    def dev(self, value):
        from dev import Dev
        if isinstance(value, Dev):
            self._dev = value
    
    @property
    def compmany(self):
        return self._compmany
    
    @compmany.setter
    def compmany(self, value):
        from company import Company
        if isinstance(value, Company):
            self._compmany = value
            
    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, value): 
        if isinstance(value,str):
            self._item_name = value
            
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value,int):
            self._value = value
        
    def print_details(self):
        return f"{self.dev} owns {self.item_name} from {self.company}"
   
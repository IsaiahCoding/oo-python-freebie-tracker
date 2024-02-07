from .freebie import Freebie

class Dev:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value,str):
            self._name = value
    
    def freebies(self):
        from freebie import Freebie
        return [freebie for freebie in Freebie.all if freebie.dev == self]        
            
    def companies(self):
         return list(set([freebie.compmany for freebie in self.Freebies()]))
        
        
    def recieved_one(self, item_name):
        recieved = False
        for freebie in self.freebies():
            if freebie.item_name == item_name:
                recieved = True
         
        return recieved
    
    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev
        
        
        
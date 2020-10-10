"""
Create a Pallet class that has a unique id and weight
Create a Truck class that has pallets with a load and unload methods 
Write a method to get the weight of the truck

Implement methods in Trailer class to for : weight, load, unload and as a follow up 
how would you implement a method for weight at any given time t 
"""

class Pallet:
    def __init__(self,id_,weight=0):
        self.id_ = id_
        self.weight = weight

    def __str__(self):
        """
        >>> print(Pallet(2,11))
        Pallet 2 -> Weight 11
        """
        return f"Pallet({self.id_}) -> Weight {self.weight}"

class Truck:
    def __init__(self):
        self.pallets = []
        self.total_weight = 0

    def load(self,pallet):
        self.pallets.append(pallet)
        self.total_weight += pallet.weight

    def unload(self,pallet):
        self.pallets.remove(pallet)
        self.pallets -= pallet.weight

    def weight(self):
        return sum([i.weight for i in self.pallets])

    def get_weight(self):
        return self.total_weight
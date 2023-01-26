# The objetive was to implement a class called Jar with the following methods:
# __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
# __str__ should return a str with 🍪, where is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
# withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
# capacity should return the cookie jar’s capacity.
# size should return the number of cookies actually in the cookie jar.
#Make a pytest code.


class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError("no hay capacidad")
        self.size = 0
        self.capacity = capacity
    
    def __str__(self):
        cookie = "🍪"
        cookie = self.size * cookie
        return cookie

    def deposit(self, n): 
        deposit = self.size + n 
        if deposit > self.capacity:
            raise ValueError("SUPERO LA CAPACIDAD")
        self.size = deposit
        return self.size

    def withdraw(self, n): 
        withdraw = self.size - n
        if withdraw < 0:
            raise ValueError ("NO HAY GALLETAS SUFICIENTES")
        self.size = withdraw
        return self.size

    @property
    def capacity(self):
        return self._capacity   #esto viene de capacity.setter

    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    print (jar)
    jar.deposit(1)
    print (jar)
    jar.deposit(11)
    print (jar)
    jar.withdraw(5)
    print (jar)

if __name__ == "__main__":
    main()
        

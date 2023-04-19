# a SpaceShip class létrehozása a Fuel, Passangers, Shields és Speedometer property-kkel
class SpaceShip:

    def __init__(self,
                 Fuel=400,
                 Passengers=["John", "Steve", "Sam", "Danielle"],
                 Shields=True,
                 Speedometer=0):
        self.Fuel = Fuel
        self.Passengers = Passengers
        self.Shields = Shields
        self.Speedometer = Speedometer

#a list_passengers metódus létrehozása az utasok listázásához

    def list_passengers(self):
        for passenger in self.Passengers:
            print(f"Passanger: {passenger}")

#az addPassenger metódus létrehozása a Passenger tömb bővítéséhez, paraméterként az új tag nevét kell megadni

    def add_passenger(self, new_passenger):
        self.Passengers.append(new_passenger)
        print(f"{new_passenger} was added to the ship")


# a travel metódus létrehozás az utazás értékeinek beállításához, paraméterként a távolságot kell megadni

    def travel(self, distance):
        #console-ra kiírjuk a megtenni kívánt távolságot
        print(f"trying to travel: {distance}")
        #amennyiben az üzemanyag értéke 0
        if self.Fuel == 0:
            #console-ra kiírjuk, hogy a tank üres
            print(f"cant go further, tank is empty")
        else:
            # a newFuel változóba kiszámoljuk a távolság megtételéhez szükséges üzemanyagot
            newFuel = distance / 2
            # ha nincs elegendő üzemanyag
            if self.Fuel - newFuel < 0:
                #a távolságot az üzemanyaggal megtehetőre módosítjuk, az üzemanyagot 0-zuk és kiírjuk console-ra a megtehető távolságot
                distance = self.Fuel * 2
                self.Fuel = 0
                print(f"can only travel: {distance}")
            #ha van elegendő üzemanyag
            else:
                #az üzemanyagot csökkentjük a megtett táv szerint
                self.Fuel -= newFuel
                #ha az üzemanyag 30 alá csökken a pajzsokat kikapcsoljuk és ezt console-ra kiírjuk
                if self.Fuel < 30:
                    self.Shields = False
                    print(f"fuel is low, turning off shields...")

            #a megtett távolsággal növeljük a km óra állását
            self.Speedometer += distance
            #console-ra kiírjuk a megtett távolságot és az aktuális üzemanyag mennyiséget
            print(f"the SpaceShip is at: {self.Speedometer}")
            print(f"the SpaceShip has: {self.Fuel} fuel")

mySpaceShip = SpaceShip()
mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)

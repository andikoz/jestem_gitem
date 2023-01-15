class BMW:
    kolor = 'czerwony'
    bagaznik = []

    def hamuj(self):
        print('Tak hamuje')
        self.skrec('lewo')

    def skrec(self,strona):
        print(f'skrec w {strona}')


    def dodaj(self, a, b):
        return a + b


moje_auto = BMW()
moje_auto.hamuj()
moje_auto.skrec('lewo')
moje_auto.skrec('prawo')
print(moje_auto.dodaj(5,8))
print(moje_auto.kolor)
moje_auto.bagaznik.append('wiertarka')
moje_auto.bagaznik.append('turboszczotka')

print(moje_auto.bagaznik)


class Calculator:  # määrab klassi nimega calculator
    def __init__(self, a, b):  #defineerib konstruktorit kus a ja b on argumendid
        self.a = a  # määrab klasiatribuut a esimesest parameetrist
        self.b = b  #määrabatribuut b teisest parameetrist

    def liitmine(self):  # Defineeri meetod liitmiseks
        return self.a + self.b  # Tagasta a ja b summa

    def lahutamine(self):  # Defineeri meetod lahutamiseks
        return self.a - self.b  # Tagasta a ja b vahe

    def korrutamine(self):  # Defineeri meetod korrutamiseks
        return self.a * self.b  # Tagasta a ja b korrutis

    def jagamine(self):  # Defineeri meetod jagamiseks
        if self.b == 0:  # Kontrolli, kas b on null, et vältida jagamist nulliga
            return  # Kui b on null, siis ei tehta midagi (tavaliselt võiks visata erandi)
        return self.a / self.b  # Tagasta a jagatuna b-ga

    def jaak(self):  # Defineeri meetod jäägi leidmiseks
        return self.a % self.b  # Tagasta a jagatuna b-ga jääk

    def ruutjuur(self):  # Defineeri meetod ruutjuure leidmiseks
        return self.a ** 0.5  # Tagasta a ruutjuur

    def astendamine(self):  # Defineeri meetod astendamiseks
        return self.a ** self.b  # Tagasta a tõstetuna b võrrandi

def menu():  # Defineeri funktsioon menüü kuvamiseks
    print('1. Liitmine')  # Prindi liitmise valik
    print('2. Lahutamine')  # Prindi lahutamise valik
    print('3. Korrutamine')  # Prindi korrutamise valik
    print('4. Jagamine')  # Prindi jagamise valik
    print('5. Jäägi leidmine')  # Prindi jäägi leidmise valik
    print('6. Ruutjuure leidmine')  # Prindi ruutjuure leidmise valik
    print('7. Astendamine')  # Prindi astendamise valik
    print('0. Välju')  # Prindi väljumise valik

def main():  # Defineeri peamine funktsioon
    a = int(input("Sisesta esimene number: "))  # Kutsu kasutajalt esimest numbrit ja muuda see täisarvuks
    b = int(input("Sisesta teine number: "))  # Kutsu kasutajalt teist numbrit ja muuda see täisarvuks

    kalk = Calculator(a, b)  # Loo Calculatori instants a ja b väärtustega

    while True:  # Alusta lõpmatut tsüklit menüü kuvamiseks ja operatsioonide jaoks
        menu()  # Kutsu esile menüü kuvamise funktsioon
        valik = int(input('Sisesta üks valikutest: '))  # Kutsu kasutajalt menüü valiku sisestamist

        if valik == 1:  # Kontrolli, kas kasutaja valis liitmise
            print("Vastus: ", kalk.liitmine())  # Prindi liitmise tulemus
        elif valik == 2:  # Kontrolli, kas kasutaja valis lahutamise
            print("Vastus: ", kalk.lahutamine())  # Prindi lahutamise tulemus
        elif valik == 3:  # Kontrolli, kas kasutaja valis korrutamise
            print("Vastus: ", kalk.korrutamine())  # Prindi korrutamise tulemus
        elif valik == 4:  # Kontrolli, kas kasutaja valis jagamise
            print("Vastus: ", kalk.jagamine())  # Prindi jagamise tulemus
        elif valik == 5:  # Kontrolli, kas kasutaja valis jäägi leidmise
            print("Vastus: ", kalk.jaak())  # Prindi jäägi leidmise tulemus
        elif valik == 6:  # Kontrolli, kas kasutaja valis ruutjuure leidmise
            print("Vastus: ", kalk.ruutjuur())  # Prindi ruutjuure leidmise tulemus
        elif valik == 7:  # Kontrolli, kas kasutaja valis astendamise
            print("Vastus: ", kalk.astendamine())  # Prindi astendamise tulemus
        elif valik == 0:  # Kontrolli, kas kasutaja soovib väljuda
            print("Kalkulaatorist väljuti")  # Prindi teade väljundi kohta
            break  # Välju tsüklist
        else:  # Kui kasutaja sisestus ei ole kehtiv valik
            print('Vale valik palun sisesta uuesti.')  # Prindi veateade ja palu sisestada kehtiv valik

if __name__ == "__main__":  # Kontrolli, kas seda moodulit käivitati otse
    main()  # Kutsu peamine funktsioon, et alustada programmi
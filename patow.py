import random
import time

prise = 0
baseball = True
balles_basses = [['Balle rapide!!', 2, 2]]
balles_hautes = [['Balle rapide!!', 3, 3]]



def force():
    a = 0
    b = 0
    global prise

    while baseball:
        lancer = [0, 0]

        choix = ''
        print('Choix de lancer:')
        while True:
            choix = input('       ')
            if choix in ('bas', 'haut'):
                break
            else:
                print('bas ou haut')



        time.sleep(0.3)
        if choix == 'bas':
            n = random.randint(1, 10)
            if n == 1:
                # m = random.randint(1,5)
                print(balles_basses[0][0])
                lancer = balles_basses[0][1:]
            else:
                lancer = [1, 1]
        else:
            n = random.randint(1, 10)
            if n == 1:
                # m = random.randint(1,5)
                print(balles_hautes[0][0])
                lancer = balles_hautes[0][1:]
            else:
                lancer = [2, 2]

        if lancer[0] == 0:
            a = random.randint(2, 5)
            b = random.randint(2, 5)
        if lancer[0] == 1:
            a = random.randint(3, 8)
            b = random.randint(3, 8)
        if lancer[0] == 2:
            a = random.randint(9, 12)
            b = random.randint(9, 12)
        if lancer[0] == 3:
            a = random.randint(6, 9)
            b = random.randint(6, 9)
        #print(a, b)

        frappe = 'n'
        print(f'{str(a)} * {str(b)} = ')
        while True:
            try:
                frappe = input('       ')
            except ValueError:
                time.sleep(0.2)
            if frappe.isdigit():
                break

        reponse = a * b
        if reponse == int(frappe):
            time.sleep(0.4)
            return lancer[1]
        else:
            time.sleep(0.3)
            prise += 1
        if prise == 1:
            print('Première prise')
            print('  ')
        if prise == 2:
            print('Deuxième prise')
            print(' ')
            # mode 2 prises pour tests
            return 0
        if prise == 3:
            prise = 0
            return 0


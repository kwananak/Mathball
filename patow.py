import random
import time
import interface as it
import turtle as tt


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

        it.lan_bas.showturtle()
        it.lan_haut.showturtle()
        it.arb_di.write('Choix de lancer', False, 'right', ('Courier', 15, 'bold'))
        time.sleep(5)
        it.arb_di.clear()

        if it.choix == 1:
            n = random.randint(1, 10)
            if n == 1:
                # m = random.randint(1,5)
                it.arb_di.write(balles_basses[0][0], False, 'right', ('Courier', 15, 'bold'))
                time.sleep(2)
                it.arb_di.clear()
                lancer = balles_basses[0][1:]
            else:
                lancer = [1, 1]
        else:
            n = random.randint(1, 10)
            if n == 1:
                # m = random.randint(1,5)
                it.arb_di.write(balles_hautes[0][0], False, 'right', ('Courier', 15, 'bold'))
                time.sleep(2)
                it.arb_di.clear()
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

        frappe = tt.numinput('Lancer!', f'{str(a)} * {str(b)} = ')

        reponse = a * b
        if reponse == int(frappe):
            time.sleep(0.4)
            return lancer[1]
        else:
            time.sleep(0.3)
            prise += 1
        if prise == 1:
            it.arb_di.write('Première prise', False, 'right', ('Courier', 15, 'bold'))
            time.sleep(2)
            it.arb_di.clear()
        if prise == 2:
            it.arb_di.write('Deuxième prise', False, 'right', ('Courier', 15, 'bold'))
            time.sleep(2)
            it.arb_di.clear()
            # mode 2 prises pour tests
            return 0
        if prise == 3:
            prise = 0
            return 0


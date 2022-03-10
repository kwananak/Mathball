import turtle
import time
import random


class joueur:
    def __init__(self):
        self.nom = turtle.textinput(" ", "Nom du joueur")
        self.numero = turtle.numinput(" ", "Numéro du joueur", 0, 1, 99)


class equipe:
    def __init__(self, top):
        if top:
            self.nom = "Les Bozos"
            self.color = (255, 0, 0)
            self.joueur1 = ('Mike', 97)
            self.joueur2 = ('Joey', 62)
            self.joueur3 = ('Igor', 8)
            self.joueur4 = ('Johanne', 21)
            self.joueur5 = ('Galipette', 5)
        else:
            self.nom = "Les Nonos"
            self.color = (0, 255, 0)
            self.joueur1 = ('Sarah-Jeanne', 23)
            self.joueur2 = ('Lucien', 78)
            self.joueur3 = ('Jean-Rodrigue', 99)
            self.joueur4 = ('Ishmaël', 16)
            self.joueur5 = ('Gollum', 9)

    def pos_champ(self):
        pass

class partie:
    def __init__(self):
        self.manche = 1
        self.qt_manches = 0
        self.top_bot = True
        self.score = [0,0]
        self.retrait = 0
        self.prise = 0
        self.balle = 0
        self.ecran = jumbotron()

    def att_qt_manches(self):
        self.qt_manches = turtle.numinput('Manches', 'Combien de manches?', default=0, minval=1, maxval=6)

    def up_manche(self):
        self.manches += 1

    def up_score(self):
        if self.top_bot:
            self.score[0] += 1
            self.ecran.w(f"{self.score[0]} - {self.score[1]}")
        else:
            self.score[1] += 1
            self.ecran.w(f"{self.score[0]} - {self.score[1]}")

    def up_prise(self):
        self.prise += 1
        if self.prise == 1:
            arbi.w("Première prise")
            time.sleep(1)
            arbi.dial.clear()
            presence_bat()
        if self.prise == 2:
            arbi.w("Deuxième prise!")
            time.sleep(1)
            arbi.dial.clear()
            presence_bat()
        if self.prise == 3:
            arbi.w("Troisième prise!!")
            time.sleep(1)
            arbi.dial.clear()
            self.up_retrait()


    def up_retrait(self):
        self.retrait += 1
        self.prise = 0
        arbi.w(f'{marbre.baton[0]} est retiré!')
        time.sleep(1)
        arbi.dial.clear()
        if self.retrait == 3:
            self.retrait = 0
            if self.top_bot:
                arbi.w("3ème retrait! Changement de bord!")
                time.sleep(1)
                arbi.dial.clear()
            else:
                arbi.w("3ème retrait! Fin de la manche!")
                time.sleep(1)
                arbi.dial.clear()
            self.resultat_manche()
        else:
            resultat_presence(0)

    # def resultat_frappe(self):
    #     if self.prise == 3:
    #         self.resultat_presence()
    #     else:
    #         presence_bat


    def resultat_manche(self):
        if self.top_bot:
            self.top_bot = False
            debut_manche()
        else:
            self.top_bot = True
            self.manche += 1
            if self.manche > self.qt_manches:
                resultat_partie()
            else:
                debut_manche()


class but:
    def __init__(self, x, y):
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.penup()
        self.turtle.left(45)
        self.turtle.shape('square')
        self.turtle.shapesize(stretch_wid=3, stretch_len=3)
        self.turtle.color('white')
        self.turtle.speed(9)
        self.turtle.setpos(x, y)
        self.baton = ()
        self.champ = ()
        self.x = x
        self.y = y

    def changer_baton(self, nouveau):
        self.baton = nouveau

    def clear_baton(self):
        self.baton = ()

    def changer_champ(self, nouveau):
        self.champ = nouveau


class ligne:
    def __init__(self,r,x,y):
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.color('white')
        self.turtle.speed(9)
        self.turtle.right(r)
        self.turtle.penup()
        self.turtle.setpos(x,y)
        self.turtle.pensize(6)
        self.turtle.pendown()


class bouton:
    def __init__(self, x, y, w, l, r, func, shape='square', color='white'):
        self.tt = turtle.Turtle()
        self.tt.ht()
        self.tt.up()
        self.tt.color(color)
        self.tt.shape(shape)
        self.tt.setpos(x, y)
        self.tt.shapesize(stretch_wid=w, stretch_len=l)
        self.tt.onclick(func)
        self.tt.right(r)


class arbitre:
    def __init__(self):
        self.pers = turtle.Turtle()
        self.pers.ht()
        self.pers.penup()
        self.pers.speed(9)
        self.pers.shape('triangle')
        self.pers.color('white')
        self.pers.setpos(-80, 130)
        self.pers.shapesize(stretch_wid=3, stretch_len=3)

        self.dial = turtle.Turtle()
        self.dial.ht()
        self.dial.penup()
        self.dial.speed(9)
        self.dial.color('white')
        self.dial.setpos(-100, 170)

    def w(self, a):
        self.dial.clear()
        self.dial.write(a, False, 'right', ('Courier', 15, 'bold'))


class jumbotron:
    def __init__(self):
        self.tt = turtle.Turtle()
        self.tt.ht()
        self.tt.penup()
        self.tt.color('white')
        self.tt.setpos(0, 220)

    def w(self, a):
        self.tt.clear()
        self.tt.write(a, False, 'center', ('System', 80, 'bold'))



##############################################


def intro():
    marbre.turtle.st()
    time.sleep(0.5)
    marbre.turtle.speed(3)
    marbre.turtle.pensize(6)
    marbre.turtle.pendown()
    marbre.turtle.setpos(-200, -50)
    premier.turtle.st()
    time.sleep(0.5)
    marbre.turtle.setpos(0, -250)
    deuxieme.turtle.st()
    time.sleep(0.5)
    marbre.turtle.setpos(200, -50)
    troisieme.turtle.st()
    time.sleep(0.5)
    marbre.turtle.setpos(0, 150)

    while True:
        ligne1.turtle.forward(6)
        ligne2.turtle.forward(6)
        if ligne2.turtle.xcor() <= -600:
            break

    game.ecran.w('Mathball')
    time.sleep(1)
    btn_debut.tt.st()


def nouv_part(x,y):
    btn_debut.tt.ht()
    arbi.pers.st()
    arbi.w('Combien de manches?')
    game.att_qt_manches()
    arbi.dial.clear()
    time.sleep(1)
    debut_partie()


def debut_partie():
    if game.qt_manches == 1:
        arbi.w('Une seule manche!')
    else:
        arbi.w(f'{int(game.qt_manches)} manches!')
    time.sleep(2)
    arbi.dial.clear()
    game.ecran.w(f"{game.score[0]} - {game.score[1]}")

    debut_manche()


def debut_manche():
    global liste_frappeurs
    if game.top_bot:
        stat_manche = 'Haut'
    else:
        stat_manche = 'Bas'
    if game.qt_manches == 1:
        nm_manche = 'l\'unique'
    elif game.manche == game.qt_manches:
        nm_manche = 'la dernière'
    else:
        if game.manche == 1:
            nm_manche = 'la première'
        if game.manche == 2:
            nm_manche = 'la seconde'
        if game.manche == 3:
            nm_manche = 'la troisième'
        if game.manche == 4:
            nm_manche = 'la quatrième'
        if game.manche == 5:
            nm_manche = 'la cinquième'

    arbi.w(f'{stat_manche} de {nm_manche} manche')
    time.sleep(1)
    arbi.dial.clear()

    if game.top_bot:
        nom_baton = equipe_top.nom
        liste_frappeurs = [equipe_top.joueur1, equipe_top.joueur2, equipe_top.joueur3, equipe_top.joueur4, equipe_top.joueur5]
    else:
        nom_baton = equipe_bot.nom
        liste_frappeurs = [equipe_bot.joueur1, equipe_bot.joueur2, equipe_bot.joueur3, equipe_bot.joueur4, equipe_bot.joueur5]



    arbi.w(f'{nom_baton} sont au bâton')
    time.sleep(1.5)
    arbi.dial.clear()

    presence_bat()


def presence_bat():
    marbre.changer_baton(liste_frappeurs[0])
    if premier.baton != ():
        arbi.w(f'{premier.baton[0]} est au premier')
        time.sleep(1)
        arbi.dial.clear()
    if deuxieme.baton != ():
        arbi.w(f'{deuxieme.baton[0]} est au deuxième')
        time.sleep(1)
        arbi.dial.clear()
    if troisieme.baton != ():
        arbi.w(f'{troisieme.baton[0]} est au troisième')
        time.sleep(1)
        arbi.dial.clear()
    if game.retrait == 0:
        arbi.w('Aucun retrait')
        time.sleep(1.5)
        arbi.dial.clear()
    if game.retrait == 1:
        arbi.w('Un retrait')
        time.sleep(1)
        arbi.dial.clear()
    if game.retrait == 2:
        arbi.w('Deux retraits')
        time.sleep(1)
        arbi.dial.clear()
    arbi.w('Choix de lancer')
    btn_fac.tt.st()
    btn_dif.tt.st()


def choix_lancer(x, y):
    arbi.dial.clear
    btn_fac.tt.ht()
    btn_dif.tt.ht()

    if x < 0:
        n = random.randint(1, 6)
        if n == 1:
            arbi.w(balles_basses[0][0])
            time.sleep(1)
            arbi.dial.clear()
            pitch = balles_basses[0][1:]
        else:
            pitch = [1, 1]
    else:
        n = random.randint(1, 6)
        if n == 1:
            arbi.w(balles_hautes[0][0])
            time.sleep(1)
            arbi.dial.clear()
            pitch = balles_hautes[0][1:]
        else:
            pitch = [2, 2]

    if pitch[0] == 0:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
    if pitch[0] == 1:
        a = random.randint(3, 8)
        b = random.randint(3, 8)
    if pitch[0] == 2:
        a = random.randint(9, 12)
        b = random.randint(9, 12)
    if pitch[0] == 3:
        a = random.randint(6, 9)
        b = random.randint(6, 9)
    reponse = a * b
    arbi.w(f"{a} * {b}")
    frappage = turtle.numinput("lancer!", f"{a} * {b}", 0, 1, 199)

    if frappage == reponse:
        resultat_presence(pitch[1])
    else:
        game.up_prise()



#     lancer(reponse, pitch[1])
#
#
# def lancer(reponse, pitch):
#


def frappe():
    game.resultat_frappe()


def resultat_presence(p):

    global liste_frappeurs
    frappeur = marbre.baton[0]

    if p == 1:
        game.ecran.tt.clear()
        game.ecran.w('Coup sûr!')
        time.sleep(1)
        game.ecran.tt.clear()
        game.ecran.w(f'{game.score[0]} - {game.score[0]}')
    if p == 2:
        game.ecran.tt.clear()
        game.ecran.w('DDouble!!')
        time.sleep(1)
        game.ecran.tt.clear()
        game.ecran.w(f'{game.score[0]} - {game.score[0]}')
    if p == 3:
        game.ecran.tt.clear()
        game.ecran.w('TTTriple!!!')
        time.sleep(1)
        game.ecran.tt.clear()
        game.ecran.w(f'{game.score[0]} - {game.score[0]}')
    if p == 4:
        game.ecran.tt.clear()
        game.ecran.w('!♥!COUP DE CIRCUIT!♥!')
        time.sleep(1)
        game.ecran.tt.clear()
        game.ecran.w(f'{game.score[0]} - {game.score[0]}')

    for i in range(p):
        if troisieme.baton != ():
            game.up_score()
            arbi.w(f"{frappeur} a fait marquer {troisieme.baton[0]}!")
            time.sleep(1)
            arbi.dial.clear()
        if deuxieme.baton == ():
            troisieme.clear_baton()
        else:
            troisieme.changer_baton(deuxieme.baton)
        if premier.baton == ():
            deuxieme.clear_baton()
        else:
            deuxieme.changer_baton(premier.baton)
        if marbre.baton == ():
            premier.clear_baton()
        else:
            premier.changer_baton(marbre.baton)
        marbre.clear_baton()



    liste_frappeurs.insert(0, liste_frappeurs.pop())

    presence_bat()



def resultat_partie():
    print('partie finie')

#######################################################

balles_basses = [['Balle rapide!!', 2, 2]]
balles_hautes = [['Balle rapide!!', 3, 3]]

equipe_top = equipe(True)
equipe_bot = equipe(False)

marbre = but(0, 150)
premier = but(-200, -50)
deuxieme = but(0, -250)
troisieme = but(200, -50)

ligne1 = ligne(45, 200, -50)
ligne2 = ligne(135, -200, -50)

game = partie()
turtle.bgcolor('black')
btn_debut = bouton(0,-50,3,6,0, nouv_part)
btn_fac = bouton(-50,-30, 3, 5, 90, choix_lancer, 'arrow')
btn_dif = bouton(50,-70, 3, 5, 270, choix_lancer, 'arrow')
arbi = arbitre()
intro()

turtle.done()
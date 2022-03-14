# Tous droits réservés, copyright 2022 Dominic Daoust


import turtle
import time
import random
from playsound import playsound


#check copyright
#envoyer joueurs au champ pour vrai
#inputs simultanés
#modèle joueurs
#inputs val equipes/joueurs
#background(s)
#statistiques joueurs
#incorporation web
#timers sur input
#liste des frappeurs = bancs des joueurs
#affichage complet jumbotron
#sons
#problème du 6ieme frappeur
#refaire basses/hautes + cartes événements


class joueur:
    all = []
    def __init__(self, nom, shape, num, x, y):
        self.tt = turtle.Turtle()
        self.tt.ht()
        self.tt.up()
        self.tt.shape(shape)
        self.tt.setpos(x, y)

        self.shape_init = shape
        self.banc = (x, y)

        self.nom = nom
        # self.nom = turtle.textinput(" ", "Nom du joueur")
        self.num = num
        # self.numero = turtle.numinput(" ", "Numéro du joueur", 0, 1, 99)

        joueur.all.append(self)

    def update_pos(self, x, y):
        self.tt.setpos(x, y)
        if x == -85 and y == 100:
            if game.top_bot:
                self.tt.shape("bleu_baton.gif")
            else:
                self.tt.shape("rouge_baton.gif")
        else:
            self.tt.shape(self.shape_init)

    def retour_banc(self):
        self.tt.shape(self.shape_init)
        self.tt.setpos(self.banc)


class equipe:
    def __init__(self, top):
        self.liste_frappeurs = []
        if top:
            self.nom = "Les Bozos"
            self.joueur1 = joueur('Mike', "joueur_bleu.gif", 97, -400, 330)
            self.liste_frappeurs.append(self.joueur1)
            self.joueur2 = joueur('Joey', "joueur_bleu.gif", 62, -400, 230)
            self.liste_frappeurs.append(self.joueur2)
            self.joueur3 = joueur('Igor', "joueur_bleu.gif", 8, -400, 130)
            self.liste_frappeurs.append(self.joueur3)
            self.joueur4 = joueur('Johanne', "joueur_bleu.gif", 21, -400, 30)
            self.liste_frappeurs.append(self.joueur4)
            self.joueur5 = joueur('Galipette', "joueur_bleu.gif", 5, -400, -70)
            self.liste_frappeurs.append(self.joueur5)
        else:
            self.nom = "Les Nonos"
            self.joueur1 = joueur('Sarah-Jeanne', "joueur_rouge.gif", 23, 400, 330)
            self.liste_frappeurs.append(self.joueur1)
            self.joueur2 = joueur('Lucien', "joueur_rouge.gif", 78, 400, 230)
            self.liste_frappeurs.append(self.joueur2)
            self.joueur3 = joueur('Jean-Rodrigue', "joueur_rouge.gif", 99, 400, 130)
            self.liste_frappeurs.append(self.joueur3)
            self.joueur4 = joueur('Ishmaël', "joueur_rouge.gif", 16, 400, 30)
            self.liste_frappeurs.append(self.joueur4)
            self.joueur5 = joueur('Gollum', "joueur_rouge.gif", 9, 400, -70)
            self.liste_frappeurs.append(self.joueur5)

    def rotation_frappeurs(self):
        self.liste_frappeurs.insert(0, self.liste_frappeurs.pop())

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

        self.btn_manches = turtle.Turtle()
        self.btn_manches.ht()
        self.btn_manches.up()
        self.btn_manches.setpos(0, -100)
        self.btn_manches.shape("btn_manches.gif")
        self.btn_manches.onclick(self.att_qt_manches)

    def att_qt_manches(self, x, y):
        if x >= self.btn_manches.xcor() - 102 and x <= self.btn_manches.xcor() - 66:
            self.qt_manches = 1
        if x >= self.btn_manches.xcor() - 60 and x <= self.btn_manches.xcor() - 24:
            self.qt_manches = 2
        if x >= self.btn_manches.xcor() - 18 and x <= self.btn_manches.xcor() + 18:
            self.qt_manches = 3
        if x >= self.btn_manches.xcor() + 24 and x <= self.btn_manches.xcor() + 60:
            self.qt_manches = 4
        if x >= self.btn_manches.xcor() + 66 and x <= self.btn_manches.xcor() + 102:
            self.qt_manches = 5
        self.btn_manches.ht()
        debut_partie()



    def up_manche(self):
        self.manches += 1

    def choix_lancer(self, x, y):
        btn_fac.tt.ht()
        btn_dif.tt.ht()

        if x < 0:
            n = random.randint(1, 6)
            if n == 1:
                arbi.w(balles_basses[0][0])
                self.pitch = balles_basses[0][1:]
            else:
                self.pitch = [1, 1]
        else:
            n = random.randint(1, 6)
            if n == 1:
                arbi.w(balles_hautes[0][0])
                self.pitch = balles_hautes[0][1:]
            else:
                self.pitch = [2, 2]

        match self.pitch[0]:
            case 0:
                a = random.randint(2, 5)
                b = random.randint(2, 5)
            case 1:
                a = random.randint(3, 8)
                b = random.randint(3, 8)
            case 2:
                a = random.randint(9, 12)
                b = random.randint(9, 12)
            case 3:
                a = random.randint(6, 9)
                b = random.randint(6, 9)
        self.reponse = a * b
        arbi.dial.write(f"{a} * {b}", False, 'right', ('Courier', 15, 'bold'))
        if game.top_bot:
            clav_bleu.delete()
            clav_bleu.tt.st()
        else:
            clav_rouge.delete()
            clav_rouge.tt.st()

    def frappe(self, de_clav):
        arbi.dial.clear()
        if int(de_clav) == self.reponse:
            resultat_presence(self.pitch[1])
        else:
            game.up_prise()

    def up_score(self):
        if self.top_bot:
            self.score[0] += 1
            self.ecran.update()
        else:
            self.score[1] += 1
            self.ecran.w(f"{self.score[0]} - {self.score[1]}")

    def up_prise(self):
        self.prise += 1
        match self.prise:
            case 1:
                arbi.w("Première prise")
                presence_bat()
            case 2:
                arbi.w("Deuxième prise!")
                presence_bat()
            case 3:
                arbi.w("Troisième prise!!")
                self.up_retrait()


    def up_retrait(self):
        self.retrait += 1
        self.prise = 0
        arbi.w(f'{marbre.baton.nom} est retiré!')
        marbre.baton.retour_banc()
        if self.retrait == 3:
            self.retrait = 0
            if self.top_bot:
                arbi.w("3ème retrait! Changement de bord!")
            else:
                arbi.w("3ème retrait! Fin de la manche!")
            self.resultat_manche()
        else:
            resultat_presence(0)


    def resultat_manche(self):
        premier.clear_baton()
        deuxieme.clear_baton()
        troisieme.clear_baton()

        for i in joueur.all:
            i.retour_banc()

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

    def reset_prise(self):
        self.prise = 0


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


class clavier_num:
    def __init__(self, x, y, shape):
        self.tt = turtle.Turtle()
        self.tt.ht()
        self.tt.up()
        self.tt.shape(shape)
        self.tt.setpos(x, y)
        self.tt.onclick(self.click)

        self.reponse = ""

        self.ecran = turtle.Turtle()
        self.ecran.ht()
        self.ecran.up()
        self.ecran.color("white")
        self.ecran.setpos(x+50, y+40)

    def click(self, x, y):
        if x >= self.tt.xcor() - 60 and x <= self.tt.xcor() - 25:
            if y <= self.tt.ycor() + 35 and y >= self.tt.ycor():
                self.update("1")
            if y <= self.tt.ycor() - 6 and y >= self.tt.ycor() -42:
                self.update("4")
            if y <= self.tt.ycor() - 48 and y >= self.tt.ycor() + -84:
                self.update("7")
            if y <= self.tt.ycor() - 90 and y >= self.tt.ycor() -126:
                self.update("0")
        if x >= self.tt.xcor() - 18 and x <= self.tt.xcor() + 18:
            if y <= self.tt.ycor() + 35 and y >= self.tt.ycor():
                self.update("2")
            if y <= self.tt.ycor() - 6 and y >= self.tt.ycor() -42:
                self.update("5")
            if y <= self.tt.ycor() - 48 and y >= self.tt.ycor() + -84:
                self.update("8")
            if y <= self.tt.ycor() - 90 and y >= self.tt.ycor() -126:
                self.delete()
        if x >= self.tt.xcor() + 25 and x <= self.tt.xcor() + 60:
            if y <= self.tt.ycor() + 35 and y >= self.tt.ycor():
                self.update("3")
            if y <= self.tt.ycor() - 6 and y >= self.tt.ycor() -42:
                self.update("6")
            if y <= self.tt.ycor() - 48 and y >= self.tt.ycor() + -84:
                self.update("9")
            if y <= self.tt.ycor() - 90 and y >= self.tt.ycor() -126:
                if self.reponse == "":
                    pass
                else:
                    self.ecran.clear()
                    self.tt.ht()
                    game.frappe(self.reponse)


    def update(self, n):
        if len(self.reponse) == 4:
            self.reponse = self.reponse[1:]
        self.reponse += n
        self.ecran.clear()
        self.ecran.write(self.reponse, False, 'right', ('System', 30, 'bold'))


    def delete(self):
        self.reponse = ""
        self.ecran.clear()


class arbitre:
    def __init__(self):
        self.pers = turtle.Turtle()
        self.pers.ht()
        self.pers.penup()
        self.pers.speed(9)
        self.pers.shape('arbi1.gif')
        self.pers.setpos(60, 220)
        self.pers.shapesize(stretch_wid=10, stretch_len=10)

        self.dial = turtle.Turtle()
        self.dial.ht()
        self.dial.penup()
        self.dial.speed(9)
        self.dial.color('white')
        self.dial.setpos(35, 240)

    def w(self, a):
        self.pers.shape('arbi2.gif')
        self.dial.write(a, False, 'right', ('Courier', 15, 'bold'))
        time.sleep(1)
        self.pers.shape('arbi1.gif')
        self.dial.clear()


class jumbotron:
    def __init__(self):
        self.tt = turtle.Turtle()
        self.tt.ht()
        self.tt.penup()
        self.tt.color('white')
        self.tt.setpos(0, 270)

    def w(self, a):
        self.tt.clear()
        self.tt.write(a, False, 'center', ('System', 80, 'bold'))
        time.sleep(1)
        self.update()

    def update(self):
        self.tt.clear()
        self.tt.write(f'{game.score[0]} - {game.score[1]}', False, 'center', ('System', 80, 'bold'))


##############################################


def intro():
    playsound("C://Users/kouan/PycharmProjects/app/theme.wav", False)
    marbre.turtle.st()
    time.sleep(0.5)
    marbre.turtle.speed(3)
    marbre.turtle.pensize(6)
    marbre.turtle.pendown()
    marbre.turtle.setpos(premier.x, premier.y)
    premier.turtle.st()
    time.sleep(0.5)
    marbre.turtle.setpos(deuxieme.x, deuxieme.y)
    deuxieme.turtle.st()
    time.sleep(0.5)
    marbre.turtle.setpos(troisieme.x, troisieme.y)
    troisieme.turtle.st()
    time.sleep(0.5)
    marbre.turtle.setpos(0, 100)

    while True:
        ligne1.turtle.forward(6)
        ligne2.turtle.forward(6)
        if ligne2.turtle.xcor() <= -600:
            break

    game.ecran.tt.write('Mathball', False, 'center', ('System', 80, 'bold'))
    time.sleep(1)
    btn_debut.tt.st()


def nouv_part(x,y):
    btn_debut.tt.ht()
    wn.bgcolor("#288722")
    wn.bgpic("back.gif")
    arbi.pers.st()

    for i in joueur.all:
        i.tt.st()
        time.sleep(0.1)

    arbi.w('Combien de manches?')
    game.btn_manches.st()


def debut_partie():
    if game.qt_manches == 1:
        arbi.w('Une seule manche!')
    else:
        arbi.w(f'{int(game.qt_manches)} manches!')

    game.ecran.update()

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
    match game.manche:
        case 1:
            nm_manche = 'la première'
        case 2:
            nm_manche = 'la seconde'
        case 3:
            nm_manche = 'la troisième'
        case 4:
            nm_manche = 'la quatrième'
        case 5:
            nm_manche = 'la cinquième'

    arbi.w(f'{stat_manche} de {nm_manche} manche')

    if game.top_bot:
        nom_baton = bleus.nom
        liste_frappeurs = [bleus.joueur1, bleus.joueur5, bleus.joueur4, bleus.joueur3, bleus.joueur2]
        rouges.joueur1.update_pos(85, 100)
        rouges.joueur1.tt.shape("rouge_champ.gif")
        rouges.joueur2.update_pos(-115, -100)
        rouges.joueur2.tt.shape("rouge_champ.gif")
        rouges.joueur3.update_pos(85, -300)
        rouges.joueur3.tt.shape("rouge_champ.gif")
        rouges.joueur4.update_pos(285, -100)
        rouges.joueur4.tt.shape("rouge_champ.gif")
        rouges.joueur5.update_pos(0, -70)
        rouges.joueur5.tt.shape("rouge_champ.gif")

    else:
        nom_baton = rouges.nom
        liste_frappeurs = [rouges.joueur1, rouges.joueur5, rouges.joueur4, rouges.joueur3, rouges.joueur2]
        bleus.joueur1.update_pos(85, 100)
        bleus.joueur1.tt.shape("bleu_champ.gif")
        bleus.joueur2.update_pos(-115, -100)
        bleus.joueur2.tt.shape("bleu_champ.gif")
        bleus.joueur3.update_pos(85, -300)
        bleus.joueur3.tt.shape("bleu_champ.gif")
        bleus.joueur4.update_pos(285, -100)
        bleus.joueur4.tt.shape("bleu_champ.gif")
        bleus.joueur5.update_pos(0, -70)
        bleus.joueur5.tt.shape("bleu_champ.gif")


    arbi.w(f'{nom_baton} sont au bâton')

    presence_bat()


def presence_bat():
    if game.top_bot:
        marbre.changer_baton(bleus.liste_frappeurs[0])
    else:
        marbre.changer_baton(rouges.liste_frappeurs[0])
    marbre.baton.update_pos(-85, 100)


    if premier.baton != ():
        arbi.w(f'{premier.baton.nom} est au premier')
    if deuxieme.baton != ():
        arbi.w(f'{deuxieme.baton.nom} est au deuxième')
    if troisieme.baton != ():
        arbi.w(f'{troisieme.baton.nom} est au troisième')
    if game.retrait == 0:
        arbi.w('Aucun retrait')
    if game.retrait == 1:
        arbi.w('Un retrait')
    if game.retrait == 2:
        arbi.w('Deux retraits')
    arbi.w('Choix de lancer')
    btn_fac.tt.st()
    btn_dif.tt.st()


def resultat_presence(p):
    frappeur = marbre.baton.nom

    match p:
        case 1:
            game.ecran.w('Coup sûr!')
        case 2:
            game.ecran.w('DDouble!!')
        case 3:
            game.ecran.w('TTTriple!!!')
        case 4:
            game.ecran.w('!♥!COUP DE CIRCUIT!♥!')

    for i in range(p):
        if troisieme.baton != ():
            troisieme.baton.update_pos(0, 175)
            game.up_score()
            arbi.w(f"{frappeur} a fait marquer {troisieme.baton.nom}!")
            troisieme.baton.retour_banc()

        if deuxieme.baton == ():
            troisieme.clear_baton()
        else:
            troisieme.changer_baton(deuxieme.baton)
            troisieme.baton.update_pos(115, -100)
        if premier.baton == ():
            deuxieme.clear_baton()
        else:
            deuxieme.changer_baton(premier.baton)
            deuxieme.baton.update_pos(-85, -300)
        if marbre.baton == ():
            premier.clear_baton()
        else:
            premier.changer_baton(marbre.baton)
            premier.baton.update_pos(-285, -100)

        marbre.clear_baton()

    game.reset_prise()
    if game.top_bot:
        bleus.rotation_frappeurs()
    else:
        rouges.rotation_frappeurs()

    presence_bat()


def resultat_partie():
    arbi.w('Partie finie!')
    if game.score[0] > game.score[1]:
        arbi.w(f"{bleus.nom} ont gagnés!")
    if game.score[0] < game.score[1]:
        arbi.w(f"{rouges.nom} ont gagnés!")
    if game.score[0] == game.score[1]:
        arbi.w("Partie nulle! Tout le monde perd!!")


#######################################################


wn = turtle.Screen()
wn.bgcolor("black")
load = turtle.Turtle()
load.ht()
load.color("white")
load.write("loading...", False, 'center', ('Courier', 15, 'bold'))

wn.addshape('arbi1.gif')
wn.addshape('arbi2.gif')
wn.addshape('jouer.gif')
wn.addshape("joueur_bleu.gif")
wn.addshape("joueur_rouge.gif")
wn.addshape("bleu_baton.gif")
wn.addshape("rouge_baton.gif")
wn.addshape("rouge_champ.gif")
wn.addshape("bleu_champ.gif")
wn.addshape("rouge_clav.gif")
wn.addshape("bleu_clav.gif")
wn.addshape("btn_manches.gif")

balles_basses = [('Balle rapide!!', 2, 2)]
balles_hautes = [('Balle rapide!!', 3, 3)]

bleus = equipe(True)
rouges = equipe(False)

marbre = but(0, 100)
premier = but(-200, -100)
deuxieme = but(0, -300)
troisieme = but(200, -100)
monticule = but(0, -100)

ligne1 = ligne(45, 200, -100)
ligne2 = ligne(135, -200, -100)

game = partie()

clav_bleu = clavier_num(-200, 200, "bleu_clav.gif")
clav_rouge = clavier_num(200, 200, "rouge_clav.gif")
btn_debut = bouton(0,-100,2,4,0, nouv_part, "jouer.gif")
btn_fac = bouton(-50,-80, 3, 5, 90, game.choix_lancer, 'arrow')
btn_dif = bouton(50,-120, 3, 5, 270, game.choix_lancer, 'arrow')
arbi = arbitre()

load.clear()
intro()

turtle.done()
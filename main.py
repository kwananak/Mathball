import patow as pt
import time
import interface as it
import turtle as tt

def coup(force):
  global marbre
  global premier
  global deuxieme
  global troisieme
  global score_bot
  global score_top
  global retrait
  frappeur = marbre[1][0]

  if force == 0:
    retrait += 1
    it.title.clear()
    it.title.write(f' {frappeur} est retiré!', False, 'center', ('Courier', 100, 'bold'))
    it.title.clear()
    it.title.write(f'{score_top} - {score_bot}', False, 'center', ('Courier', 100, 'bold'))
  if force == 1:
    it.title.clear()
    it.title.write('Coup sûr!', False, 'center', ('Courier', 100, 'bold'))
    it.title.clear()
    it.title.write(f'{score_top} - {score_bot}', False, 'center', ('Courier', 100, 'bold'))
  if force == 2:
    it.title.clear()
    it.title.write('DDouble!!', False, 'center', ('Courier', 100, 'bold'))
    it.title.clear()
    it.title.write(f'{score_top} - {score_bot}', False, 'center', ('Courier', 100, 'bold'))
  if force == 3:
    it.title.clear()
    it.title.write('TTTriple!!!', False, 'center', ('Courier', 100, 'bold'))
    it.title.clear()
    it.title.write(f'{score_top} - {score_bot}', False, 'center', ('Courier', 100, 'bold'))
  if force == 4:
    it.title.clear()
    it.title.write('!♥!COUP DE CIRCUIT!♥!', False, 'center', ('Courier', 100, 'bold'))
    it.title.clear()
    it.title.write(f'{score_top} - {score_bot}', False, 'center', ('Courier', 100, 'bold'))

  else:
    for i in range(force):
      if troisieme[1] != []:
        if top_bot:
          score_top += 1
        else:
          score_bot += 1
        print(f'{frappeur} à fait marquer {troisieme[1][0]}!')
        it.title.clear()
        it.title.write(f'{score_top} - {score_bot}', False, 'center', ('Courier', 100, 'bold'))
      troisieme[1] = deuxieme[1]
      deuxieme[1] = premier[1]
      premier[1] = marbre[1]
      marbre[1] = []

def role_champ():
  global monticule
  global marbre
  global premier
  global deuxieme
  global troisieme

  time.sleep(0.7)
  print('  ')
  if manche == 1:
    monticule[0] = int(input('numéro du lanceur: '))
    marbre[0] = int(input('numéro du catcher: '))
    premier[0] = int(input('numéro du premier but: '))
    deuxieme[0] = int(input('numéro du deuxième but: '))
    troisieme[0] = int(input('numéro du troisième but: '))
  else:
    recup = input('Voulez-vous garder les mêmes positions que la manche précédente? ')
    if recup == 'oui':
      if top_bot:
        monticule[0] = pos_bot[0]
        marbre[0] = pos_bot[1]
        premier[0] = pos_bot[2]
        deuxieme[0] = pos_bot[3]
        troisieme[0] = pos_bot[4]
      else:
        monticule[0] = pos_top[0]
        marbre[0] = pos_top[1]
        premier[0] = pos_top[2]
        deuxieme[0] = pos_top[3]
        troisieme[0] = pos_top[4]
    else:
      monticule[0] = int(input('numéro du lanceur: '))
      marbre[0] = int(input('numéro du catcher: '))
      premier[0] = int(input('numéro du premier but: '))
      deuxieme[0] = int(input('numéro du deuxième but: '))
      troisieme[0] = int(input('numéro du troisième but: '))



#input_baton
#input_champ
#input_lanceur

score_top = 0
score_bot = 0
retrait = 0
qt_manches = 0

monticule = [0]
marbre = [[], []]
premier = [[], []]
deuxieme = [[], []]
troisieme = [[], []]

#input d'équipes + joueurs

joueur1 = ['Mike', 97]
joueur2 = ['Joey', 62]
joueur3 = ['Igor', 8]
joueur4 = ['Johanne', 21]
joueur5 = ['Galipette', 5]

joueur6 = ['Sarah-Jeanne', 23]
joueur7 = ['Lucien', 78]
joueur8 = ['Jean-Rodrigue', 99]
joueur9 = ['Ishmaël', 16]
joueur10 = ['Gollum', 9]

nom_top = 'Les Bozos' #input('Nom de l\'équipe à domicile: ')
nom_bot = 'Les Nonos'#input('Nom de l\'équipe visitrice: ')

equipe_top = [nom_top, joueur1, joueur2, joueur3, joueur4, joueur5]
equipe_bot = [nom_bot, joueur6, joueur7, joueur8, joueur9, joueur10]

manche = 1
top_bot = True
pos_top = []
pos_bot = []

print('╔══╗╔══╦════╦═════╦═╗ ╔═╦════╦════╦═╗ ╔═╗  ')
print('║  ╚╝  ║ ╔╗ ║     ║ ╚═╝ ║ ╔╗ ║ ╔╗ ║ ║ ║ ║  ')
print('║      ║ ╚╝ ╠═╗ ╔═╣     ║ ╠╣ ╣ ╚╝ ║ ╚═╣ ╚═╗')
print('║ ╠══╣ ║ ╔╗ ║ ║ ║ ║ ╔═╗ ║ ╚╝ ║ ╔╗ ║   ║   ║')
print('╚═╝  ╚═╩═╝╚═╝ ╚═╝ ╚═╝ ╚═╩════╩═╝╚═╩═══╩═══╝')

time.sleep(1)

it.arb_pers.showturtle()
qt_manches = int(tt.numinput('Manches','Combien de manches?', 1, 1, 9))

if qt_manches  == 1:
  it.arb_di.write('Une seule manche!', False, 'right', ('Courier', 15, 'bold'))
else:
  it.arb_di.write(f'{qt_manches} manches!', False, 'right', ('Courier', 15, 'bold'))
time.sleep(2)
it.arb_di.clear()
time.sleep(0.5)
it.title.clear()
time.sleep(1)
it.title.write('0 - 0', False, 'center', ('Courier', 100, 'bold'))
time.sleep(1)

while manche <= qt_manches:
  if top_bot:
    stat_manche = 'Haut'
  else:
    stat_manche = 'Bas'
  if qt_manches == 1:
    nm_manche = 'l\'unique'
  elif manche == qt_manches:
    nm_manche = 'la dernière'
  else:
    if manche == 1:
      nm_manche = 'la première'
    if manche == 2:
      nm_manche = 'la seconde'
    if manche == 3:
      nm_manche = 'la troisième'
    if manche == 4:
      nm_manche = 'la quatrième'
    if manche == 5:
      nm_manche = 'la cinquième'

  it.arb_di.write(f'{stat_manche} de {nm_manche} manche', False, 'right', ('Courier', 15, 'bold'))
  time.sleep(1.5)
  it.arb_di.clear()

  if top_bot:
    nom_baton, *au_baton = equipe_top
    nom_baton, *au_champ = equipe_bot
  else:
    nom_baton, *au_baton = equipe_bot
    nom_champ, *au_champ = equipe_top

  it.arb_di.write(f'{nom_baton} sont au bâton', False, 'right', ('Courier', 15, 'bold'))
  time.sleep(1.5)
  it.arb_di.clear()

  # role_champ()

  print('## mode 2 prises & 2 retraits pour tests ##')
  while retrait < 2:
    if premier[1] != []:
      print(f'{premier[1][0]} est au premier')
    if deuxieme[1] != []:
      print(f'{deuxieme[1][0]} est au deuxième')
    if troisieme[1] != []:
      print(f'{troisieme[1][0]} est au troisième')
    if retrait == 0:
      it.arb_di.write('Aucun retrait', False, 'right', ('Courier', 15, 'bold'))
      time.sleep(1.5)
      it.arb_di.clear()
    if retrait == 1:
      it.arb_di.write('Un retrait', False, 'right', ('Courier', 15, 'bold'))
      time.sleep(1.5)
      it.arb_di.clear()
    if retrait == 2:
      it.arb_di.write('Deux retraits', False, 'right', ('Courier', 15, 'bold'))
      time.sleep(1.5)
      it.arb_di.clear()

    marbre[1] = au_baton[0]
    coup(pt.force())
    au_baton.insert(0, au_baton.pop())

    if retrait == 3:
      if top_bot:
        it.arb_di.write('Troisième retrait! Changement de bord!', False, 'right', ('Courier', 15, 'bold'))
        time.sleep(2)
        it.arb_di.clear()
      else:
        it.arb_di.write('Troisième retrait! Fin de la manche!', False, 'right', ('Courier', 15, 'bold'))
        time.sleep(2)
        it.arb_di.clear()

  retrait = 0
  marbre = [[], []]
  premier = [[], []]
  deuxieme = [[], []]
  troisieme = [[], []]
  if top_bot:
    top_bot = False
    pos_bot = [monticule, marbre[0], premier[0], deuxieme[0], troisieme[0]]
  else:
    top_bot = True
    pos_top = [monticule, marbre[0], premier[0], deuxieme[0], troisieme[0]]
    manche += 1

print('  ')
time.sleep(0.5)
print(f'Score final: {str(score_top)} pour {equipe_top[0]} à {str(score_bot)} pour {equipe_bot[0]}!!')
time.sleep(0.4)
if score_top > score_bot:
  print(f'    {equipe_top[0]} remportent la victoire!')
elif score_top < score_bot:
  print(f'    {equipe_bot[0]} remportent la victoire!')
else:
  print('    Partie nulle! Tout le monde perd!!')

time.sleep(1)
print('                ♥♥ ♥♥ ')
print('               ♥  ♥  ♥')
print('                ♥   ♥ ')
print('                  ♥   ')




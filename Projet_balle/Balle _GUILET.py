# Arthur et Aurelien
import pygame                           #importation des bibi
from pygame import*
from pygame.gfxdraw import*
from random import*
import math

largeur = 1920
hauteur = 1080


class Jeux:
    def __init__(self):
        #Variables bool pour les inits des pages du jeu
        self.lejeux= True
        self.menu = True
        self.jouer, self.numero, self.niveau, self.facile, self.resultat, self.partager, self.regle_jeux  = False, False, False, False , False, False, False
         #variables de couleur texte et coordo du centre avec la largeur et hauteur d'ecran
        self.bleu = (40, 120, 230)
        self.vert = (40, 230, 120)
        self.blanc = (255,255,255)

        self.centre_x, self.centre_y = largeur//2, hauteur//2
        #variables de jeux
        self.valeur = ""
        self.compteur=0                                              #init du compteur
        self.secondesecoul=0                                       #init seconde

        #init raquette
        self.x=0
        self.y=0
        self.r=50

        #init des écritures appliquer pour l'affichage
        self.font = pygame.font.SysFont('Comic Sans MS,Arial', 40)
        self.monfont = pygame.font.SysFont("Comic Sans MS,Arial",50)

        #variables qui appel toute les graphismes exterieur
        self.affich = self.monfont.render('Entrez un nombre : ', True, self.bleu)                   #affiche " Entrez un nombre " dans la page pour preparer le jeu
        self.affich_rect = self.affich.get_rect(center=(self.centre_x, self.centre_y))

        self.v_input = self.monfont.render(self.valeur, True, self.vert)                            #affiche " le nombre que l'on écrit " dans la page pour preparer le jeu
        self.v_input_rect = self.v_input.get_rect(topleft=self.affich_rect.topright)

        """"""
        #image d'acceuil
        self.acceuil = image.load("assets/acceuil.jpg")
        self.acceuil = pygame.transform.scale(self.acceuil,(largeur,hauteur))
        #image de jeu
        self.fond = image.load("assets/pari.jpg")
        self.fond = pygame.transform.scale(self.fond,(largeur,hauteur))

        #image bouton regle du jeu
        self.reglejeu = image.load("assets/reglejeu.png")
        self.reglejeu = pygame.transform.scale(self.reglejeu,(largeur,hauteur))
        self.reglejeu_rect =  self.reglejeu.get_rect(center=(self.centre_x, self.centre_y))
        #image bouton play
        self.assetplay = image.load("assets/play.png")
        self.assetplay = pygame.transform.scale(self.assetplay,(350,150))
        self.assetplay_rect = self.assetplay.get_rect(center=(self.centre_x, self.centre_y/1.4))
        #image bouton quitter
        self.assetexit = image.load("assets/exit.png")
        self.assetexit =  pygame.transform.scale(self.assetexit,(350,150))
        self.assetexit_rect = self.assetexit.get_rect(center=(self.centre_x, self.centre_y/0.68))
        #image bouton suivant
        self.assetsuivant = image.load("assets/suivant.png")
        self.assetsuivant =  pygame.transform.scale(self.assetsuivant,(200,150))
        self.assetsuivant_rect = self.assetsuivant.get_rect(center=(self.centre_x/0.55, self.centre_y/0.56))
        #image bouton retour
        self.assetretour = image.load("assets/retour.png")
        self.assetretour =  pygame.transform.scale(self.assetretour,(200,150))
        self.assetretour_rect = self.assetretour.get_rect(center=(self.centre_x/6, self.centre_y/0.56))
        #image bouton partager
        self.assetpartage = image.load("assets/partage.png")
        self.assetpartage =  pygame.transform.scale(self.assetpartage,(150,100))
        self.assetpartage_rect = self.assetpartage.get_rect(center=(self.centre_x/1.13, self.centre_y/0.92))
        #image des regles du jeu
        self.assetregle = image.load("assets/regle.png")
        self.assetregle =  pygame.transform.scale(self.assetregle,(150,100))
        self.assetregle_rect = self.assetregle.get_rect(center=(self.centre_x/0.89, self.centre_y/0.92))
        #affiche quand on gagne
        self.gagner = self.font.render("Vous avez gagné félicitation votre gains est de 1 millards d'euros!",True,(0,255,0))
        self.gagner_rect = self.gagner.get_rect(center=(self.centre_x, self.centre_y))
        #affiche quand on perd
        self.perdu = self.font.render("Vous avez perdu, réessayer pour perdre un maximum d'argent!",True,(0,255,0))
        self.perdu_rect = self.perdu.get_rect(center=(self.centre_x, self.centre_y))


        self.assetfacile = image.load("assets/easy.png")
        self.assetfacile =  pygame.transform.scale(self.assetfacile,(300,150))
        self.assetfacile_rect = self.assetfacile.get_rect(center=(self.centre_x/1.15, self.centre_y/0.92))

        self.assetdur = image.load("assets/hard.png")
        self.assetdur =  pygame.transform.scale(self.assetdur,(300,150))
        self.assetdur_rect = self.assetdur.get_rect(center=(self.centre_x/0.85, self.centre_y/0.92))
        #importer le son rebond
        self.son = pygame.mixer.music.load('assets/rebond.ogg')

        self.CLOCK = pygame.time.Clock()
        self.FPS = 180


#POO

#----Programme balle ----

class Balle:

    def __init__(self):
        """variable de la classe balle"""
        #variables du l'apparition de la balle et son rayon
        self.r=randint(60,68)
        self.px=randint(0+self.r,1000-self.r)                                   # X position initiale aleatoire
        self.py=randint(0+self.r, 720-self.r)                                    # Y ...
        #variables de la vitesse de la balle
        self.vx= randint(-5.0,5.0)
        self.vy= randint(-5.0,5.0)
        self.VA= randint(1.0,2.0)                                       #vitesse supp alea
        """"""

    def couleur_balle(self):
        """creer une couleur aléatoir pour la balle"""
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)

    def affichage_balle(self,px,py,r):
        """fonction pour avoir l'affichage complet de la balle"""
        self.balle = filled_circle(fenetre,px,py,r,couleur)
    def mouvement_balle(self):

         #init du deplacement de la balle
        self.px = self.px + self.vx
        self.py = self.py + self.vy
    #conditon pour chaque coter de la fenetre lors du rebondissement
        if self.px >= largeur-self.r:
            self.vx = -self.vx    #rebondissement de la balle
            self.vy=self.vy-self.VA #acceleration de la balle
            self.vx=self.vx-self.VA

        if self.px <= 0+self.r:
            self.vx = -self.vx
            self.vy=self.vy+self.VA
            self.vx=self.vx+self.VA


        if self.py >= hauteur-self.r:
            self.vy = -self.vy
            self.vy=self.vy-self.VA
            self.vx=self.vx-self.VA

        if  self.py <= 0+self.r:
            self.vy = -self.vy
            self.vy=self.vy+self.VA
            self.vx=self.vx+self.VA




#---Programme principale---

pygame.init()
#Instance pour appeler la classe compression du programme
IB=Balle()                                                     # simplification de la classe balle pour les objets
IJ=Jeux()
couleur=IB.couleur_balle()
#ecran
fenetre = pygame.display.set_mode((largeur,hauteur),pygame.FULLSCREEN)        #init de la fenetre graphique
#affichage de balle
IB.affichage_balle(IB.px,IB.py,IB.r)
#nom de la fenetre
pygame.display.set_caption("Le parieur de rebond de Balle")




display.flip()


#--- ecran de jeu ----
while IJ.lejeux :

    IJ.CLOCK.tick(IJ.FPS)                       #actualisation 180 images par seconde
    #page du menu de jeu
    if IJ.menu:

        #remise a 0 du jeu quand on est dans le menu
        IB.__init__()
        IJ.__init__()
        pygame.display.flip() #actualiser la page
        #conditon de retour ou d'avancer dans les differentes fentre du jeu
        for evenement in pygame.event.get():
            #la touche echap permet de revenir a la page précedante ou quitter le jeu sur le menu
            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.lejeux = False
            #le clic bouton permet d'interagir avec les boutons de chaque page du jeu
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if IJ.assetplay_rect.collidepoint(evenement.pos):
                    IJ.numero = True
                    IJ.menu = False

                if IJ.assetexit_rect.collidepoint(evenement.pos):
                    IJ.lejeux = False

                if IJ.assetregle_rect.collidepoint(evenement.pos):
                    IJ.menu = False
                    IJ.regle_jeux = True

                if IJ.assetpartage_rect.collidepoint(evenement.pos):
                    IJ.menu = False
                    IJ.partager = True
                #apparition de tout les graphisme pour le menu

        fenetre.blit(IJ.acceuil,(0,0))
        fenetre.blit(IJ.assetplay,IJ.assetplay_rect)
        fenetre.blit(IJ.assetexit,IJ.assetexit_rect)
        fenetre.blit(IJ.assetregle,IJ.assetregle_rect)
        fenetre.blit(IJ.assetpartage,IJ.assetpartage_rect)


    #page des regles du jeu
    if IJ.regle_jeux:

        for evenement in pygame.event.get():

            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.regle_jeux = False
                    IJ.menu = True
            if evenement.type == pygame.QUIT:
                IJ.jouer = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if IJ.assetretour_rect.collidepoint(evenement.pos):
                    IJ.regle_jeux = False
                    IJ.menu = True
        fenetre.blit(IJ.reglejeu,IJ.reglejeu_rect)
        fenetre.blit(IJ.assetretour,IJ.assetretour_rect)
        pygame.display.flip()

    #page pour partager des informations""
    if IJ.partager:

        for evenement in pygame.event.get():

            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.partager = False
                    IJ.menu = True
            if evenement.type == pygame.QUIT:
                IJ.lejeux = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if IJ.assetretour_rect.collidepoint(evenement.pos):
                    IJ.partager = False
                    IJ.menu = True

        fenetre.fill(0)
        fenetre.blit(IJ.assetretour,IJ.assetretour_rect)
        pygame.display.flip()
    """"""
    #page qui permet de miser le nombre que l'on souhaite pour jouer au jeu
    if IJ.numero:

        for evenement in pygame.event.get():

            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.numero = False
                    IJ.menu = True
            if evenement.type == pygame.QUIT:
                IJ.lejeux = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if IJ.assetretour_rect.collidepoint(evenement.pos):
                    IJ.numero = False
                    IJ.menu = True
                if IJ.assetsuivant_rect.collidepoint(evenement.pos):
                    IJ.numero = False
                    IJ.niveau = True
            #evenement pour l'affichage de l'interaction "nombre" du joueur et le jeu
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    IJ.niveau = True
                    IJ.numero= False
                elif evenement.key == pygame.K_BACKSPACE:
                    IJ.valeur = IJ.valeur[:-1]
                else:
                    IJ.valeur += evenement.unicode
                IJ.v_input = IJ.monfont.render(IJ.valeur, True, IJ.vert)
                IJ.v_input_rect = IJ.v_input.get_rect(topleft=IJ.affich_rect.topright)

        fenetre.fill(0)
        fenetre.blit(IJ.affich, IJ.affich_rect)
        fenetre.blit(IJ.v_input, IJ.v_input_rect)
        fenetre.blit(IJ.assetretour,IJ.assetretour_rect)
        fenetre.blit(IJ.assetsuivant,IJ.assetsuivant_rect)
        pygame.display.flip()

    if IJ.niveau:
        for evenement in pygame.event.get():

            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.niveau = False
                    IJ.numero = True
            if evenement.type == pygame.QUIT:
                IJ.lejeux = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if IJ.assetfacile_rect.collidepoint(evenement.pos):
                    IJ.niveau = False
                    IJ.jouer = True
                    IJ.facile = True
                if IJ.assetdur_rect.collidepoint(evenement.pos):
                    IJ.niveau = False
                    IJ.jouer = True
                    IJ.facile = False

        fenetre.fill(0)
        fenetre.blit(IJ.assetdur,IJ.assetdur_rect)
        fenetre.blit(IJ.assetfacile,IJ.assetfacile_rect)
        debut_temps=pygame.time.get_ticks()
        pygame.display.flip()


    #page ou le jeux est lancer avec l'interaction de la boulle
    if IJ.jouer:
        #init du chrono
        IJ.secondesecoul = (pygame.time.get_ticks()-debut_temps)//1000

        IB.mouvement_balle()

        if  IB.py <= 0+IB.r or IB.py >= hauteur-IB.r or IB.px <= 0+IB.r or IB.px >= largeur-IB.r:
            couleur=IB.couleur_balle() #actualisation de la couleur de la balle pour chaque rebond
            IJ.compteur=IJ.compteur+1 #actualisation du score de la balle pour chaque rebond
            IJ.son = pygame.mixer.music.play() #actualisation du son pour chaque rebond

        #apparition score et le temps
        scoretext = IJ.monfont.render("Score {0}".format(IJ.compteur),True,(0,255,0))                     #affichage du score et actualisation au fur et a mesure des rebondissement
        scoretext_rect = scoretext.get_rect(center=(IJ.centre_x/8, IJ.centre_y/10))

        chronotext = IJ.monfont.render("Chrono : {0}".format(IJ.secondesecoul),True,(0,255,0))    #affichage du temps et actualisation au fur et a mesure des rebondissement
        chronotext_rect = chronotext.get_rect(center=(IJ.centre_x/0.55, IJ.centre_y/10))
        #apparition du fond de la balle,

        if IJ.facile:

            if evenement.type == pygame.MOUSEMOTION:
                #la raquette suivre la souris avec comme parametre x et y
                IJ.x, IJ.y = evenement.pos


                distance = math.hypot(IB.px-IJ.x, IB.py-IJ.y)
                if distance<= IB.r + IJ.r:
                    IB.vx = -IB.vx
                    IB.vy = -IB.vy
                    IB.vy=IB.vy-1
                    IB.vx=IB.vx-1
                    IJ.son = pygame.mixer.music.play()

                filled_circle(fenetre,IJ.x,IJ.y,IJ.r,couleur)
                pygame.display.flip()

        pygame.display.flip()


        for evenement in pygame.event.get():

            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.jouer = False
                    IJ.resultat = True


        #arret du jeu quand le temps et = a 20 secondes
        if IJ.secondesecoul>20:
            IJ.jouer = False
            IJ.resultat = True

        fenetre.blit(IJ.fond,(0,0))
        #blit du chrono score balle
        IB.affichage_balle(IB.px,IB.py,IB.r)
        fenetre.blit(scoretext, scoretext_rect)
        fenetre.blit(chronotext, chronotext_rect)

    #page des resultats du jeu
    if IJ.resultat:

                #conditon pour verifier si les deux valeurs sont les memes ou differentes
        if int(IJ.compteur)==int(IJ.valeur):
               #phrase qui indique la victoire qui viens de la balle
               fenetre.blit(IJ.gagner,IJ.gagner_rect)

        if int(IJ.compteur)!=int(IJ.valeur):
                #phrase qui indique la defaite
               fenetre.blit(IJ.perdu,IJ.perdu_rect)
        pygame.display.flip()

        fenetre.fill(0)
        #la mise de depart
        comp = IJ.font.render("Le score que tu as fais {0} ".format(IJ.compteur),True,(0,255,0))
        comp_rect = comp.get_rect(center=(IJ.centre_x, IJ.centre_y-100))
        fenetre.blit(comp,comp_rect)
        #le score realiser pendant le jeu
        val = IJ.font.render("Ce que tu as misé {0} ".format(IJ.valeur),True,(0,255,0))
        val_rect = val.get_rect(center=(IJ.centre_x, IJ.centre_y-150))
        fenetre.blit(val,val_rect)
        fenetre.blit(IJ.assetsuivant,IJ.assetsuivant_rect)



        for evenement in pygame.event.get():
            if evenement.type == KEYDOWN:
                if evenement.key == K_ESCAPE:
                    IJ.resultat = False
                    IJ.menu = True
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if IJ.assetsuivant_rect.collidepoint(evenement.pos):
                    IJ.resultat = False
                    IJ.menu = True

#fin du programme
pygame.quit()

#info utile du programme
print(IB.px,IB.py)           #affichage des coordonnes de spwan de la balle
print(IB.VA)                 #affichage de la vitesse ajouter a chaque rebond


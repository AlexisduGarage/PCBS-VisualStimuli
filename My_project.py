
""" This is a simple reaction time experiment.

At each trial, a cross is displayed after some random time interval.
The user must click as quickly as possible on a key or a mouse button.

Reaction times are measured and saved in a file for further analyses.

"""

#Importer le package Expyriment (ainsi que random (pour avoir de snombre random et pygame pour dessiner des stimuli)) afin de pouvoir l'utiliser
import expyriment
import random
import pygame

#On créer un nouveau Expyriment object appelé exp et composé d'une expérience appelée "First Experiment"
exp = expyriment.design.Experiment(name="Visual Stimuli Experiment")

#On initialise l'expérience afin qu'elle soit active et prête à être lancée (on la charge)> elle est dans la "salle d'attente"
expyriment.control.initialize(exp)

#On cré (expyriment.design) quatre block experimentaux
block_one = expyriment.design.Block(name="First Block")
block_two = expyriment.design.Block(name="Second Block")
block_three = expyriment.design.Block(name="Third Block")
block_four = expyriment.design.Block(name="Fourth Block") 

N_TRIALS = 15  # total number of trial within one block
MIN_WAIT_TIME = 2000 # 2 secondes d'attentes entre deux stiumulis minimum
MAX_WAIT_TIME = 3000 # 3 secondes d'attentes entre deux stiumulis maximum
MAX_RESPONSE_DELAY = 380 # Délais maximum de réponse au stimulus 380 ms
RESULT_FILE = 'reaction_times.csv'

#On cré (expyriment.design) 1 essais (qui sera répété 15 fois)
trial = expyriment.design.Trial()
stim = expyriment.stimuli.Rectangle()
stim.preload()

#On lance l'expérience active (qui a été initialisé)
expyriment.control.start() 
exp.data_variable_names = ["Block", "Trial", "RT"]

#On fait une loop pour display chacun de nos stimulus ranger dans les essais eux même ranger dans les block
for block in exp.blocks : #Pour chaque block faisant partie de l'expérience "exp"
 for trial in block.trials : #Pour chaque essais dans le block sélectionné
  trial.stimuli[0].present() #Presenter le premier ([0]) stimuli dans l'essais sélectionné -> A VOIR PAS SUR QUE LE STIMULI SOIT DESIGN COMME CA
  rt = exp.keyboard.wait([expyriment.misc.constants.K_SPACE]) #This function returns the key that was pressed as well as the reaction time.
  exp.data.add([block.name, trial.id, rt]) # We added the name of the block, the id of the trial, the pressed key and the reaction time to the data file
  exp.clock.wait(32) #Chaque stimuli dure 1000ms (après la boucle passe au stimuli suivant)

expyriment.control.end() #On fait se terminer l'expérience qui a été lancée


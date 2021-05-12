The point of the project is to see if there is a response time difference to visual information in fonction of the position of these visual information in our visual field and of 
the hand that we use to respond. We know that the central connexions of the retinae are such that each half of the visual field is projected on to the cortex of the opposite
hemisphere (the left part of the visual field is projected on the right hemisphere of the cortex). We also know that the movements of each hand are to a major extent controlled by
the opposite motor cortex. So for example, we can expecte that responding to visual information with the right hand is faster when the stimuli is situated in the right part of the 
visual field than the left. In order to test that we designed the following experience.

We made a two block experiment of 15 trial each. In the first block, the subject use its right hand to respond in the second block the left. The python project has been designed 
in order to add as many blocks as we want in the order that we want. We just have to specify the hand used in the block and the number of the block and it's order (1, 2, 3...) for 
the data treatment. Our displayed stimulus will be a square patch of light, with one square degree in area, that will be flashed on different points of the screen.

At the begining of each block the participant has a description of the hand that he must use and the task that he has to accomplish (pushing the space bar quickly as possible when 
he sees the stimulus). A warning "ready" signal, delivered to the subject visually, preceded each trial. The duration of the fore-period was randomly varied with a range of 2 to 3 
sec (to prevent anticipatory responses). There is minimum response delay and a maximum response delay in order to not take into account anticipatory responses and anormally long responses of the participants (due to 
lack of attention for example). In this version, anticipatory responses were defined as any reaction time less than 150 msec, while the limits of delay of response was 500 msec 
(its changeable).

The stimulus is a 80 by 120 pixel white rectangle. The duration of the stimulus is changeable and has been fixed in this version to 32 msec. At each trial the stimulus take 
randomly one of six different positions (3 situated in the right visual field and 3 situated in the left). The position of the stimulus relatively to the center of the screen is 
specified in the result document for each trial. Before the experiment, experimenter has to tell participants to place their head at the center and fixed the ready signal ("ready" 
write in white letters) between each trials.

When a block is done a cvs file is created which has in its title the number of the block and the hand used in it. It contains the position of the stimulus, reaction time and the 
waiting time.

Given more time I would have liked to add a way of adding one trial to the block each time a response is discarded (because it's anticipartory or too long) in order to have a consistent number (15) of valid trials between each subjects. I would have also liked to make the code cleaner it's a never ending task.

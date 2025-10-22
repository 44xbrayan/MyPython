#### Modules ###
import python_ricochet.module as module
module.printValues("Hola python!")
module.sumValues(33, 44)

from python_ricochet.module import sumValues, printValues

sumValues(22, 88)
printValues("Rayos") 

import math
print(math.sqrt(3)) #Raiz Cuadrada
print(math.pow(2,3)) #Exponente

from math import pi as pi_value
print(pi_value)
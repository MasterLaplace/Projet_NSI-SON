"""
Test - Mesure de distance

"""
from SOPROLAB_V2 import *
from machine import Pin
from neopixel import NeoPixel

try :
	from SOPROLAB_UltraSonV1 import *

    print("Fonctionnement capteur de distance ....")

    HCSR_connected = True

except :

    print("Il semblerait que le capteur de distance ne soit pas branché !")

	HCSR_connected = False
	
class Module:
 	def __init__():
    	self.led = NeoPixel ( Pin(2), 8 )
    	self.rouge = ( 125,   0, 0 )
    	self.Liste = []
		self.Liste_inter = []
    	self.Liste_final = []
  
 	def marche_module(self):
    	while HCSR_connected == True :
      		# Pour tester le module de test uniquement
      		for cptr in range ( 100 ) :
        		if BP.impulsion:# verification
           			while BP.impulsion==True:
                		continue
            		self.Liste.append('][')
            		sleep_ms(500)
        
        		else:
            		#test = int(HCSR.distance_mm)
            		if HCSR.distance_mm < 100 and HCSR.distance_mm > 1:
                		NEOPIX.bargraphe(1)
                		print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

            		elif HCSR.distance_mm < 200 and HCSR.distance_mm > 101:
                		NEOPIX.bargraphe(2)
                		print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

            		elif HCSR.distance_mm < 400 and HCSR.distance_mm > 201:
               			NEOPIX.bargraphe(3)
                		print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

            		elif HCSR.distance_mm < 800 and HCSR.distance_mm > 401:
                		NEOPIX.bargraphe(4)
                		print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

           			elif HCSR.distance_mm < 1200 and HCSR.distance_mm > 801:
                    	NEOPIX.bargraphe(5)
                    	print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                    	self.Liste.append(HCSR.distance_mm)

            		elif HCSR.distance_mm < 1600 and HCSR.distance_mm > 1201:
                		NEOPIX.bargraphe(6)
                		print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

            		elif HCSR.distance_mm < 2000 and HCSR.distance_mm > 1601:
                		NEOPIX.bargraphe(7)
                		print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

            		elif HCSR.distance_mm < 4000 and HCSR.distance_mm > 2001:
                		NEOPIX.bargraphe(8)
               			print ("Distance : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append(HCSR.distance_mm)

            		else :
                		for i in range(8):
                    		self.led[i] = self.rouge
                		self.led.write()
                		print ("Distance ++ : {:4d} mm".format(HCSR.distance_mm) )
                		self.Liste.append('][')
        		print ("Distance ++ : {:4d} mm".format(HCSR.distance_mm) )
        		sleep_ms(10)
			HCSR = False
      	return self.Liste
    
    def supr(self):
        while '][' in self.Liste:
            del self.Liste[self.Liste.index('][')]
		return self.Liste
	
    def compression(self):
    	for i in range(len(Liste)):
        	if Liste:
            	i = 0
        	else:
            	break
        	for j in range(len(Liste)):
            	if Liste[j] <= Liste[i] + 5 or Liste[j] <= Liste[i] - 5:
                	if Liste[j] == Liste[-1]:
                    	Liste_inter = Liste_inter + [Liste[-1]]
                    	del Liste[i:j+1]
                	else:
                    	Liste_inter=Liste_inter + [Liste[j]]
            	else:
                	nbr_multiple = len(Liste_inter)
                	for n in range(len(Liste_inter)):
                    	if Liste_inter == False:
                        	break
                    	else:
                        	Liste_inter.pop()
                	Liste_final = Liste_final + ["{nbr_multiple}x{Liste[i]}"]
                	del Liste[i:j]
               		break
        return self.Liste, self.Liste_final

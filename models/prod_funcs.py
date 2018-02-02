# -*- coding: utf-8 -*-

from openerp import models, fields, api




# Progress 
_hap = {
			
			'laser_quick':         	'Quick', 
			'laser_co2':          	'Co2', 
			'laser_excilite':       'Exc', 
			'laser_ipl':         	'Ipl', 
			'laser_ndyag':        	'Ndy', 

			'hyaluronic_acid':      'Hial', 
			'criosurgery':         	'Crio', 
			'sclerotherapy':        'Escl', 
			'lepismatic':         	'Lepi', 
			'mesotherapy_nctf':     'Meso', 
			'plasma':         		'Plasma', 
			'botulinum_toxin':      'Botox', 
			'intravenous_vitamin':  'Vita Int', 


			# Zona 
			'body_local': 			'Cuerpo loc', 

			'cheekbones': 			'Pom', 

			'face_all': 			'Rostro', 

			'face_all_hands': 		'Rostro Man', 
			
			'face_all_neck': 		'Rostro Cue', 
			
			'face_local': 			'Rostro loc', 

			'hands': 				'Manos', 

			'neck': 				'Cuello', 

			'neck_hands': 			'Cuello Man', 


			'vagina': 				'Vag', 



			'face': 				'Rostro', 
			'arms': 				'Brazos', 
			'gluteus': 				'Gluteos', 
			'feet': 				'Pies', 
			'armpits': 				'Axilas', 
			'shoulders': 			'Hombros', 
			'belly': 				'Vientre', 
			'areolas': 				'Ariolas', 
			'back': 				'Espalda', 
			'breast': 				'Pecho', 
			'legs': 				'Piernas', 

			#'neck_hands': 			'Cuello Manos', 
}





# Get Ticket Name 
@api.multi
#def get_ticket_name(self):
#def get_ticket_name(self, treatment, zone, pathology):
def get_ticket_name(self, treatment, zone, pathology, family, x_type):


	print 'jx'
	print 'Get Ticket Name'

	name_ticket = 'jx'



	if x_type == 'service': 

		if family == 'laser': 
			#name_ticket = _hap[treatment] + ' ' + zone + ' ' + pathology 
			name_ticket = _hap[treatment] + ' ' + _hap[zone] + ' ' + pathology 
		else:
			#name_ticket = treatment + ' ' + zone + ' ' + pathology 
			name_ticket = _hap[treatment] + ' ' + zone + ' ' + pathology 



	return name_ticket






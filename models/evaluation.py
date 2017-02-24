# -*- coding: utf-8 -*-
#
# 	*** Evaluation 
# 

# Created: 				26 Aug 2016
# Last updated: 	 	28 Oct 2016



from openerp import models, fields, api
from datetime import datetime

import jxvars
import eval_vars

#import service_vars
import prodvars





#------------------------------------------------------------------------
class Evaluation(models.Model):
	#_name =	'openhealth.evaluation5'
	_inherit = 'oeh.medical.evaluation'



	#name = fields.Char(
	#		)




	appointment = fields.Many2one(
			'oeh.medical.appointment',
			
			#string='Appointment #'
			string='Cita #', 

			required=False, 
			)









# ----------------------------------------------------------- Relationals ------------------------------------------------------

	treatment = fields.Many2one(
			'openhealth.treatment',			
			ondelete='cascade', 
			)


	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
			)









	# Commons
	vspace = fields.Char(
			' ', 
			readonly=True
			)



	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			required=True, 
	)

	patient_id = fields.Integer(
			default=3025, 
	)








	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
			#required=True, 
			required=False, 
			)

	therapist = fields.Many2one(
			'openhealth.therapist',

			#string = "Terapeuta", 	
			string = "Cosmeatra", 	

			#required=True, 
			required=False, 
			)







	evaluation_start_date = fields.Date(

			string = "Fecha", 	
		
			#default = fields.Date.today, 
			required=True, 
			)



	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 

			#selection = jxvars._pathology_list, 
			selection = jxvars._chief_complaint_list, 

			required=True, 
			)


	evaluation_type = fields.Selection(
			selection = eval_vars.EVALUATION_TYPE, 
			string = 'Tipo',
			required=True, 
			)



	


	# Product
	product = fields.Many2one(
			'product.template',
			string="Producto",
			#required=True, 
			)
	





	laser = fields.Selection(
			#selection = jxvars._laser_type_list, 
			
			#selection = service_vars._laser_type_list, 
			selection = prodvars._laser_type_list, 
			
			string="Láser", 			
			compute='_compute_laser', 			
			)
	

	
	#@api.multi
	@api.depends('product')
	def _compute_laser(self):
		for record in self:
			record.laser = record.product.x_treatment 





	zone = fields.Selection(
			selection = jxvars._zone_list, 
			string="Zona", 			
			compute='_compute_zone', 			
			)
	
	#@api.multi
	@api.depends('product')
	def _compute_zone(self):
		for record in self:
			record.zone = record.product.x_zone




	# Completed
	x_done = fields.Boolean(
			default=False,
			string="Realizado", 			
		)








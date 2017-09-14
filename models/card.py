# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Card 
# 
# Created: 				25 Aug 2017
# Last updated: 	 	25 Aug 2017


from openerp import models, fields, api
from datetime import datetime



class card(models.Model):

	_name = 'openhealth.card'		
	#_inherit = 'oeh.medical.card'




	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)



	name = fields.Char(
			string="Tarjeta Vip #", 
			required=True, 
		)



	date_created = fields.Date(
			string = "Fecha de Creación",
			default = fields.Date.today, 
			#readonly = True, 
			required=True, 
		)






	patient_name = fields.Char(
			string = "Paciente nombre",
			default = "", 
			#readonly=True
			required=True, 
			)







	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			#required=True, 
			compute='_compute_patient', 

			#store=True, 
		)


	#@api.multi
	@api.depends('patient_name')

	def _compute_patient(self):
		for record in self:

			patient = record.env['oeh.medical.patient'].search([
															#('name','like', record.patient.name),
															#('name','like', record.patient),
															('name','=', record.patient_name),
														],
														#order='appointment_date desc',
														limit=1,)

			record.patient = patient

	# 









	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			#required=True, 
			compute='_compute_partner_id', 
		)


	#@api.multi
	@api.depends('patient_name')

	def _compute_partner_id(self):
		for record in self:

			partner_id = record.env['res.partner'].search([
															#('name','like', record.patient.name),
															#('name','like', record.patient),
															('name','=', record.patient_name),
														],
														#order='appointment_date desc',
														limit=1,)

			record.partner_id = partner_id

	# 







	date_product = fields.Date(
			string = "Fecha de Servicio",
			default = fields.Date.today, 
			#readonly = True, 
			#required=True, 
			required=False, 
		)

	product = fields.Char(
			string = "Servicio",
			default = "", 
			#readonly=True
			#required=True, 
			required=False, 
			)

	days_after = fields.Integer(
			string = "Días después",
			default = 0, 
			#readonly=True
			#required=True, 
			required=False, 
			)


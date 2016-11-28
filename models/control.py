# -*- coding: utf-8 -*-
#
# 	Control 	
# 

from openerp import models, fields, api

#from datetime import datetime
import datetime


import jxvars
import time_funcs




class Control(models.Model):
	_name = 'openhealth.control'
	_inherit = 'oeh.medical.evaluation'




	# Owner 
	owner_type = fields.Char(
			default = 'control',
		)





	# Appointments 

	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'control', 

			string = "Citas", 
			)





	name = fields.Char(
			string = 'Control #',
			)


	observation = fields.Text(
			string="Observación",
			size=200,
			required=True,
			)


	evaluation_next_date = fields.Date(
			string = "Fecha próximo control", 	
			#compute='_compute_evaluation_next_date', 
			required=True, 
			#default = fields.Date.today, 
			)

	
	#@api.multi
	#@api.depends('evaluation_start_date')
	#def _compute_evaluation_next_date(self):
	#	date_format = "%d days, 0:00:00"
	#	delta = datetime.timedelta(weeks=1)
	#	to = datetime.datetime.today()
	#	next_week = delta + to
	#	for record in self:
	#		record.evaluation_next_date = next_week



	@api.onchange('evaluation_start_date')
	def _onchange_evaluation_start_date(self):

		date_format = "%Y-%m-%d"
		delta = datetime.timedelta(weeks=1)
		#to = datetime.datetime.today()
		sd = datetime.datetime.strptime(self.evaluation_start_date, date_format)
		next_week = delta + sd

		self.evaluation_next_date = next_week

		#print
		#print 'onchange'
		#print self.evaluation_start_date
		#print sd 
		#print next_week
		#print 





	# Relational 

	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			
			
	


			

	# Open Appointment
	# -----------------
	@api.multi
	def open_appointment(self):  

		print 
		print 'open appointment'


		owner_id = self.id 
		owner_type = self.owner_type


		patient_id = self.patient.id
		doctor_id = self.doctor.id

		#treatment_id = self.treatment.id 
		treatment_id = self.procedure.treatment.id 



		GMT = time_funcs.Zone(0,False,'GMT')
		#appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		appointment_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#appointment_date = '2016-12-23'


		return {
				'type': 'ir.actions.act_window',

				'name': ' New Appointment', 
				
				'view_type': 'form',
				
				#'view_mode': 'form',			
				'view_mode': 'calendar',			
				
				'target': 'current',
				

				'res_model': 'oeh.medical.appointment',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_control': owner_id,

							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_x_type': owner_type,


							'default_appointment_date': appointment_date,
							}
				}





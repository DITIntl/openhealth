# -*- coding: utf-8 -*-
#
# 	Session 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars
import time_funcs




class Session(models.Model):
	_name = 'openhealth.session'
	_inherit = 'oeh.medical.evaluation'




	# Owner 
	owner_type = fields.Char(
			default = 'session',
		)

			
			


	# Appointments 

	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'session', 

			string = "Citas", 
			)




	name = fields.Char(
			string = 'Sesión #',
			)


	# Relational 

	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			






	#------------------------------------- Session ----------------------------------------


	# Calibration - Co2

	co2_power=fields.Float(
			string="Potencia (W)",
			)
	
	co2_frequency=fields.Float(
			string="Frecuencia (Hz)",
			)
	
	co2_energy=fields.Float(
			string="Energía de pulso (mJ)",
			)
	
	co2_mode_emission=fields.Char(
			string="Modo de emisión",
			)
	
	co2_mode_exposure=fields.Char(
			string="Modo de exposición",
			)
	
	co2_observations=fields.Text(
			string="Observaciones",
			)



	# Calibration - Excilite

	exc_time=fields.Float(
			string="Tiempo de tratamiento",
			)
			
	exc_dose=fields.Char(
			string="Dosis",
			)
			
	exc_dose_selected=fields.Float(
			string="Seleccionado (J/cm2)",
			)

	exc_dose_provided=fields.Float(
			string="Entregado (J/cm2)",
			)

	exc_observations=fields.Text(
			string="Observaciones",
			)



	# Calibration - Ipl

	ipl_fluency=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ipl_phototype=fields.Char(
			string="Fototipo",
			)
			
	ipl_lesion_type=fields.Char(
			string="Tipo de lesión",
			)
	
	ipl_lesion_depth=fields.Char(
			string="Profundidad de lesión",
			)
			
	ipl_pulse_type=fields.Selection(
			selection=jxvars._ipl_pulse_type,
			string="Tipo de pulso",
			)
			
	ipl_pulse_duration=fields.Char(
			string="Duración de pulso",
			)
			
	ipl_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
			)
			
	ipl_filter=fields.Char(
			string="Filtro",
			)
			
	ipl_spot=fields.Char(
			string="Spot",
			)
			
	ipl_observations=fields.Text(
			string="Observaciones",
			)

	
	
	# Calibration - Ndyag

	ndy_fluency=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ndy_phototype=fields.Char(
			string="Fototipo",
			)
			
	ndy_lesion_type=fields.Char(
			string="Tipo de lesión",
			)
			
			
	
	ndy_lesion_depth=fields.Char(
			string="Profundidad de lesión",
			)
			
	ndy_pulse_type=fields.Selection(
			selection=jxvars._ndyag_pulse_type,
			string="Tipo de pulso",
			)
			
	ndy_pulse_duration=fields.Char(
			string="Duración de pulso",
			)
			
			
			
	ndy_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
			)
			
	ndy_pulse_spot=fields.Selection(
			selection=jxvars._ndyag_pulse_spot,
			string="Spot",
			)
			
	ndy_observations=fields.Text(
			string="Observaciones",
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
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
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
							'default_session': owner_id,	

							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_x_type': owner_type,


							'default_appointment_date': appointment_date,
							}
				}


		
# -*- coding: utf-8 -*-
#
# 	Procedure 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Procedure(models.Model):
	_name = 'openhealth.procedure'
	_inherit = 'oeh.medical.evaluation'



	name = fields.Char(
			#string = 'Procedimiento #',
			string = 'Proc #',
			)








	# Redefinition 

	evaluation_type = fields.Selection(
			default = 'Ambulatory', 
			)



	# Relational 

	control_ids = fields.One2many(
			'openhealth.control', 
			'procedure', 
			string = "Controles", 
			)
			
	session_ids = fields.One2many(
			'openhealth.session', 
			'procedure', 
			string = "sessiones", 
			)

	treatment = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			)



	
	
	# Controls - Number

	nr_controls = fields.Integer(
			string="Controles",
			compute="_compute_nr_controls",
	)
	
	#@api.multi
	@api.depends('control_ids')

	def _compute_nr_controls(self):
		for record in self:
			ctr = 0 
			for c in record.control_ids:
				ctr = ctr + 1
			record.nr_controls = ctr		




	# Sessions - Number

	nr_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_nr_sessions",
	)
	
	#@api.multi
	@api.depends('session_ids')
	
	def _compute_nr_sessions(self):
		for record in self:
			ctr = 0 
			for c in record.session_ids:
				ctr = ctr + 1
			record.nr_sessions = ctr

	
	
	




	#------------------------------------ Buttons -----------------------------------------


	# Consultation - Quick Self Button  

	@api.multi

	def open_line_current(self):  

		procedure_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Consultation Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': procedure_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context':   {}
		}





	# Open Control 

	@api.multi

	def open_control(self):  

		procedure_id = self.id 

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		
		evaluation_type = 'Periodic Control'
		product_id = self.product.id
		laser = self.laser
		

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open control Current',


			# Optional 
			'res_model': 'openhealth.control',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_chief_complaint': chief_complaint,

				'default_procedure': procedure_id,
				'default_evaluation_type':evaluation_type,
								
				'default_product': product_id,
				'default_laser': laser,
				
			}
		}







	# Open Session  

	@api.multi

	def open_session(self):  

		procedure_id = self.id 

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		
		evaluation_type = 'Session'
		product_id = self.product.id
		laser = self.laser
		
		
		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open session Current',


			# Optional 
			'res_model': 'openhealth.session',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_chief_complaint': chief_complaint,

				'default_procedure': procedure_id,
				'default_evaluation_type':evaluation_type,
								
				'default_product': product_id,
				'default_laser': laser,
				
			}
		}



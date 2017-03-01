# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient 
# 
# Created: 				26 Aug 2016
# Last updated: 	 	20 Jan 2017

from openerp import models, fields, api
from datetime import datetime

import pat_funcs
import pat_vars


class Patient(models.Model):
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated

	_inherit = 'oeh.medical.patient'





# ----------------------------------------------------------- Autofill ------------------------------------------------------
	
	# Autofill

	x_autofill = fields.Boolean(
		string="Autofill",
		default=False, 
	)

	@api.onchange('x_autofill')
	
	def _onchange_x_autofill(self):

		if self.x_autofill == True:

			self.sex = 'Male'
			self.dob = '1965-05-26'
			self.x_dni = '09817194'
			self.email = 'tigroide55@gmail.com'
			self.phone_1 = '4760118'
			self.x_allergies = 'Ninguna'
			self.x_first_contact = 'recommendation'
			self.street = 'Av. San Borja Norte 610'
			self.street2_sel = 41

			#self.x_last_name = 'Fuchs Vibors'
			#self.x_first_name = 'Hans'
			#self.name = self.x_last_name + ' ' + self.x_first_name
			#self.street2 = 'San Borja'
			#self.zip = 41
			#self.city = 'Lima'
			#self.country_id = 175



# ----------------------------------------------------------- Relational ------------------------------------------------------


	treatment_ids = fields.One2many(
			'openhealth.treatment', 		
			'patient', 
			string="Tratamientos"
			)


	cosmetology_ids = fields.One2many(
			'openhealth.cosmetology', 		
			'patient', 
			string="Cosmiatrías"
			)







	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'patient', 
			
			string = "Citas", 
			)


# ----------------------------------------------------------- Re-definitions ------------------------------------------------------

	age = fields.Char(
			string = "Edad", 		
			)

	
	sex = fields.Selection(
			string="Sexo",

			required=True, 
			#required=False, 
		)


	dob = fields.Date(
			string="Fecha nacimiento",

			required=True, 
			#required=False, 
		)



	street = fields.Char(
			string = "Dirección", 	
			required=True, 
			#required=False, 
		)


	street2 = fields.Char(
			string = "Distrito", 	
			required=True, 
			#required=False, 
		)



	zip = fields.Integer(
			string = 'Código',  
			#compute='_compute_zip', 
			required=True, 			
			#required=False, 			
			)
	#@api.multi
	@api.depends('street2','city')

	def _compute_zip(self):
		for record in self:
			if (record.street2 in pat_vars.zip_dic) and (record.city == 'lima')  :
				record.zip=pat_vars.zip_dic[record.street2]
			else:
				record.zip=0



	email = fields.Char(
			string = 'email',  
			placeholder = '',

			required=True, 
			#required=False, 
			)

	country_id = fields.Many2one(
			'res.country', 
			string = 'País', 
			default = 175,	# Peru
			#required=False, 
			required=True, 
			)

	city = fields.Selection(
			selection = pat_vars._city_list, 
			string = 'Departamento',  
			default = 'lima', 
			required=True, 
			#required=False, 
		)

	phone_1 = fields.Char(
		string="Teléfono 1",
		required=True, 
		#required=False, 
		)


	# Phone 2
	phone_2 = fields.Char(
		string="Teléfono 2",
		required=False, 
		)



	phone_3 = fields.Char(
		string="Teléfono",
		required=False, 
		)


	street2_char = fields.Char(
			string = "Distrito", 	
			#required=True, 
		)


	street2_sel = fields.Selection(
			selection = pat_vars._street2_list, 
			string = "Distrito", 	
			#required=True, 
		)


	function = fields.Char(
			string = 'Ocupación',  
			placeholder = '',
			#required=True, 
			)





# ----------------------------------------------------------- New fields ------------------------------------------------------



	# Full name
	x_full_name = fields.Char(
		string = "Nombre completo",

		compute='_compute_full_name',
	)
	

	@api.depends('x_first_name', 'x_last_name')
	#@api.multi

	def _compute_full_name(self):
		for record in self:
			if record.x_first_name and record.x_last_name:				
				full = record.x_last_name.lower() + '_' + record.x_first_name.lower()
				full = full.replace (" ", "_")
				full = pat_funcs.strip_accents(full)
				record.x_full_name = full





	x_first_name = fields.Char(
		string = "Nombres", 	
		required=True, 
		default='',		
	)



	x_last_name = fields.Char(
		string = "Apellidos", 	
		required=True, 
		default='',	
	)



	x_date_created = fields.Date(
			string = "Fecha de apertura",
			default = fields.Date.today, 
			#readonly = True, 
			required=True, 
			)



	x_date_consent = fields.Date(
			string = "Fecha de consentimiento informado", 	
			default = fields.Date.today, 
			#readonly = True, 
			#required=True, 
			)



	x_active = fields.Boolean(
			string = "Activa", 	
			default = True, 
			#readonly = True, 
			required=True, 
			)



	x_dni = fields.Char(
			string = "DNI", 		
			required=True, 
			#required=False, 
			)



	x_allergies = fields.Char(
			string = "Alergias", 	
			required=True, 
			#required=False, 
			)



	x_first_contact = fields.Selection(
			selection = pat_vars._first_contact_list, 
			string = '¿ Cómo se enteró ?',
			#default = 'none', 			
			required=True, 
			#required=False, 
			)


	# Caregiver
	x_caregiver_last_name = fields.Char(
			string = 'Apellidos',
			#default = '', 
			#required=True, 
			)

	x_caregiver_first_name = fields.Char(
			string = 'Nombres',
			#default = '', 
			#required=True, 
			)

	x_caregiver_dni = fields.Char(
			string = "DNI", 	
			#required=True, 
			)

	x_caregiver_relation = fields.Selection(
			selection = pat_vars._FAMILY_RELATION, 		
			string = 'Parentesco',
			default = 'none', 
			#required=True, 
			)



	x_country_residence= fields.Many2one(
			'res.country', 
			string = 'País de residencia', 
			default = '', 
			#required=True, 
			)

	x_education_level= fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
			#default = 'university', 
			#required=True, 
			)



	# Control docs 

	x_control_dni_copy = fields.Boolean(
			string = 'Copia de DNI', 
			default = False 
			)

	x_control_informed_consent = fields.Boolean(
			string = 'Consentimiento informado', 
			default = False 
			)

	x_control_visia_record = fields.Boolean(
			string = 'Registro VISIA pre-procedimiento', 
			default = False 
			)

	x_control_photo_record = fields.Boolean(
			string = 'Registro fotográfico pre-procedimiento', 
			default = False 
			)

	x_control_treatment_signed_patient = fields.Boolean(
			string = 'Copia de información de tratamiento Láser firmada por el paciente', 
			default = False 
			)

	x_control_postlaser_instructions_signed = fields.Boolean(
			string = 'Copia de indicaciones post-Láser firmado por el paciente', 
			default = False 
			)

	x_control_treatment_signed_doctor = fields.Boolean(
			string = 'Informe de tratamiento Láser firmado por el doctor', 
			default = False 
			)

	x_control_clinical_analsis = fields.Boolean(
			string = 'Análisis clínicos', 
			default = False 
			)

	x_control_control_pictures = fields.Boolean(
			string = 'Fotos de controles', 
			default = False 
			)

	x_control_control_pictures_visia = fields.Boolean(
			string = 'Fotos de controles con VISIA', 
			default = False 
			)

	x_control_physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico responsable del control", 
			#required=True, 
			#index=True
			)







# ----------------------------------------------------------- On Changes ------------------------------------------------------



	# Last Name 
	@api.onchange('x_last_name', 'x_first_name')
	def _onchange_x_last_name(self):
		if self.x_last_name and self.x_first_name:
			self.name = pat_funcs.strip_accents(self.x_last_name.upper() + ' ' + self.x_first_name)



	# DNI 
	@api.onchange('x_dni')
	def _onchange_x_dni(self):
		ret = pat_funcs.test_for_digits(self, self.x_dni)
		if ret != 0: 
			return ret
		ret = pat_funcs.test_for_length(self, self.x_dni, 8)
		if ret != 0: 
			return ret



	# Phone 1
	@api.onchange('phone_1')
	def _onchange_phone_1(self):
		ret = pat_funcs.test_for_digits(self, self.phone_1)
		if ret != 0: 
			return ret



	# Phone 2
	@api.onchange('phone_2')
	def _onchange_phone_2(self):
		ret = pat_funcs.test_for_digits(self, self.phone_2)
		if ret != 0: 
			return ret



	# Phone 3 - Caregiver 
	@api.onchange('phone_3')
	def _onchange_phone_3(self):
		ret = pat_funcs.test_for_digits(self, self.phone_3)
		if ret != 0: 
			return ret



	@api.onchange('street2_sel')
	def _onchange_street2_sel(self):
		self.street2 = pat_vars.zip_dic_inv[self.street2_sel]
		self.zip = self.street2_sel



	@api.onchange('street2_char')
	def _onchange_street2_char(self):
		self.street2 = self.street2_char






# ----------------------------------------------------------- Computes ------------------------------------------------------



	# Treatment count  
	x_treatment_count = fields.Integer(
			compute='_compute_x_treatment_count',
			string = "Número de tratammientos",
			default = 0, 
			)

	@api.multi
	#@api.depends('x_allergies')
	def _compute_x_treatment_count(self):
		for record in self:
			#record.x_treatment_count = 5
			sub_total = 0 
			for tr in record.treatment_ids:   
				sub_total = sub_total + 1  
			record.x_treatment_count = sub_total  




	nr_treatments = fields.Integer(
			compute='_compute_nr_treatments',
			string = "Número de vacunas",
			default = 55, 
			)

	@api.multi
	def _compute_nr_treatements(self):
		for record in self:
			record.nr_treatments = 5  
			#record.x_nr_treatments = 5  
			#sub_total = 0 
			#for tr in record.treatment_ids:   
			#	sub_total = sub_total + 1  
			#record.x_nr_treatments= sub_total  











# ----------------------------------------------------------- Buttons Treatment ------------------------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def open_treatment_current(self):  

		print 
		print 'Open Treatment'
		patient_id = self.id 
		print patient_id

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',

			# Window action 
			'res_model': 'openhealth.treatment',

			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',

			'context':   {
				'search_default_patient': patient_id,
				'default_patient': patient_id,
			}
		}

	# open_treatment_current 








# ----------------------------------------------------------- Buttons Cosmetology ------------------------------------------------------


	# Button - Cosmetology 
	# -------------------
	@api.multi
	def open_cosmetology_current(self):  

		print 
		print 'Open Cosmetology'
		patient_id = self.id 
		print patient_id

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open cosmetology Current',


			# Window action 
			'res_model': 'openhealth.cosmetology',


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',

			'context':   {
				'search_default_patient': patient_id,
				'default_patient': patient_id,
			}
		}

	# open_cosmetology_current 









# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):

		print 
		#print 'jx: begin'
		print 'jx'
		print 'Patient - Create - Override'
		print 
		#print vals
		print 
	


		# Put your logic here 
		res = super(Patient, self).create(vals)
		# Put your logic here 



		# My logic 

		# Create a Treatment - When Patient is created
		name = vals['name']
		print 'name: ', name 
		patient_id = self.env['oeh.medical.patient'].search([('name', '=', name),]).id 
		print 'patient_id: ', patient_id

		treatment = self.env['openhealth.treatment'].create({'patient': patient_id,})

		#print 'jx: end '
		print 


		return res

	# CRUD - Create 


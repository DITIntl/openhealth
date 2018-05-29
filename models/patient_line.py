# -*- coding: utf-8 -*-
#
# 	Patient Line
# 
# Created: 				16 May 2018
#

from openerp import models, fields, api

import pat_vars


class PaitentLine(models.Model):
	
	_name = 'openhealth.patient.line'

	_order = 'date_create asc'





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
		)





# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Consus
	consu_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_consu_id',
		)



	# Sales
	sale_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_sale_id',
		)



	# Recommendations
	reco_line = fields.One2many(
			'openhealth.marketing.recom.line', 
			'patient_line_id',
			string="Recom.", 
		)



	# Procedures
	procedure_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id_proc',
		
			string="Procedimientos", 
		)



	# Vip Sales
	order_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id',
		)


	# Vip Sales - With Vip Card
	order_line_vip = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id_vip',
		)




# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date Created 
	date_create = fields.Datetime(
			string="Fecha de Creación", 
		)

	# Date Record 
	date_record = fields.Datetime(
			string="Fecha de Registro", 
			#string="Fecha creación", 
		)




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Nr lines Proc 
	nr_lines_proc = fields.Integer(
			'Nr Proc', 
			#default=-1, 
		)




	# Nr lines Vip 
	nr_lines_vip = fields.Integer(
			#'Ventas Usando la tarjeta Vip', 
			'Compras Con Tarjeta Vip', 
			default=-1, 
		)



	# Date Vip card 
	vip_date = fields.Datetime(
			string="Fecha Vip", 
		)


	# Marketing Id 
	marketing_id = fields.Many2one(
			#'openhealth.account.contasis'
			'openhealth.marketing', 

			ondelete='cascade', 
		)





	# Age 
	age = fields.Char(
			string = "Edad", 		
		)

	age_years = fields.Integer(
			string = "Edad", 		
			#default=0, 
			default=-1, 
		)

	dob = fields.Date(
			string="Fecha nacimiento",
			required=False, 
		)



	# Sex 
	sex = fields.Selection(
			selection = pat_vars._sex_type_list, 
			string="Sexo",
			#required=False, 
		)

	mea_m = fields.Integer(
			'M', 
		)

	mea_f = fields.Integer(
			'F', 
		)

	mea_u = fields.Integer(
			'U', 
		)



	# First Contact 
	first_contact = fields.Selection(

			selection = pat_vars._first_contact_list, 
		
			string = 'Primer contacto',
		)
	
	mea_recommendation = fields.Integer(
			'Pri Recomendación', 
		)

	mea_tv = fields.Integer(
			'Pri Tv', 
		)

	mea_radio = fields.Integer(
			'Pri Radio', 
		)

	mea_internet = fields.Integer(
			'Pri Internet', 
		)

	mea_website = fields.Integer(
			'Pri Website', 
		)

	mea_mail_campaign = fields.Integer(
			'Pri Mail', 
		)

	mea_how_none = fields.Integer(
			'Pri Ninguno', 
		)

	mea_how_u = fields.Integer(
			'Pri Ind', 
		)




	# Education 
	education = fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
		)

	mea_first = fields.Integer(
			'Edu Primaria', 
		)

	mea_second = fields.Integer(
			'Edu Secundaria', 
		)
	
	mea_technical = fields.Integer(
			'Edu Instituto', 
		)
	
	mea_university = fields.Integer(
			'Edu Universidad', 
		)
	
	mea_masterphd = fields.Integer(
			'Edu Posgrado', 
		)

	mea_edu_u = fields.Integer(
			'Edu Ind', 
		)
	




	# Vip 
	vip = fields.Boolean(
			string = 'Vip',
		)

	mea_vip = fields.Integer(
			'Vip', 
		)

	mea_vip_no = fields.Integer(
			'No Vip', 
		)





	# Address
	country = fields.Char(
			'Pais', 
		)

	city = fields.Char(
			'Ciudad', 
		)

	district = fields.Char(
			'Distrito', 
		)








# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  

		#print
		#print 'Update Fields - Patient'


		# Age 
		if self.age.split()[0] != 'No': 
			self.age_years = self.age.split()[0]
			ret = 1
		else:
			ret = -1



		# Places
		if self.city != False: 
			self.city = self.city.title()

		if self.district != False: 
			self.district = self.district.title()


		

		# Measures

		# Sex 
		if self.sex == 'Male': 
			self.mea_m = 1
		elif self.sex == 'Female':
			self.mea_f = 1
		else:
			self.mea_u = 1

		# Vip 
		if self.vip: 
			self.mea_vip = 1
		else: 
			self.mea_vip_no	= 1


		# Education
		if self.education == 'first': 
			self.mea_first = 1

		elif self.education == 'second': 
			self.mea_second = 1

		elif self.education == 'technical': 
			self.mea_technical = 1

		elif self.education == 'university': 
			self.mea_university = 1

		elif self.education == 'masterphd': 
			self.mea_masterphd = 1 

		else: 
			self.mea_edu_u = 1			


		# First Contact 
		if self.first_contact == 'recommendation': 
			self.mea_recommendation = 1

		elif self.first_contact == 'tv': 
			self.mea_tv = 1

		elif self.first_contact == 'radio': 
			self.mea_radio = 1

		elif self.first_contact == 'internet': 
			self.mea_internet = 1

		elif self.first_contact == 'website': 
			self.mea_website = 1

		elif self.first_contact == 'mail_campaign': 
			self.mea_mail_campaign = 1

		elif self.first_contact == 'none': 
			self.mea_how_none = 1

		else: 
			self.mea_how_u = 1

	
		return ret 

	# update_fields




	# Update fields Vip
	@api.multi
	def update_fields_vip(self):  
		
		#print 
		#print 'Update fields - Vip'
		

		# Nr Lines Vip 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_id_vip','=', self.id),
																			]) 
		self.nr_lines_vip = count

	# update_fields_vip




	# Update fields Proc
	@api.multi
	def update_fields_proc(self):  

		print 
		print 'Update fields - Proc'


		# Nr Lines proc 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_id_proc','=', self.id),
																			]) 
		self.nr_lines_proc = count

	# update_fields_proc




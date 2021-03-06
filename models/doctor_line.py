# -*- coding: utf-8 -*-
#
# 	Doctor Line 
# 
# Created: 				18 May 2018
#

from openerp import models, fields, api

import collections

import mgt_vars



class DoctorLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	_name = 'openhealth.management.doctor.line'
	
	_order = 'amount desc'




# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Sales
	order_line = fields.One2many(

			'openhealth.management.order.line', 
		
			'doctor_id',
		)


	# Family 
	family_line = fields.One2many(

			'openhealth.management.family.line', 
			
			'doctor_id',
		)


	# Sub family 
	sub_family_line = fields.One2many(

			'openhealth.management.sub_family.line', 
			
			'doctor_id',
		)





# ----------------------------------------------------------- Primitives ------------------------------------------------------
	# Nr
	nr_consultations = fields.Integer(
			'Nr Consultas', 
			default=0, 
		)

	nr_procedures = fields.Integer(
			'Nr Proc', 
			default=0, 
		)

	nr_procedures_co2 = fields.Integer(
			'Nr Proc Co2', 
			default=0, 
		)

	nr_procedures_quick = fields.Integer(
			'Nr Proc Quick', 
			default=0, 
		)



	nr_products = fields.Integer(
			'Nr Productos', 
			default=0, 
		)

	nr_medicals = fields.Integer(
			'Nr T Médicos', 
			default=0, 
		)





	# Ratios 
	ratio_pro_con = fields.Float(
			'Ratio %', 
		)

	ratio_pro_con_co2 = fields.Float(
			'Ratio Co2 %', 
		)

	ratio_pro_con_quick = fields.Float(
			'Ratio Quick %', 
		)





# ----------------------------------------------------------- Stats ------------------------------------------------------

	# Set Stats
	@api.multi
	def stats(self):  

		print 
		print 'Set Stats'
		print 


		# Using collections - More Abstract !


		# Clear 
		self.sub_family_line.unlink()
		self.family_line.unlink()


		print 
		print 


		# Init
		family_arr = []
		sub_family_arr = []
		self.nr_consultations = 0
		self.nr_procedures = 0
		self.nr_procedures_co2 = 0
		self.nr_procedures_quick = 0
		self.nr_products = 0
		self.nr_medicals = 0

		self.ratio_pro_con = 0
		self.ratio_pro_con_co2 = 0
		self.ratio_pro_con_quick = 0





		# Loop 
		for line in self.order_line: 

			# Family
			#family_arr.append( (line.family, line.price_total)  )
			family_arr.append(line.family)


			# Sub family
			sub_family_arr.append(line.sub_family)




		
		# Count and Create 

		print 'Count and Create'
		print 

		# Family 

		counter_family = collections.Counter(family_arr)


		for key in counter_family: 

			count = counter_family[key]

			print key 
			print count

			family = self.family_line.create({
												#'name': mgt_vars._h_family_sp[key], 
												'name': key, 
												'x_count': count, 
												'doctor_id': self.id, 
											})

			family.update_fields()


			# Ratios 
			if key == 'consultation': 
				self.nr_consultations = count
			
			elif key == 'procedure': 			
				self.nr_procedures = count

			elif key == 'product': 
				self.nr_products = count

			elif key == 'medical': 
				self.nr_medicals = count




		# Subfamily 

		counter_sub_family = collections.Counter(sub_family_arr)

		for key in counter_sub_family: 

			count = counter_sub_family[key]

			sub_family = self.sub_family_line.create({
														'name': key, 
														'x_count': count, 
														'doctor_id': self.id, 
												})

			sub_family.update_fields()


			# Ratios 
			if key == 'laser_co2': 
				self.nr_procedures_co2 = count
			elif key == 'laser_quick': 			
				self.nr_procedures_quick = count






		# Amounts 

		print
		print 'Amounts'
		print 

		# Family 
		for family in self.family_line: 
			
			amount = 0 

			orders = self.env['openhealth.management.order.line'].search([
																			('family', '=', family.name),
																			('doctor_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)

			for order in orders: 
				amount = amount + order.price_total


			family.amount = amount

			print family.name 
			print amount
			#print orders
			print 



		# Sub Family 
		for sub_family in self.sub_family_line: 
			
			amount = 0 

			orders = self.env['openhealth.management.order.line'].search([
																			('sub_family', '=', sub_family.name),
																			('doctor_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)

			for order in orders: 
				amount = amount + order.price_total


			sub_family.amount = amount

			print sub_family.name 
			print amount
			#print orders
			print 



		self.update_fields()

	# set_stats




# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  

		print 
		print 'Update Fields'


		# Names 
		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name



		# Ratios

		if self.nr_consultations != 0: 
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100 

			self.ratio_pro_con_co2 = (float(self.nr_procedures_co2) / float(self.nr_consultations)) * 100 

			self.ratio_pro_con_quick = (float(self.nr_procedures_quick) / float(self.nr_consultations)) * 100 


	# update_fields



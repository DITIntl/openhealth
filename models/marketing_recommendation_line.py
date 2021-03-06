# -*- coding: utf-8 -*-
#
#
# 	Marketing Recommendation Line 
# 

from openerp import models, fields, api
import prodvars


class marketing_recommendation_line(models.Model):


	_inherit='openhealth.medical'

	_name = 'openhealth.marketing.recom.line'

	_description = "Openhealth Marketing Recommendation Line"






# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Prices
	
	price = fields.Float(
			string='Precio Standard', 
		) 

	price_vip = fields.Float(
			string='Precio VIP', 
		) 

	price_manual = fields.Float(
			string="Precio Manual",
		)

	price_applied = fields.Float(
			string='Precio Aplicado', 
		) 






# ----------------------------------------------------------- Handles ------------------------------------------------------
	
	# Patient Line
	patient_line_id = fields.Many2one(
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



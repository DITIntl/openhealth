# -*- coding: utf-8 -*-
#
# 	Service Excilite 
# 

from openerp import models, fields, api
from datetime import datetime


from . import exc




class ServiceExcilite(models.Model):
	_name = 'openhealth.service.excilite'
	_inherit = 'openhealth.service'
	
	

	
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_excilite'),
					],
	)
	
	


	

# ----------------------------------------------------------- Variables ------------------------------------------------------

	psoriasis = fields.Selection(
			selection = exc._psoriasis_list, 
			string="Psoriasis", 
			default='none',	
			)

	vitiligo = fields.Selection(
			selection = exc._vitiligo_list, 
			string="Vitiligo", 
			default='none',	
			)
		
	alopecias = fields.Selection(
			selection = exc._alopecias_list, 
			string="Alopecias", 
			default='none',	
			)
	


# ----------------------------------------------------------- On changes ------------------------------------------------------

	@api.onchange('vitiligo')
	def _onchange_vitiligo(self):
	
		if self.vitiligo != 'none':	
			self.vitiligo = self.clear_all(self.vitiligo)

			self.zone = self.vitiligo
			self.pathology = 'vitiligo'
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}

	@api.onchange('psoriasis')
	def _onchange_psoriasis(self):
	
		if self.psoriasis != 'none':	
			self.psoriasis = self.clear_all(self.psoriasis)

			self.zone = self.psoriasis
			self.pathology = 'psoriasis'
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
	@api.onchange('alopecias')
	def _onchange_alopecias(self):
	
		if self.alopecias != 'none':	
			
			self.alopecias = self.clear_all(self.alopecias)

			self.zone = self.alopecias
			self.pathology = 'alopecia'
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			

# ----------------------------------------------------------- Functions ------------------------------------------------------
		
	@api.multi
	def clear_local(self):
	
		# First
		self.vitiligo = 'none'
		self.psoriasis = 'none'
		self.alopecias = 'none'
		
		
		# Times
		self.time = ''
		self.time_1 = 'none'
		#self.clear_common_times
		
		


# ServiceExcilite

	
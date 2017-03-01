# -*- coding: utf-8 -*-
#
# 	*** Session Med
#

# Created: 				 24 Feb 2017
# Last updated: 	 	 24 Feb 2017 



from openerp import models, fields, api
from datetime import datetime

import jxvars
#import cosvars

import time_funcs
import jrfuncs
#import session_funcs



class SessionMed(models.Model):
	
	_name = 'openhealth.session.med'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.session'











	#------------------------------------------------------ Session Med ----------------------------------------------------------


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
			default="x",
			)
	
	co2_mode_exposure=fields.Char(
			string="Modo de exposición",
			default="x",
			)
	
	co2_observations=fields.Text(
			string="Observaciones",
			default="x",
			)





	# Calibration - Excilite

	exc_time=fields.Float(
			#string="Tiempo de tratamiento",
			#required=True, 
			)
			
	exc_dose=fields.Char(
			string="Dosis",
			#default="x",
			#required=True, 
			)
			
	exc_dose_selected=fields.Float(
			#string="Seleccionado (J/cm2)",
			#required=True, 
			)

	exc_dose_provided=fields.Float(
			#string="Entregado (J/cm2)",
			#required=True, 
			)

	exc_observations=fields.Text(
			string="Observaciones",
			#default="x",
			#required=True, 
			)





	# Calibration - Ipl

	ipl_fluency=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ipl_phototype=fields.Char(
			string="Fototipo",
			#required=True, 
			)
			
	ipl_lesion_type=fields.Char(
			string="Tipo de lesión",
			#required=True, 
			)
	
	ipl_lesion_depth=fields.Char(
			string="Profundidad de lesión",
			#required=True, 
			)
			
	ipl_pulse_type=fields.Selection(
			selection=jxvars._ipl_pulse_type,
			string="Tipo de pulso",
			#required=True, 
			)
			
	ipl_pulse_duration=fields.Char(
			string="Duración de pulso",
			#required=True, 
			)
			
	ipl_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
			#required=True, 
			)
			
	ipl_filter=fields.Char(
			string="Filtro",
			#required=True, 
			)
			
	ipl_spot=fields.Char(
			string="Spot",
			#required=True, 
			)
			
	ipl_observations=fields.Text(
			string="Observaciones",
			#required=True, 
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




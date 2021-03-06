# -*- coding: utf-8 -*-
#
# 	Account Line
# 
# Created: 				18 April 2018
#

from openerp import models, fields, api

import datetime
import acc_funcs


class AccountLine(models.Model):
	
	#_inherit='sale.closing'
	_name = 'openhealth.account.line'

	_order = 'date_time asc'
	#_order = 'tipodocumento,numerofactura asc'







# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date 
	date = fields.Date(
			#string="Fecha", 
		)

	# Datetime 
	date_time = fields.Datetime(
			string="Fecha y hora", 
		)





	# Corr 
	date_time_corr = fields.Datetime(
			#string="Fecha", 
		)


	# Date 
	date_char = fields.Char(
			string="Fecha", 
		)

	# Time 
	time_char = fields.Char(
			string="Hora", 
		)






# ----------------------------------------------------------- Relational ------------------------------------------------------

	account_id = fields.Many2one(
			'openhealth.account.contasis'
		)





# ----------------------------------------------------------- Contasis ------------------------------------------------------


	# Fechas 
	fecha = fields.Char(
			'fecha', 
		)

	fechavencimiento = fields.Char(
			'fechavencimiento', 
		)





	# Comprobante de pago 
	tipodocumento = fields.Char(
			'tipodocumento', 
		)

	numeroserie = fields.Char(
			'numeroserie', 
		)

	numerofactura = fields.Char(
			'numerofactura', 
		)










	# Documento de identidad
	tipodoc = fields.Char(
			'tipodoc', 
		)

	numdoc = fields.Char(
			'numdoc', 
		)




	# Name 
	nombre = fields.Char(
			'nombre', 
		)







	# Exportacion
	EXPortacion = fields.Char(
			'EXPortacion', 
			default='0', 
		)




	# Importe
	neto = fields.Char(
			'neto', 
		)


	exonerado = fields.Char(
			'exonerado', 
			default='0', 
		)

	inafecto = fields.Char(
			'inafecto', 
			default='0', 
		)





	isc = fields.Char(
			'isc', 
			default='0', 
		)

	igv = fields.Char(
			'igv', 
		)

	otros = fields.Char(
			'otros', 
			default='0', 
		)




	total = fields.Char(
			'total', 
		)

	tipocambio = fields.Char(
			'tipocambio', 
			default='3.3', 
		)







	# Referencia modificada
	fechar = fields.Char(
			'fechar', 
		)

	tipor = fields.Char(
			'tipor', 
		)

	serier = fields.Char(
			'serier', 
		)

	numr = fields.Char(
			'numr', 
		)




	moneda = fields.Char(
			'moneda', 
			default='S', 
		)

	dolares = fields.Char(
			'dolares', 
			default='0', 
		)

	fechavencimiento2 = fields.Char(
			'fechavencimiento2', 
		)

	condicion = fields.Char(
			'condicion', 
			default='CON', 
		)

	ccosto = fields.Char(
			'ccosto', 
		)

	ccosto2 = fields.Char(
			'ccosto2', 
		)






	cuentab = fields.Char(
			'cuentab', 
			#default='701101001', 
		)

	cuentao = fields.Char(
			'cuentao', 
			#default='CON', 
		)

	cuentacontable = fields.Char(
			'cuentacontable', 
			default='121210001', 
		)






	regimen = fields.Char(
			'regimen', 
			default='0', 
		)

	porcen = fields.Char(
			'porcen', 
			default='0', 
		)

	importer = fields.Char(
			'importer', 
			default='0', 
		)





	seried = fields.Char(
			'seried', 
			#default='0', 
		)

	numdocr = fields.Char(
			'numdocr', 
			#default='CON', 
		)

	fechad = fields.Char(
			'fechad', 
			#default='CON', 
		)

	codigop = fields.Char(
			'codigop', 
			#default='CON', 
		)





	porigv = fields.Char(
			'porigv', 
			#default='CON', 
		)

	glosa = fields.Char(
			'glosa', 
			default='POR VENTA DE 01-', 
		)





	mediop = fields.Char(
			'mediop', 
			#default='CON', 
		)

	comd = fields.Char(
			'comd', 
			#default='CON', 
		)

	importec = fields.Char(
			'importec', 
			default='0', 
		)







# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  

		#print
		#print 'Update Contasis'




		# Dates 
		self.date_time_corr, date_time_str = acc_funcs.correct_time(self,self.date_time, -5)

		self.date_char = date_time_str.split()[0]
		self.time_char = date_time_str.split()[1]

		self.fecha = self.date_char
		self.fechavencimiento  = self.date_char
		self.fechavencimiento2 = self.date_char





		# Product
		self.product_type = self.product.type 
		self.cuentab = acc_funcs._cuentab[self.product_type]



		# Name 
		if self.x_type in ['invoice', 'ticket_invoice']:			# Ruc
			self.nombre = self.patient.x_firm 

			#doc_type = '6'

		else: 														
			self.nombre = self.patient.name 

			#if self.patient.x_dni != False: 		# Dni 
			#	doc_type = '1'
			#else: 
			#	doc_type = acc_funcs._doc_type[self.patient.x_id_doc_type]





		# Id Doc 
		self.tipodoc = self.document_type
		self.numdoc = self.document





		# Serial number 
		if self.serial_nr != False: 
			self.numeroserie = self.serial_nr.split('-')[0]
			self.numerofactura = self.serial_nr.split('-')[1]

			self.glosa = self.glosa + self.serial_nr




		self.tipodocumento = acc_funcs._h_type[self.x_type]









		

		# Dates	- Must be converteed to a datetime object, before converting to the proper format. 
		#DATETIME_FORMAT = "%Y-%m-%d"
		#self.fecha  = datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%d/%m/%Y')
		#self.fechavencimiento  = datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%d/%m/%Y')
		#self.fechavencimiento2 = self.fechavencimiento


		# Month 
		#self.cuo_mes =  datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%m')


		# Constants 
		#self.EXPortacion = '0.00'
		#self.exonerad = '0.00'
		#self.inafecto = '0.00'
		#self.isc = '0.00'
		#self.otros = '0.00'
		#self.tipor = '00'
		#self.tipocambio = '3.2100'






		# Actual amount
		if self.state == 'cancel': 

			self.amount = 0
			self.amount_net = 0
			self.amount_tax = 0

			#self.total = 0
			#self.neto = 0 
			#self.igv = 0 
			#self.porigv = 0

		else: 

			#self.amount_net = self.amount/1.18
			net = self.amount/1.18
			self.amount_net = round(net, 2)
			

			#self.amount_tax = self.amount_net * 0.18
			tax = net * 0.18
			self.amount_tax = round(tax, 2)



			#self.total = self.amount
			#self.neto = self.amount_net 
			#self.igv = self.amount_tax 			
			#self.porigv = self.igv

			#self.neto = str(float(self.amount)/1.18)
			#self.igv = str(float(self.neto) * 0.18)


		self.total = self.amount
		self.neto = self.amount_net 
		self.igv = self.amount_tax 			
		self.porigv = self.igv





# ----------------------------------------------------------- Meta ------------------------------------------------------


	name = fields.Char(
			'Nr', 
		)


	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Nombre", 
		)




	#qty = fields.Float(
	qty = fields.Integer(
			string="Cantidad", 
		)


	product = fields.Many2one(
			'product.product', 
			string="Producto", 
		)

	product_type = fields.Selection(
			[	('service', 			'Servicio'),
				('product', 			'Producto'),
				('consu', 				'Consumible'),
			], 
			string='Tipo Prod', 
			#required=False,
		)




	state = fields.Selection(
			[	('sale', 			'Venta'),
				('cancel', 			'Anulado'),
			], 
			string='Estado', 
			#required=False,
		)


	serial_nr = fields.Char(
			string="Nr. de serie", 
		)


	x_type = fields.Selection(
			[	('receipt', 			'Boleta'),
				('invoice', 			'Factura'),
				('advertisement', 		'Canje Publicidad'),
				('sale_note', 			'Canje NV'),
				('ticket_receipt', 		'Ticket Boleta'),
				('ticket_invoice', 		'Ticket Factura'),	], 

			string='Tipo', 
			
			#required=False,
		)









	# Id Document 
	document = fields.Char(
			string="Documento", 
		)

	document_type = fields.Char(
			string="Tipo Documento", 
		)



	# Amount 
	amount = fields.Float(
			string="Total", 
		)

	amount_net = fields.Float(
			string="Neto", 
		)

	amount_tax = fields.Float(
			string="Impuesto", 
		)







# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	
	# Codigo Unico Ope
	#cuo_mes = fields.Char(
	#		'MES', 
	#	)


	#cuo_sd = fields.Char(
	#		'SD', 
	#	)

	#cuo_asi = fields.Char(
	#		'ASI', 
	#	)


		#self.cuo_asi = 
		#self.cuo_sd = '02'



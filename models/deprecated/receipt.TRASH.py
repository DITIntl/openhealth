

# 6 Feb 2018




	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Receipt - Create Override'
		#print 
		#print vals
		#print 
	



		# Counter - Deprecated 
		#counter = self.env['openhealth.counter'].search([('name', '=', 'receipt')])
		#vals['serial_nr'] = counter.total
		#counter.increase()




		#Write your logic here
		res = super(Receipt, self).create(vals)
		#res = super(family.capitalize(), self).create(vals)
		#Write your logic here

		return res


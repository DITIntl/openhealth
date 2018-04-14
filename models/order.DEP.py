



# ----------------------------------------------------------- Test and Hunt ------------------------------------------------------
	# Test Bug 
	#@api.multi 
	#def test_bug(self):
	#	print 'jx'
	#	print 'Test and Hunt !'
	#	target_line = 'quick_body_local_cyst_2'
	#	print target_line
	#	ret = self.x_create_order_lines_target(target_line)
	#	print ret  



# ----------------------------------------------------------- Validate Stock Picking ------------------------------------------------------

	@api.multi 
	def do_transfer(self):
		print 'jx'
		print 'Do Transfer'
		print self.picking_ids
		for pick in self.picking_ids: 
			ret = pick.do_transfer()
			print ret


	# From Action confirm 
	@api.multi 
	def validate_stock_picking(self):
		print 'jx'
		print 'Validate Stock Picking'
		print self.picking_ids
		for pick in self.picking_ids: 
			print pick
			print pick.name 
			ret = pick.force_assign()
			print ret







# ----------------------------------------------------------- Buttons - Order  ------------------------------------------------------

	@api.multi
	def remove_myself(self):  
		self.x_reset()
		self.unlink()





# ----------------------------------------------------------- Nr Mac Clones  ------------------------------------------------------

	@api.multi 
	def get_nr_mc(self):
		nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([
																			('appointment_date','=', self.x_appointment.appointment_date),													
																			('x_machine','=', self.x_appointment.x_machine),
																		]) 
		return nr_mac_clones










	# Open Cosmetology
	#@api.multi 
	#def open_cosmetology(self):
		#print 
		#print 'Open cosmetology'
	#	ret = self.cosmetology.open_myself()
	#	return ret 
	# open_cosmetology






	# Open Treatment
	@api.multi 
	def open_treatment(self):

		if self.treatment.name != False:
			ret = self.treatment.open_myself()
		elif self.cosmetology.name != False:
			ret = self.cosmetology.open_myself()
		else:
			#print 'This should not happen !'
			ret = 0 

		return ret 







	# Default Doctor
	@api.multi
	def _get_default_doctor(self): 
		name = 'Clinica Chavarri'
		doctor = self.env['oeh.medical.physician'].search([
																		('name', '=', name),			
																	],
																	#order='start_date desc',
																	limit=1,
																)
		return doctor.id 




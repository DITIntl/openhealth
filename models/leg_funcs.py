# -*- coding: utf-8 -*-
#
# 	*** Leg Funcs
# 
# Created: 				 26 Feb 2017
# Last updated: 	 	 id

from openerp import models, fields, api

#from datetime import timedelta
import datetime





#------------------------------------------------ Functions ---------------------------------------------------

def create_patient(self, name, hc_code, doc_code, sex, 		date_record, date_created, date_birth, 		address, district, phone, mobile, email, comment):


	_hac = {
				'F': 				'Female', 
				'M': 				'Male', 
			}


	sex_h = _hac[sex]



	ret = self.env['oeh.medical.patient'].create({

															'name': name,

															'x_id_code': hc_code,

															'x_dni': doc_code,

															'sex': sex_h,



															'x_date_record': date_record,

															'x_date_created': date_created,
															
															'x_datetime_created': date_created,

															'dob': date_birth,



															'street': address,

															'x_district': district,

															'phone': phone,

															'mobile': mobile,

															'email': email,


															'comment': comment,

													})

	print ret 





def correct_time(self, date):

	#print 'jx'
	#print 'Correct'
	#print date 



	#if date != False  and  year >= 1900:
	if date != False: 


		#1876-10-10 00:00:00
		year = int(date.split('-')[0])
		#print year 


		if year >= 1900:


			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


			date_field1 = datetime.datetime.strptime(date, DATETIME_FORMAT)


			date_corr = date_field1 + datetime.timedelta(hours=+5,minutes=0)


			return date_corr




def get_date_from_char(self, date_char):

	#print 'jx'
	#print 'Get date from c'
	#print date_char



	if date_char != False: 


		a = date_char


		e = a.split()

		#b = a.split('/')
		b = e[0].split('/')


		#c = b[2] + '-' + b[1] + '-' + b[0] #+ ' ' + e[1]
		#c = b[2].zfill(4) + '-' + b[1].zfill(2) + '-' + b[0].zfill(2) 
		c = b[2].zfill(4) + '-' + b[1].zfill(2) + '-' + b[0].zfill(2) + ' ' + e[1]
	 	

		#c = c +  timedelta(hour=5)

	 	#+ ' ' + e[1]
		#.zfill()



		#date_d = date_char
		date_d = c


		#print date_d
		return date_d

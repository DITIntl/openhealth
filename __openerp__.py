# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
#

{
    'name': "openHealth",

    'summary': """
		Extension for Odoo-oeHealth. 
		Treatments. 
	""",

    'description': """

		Installed: 	 7 Sep 2016.\n 
		Upgraded: 	 12 Oct 2016.\n 
		\n

		This is my first extension for oeHealth.
		Completely independent and self-referecing.\n
		It provides the following objects:
            - Patients
            - Treatments
            - Evaluations
            - Consultations
            - Procedures
            - Controls 
            - Services
    """,

    'author': "DataMetrics",
	'website': "http://javier-revilla.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health',
    'version': '1.0',


    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['base', 'oehealth'],
    #'depends': ['base', 'oehealth', 'openextension'],
    #'depends': ['base', 'openextension'],




    # always loaded
    'data': [

		'views/openhealth.xml',

        
        # Generated
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
		
        
		
		# Consultation
		'views/evaluations/consultation.xml',
		'views/evaluations/consultation_first.xml',

		'views/evaluations/consultation_services_co2.xml',
		'views/evaluations/consultation_services_excilite.xml',
		'views/evaluations/consultation_services_ipl.xml',
		'views/evaluations/consultation_services_ndyag.xml',



		'views/evaluations/consultation_services.xml',
		'views/evaluations/consultation_order.xml',
		#'views/evaluations/consultation_order_lines.xml',


		#'views/evaluations/consultation_procedures.xml',
		
		
		
		
		
        # Learning 
        #'views/learning/learn.xml',




		
		
		
		# Services
		'views/services/service.xml',
		
		'views/services/service_co2.xml',
		'views/services/service_co2_zone.xml',

		'views/services/service_excilite.xml',
		'views/services/service_excilite_zone.xml',

		'views/services/service_ipl.xml',
		'views/services/service_ipl_zone.xml',
		
		'views/services/service_ndyag.xml',
		'views/services/service_ndyag_zone.xml',


		# Orders
		#'views/evaluations/order.xml',
		'views/orders/order.xml',


		


		# Invoices
		#'views/treatments/invoice.xml',

		
        # Patients 
        'views/patients/patient.xml',
		'views/patients/patient_personal.xml',
		'views/patients/patient_treatments.xml',
		'views/patients/patient_control_docs.xml',
		
        #'views/patients/patient_lab.xml',
		#'views/patients/patient_med.xml',



        # Evaluations
		#'views/evaluations/evaluation.xml',
		'views/evaluations/evaluation_oeh.xml',
		



		# jx_eval
		#'views/evaluations/jx_eval_co2.xml',
		#'views/evaluations/jx_eval_excilite.xml',
		#'views/evaluations/jx_eval_ipl.xml',
		#'views/evaluations/jx_eval_ndyag.xml',



		
        #'views/evaluations/consultation_quotation.xml',        
		#'views/evaluations/quotation.xml',

        
		'views/evaluations/procedure.xml',


        # Treatments 
		'views/treatments/treatment.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
	
	
	
	# Static - jx 
	#'js': ['static/src/js/widget_radio.js'],
	#'qweb': ['static/src/xml/widget_radio.xml'],
    #'css': ['static/src/css/my_css.css'],
	'css': ['static/src/css/jx.css'],
	
	
}

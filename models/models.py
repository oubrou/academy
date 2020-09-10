# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char('Nom',required=True)
    lastname= fields.Char('Prénom',required=True)
    name_ar = fields.Char('الإسم العائلي ')
    lastname_ar= fields.Char('الإسم الشخصي')
    birth_day= fields.Date(string="Date de naissance")
    card_number=fields.Char('CIN')
    birthplace = fields.Char('Lieu de naissance')
    image = fields.Binary('Photo',attachment=True)
    biography = fields.Html()
    state= fields.Selection([('A','A'),('B','B'),('C','C')],'State',default='A')
    taille = fields.Integer('Taille')
	
    _sql_constraints = [
	    ('name_unique',
         'UNIQUE(name)',
         'The name must be unique sql constraint'),
        ('card_number_unique',
         'unique(card_number)',
         "The card number must be unique sql constraint")
    ]
	 
    @api.onchange('taille')
    def taille_changed(self):
        if self.taille < 170:
            return{
			     'warning':{
				            'title':'Attention',
							'message':'Votre taille est inférieur a la taille demandé',
				 
				 },
				 }
				      
    def btn_submit_to_b(self):
        self.write({'state':'B'})		
    def btn_submit_to_c(self):
        self.write({'state':'C'})
    def btn_submit_to_a(self):
        self.write({'state':'A'})
    def btn_sent_email(self):
	    return {
			     'warning':{
				            'title':'',
							'message':'Your message has ben sent succesfully',
				 
				 },
				 }		
   





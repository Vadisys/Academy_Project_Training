# _*_ coding : utf-8 _*_ 

from odoo import models, fields, api

class Course(models.Model):

    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.char(string='Title', required = True)
    description = fields.text(string='Description')
    
    level = fields.Selection( string= 'Level',
                            
                            selection = [ ('begineer', 'Begineer'), 
                                          ('intermediate', 'Intermediate'),
                                          ('advnanced', 'Advanced') ],
                             copy = False )
    
    active = fields.Boolean(string= 'Active', defaults = True)
    
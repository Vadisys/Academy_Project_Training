# _*_ coding : utf-8 _*_

from odoo import models, fields, api

class Spaceship(models.Model):
        
    _name = 'spaceship.mission'
    _description = 'Spaceship Information'
   
    ship_dimention = fields.Float (string='Ship Dimension', default=0.00)
    fuel_type = fields.Selection (string= 'Fuel Type',
                                 selection = [ ('solid' 'Solid'),
                                               ('liquid', 'Liquid'),
                                               ('solar', 'Solar') ],
                                            
                                 copy=False)
    ship_type = fields.Selection (string ='Ship Type',
                                  selection = [ ('flyby', 'Flyby') ,
                                               ('orbiter', 'Orbiter'),
                                               ('atmospheric','Atmospheric'),
                                               ('lander','Lander'),
                                               ('rover', 'Rover'),
                                               ('observatory', 'Observatory') ],
                                 
                                 copy=False)                                    
                                            
                                              
    no_passenger  = fields.Integer (string='Number of Passengers', default=0)
    sapce_crew = fields.Char (string='Space Crew', required=True)
    active = fields.Boolean (string= 'Active', required=True)
    

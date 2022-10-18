# _*_ coding : utf-8 _*_

from odoo import models, fields, api

class Spaceship(models.Model):
        
    _name = 'spaceship.mission'
    _description = 'Spaceship Information'
   
    ship_dimention = fields.Integer (string='Ship Dimension', required=True)
    fuel_type = fields.Selection (string= 'Fuel Type',
                                 selection = [ ('solid' 'Solid'),
                                               ('liquid', 'Liquid'),
                                               ('solar', 'Solar') ]
                                            
                                 )
    ship_type = fields.Selection (string ='Ship Type',
                                  slection = [ ('flyby', 'Flyby') ,
                                               ('orbiter', 'Orbiter'),
                                               ('atmospheric','Atmospheric'),
                                               ('lander','Lander'),
                                               ('rover', 'Rover'),
                                               ('observatory', 'Observatory') ]
                                 
                                 )                                    
                                            
                                              
    no_passenger  = fields.Integer (string='Number of Passengers', required= True)
    sapce_crew = fields.Char (string='Space Crew', required=True)
    active = fields.Boolean (string= 'Active', required=True)
    

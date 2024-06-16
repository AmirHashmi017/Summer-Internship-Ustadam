from odoo import fields, models

class estate_property_pictures(models.Model):
    _name = "estate.property.pictures"
    image = fields.Image("Property Image")
    property_id = fields.Many2one("estate.property")
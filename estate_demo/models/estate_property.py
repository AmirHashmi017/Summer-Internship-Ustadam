from odoo import fields, models

class estate_property(models.Model):
    _name = "estate.property"
    _description = "will hold porperty info"
    name = fields.Char("Property Name", required=True, translate=True)
    expected_price = fields.Float("Asking Price", required=True)
    primary_image = fields.Image("Primary Image")
    active = fields.Boolean("Active", default=True)
    sequence = fields.Integer("Sequence", default=10)   
    owner_id = fields.Many2one(comodel_name="res.users")
    email = fields.Char("Email")
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    pictures = fields.One2many("estate.property.pictures", "property_id")
    active_date = fields.Date("Property Active Date")
    property_tags_ids=fields.Many2many('estate.property.tags')
from odoo import models,fields
class estate_property_tags(models.Model):
    _name="estate.property.tags"
    _description="this table shall hold the tags of a property"
    name=fields.Char(string='Tag Name')
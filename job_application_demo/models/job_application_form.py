from odoo import fields, models

class job_application_form(models.Model):
    _name = "job.application.form"
    _description = "will hold applicant info"
    name = fields.Char("Applicant Name", required=True, translate=True)
    email = fields.Char("Email", required=True)
    phone_number = fields.Char("Phone", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", required=True)
    birth_date = fields.Date("Date Of Birth",required=True)
    cnic = fields.Char("CNIC", required=True)
    highest_degree = fields.Char("Top Academic Qualification", required=True)
    primary_image = fields.Image("Applicant Image", required=True)
    resume = fields.Binary("Resume", required=True)
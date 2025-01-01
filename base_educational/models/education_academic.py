from odoo import api, models, fields

class EducationAcademic(models.Model):
    _name = 'education.academic'
    _description = 'Academic Year'

    name = fields.Char(string='Name', required=True, help='Name of academic year')
    ay_code = fields.Char(string='Code', required=True, help='Code of academic year')
    sequence = fields.Integer(string='Sequence', required=True)
    ay_start_date = fields.Date(string='Start Date', required=True, help='Starting date of academic year.')
    ay_end_date = fields.Date(string='End Date', required=True, help='Ending date of academic year.')
    description = fields.Text(string='Description', help='Description about the academic year.')
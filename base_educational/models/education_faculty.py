from odoo import api, fields, models



class EducationFaculty(models.Model):
    _name = 'education.faculty'
    _description = 'Faculty Record'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='First Name', required=True, help='Enter The First Name.')
    last_name = fields.Char(string='Last Name', required=True, help='Enter The Last Name.')
    faculty_id = fields.Char(string='ID', readonly=True)
    image = fields.Binary(string='Image', attachment=True)
    email = fields.Char(string='Email', help='Enter the email for contact purpose.')
    phone = fields.Char(string='Phone', help='Enter the phone for contact purpose.')
    mobile = fields.Char(string='Mobile', help='Enter the mobile for contact purpose.')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender', required=True, default='male',track_visibility='onchange')
    date_of_birth = fields.Date(string='Date of Birth')
    father_name = fields.Char(string='Father Name', help='Your father name is...')
    mother_name = fields.Char(string='Mother Name', help='Your mother name is...')
    blood_group = fields.Selection([('a+','A+'),
                                    ('a+','A+'),
                                    ('a+','A+'),
                                    ('a+','A+'),
                                    ('a+','A+'),
                                    ('a+','A+'),
                                    ], string='Blood Group', required=True, track_visibility='onchange')

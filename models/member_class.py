from odoo import models, fields

class MemberClass(models.Model):

    _name = 'member.class'
    _description = 'Member Class'

    #basic
    nis = fields.Char(string='NIS')
    name = fields.Char(string='Nama Lengkap')
    grade = fields.Char(string='Kelas')

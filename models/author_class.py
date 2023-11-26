from odoo import models, fields

class AuthorClass(models.Model):

    _name = 'author.class'
    _description = 'Author Class'

    #basic
    name = fields.Char(string='Nama')

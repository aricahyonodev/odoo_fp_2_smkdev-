from odoo import models, fields

class PublisherClass(models.Model):

    _name = 'publisher.class'
    _description = 'publisher Class'

    name = fields.Char(string='Nama')

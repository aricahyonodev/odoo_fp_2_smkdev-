from odoo import models, fields

class BookClass(models.Model):

    _name = 'book.class'
    _description = 'Book Class'

    #basic
    number_inventaris = fields.Char(string='No Inventaris')
    name = fields.Char(string='Judul Buku')
    author = fields.Many2many('author.class', string='Penulis')
    publication_year = fields.Char(string='Tahun Terbit')
    publisher_id = fields.Many2one('publisher.class','Penerbit Id')
    publisher = fields.Char(
        string='Penerbit', related='publisher_id.name')

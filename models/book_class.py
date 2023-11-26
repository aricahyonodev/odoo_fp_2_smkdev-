from odoo import models, fields

class BookClass(models.Model):

    _name = 'book.class'
    _description = 'Book Class'

    #basic
    number_inventaris = fields.Char(string='No Inventaris', required=True)
    name = fields.Char(string='Judul Buku', required=True)
    author = fields.Many2many('author.class', string='Penulis',  required=True)
    publication_year = fields.Char(string='Tahun Terbit', required=True)
    publisher_id = fields.Many2one('publisher.class','Penerbit')
    publisher = fields.Char(
        string='Penerbit', related='publisher_id.name' )

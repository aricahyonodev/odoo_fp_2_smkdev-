from odoo import models, fields, api

class BookClass(models.Model):

    _name = 'book.class'
    _description = 'Book Class'

    name = fields.Char(string='Judul Buku', required=True)
    number_inventaris = fields.Char(string='No Inventaris', required=True)
    author = fields.Many2many('author.class', string='Penulis',  required=True)
    publication_year = fields.Char(string='Tahun Terbit', required=True)
    publisher_id = fields.Many2one('publisher.class','Penerbit')
    publisher = fields.Char(
        string='Penerbit', related='publisher_id.name' )
    book_authors = fields.Char(string="Penulis", compute="_compute_book_authors")

    @api.depends("author")
    def _compute_book_authors(self):
        for rec in self:
            rec.book_authors = ', '.join(rec.author.mapped('name'))



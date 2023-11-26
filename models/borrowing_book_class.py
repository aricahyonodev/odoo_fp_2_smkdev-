from odoo import models, fields

class BorrowingBookClass(models.Model):

    _name = 'borrowing.book.class'
    _description = 'Borrowing Book Class'

    # basic
    name = fields.Char(string='Kode Peminjaman')
    member_id = fields.Many2one('member.class','Nama Member')
    book_id = fields.Many2one('book.class','Nama Buku')
    date_of_borrowing = fields.Date(string="Tanggal Peminjaman", default=fields.Date.today)
    date_of_return = fields.Date(string="Tanggal Pengembalian")

    state = fields.Selection(
        [('plan', 'Rancangan'), ('borrowed', 'Dipinjam')], string='Status', default='plan')
    

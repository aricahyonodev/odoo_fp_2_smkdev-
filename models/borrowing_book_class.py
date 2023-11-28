from odoo import models, fields, api

class BorrowingBookClass(models.Model):

    _name = 'borrowing.book.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Borrowing Book Class'

    # basic
    name = fields.Char(string='No. Inventaris')
    member_id = fields.Many2one('member.class','Nama Member', required=True)
    book_id = fields.Many2one('book.class', 'Nama Buku', required=True)
    date_of_borrowing = fields.Date(string="Tanggal Peminjaman", default=fields.Date.today)
    date_of_return = fields.Date(string="Tanggal Pengembalian", required=True)

    state = fields.Selection(
        [('plan', 'Rancangan'), ('borrowed', 'Dipinjam')], string='Status', default='plan')
    
    @api.model
    def create(self, vals):
       vals['name'] = self.env['ir.sequence'].next_by_code('borrowing.book.class')
       record = super(BorrowingBookClass, self).create(vals)
       
       record.message_post(body="Peminjaman buku berhasil!")

       return record 

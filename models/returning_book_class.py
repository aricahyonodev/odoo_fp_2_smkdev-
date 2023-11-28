from odoo import models, fields, api

class ReturningBookClass(models.Model):

    _name = 'returning.book.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Returning Book Class'

    # basic
    name = fields.Char(string='No. Inventaris')
    borrowing_book_id = fields.Many2one('borrowing.book.class', 'Kode Peminjaman', required=True)
    member_name = fields.Char(string='Nama Anggota', related='borrowing_book_id.member_id.name')
    book_name = fields.Char(
        string='Judul Buku', related='borrowing_book_id.book_id.name')

    date_of_borrowing = fields.Date(
        string="Tanggal Peminjaman", related='borrowing_book_id.date_of_borrowing')
    date_of_return = fields.Date(
        string="Batas Pengembalian", related='borrowing_book_id.date_of_return')
    
    date_of_return_now = fields.Date(
        string="Tanggal Pengembalian", default=fields.Date.today, required=True)
        
    state = fields.Selection(
        [('borrowed', 'Dipinjam'), ('finished', 'Selesai'), ], string='Status')

    @api.onchange('borrowing_book_id')
    def _onchange_state_selection(self):
        self.state = self.borrowing_book_id.state

    @api.model
    def create(self, vals):
       vals['name'] = self.env['ir.sequence'].next_by_code('returning.book.class')
       record = super(ReturningBookClass, self).create(vals)
       
       record.message_post(body="Pengembalian buku berhasil!")

       return record 

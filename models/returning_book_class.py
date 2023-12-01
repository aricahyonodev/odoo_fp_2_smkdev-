from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ReturningBookClass(models.Model):

    _name = 'returning.book.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Returning Book Class'

    name = fields.Char(string='No. Inventaris')
    borrowing_book_id = fields.Many2one('borrowing.book.class', 'Kode Peminjaman', required=True)

    # Admin
    admin_name = fields.Char(string='Nama Admin',
                              related='borrowing_book_id.admin_name')
    admin_email = fields.Char(string='Nama Admin',
                              related='borrowing_book_id.admin_email')
    # Member
    member_name = fields.Char(string='Nama Anggota', related='borrowing_book_id.member_id.name')
    member_grade = fields.Char(
        string="Kelas", related="borrowing_book_id.member_id.grade")
    member_address = fields.Char(
        string="Alamat", related="borrowing_book_id.member_id.address")
   
    # Date Borrowing BOok
    date_of_borrowing = fields.Char(
        string="Tanggal Peminjaman", related='borrowing_book_id.date_of_borrowing')
    date_of_return = fields.Char(
        string="Batas Pengembalian", related='borrowing_book_id.date_of_return')
    
    date_of_return_now = fields.Date(
        string="Tanggal Pengembalian", default=fields.Date.today, required=True)
        
    state = fields.Selection(
        [('borrowed', 'Dipinjam'), ('finished', 'Selesai'), ], string='Status')

    # Make line
    returning_book_line_ids = fields.One2many(
        string='Judul Buku', related='borrowing_book_id.borrowing_book_line_ids')

    @api.constrains('state')
    def _check_state(self):
        if self.state == "borrowed":
            raise ValidationError("Mohon ubah status ke simpan!")
        
    @api.onchange('borrowing_book_id')
    def _onchange_state_selection(self):
        self.state = self.borrowing_book_id.state

    @api.model
    def create(self, vals):
       vals['name'] = self.env['ir.sequence'].next_by_code('returning.book.class')
       record = super(ReturningBookClass, self).create(vals)
       
       record.message_post(body="Pengembalian buku berhasil!")

       return record 

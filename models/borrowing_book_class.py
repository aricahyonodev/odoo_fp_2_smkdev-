from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
import math

class BorrowingBookClass(models.Model):

    _name = 'borrowing.book.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Borrowing Book Class'

    name = fields.Char(string='No. Inventaris')

    # Member
    member_id = fields.Many2one('member.class','Nama Member', required=True)
    member_grade = fields.Char(string="Kelas", related="member_id.grade")
    member_address = fields.Char(string="Alamat", related="member_id.address")
    admin_name = fields.Char(
        string='Nama Admin', default=lambda self: self.env.user.name, readonly=True)
    admin_email = fields.Char(
        string='Email', default=lambda self: self.env.user.email, readonly=True)

    # Date Borrowing Book
    date_of_borrowing = fields.Char(
        string="Tanggal Peminjaman", default=datetime.now().strftime('%d-%m-%Y'), required=True, readonly=True)
    date_of_return = fields.Char(
        string="Tanggal Pengembalian", compute="_compute_date_of_return")
    length_of_book_borrowing = fields.Selection(
        [('7', '7 Hari'), ('14', '14 hari'), ('21', '21 Hari')], string='Lama Pinjam Buku', default='7')
    library_cash = fields.Char(
        string='Biaya Peminjaman', readonly=True, compute="_compute_library_cash", create=True)
    
    state = fields.Selection(
        [('plan', 'Rancangan'), ('borrowed', 'Dipinjam')], string='Status', default='plan')
    
    # Make line
    borrowing_book_line_ids = fields.One2many(
        'borrowing.book.line', 'borrowing_book_line_id', required=True)
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('borrowing.book.class')
        record = super(BorrowingBookClass, self).create(vals)
        record.message_post(body="Peminjaman buku berhasil!")
        return record

    @api.constrains('borrowing_book_line_ids')
    def _check_borrowing_book_lines(self):
        if len(self.borrowing_book_line_ids) == 0:
            raise ValidationError("Belum ada buku yang dipilih!")
    @api.constrains('state')
    def _check_state(self):
        if self.state == "plan":
            raise ValidationError("Mohon ubah status ke pinjam!")
    
    @api.depends('length_of_book_borrowing', 'borrowing_book_line_ids')
    @api.onchange('length_of_book_borrowing', 'borrowing_book_line_ids')
    def _compute_date_of_return(self):
      for rec in self:
        length_of_book_borrowing = int(rec.length_of_book_borrowing)
        date_of_return =  datetime.now() + timedelta(days=length_of_book_borrowing)
        rec.date_of_return = date_of_return.strftime('%d-%m-%Y')
        
        cost_table = length_of_book_borrowing // 7
        cost_length_of_borrowing = 1000 * cost_table
        if cost_table > 2:
            cost_length_of_borrowing = 2500
        rec.library_cash = "Rp. " + str(cost_length_of_borrowing * len(self.borrowing_book_line_ids)) 

class BorrowingBookLine(models.Model):
   _name        = 'borrowing.book.line'
   _description = 'Borrowing Book Line'

   borrowing_book_line_id = fields.Many2one('borrowing.book.class', string="dwa")
   book_id = fields.Many2one('book.class', string="Nama Buku")
   list_author = fields.Many2many(related='book_id.author')
   
   book_authors = fields.Char(string="Penulis", compute="_compute_book_authors")
   book_year = fields.Char(string="Tahun", related='book_id.publication_year')
   book_publisher = fields.Char(string="Penerbit", related="book_id.publisher")

   @api.depends("book_id")
   def _compute_book_authors(self):
      for rec in self:
        rec.book_authors = ', '.join(rec.list_author.mapped('name'))

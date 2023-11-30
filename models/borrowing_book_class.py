from odoo import models, fields, api
from datetime import datetime, timedelta
import math

class BorrowingBookClass(models.Model):

    _name = 'borrowing.book.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Borrowing Book Class'

    # basic
    name = fields.Char(string='No. Inventaris')
    member_id = fields.Many2one('member.class','Nama Member', required=True)
    book_id = fields.Many2one('book.class', 'Nama Buku', required=True)
    date_of_borrowing = fields.Char(
        string="Tanggal Peminjaman", default=datetime.now().strftime('%d-%m-%Y'), required=True, readonly=True)
    date_of_return = fields.Char(
        string="Tanggal Pengembalian", compute="_compute_date_of_return")

    length_of_book_borrowing = fields.Selection(
        [('7', '7 Hari'), ('14', '14 hari'), ('21', '21 Hari')], string='Lama Pinjam Buku', default='7')
   
    library_cash = fields.Char(
        string='Biaya Peminjaman', readonly=True, compute="_compute_library_cash")
    
    state = fields.Selection(
        [('plan', 'Rancangan'), ('borrowed', 'Dipinjam')], string='Status', default='plan')
    

    @api.model
    def create(self, vals):
       vals['name'] = self.env['ir.sequence'].next_by_code('borrowing.book.class')
       record = super(BorrowingBookClass, self).create(vals)
       
       record.message_post(body="Peminjaman buku berhasil!")

       return record
    
    @api.depends("length_of_book_borrowing")
    def _compute_date_of_return(self):
      for rec in self:
        length_of_book_borrowing = int(rec.length_of_book_borrowing)
        date_of_return =  datetime.now() + timedelta(days=length_of_book_borrowing)
        rec.date_of_return = date_of_return.strftime('%d-%m-%Y')
        
        cost_table = length_of_book_borrowing // 7
        cost_length_of_borrowing = 1000 * cost_table
        if cost_table > 2:
            cost_length_of_borrowing = 2500
        rec.library_cash = "Rp. " + str(cost_length_of_borrowing)

    @api.onchange('length_of_book_borrowing')
    def _onchange_state_selection(self):
      length_of_book_borrowing = int(self.length_of_book_borrowing)
      date_of_return =  datetime.now() + timedelta(days=length_of_book_borrowing)
      self.date_of_return = date_of_return.strftime('%d-%m-%Y')

      cost_table = math.floor(length_of_book_borrowing / 7)
      cost_length_of_borrowing = 1000 * cost_table
      if cost_table > 2:
        cost_length_of_borrowing = 2500
      self.library_cash = "Rp. " + str(cost_length_of_borrowing)


from odoo import models, fields

class MemberClass(models.Model):

    _name = 'member.class'
    _description = 'Member Class'

    nis = fields.Char(string='NIS', required=True)
    name = fields.Char(string='Nama Lengkap', required=True)
    grade = fields.Char(string='Kelas', required=True)
    address = fields.Char(string='Alamat', required=True)

    borrowing_book_ids = fields.One2many('borrowing.book.class', 'member_id', string='Kode Peminjaman')

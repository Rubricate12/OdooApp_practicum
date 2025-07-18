from odoo import models, fields, api

class PracticumStudent(models.Model):
    _name = 'practicum.student'
    _description = 'Data Mahasiswa'
    #pakai display_name biar terlihat lebih rapi
    _rec_name = 'display_name' 

    name = fields.Char(string='Nama Mahasiswa', required=True)
    student_nim = fields.Char(string='NIM', required=True)
    student_prodi = fields.Char(string='Prodi')
    semester = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
        ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
        ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'),
        ('13', '13'), ('14', '14'),
    ], string="Semester", required=True, default='1')

    tingkat = fields.Selection([
        ('1', 'Tingkat 1'),
        ('2', 'Tingkat 2'),
        ('3', 'Tingkat 3'),
        ('4', 'Tingkat 4'),
    ], string="Tingkat", compute='_compute_tingkat', store=True)

    registration_ids = fields.One2many(
        'practicum.registration', 
        'student_id', 
        string='Riwayat Pendaftaran'
    )
    #definisikan display_name (gunakan agar tidak bingung jika ada nama yang sama)
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)
    #utk memberitau odoo jalankan fungsi setiap nama dan nim berubah
    @api.depends('name', 'student_nim')
    #fungsi display name menggunakan fprint utk menggabungkan record nama dan nim
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.student_nim})"

    @api.depends('semester')
    def _compute_tingkat(self):
        for record in self:
            if record.semester in ['1', '2']:
                record.tingkat = '1'
            elif record.semester in ['3', '4']:
                record.tingkat = '2'
            elif record.semester in ['5', '6']:
                record.tingkat = '3'
            elif record.semester:
                record.tingkat = '4'
            else:
                record.tingkat = False
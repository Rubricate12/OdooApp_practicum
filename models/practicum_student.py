from odoo import models, fields, api

class PracticumStudent(models.Model):
    _name = 'practicum.student'
    _description = 'Data Mahasiswa'
    #pakai display_name biar terlihat lebih rapi
    _rec_name = 'display_name' 

    name = fields.Char(string='Nama Mahasiswa', required=True)
    student_nim = fields.Char(string='NIM', required=True)
    student_prodi = fields.Char(string='Prodi')
    student_sem = fields.Selection([
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
        ('9', 'Semester 9'),
        ('10', 'Semester 10')
        ('11', 'Semester 11')
        ('12', 'Semester 12')
        ('13', 'Semester 13')
        ('14', 'Semester 14')
    ])

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
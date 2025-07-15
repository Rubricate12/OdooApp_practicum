from odoo import models, fields, api

class PracticumStudent(models.Model):
    _name = 'practicum.student'
    _description = 'Data Mahasiswa'
    #pakai display_name biar terlihat lebih rapi
    _rec_name = 'display_name' 

    name = fields.Char(string='Nama Mahasiswa', required=True)
    student_nim = fields.Char(string='NIM', required=True)
    student_prodi = fields.Char(string='Prodi')
    
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
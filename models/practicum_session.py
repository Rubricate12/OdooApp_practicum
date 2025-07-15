from odoo import models, fields

class PracticumSession(models.Model):
    _name = 'practicum.session'
    _description = 'Sesi Praktikum'
    _rec_name = 'name'

    name = fields.Char(string='Nama Praktikum', required=True)
    session_code = fields.Char(string='Kode Sesi')
    supervisor_id = fields.Many2one('res.partner', string='Pengawas') # anggap saja diambil dari model kontak dari odoo
    session_date = fields.Datetime(string='Jadwal Praktikum')
    
    participant_ids = fields.One2many(
        'practicum.registration', 
        'practicum_id', 
        string='Peserta Terdaftar'
    )
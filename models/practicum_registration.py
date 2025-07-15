from odoo import models, fields

class PracticumRegistration(models.Model):
    _name = 'practicum.registration'
    _description = 'Pendaftaran Praktikum Mahasiswa'

    student_id = fields.Many2one('practicum.student', string='Mahasiswa', required=True)
    practicum_id = fields.Many2one('practicum.session', string='Sesi Praktikum', required=True)
    
    registration_date = fields.Date(string='Tanggal Daftar', default=fields.Date.context_today)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('done', 'Selesai'),
    ], string='Status', default='draft', required=True)
    
    notes = fields.Text(string='Catatan')
    #aksi utk mengubah state registration
    def action_submit(self):
        self.write({'state': 'submitted'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_reset_to_draft(self):
        self.write({'state': 'draft'})
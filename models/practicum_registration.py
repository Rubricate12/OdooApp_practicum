from odoo import models, fields

class PracticumRegistration(models.Model):
    _name = 'practicum.registration'
    _description = 'Pendaftaran Praktikum Mahasiswa'

    student_id = fields.Many2one('practicum.student', string='Mahasiswa', required=True)
    practicum_id = fields.Many2one('practicum.session', string='Sesi Praktikum', required=True)
    
    registration_date = fields.Date(string='Tanggal Daftar', default=fields.Date.context_today)
    
    student_nim_related = fields.Char(
        related='student_id.student_nim', 
        string="NIM Mahasiswa", 
    )
    student_prodi_related = fields.Char(
        related='student_id.student_prodi', 
        string="Jurusan Mahasiswa", 
    )
    session_code_related = fields.Char(
        related='practicum_id.session_code',
        string="Kode Sesi",
    )
    supervisor_related = fields.Many2one(
        'res.partner',
        related='practicum_id.supervisor_id',
        string="Supervisor",
        readonly=True
    )
    session_date_related = fields.Datetime(
        related='practicum_id.session_date',
        string="Tanggal sesi",
    )

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
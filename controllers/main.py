from odoo import http
from odoo.http import request
import base64

class PraktikumController(http.Controller):

    @http.route('/praktikum/daftar', type='http', auth='public', website=True)
    def show_form(self):
        students = request.env['practicum.student'].sudo().search([])
        sessions = request.env['practicum.session'].sudo().search([])
        return request.render('om_praktikum.registration_form_template', {
            'students': students,
            'sessions': sessions,
        })

    @http.route('/praktikum/submit', type='http', auth='public', website=True, csrf=False)
    def submit_form(self, **post):
        student_id = int(post.get('student_id'))
        session_id = int(post.get('session_id'))

        file_storage = request.httprequest.files.get('attachment')
        file_content = file_storage.read()
        encoded_file = base64.b64encode(file_content)

        registration = request.env['practicum.registration'].sudo().create({
            'student_id': student_id,
            'practicum_id': session_id,
            'attachment': encoded_file,
            'attachment_filename': file_storage.filename,
        })

        student = request.env['practicum.student'].sudo().browse(student_id)
        session = request.env['practicum.session'].sudo().browse(session_id)

        return request.render('om_praktikum.registration_thank_you', {
            'student': student,
            'session': session,
        })
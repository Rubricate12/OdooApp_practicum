{
    'name': 'Manajemen Praktikum',
    'version': '18.0.1.0.0',
    'summary': 'Modul untuk pendataan jadwal dan pendaftaran praktikum mahasiswa.',
    'description': """
        Modul ini membantu dalam mengelola sesi praktikum dan pendaftaran
        yang dilakukan oleh mahasiswa.
    """,
    'author': 'Arnoldus Bryan H',
    'website': 'https://www.contohwebsite.com',
    'category': 'Education',
    'depends': ['base'], 
    'data': [
        'security/ir.model.access.csv',
        'security/practicum_security.xml',
        'views/practicum_student_views.xml',
        'views/practicum_session_views.xml',
        'views/practicum_registration_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
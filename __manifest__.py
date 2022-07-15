{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Prodoctivity',
    'summary': 'Hospital Management',
    'sequence': -100000,
    'description': 'Hospital Management ',
    'depends': [
        'mail',
        'board'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu.xml',
        'wizards/change_status.xml',
        'reports/patient_cards.xml',
        'reports/report.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/dashboard.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Prodoctivity',
    'summary': 'Hospital Management',
    'sequence': -100000,
    'description': 'Hospital Management ',
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
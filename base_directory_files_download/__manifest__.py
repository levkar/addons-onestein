# Copyright 2017 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Directory Files Download',
    'summary': 'Download all files of a directory on server',
    'author': 'Onestein',
    'website': 'http://www.onestein.eu',
    'category': 'Tools',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ir_filesystem_directory.xml',
    ],
    'installable': True,
}

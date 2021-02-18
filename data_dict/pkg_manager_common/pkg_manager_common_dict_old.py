import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.pkg_manager_common import table_of_common_package_managers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('pkg_manager_common', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'pkg_manager_common'
information = {
	'tool': 'Package Management',
	'title': 'Package Management',
	'subtitle': 'This site is a reference for common package managers.',
	'description': 'Packages are software applications that resides in archives. A package manager is a tool that automates the process of installing, updating, upgrading and removing packages.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '✔',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'PackageManager', [
				helper.characteristics.get('sys-admin'),
				helper.characteristics.get('dev-ops'),
				helper.characteristics.get('tool'),
			])
	],
	'topic_uris': [
		'sys-admin',
		'dev-ops',
		'tool',
	],
}
affiliate_products = [],
# TODO: Include table of common package managers.
# https://www.volkerschatz.com/unix/linuxpack.html
general_info_text = 'Common Package Management Operations'
general_info_text_lead = 'Commands for Common Package Management across Distributions'
general_info_links = {}
general_info = [
	Markup(table_of_common_package_managers.table),
]
general_info_flag = True
see_also = [
	{
	},
]

cheatsheet = [
	{
		'heading': helper.set_folder('Yum'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Pacman'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Apt'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Aptitude'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('RPM'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('DNF'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Zypper'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('NPM'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('pip'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('PyPi'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('')[0]),
					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},

]

resources = [
	# ResourceCollector.recieve_resources_from_dicts(
	#     {
	#         'link': 'https://www.example.com/',
	#         'title': 'Ex',
	#         'description': Markup('Ex'),
	#         'footer': '',
	#         'screencapture': ''
	#     },
	# )
]

licensing = [
	Markup('')
]

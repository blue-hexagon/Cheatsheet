import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.helper_functions import Helpers
from static.public.data_dict.pkg_manager_common import table_of_common_package_managers
from static.resource_collector import ResourceCollector

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
		'heading':helper.set_folder('Yum'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '06070c0bd3294269bcd329c87d9861de',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ae5629debca54de98fe4d93355a90ef4')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Pacman'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '1e43dc7bcc12416e952afbe5a72c7b80',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('637023eae1e44f09bf458096b50c51f7')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Apt'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '083bb8dc06e8419798d61f3adfa78031',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('39f779066e6d46d385b310b419a37933')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Aptitude'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f6231a566d504aebabbe724a6cb6950a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9f9dea01192c44a4a41bc9eba0d9536f')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('RPM'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '01bb1d23aa3447b9ab7f1b4d920795e4',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8341aabf7d0141698e5afd1c25c438a9')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('DNF'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'b25f307bb7534adc890d9b57f83cb1d8',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('165c0ef83add4f4fba376ac8a110967a')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Zypper'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '48784b81a3a84dfe975e583f2d3fcf41',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a3ed754d95e448cfb615248653024924')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('NPM'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5b7d0b1087494dbe99d3ef773e0c92bb',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('f47f6631760e4e3a95539001134abfdf')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('pip'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'fd3518f7ceaa464caf6ef5f71ce57b99',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0e730f82c8c44e83aea595508800b0ee')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('PyPi'),
		'subtitle': 'Yum Package Manager',
		'description': '.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '9dc246246e3f42e3b47752f57877985d',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e8f0fd201c1b4e6eb5b26e9c7fa37109')[0]),
					'flag': helper.set_entry_command_string(''),

					'description': Markup(''),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),

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

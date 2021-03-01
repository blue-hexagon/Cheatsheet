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
meta = {
	'title': 'Package Managers Cheatsheet',
	'description': 'Apt · Pip · NPM · Zypper · Pacman · Yum · RPM · DNF',
	'keywords': 'package manager, yum, apt, rpm, pacman, aptitude, dnf, zypper, npm, pip, pypi, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/packagemanagement/',

	'opengraph_title': 'Package Managers Cheatsheet',
	'opengraph_description': 'Apt · Pip · NPM · Zypper · Pacman · Yum · RPM · DNF',
	'opengraph_image': 'opengraph_package_management.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/packagemanagement/',

	'twitter_title': 'Package Managers Cheatsheet',
	'twitter_description': 'Apt · Pip · NPM · Zypper · Pacman · Yum · RPM · DNF',
	'twitter_image': 'twitter_card_package_management.png',
}
information = {
	'tool': 'Package Management',
	'title': 'Package Management',
	'subtitle': 'This site is a reference for common package managers.',
	'description': 'Packages are software applications that resides in archives. A package manager is a tool that automates the process of installing, updating, upgrading and removing packages.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
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
		'description': 'The Yellowdog Updater, Modified (YUM) package manager is a package manager for Linux operating systems.',
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
					'flag': Markup(helper.set_entry_command_string('yum list updates')),
					'description': Markup('Display list of updated software and security fixes'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Pacman'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Flags are case-sensitive with pacman: -S is not the same as -s'
		},
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
					'flag': Markup(helper.set_entry_command_string('pacman -Syu pkg')),
					'description': Markup('Install pkg and update the package list'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Apt'),
		'subtitle': 'Advanced Package Tool',
		'description': '',
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
					'flag': Markup(helper.set_entry_command_string('apt-get install pkg')),
					'description': Markup('Install pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Aptitude'),
		'subtitle': '',
		'description': '',
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
					'flag': Markup(helper.set_entry_command_string('aptitude install pkg')),
					'description': Markup('Install pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('RPM'),
		'subtitle': 'Redhat Package Manager',
		'description': 'Not only used for Red Hat Linux',
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
					'flag': Markup(helper.set_entry_command_string('rpm -i pkg')),
					# 'flag_alt': Markup('rpm --install pkg'),
					'description': Markup('Installs pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('DNF'),
		'subtitle': 'Dandified YUM',
		'description': '',
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
					'flag': Markup(helper.set_entry_command_string('dnf install pkg')),
					'description': Markup('Install pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Zypper'),
		'subtitle': '',
		'description': '',
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
					'flag': Markup(helper.set_entry_command_string('zypper install pkg')),
					# 'flag_alt': Markup('zypper in pkg'),
					'description': Markup('Install pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('NPM'),
		'subtitle': 'Node Package Manager',
		'description': '',
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
					'flag': Markup(helper.set_entry_command_string('npm install pkg')),
					'description': Markup('Install pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('pip'),
		'subtitle': '',
		'description': '',
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
					'flag': Markup(helper.set_entry_command_string('pip install pkg')),
					'description': Markup('Install pkg'),
					'video': Markup(''),
					'example': helper.example_path(),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
]
resources = [
]
licensing = [
	Markup('Common Package Management Operations: <a href="https://www.volkerschatz.com/unix/linuxpack.html">See original work here.</a>')
]

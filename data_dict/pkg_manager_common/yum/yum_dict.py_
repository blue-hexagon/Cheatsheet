import os
import pathlib
from datetime import datetime

from flask import url_for
import uuid
from markupsafe import Markup
from application.static.cheatsheet.helper_functions import Helpers
from application.static.cheatsheet.resource_collector import ResourceCollector
import os

script_dir = os.path.dirname(__file__)
helper = Helpers('yum', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'yum'
information = {
	'tool': 'Yum',
	'title': 'Yum Cheatsheet',
	'subtitle': 'This site is a reference for the package manager Yum',
	'description': '',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '⚠',

	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Yum',
			[
				helper.characteristics.get('front-end'),
			])
	],
	'topic_uris': [
		'front-end',
	],
}
general_info_text = ''
general_info_text_lead = ''
general_info_links = {}
general_info = [
	Markup(
		''),
]
general_info_flag = False
see_also = [
	{
	},
]

cheatsheet = [
	{
		'heading': helper.set_folder('General Use'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("yum install")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid()
				},
				{
					'flag': Markup(helper.set_entry_folder("yum update")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid()
				},
			]
		}
	},


]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://websitesetup.org/wp-content/uploads/2020/03/Bootstrap-Cheat-Sheet-Summary-Full.png',
			'title': 'Cheatsheet Graphic',
			'description': Markup('A giant printable cheatsheet'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://www.creative-tim.com/cheatsheet/bootstrap4',
			'title': 'Creative Tim\' BS4 Cheatsheet',
			'description': Markup('Highly useful'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://gist.github.com/JacobLett/3f16b4c857fdec22472ac20e3dd0366a',
			'title': 'A Full List of All BS4 Classes',
			'description': Markup('Textfile with all classes available in BootStrap4'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://bootstrapcreative.com/resources/bootstrap-4-css-classes-index/',
			'title': 'Searchable List of All BS4 Classes and Components with Examples',
			'description': Markup(''),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

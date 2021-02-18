import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('tmux', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'tmux'
information = {
	'tool': 'Tmux',
	'title': 'Tmux Cheatsheet',
	'subtitle': 'This site is a reference for the terminal multiplexer Tmux',
	'description': 'Tmux is a terminal multiplexer used for ...',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Git',
			[
				helper.characteristics.get('cvs'),
			])
	],
	'topic_uris': [
		'cvs',
	],

}
general_info_text = ''
general_info_text_lead = ''
general_info_links = {}
general_info = [
	'',
]
general_info_flag = False
see_also = [
	{
		'': '',
	},
]
affiliate_products = [{
	Markup(''),
	Markup(''),
	Markup(''),
}],
cheatsheet = [
	{
		'heading': helper.set_folder('New Session'),
		'subtitle': 'Subheading.',
		'description': 'Description',
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
					'flag': Markup(helper.set_entry_folder('tmux')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux new'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux new-session'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux new -s sessionname'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Attach Session',
		'subtitle': 'Subheading.',
		'description': 'Description',
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
					'flag': Markup('tmux a'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux att'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux attach'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux attach-session'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux a -t sessionname'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Remove Session',
		'subtitle': 'Subheading.',
		'description': 'Description',
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
					'flag': Markup('tmux kill-ses'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('tmux kill-session -t sessionname'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Key Binding',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Panes',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Key Bindings',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Heading',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Heading',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Heading',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': 'Heading',
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
			'Warning 1'
		},
		'danger': {
			'Danger 1'
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('cmd'),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://github.com',
			'title': 'Github',
			'description': Markup('A collection of thousands of git-repositories from individual users'),
			'footer': Markup('You properly know it'),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
# style="max-height:150px; max-width: 150px;
licensing = [
	Markup('')
]

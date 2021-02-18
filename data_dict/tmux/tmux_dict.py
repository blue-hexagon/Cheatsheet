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
		'heading':helper.set_folder('New Session'),
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '2aab3db3bc084cc38108c04756870136',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('aba0f03b913e4617bb5c7222bea1dda6')[0]),
					'flag': helper.set_entry_command_string('tmux'),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b3372c9bccd04696afd4e093c577241a')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux new')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a12a3f57a9ea41e7a9cbda851795bd55')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux new-session')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a0fa2d7530944bceb5f1476277f05388')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux new -s sessionname')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Attach Session'),
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f6c4033099d4446bba569e3fa9470117',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('3c2f849d0a8e4f01b2a868cd7bab9344')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux a')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e3c5ce2db8ca40f7877c4e0af347273e')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux att')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fc9d4205ebad4c2e8094c8c2ff5181fd')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux attach')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8ebc21f3a81e42808073a2b46961639d')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux attach-session')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('17a9843a9faa40d08369e306ef9e0534')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux a -t sessionname')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Remove Session'),
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '7432780ed5f3492f9c9a954c801a02e5',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('53427704f6bd48da8dbe476c28447b01')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux kill-ses')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('17cc028909dc4b74ab74ccafedd4bebd')[0]),
					'flag': helper.set_entry_command_string(Markup('tmux kill-session -t sessionname')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Key Binding'),
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
		'static_red': '6f7c31286bd44f38bacbd61a6788aebd',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('7582b5b4fb09485aa9409de9ec9f70f2')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Panes'),
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
		'static_red': 'aa1fd47be54a4989a15d310030002d5a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b3f36ad3112c47ed808b9a362d13bab2')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Key Bindings'),
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
		'static_red': '95432028d8964a8c9df1102d820f8fa8',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9a685e77299a4cef918e27fb9f235592')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Heading'),
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
		'static_red': 'ab3476e189c44049800df682d304ce93',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6d65544d2a29424eaee12e95a96949d1')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Heading'),
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
		'static_red': '45f2ddfcf0514668a07bb38538ee9879',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('32b73502c5cc442a830982469e56de1e')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Heading'),
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
		'static_red': '536dec8d802944a58e8b21185c523f0e',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('163e71922f8d49d7881d80463c57856a')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Heading'),
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
		'static_red': '61fb66f07ae74e91a1acabe0da763c46',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('684ffb53febd48c1b1d0485517b2b190')[0]),
					'flag': helper.set_entry_command_string(Markup('cmd')),

					'description': Markup('Command description'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),

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

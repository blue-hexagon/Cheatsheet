import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('nano', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'nano'
information = {
	'tool': 'Nano',
	'title': 'Nano Cheatsheet',
	'subtitle': 'This site is a reference for the text editor Nano',
	'description': 'GNU Nano, formerly known as TIP (TIP is Not Pico) is a text editor based off of the Pico text editor.\n The text editor is pretty straight compared to Vi, Vim or Emacs and is the first encountered text editor of most GNU/Linux novices.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '✔',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Nano', [
				helper.characteristics.get('text-editor'),
			])
	],
	'topic_uris': [
		'text-editor',
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
	},
]
affiliate_products = [],
cheatsheet = [
	{
		'heading': helper.set_folder('File Handling'),
		'subtitle': 'How to save and open files in Nano',
		'description': 'Shortcuts for file handling.',
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
					'flag': Markup(helper.set_entry_folder('Ctrl+S')[0]),
					'description': Markup('Save current file'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+O')[0]),
					'description': Markup('Offer to write file ("Save as")'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+R')[0]),
					'description': Markup('Insert a file into current one'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+X')[0]),
					'description': Markup('Close buffer, exit from nano'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Editing'),
		'subtitle': 'How to edit files in Nano',
		'description': 'Cutting, copy, pasting, word completion and more',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Ctrl+K')[0]),
					'description': Markup('Cut current line into cutbuffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+6')[0]),
					'description': Markup('Copy current line into cutbuffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+U')[0]),
					'description': Markup('Paste contents of cutbuffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+T')[0]),
					'description': Markup('Cut until end of buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+]')[0]),
					'description': Markup('Complete current word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+3')[0]),
					'description': Markup('Comment/uncomment line/region'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+U')[0]),
					'description': Markup('Undo last action'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+E')[0]),
					'description': Markup('Redo last undone action'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Moving Around'),
		'subtitle': 'Moving around text and buffers in Nano',
		'description': 'Moving between words, buffers, characters and more',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Ctrl+B')[0]),
					'description': Markup('One character backward'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+F')[0]),
					'description': Markup('One character forward'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+←')[0]),
					'description': Markup('One word backward'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+→')[0]),
					'description': Markup('One word forward'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+A')[0]),
					'description': Markup('To start of line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+E')[0]),
					'description': Markup('To end of line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+P')[0]),
					'description': Markup('One line up'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+N')[0]),
					'description': Markup('One line down'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+↑')[0]),
					'description': Markup('To previous block'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+↓')[0]),
					'description': Markup('To next block'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+Y')[0]),
					'description': Markup('One page up'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+V')[0]),
					'description': Markup('One page down'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+\\')[0]),
					'description': Markup('	To top of buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+/')[0]),
					'description': Markup('	To end of buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Search & Replace'),
		'subtitle': 'How to search for text in Nano',
		'description': 'Searching and replacing text',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Ctrl+Q')[0]),
					'description': Markup('Start backward search'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+W')[0]),
					'description': Markup('Start forward search'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+Q')[0]),
					'description': Markup('Find next occurrence backward'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+W')[0]),
					'description': Markup('Find next occurrence forward'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+R')[0]),
					'description': Markup('Start a replacing session'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Special Movement'),
		'subtitle': 'Special movement commands in Nano',
		'description': 'Scroll the viewport, goto a given linenumber, goto complementary bracket or switch to a preceding buffer',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Alt+G')[0]),
					'description': Markup('Go to specified line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+]')[0]),
					'description': Markup('Go to complementary bracket'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+↑')[0]),
					'description': Markup('Scroll viewport up'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+↓')[0]),
					'description': Markup('Scroll viewport down'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+<')[0]),
					'description': Markup('Switch to preceding buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+>')[0]),
					'description': Markup('Switch to succeeding buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Deletion'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Ctrl+H')[0]),
					'description': Markup('Delete character before cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+D')[0]),
					'description': Markup('Delete character under cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+Bsp')[0]),
					'description': Markup('Delete word to the left'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+Del')[0]),
					'description': Markup('Delete word to the right'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+Del')[0]),
					'description': Markup('Delete current line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Information'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Ctrl+C')[0]),
					'description': Markup('Report cursor position'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+D')[0]),
					'description': Markup('Report word/line/char count'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+G')[0]),
					'description': Markup('Display help text'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Operations'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Ctrl+T')[0]),
					'description': Markup('Execute some command'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+J')[0]),
					'description': Markup('Justify paragraph or region'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+J')[0]),
					'description': Markup('Justify entire buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+B')[0]),
					'description': Markup('Run a syntax check'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+F')[0]),
					'description': Markup('Run a formatter/fixer/arranger'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+:')[0]),
					'description': Markup('Start/stop recording of macro'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+;')[0]),
					'description': Markup('Replay macro'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Various'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
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
					'flag': Markup(helper.set_entry_folder('Alt+A')[0]),
					'description': Markup('	Turn the mark on/off'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Tab')[0]),
					'description': Markup('	Indent marked region'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Shift+Tab')[0]),
					'description': Markup('Unindent marked region'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+N')[0]),
					'description': Markup('Turn line numbers on/off'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+P')[0]),
					'description': Markup('Turn visible whitespace on/off'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt+V')[0]),
					'description': Markup('Enter next keystroke verbatim'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+L')[0]),
					'description': Markup('Refresh the screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+Z')[0]),
					'description': Markup('Suspend nano'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
					'static_ref': '',
				},
			]
		}
	},
]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://www.nano-editor.org/',
			'title': 'Nano Official Website',
			'description': Markup('The official website for Nano'),
			'footer': '',
			'screencapture': ''
		},
	)
]
licensing = [
	Markup('')
]

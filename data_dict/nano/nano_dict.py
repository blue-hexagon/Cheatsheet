import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('nano', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'nano'
meta = {
	'title': 'GNU Nano Cheatsheet',
	'description': 'File Handling · Editing · Moving Around · Search & Replace · Deletion · Operations · Special Movement',
	'keywords': 'nano, tip, vi, vim, ed, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/Nano/',

	'opengraph_title': 'GNU Nano Cheatsheet',
	'opengraph_description': 'File Handling · Editing · Moving Around · Search & Replace · Deletion · Operations · Special Movement',
	'opengraph_image': 'opengraph_nano.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/nano/',

	'twitter_title': 'GNU Nano Cheatsheet',
	'twitter_description': 'File Handling · Editing · Moving Around · Search & Replace · Deletion · Operations · Special Movement',
	'twitter_image': 'twitter_card_nano.png',
}
information = {
	'tool': 'Nano',
	'title': 'Nano Cheatsheet',
	'subtitle': 'This site is a reference for the text editor Nano',
	'description': 'GNU Nano, formerly known as TIP (TIP is Not Pico) is a text editor based off of the Pico text editor.\n The text editor is pretty straight compared to Vi, Vim or Emacs and is the first encountered text editor of most GNU/Linux novices.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
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
		'static_red': '95dd5db58dfc46f1a1837c9662a315df',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6f95f8827a384f8d918b2318a8ed0871')[0]),
					'flag': helper.set_entry_command_string('Ctrl+S'),
					'description': [
						Markup('Save current file'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1541492444044fcea9a71bfc442e01d2')[0]),
					'flag': helper.set_entry_command_string('Ctrl+O'),
					'description': [
						Markup('Offer to write file ("Save as")'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2c86dab7906d4fcb9f863f6ed1f02a51')[0]),
					'flag': helper.set_entry_command_string('Ctrl+R'),
					'description': [
						Markup('Insert a file into current one'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('83a4f7364ec54456831f91fc8610f17c')[0]),
					'flag': helper.set_entry_command_string('Ctrl+X'),
					'description': [
						Markup('Close buffer, exit from nano'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '93bfb394e5d44adeb48830b533e90a77',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9e9775f9f2e848fba8bad744f144dc24')[0]),
					'flag': helper.set_entry_command_string('Ctrl+K'),
					'description': [
						Markup('Cut current line into cutbuffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7b241628e34b4b899ac1f67e6f850baf')[0]),
					'flag': helper.set_entry_command_string('Alt+6'),
					'description': [
						Markup('Copy current line into cutbuffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5c556850536f4eca8659fd66508141bb')[0]),
					'flag': helper.set_entry_command_string('Ctrl+U'),
					'description': [
						Markup('Paste contents of cutbuffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('84fb36be4f074eb3ad66078a71485c78')[0]),
					'flag': helper.set_entry_command_string('Alt+T'),
					'description': [
						Markup('Cut until end of buffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('185ead0b4cf747b4ae686496edd1062b')[0]),
					'flag': helper.set_entry_command_string('Ctrl+]'),
					'description': [
						Markup('Complete current word'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a7286cdbf394427ab1689a51f88227f2')[0]),
					'flag': helper.set_entry_command_string('Alt+3'),
					'description': [
						Markup('Comment/uncomment line/region'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('356ee69d209f460f85ff939a0e9a7651')[0]),
					'flag': helper.set_entry_command_string('Alt+U'),
					'description': [
						Markup('Undo last action'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9b075530bdf74ea2845b028c81571577')[0]),
					'flag': helper.set_entry_command_string('Alt+E'),
					'description': [
						Markup('Redo last undone action'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '1accd34eb72d434bbb592245544403ef',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e22f8a4db1764581b28d09f3792a6e3a')[0]),
					'flag': helper.set_entry_command_string('Ctrl+B'),
					'description': [
						Markup('One character backward'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a00c8b16356c4bd8a626214a870226a7')[0]),
					'flag': helper.set_entry_command_string('Ctrl+F'),
					'description': [
						Markup('One character forward'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('72250f900cca4dad93654d1ca691d402')[0]),
					'flag': helper.set_entry_command_string('Ctrl+←'),
					'description': [
						Markup('One word backward'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a82153b647a34f41a5fefa7650ce6609')[0]),
					'flag': helper.set_entry_command_string('Ctrl+→'),
					'description': [
						Markup('One word forward'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('98b04cc3aebe4192b07ba4e6ebfbce2d')[0]),
					'flag': helper.set_entry_command_string('Ctrl+A'),
					'description': [
						Markup('To start of line'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ba0473f27e6e465da536700fd941be3c')[0]),
					'flag': helper.set_entry_command_string('Ctrl+E'),
					'description': [
						Markup('To end of line'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1a788e41e6254adabff95c44a283aa76')[0]),
					'flag': helper.set_entry_command_string('Ctrl+P'),
					'description': [
						Markup('One line up'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c8d068fe5fc24594ae71f9ef96ba978c')[0]),
					'flag': helper.set_entry_command_string('Ctrl+N'),
					'description': [
						Markup('One line down'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('07bd445229c343cc84d2f6bfdfb8843c')[0]),
					'flag': helper.set_entry_command_string('Ctrl+↑'),
					'description': [
						Markup('To previous block'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('80c2539c2ede4d80b830cbfb8cbf4eac')[0]),
					'flag': helper.set_entry_command_string('Ctrl+↓'),
					'description': [
						Markup('To next block'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c78a3ebc92c04d4b97d31e95a6ec4bf5')[0]),
					'flag': helper.set_entry_command_string('Ctrl+Y'),
					'description': [
						Markup('One page up'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fa8cb84b5a6c46cdb0586ca54708189a')[0]),
					'flag': helper.set_entry_command_string('Ctrl+V'),
					'description': [
						Markup('One page down'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5451ac19116c4250b418ceacadc3be5d')[0]),
					'flag': helper.set_entry_command_string('Alt+\\'),
					'description': [
						Markup('	To top of buffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e5e4ab1e8fbf44158a7a4cb8a67790aa')[0]),
					'flag': helper.set_entry_command_string('Alt+/'),
					'description': [
						Markup('	To end of buffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': 'e178472be2a04b9692218abe43930676',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('791b75bf97a344e88424af31d3083a01')[0]),
					'flag': helper.set_entry_command_string('Ctrl+Q'),
					'description': [
						Markup('Start backward search'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7c8e721d985342b184adcb2245db95d5')[0]),
					'flag': helper.set_entry_command_string('Ctrl+W'),
					'description': [
						Markup('Start forward search'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e730ff0bf7364780979f4fd1acf62ded')[0]),
					'flag': helper.set_entry_command_string('Alt+Q'),
					'description': [
						Markup('Find next occurrence backward'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('304c8d662ea24886aa15270fbb1abdb2')[0]),
					'flag': helper.set_entry_command_string('Alt+W'),
					'description': [
						Markup('Find next occurrence forward'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2e4324ce0aa94794b0772ab00db38971')[0]),
					'flag': helper.set_entry_command_string('Alt+R'),
					'description': [
						Markup('Start a replacing session'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '5ec215ac83d745529dddc55de6eb8b8e',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ce6ab6b7bcdf4786846a286555e81ccc')[0]),
					'flag': helper.set_entry_command_string('Alt+G'),
					'description': [
						Markup('Go to specified line'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('13bfdfceccf7465480171a8336bd1b6f')[0]),
					'flag': helper.set_entry_command_string('Alt+]'),
					'description': [
						Markup('Go to complementary bracket'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('53950e2f751141339d3d35a4f25f72c8')[0]),
					'flag': helper.set_entry_command_string('Alt+↑'),
					'description': [
						Markup('Scroll viewport up'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('747a4115738244e192231c5e96e1c239')[0]),
					'flag': helper.set_entry_command_string('Alt+↓'),
					'description': [
						Markup('Scroll viewport down'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('923fd501e09a4c839e663f83c4b4fcfe')[0]),
					'flag': helper.set_entry_command_string('Alt+<'),
					'description': [
						Markup('Switch to preceding buffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('19e2b722b85a4ad49c788d51a96bfc7c')[0]),
					'flag': helper.set_entry_command_string('Alt+>'),
					'description': [
						Markup('Switch to succeeding buffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '087e2912047c4a5b976b7214ce8be2bc',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('7f05061060f24417af98ba8a6c803028')[0]),
					'flag': helper.set_entry_command_string('Ctrl+H'),
					'description': [
						Markup('Delete character before cursor'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('574274c39c7b46919587fdceec7b281f')[0]),
					'flag': helper.set_entry_command_string('Ctrl+D'),
					'description': [
						Markup('Delete character under cursor'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('735c390b8a964a8bab6eac07faff2c3e')[0]),
					'flag': helper.set_entry_command_string('Alt+Bsp'),
					'description': [
						Markup('Delete word to the left'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('27a3fe6369454e30afb86d9fe56be30c')[0]),
					'flag': helper.set_entry_command_string('Ctrl+Del'),
					'description': [
						Markup('Delete word to the right'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a1279c12a8364fa5924eae59593d8103')[0]),
					'flag': helper.set_entry_command_string('Alt+Del'),
					'description': [
						Markup('Delete current line'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '30df03346b5e46368719d12f63c48c81',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('15fe01f36ee1422ead8ce015fee5f3fa')[0]),
					'flag': helper.set_entry_command_string('Ctrl+C'),
					'description': [
						Markup('Report cursor position'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8d0148e4ece04a12af8cbd04f6f8a6ee')[0]),
					'flag': helper.set_entry_command_string('Alt+D'),
					'description': [
						Markup('Report word/line/char count'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fa63739cbe074001a5fea9cbd9e9eb9f')[0]),
					'flag': helper.set_entry_command_string('Ctrl+G'),
					'description': [
						Markup('Display help text'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '2cd58294f4f9424a8bf06d282e81ab5a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('067cff5949fc4b23b85c347612fe6b24')[0]),
					'flag': helper.set_entry_command_string('Ctrl+T'),
					'description': [
						Markup('Execute some command'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('09dd028c3cd445b08fc70188fb6d5051')[0]),
					'flag': helper.set_entry_command_string('Ctrl+J'),
					'description': [
						Markup('Justify paragraph or region'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5a20aa48b76a45a3b8751dba1328effb')[0]),
					'flag': helper.set_entry_command_string('Alt+J'),
					'description': [
						Markup('Justify entire buffer'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('acdcb6a93ad64a4e9bdf36a97d9e1a1a')[0]),
					'flag': helper.set_entry_command_string('Alt+B'),
					'description': [
						Markup('Run a syntax check'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('427fe0de13894a61bdb3fa3762f570ef')[0]),
					'flag': helper.set_entry_command_string('Alt+F'),
					'description': [
						Markup('Run a formatter/fixer/arranger'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('27b6302f4d5f40b2b8eef11eb11d5c55')[0]),
					'flag': helper.set_entry_command_string('Alt+:'),
					'description': [
						Markup('Start/stop recording of macro'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('33286d5698d2465f82dac07260c8d916')[0]),
					'flag': helper.set_entry_command_string('Alt+;'),
					'description': [
						Markup('Replay macro'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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
		'static_red': '9f549fd3005548729513b1db343da03e',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('282dcd04f5654b4587c937941d06fb60')[0]),
					'flag': helper.set_entry_command_string('Alt+A'),
					'description': [
						Markup('Turn the mark on/off'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('25ea9b69d40f43e187afa4256ed7a34c')[0]),
					'flag': helper.set_entry_command_string('Tab'),
					'description': [
						Markup('Indent marked region'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d4f3146d8b3a4166a9f1c5676d50dce9')[0]),
					'flag': helper.set_entry_command_string('Shift+Tab'),
					'description': [
						Markup('Unindent marked region'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d6d65e0361594984a8d5fb3f4cc23ab2')[0]),
					'flag': helper.set_entry_command_string('Alt+N'),
					'description': [
						Markup('Turn line numbers on/off'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('462c79979f4a420c831b97eb50c99237')[0]),
					'flag': helper.set_entry_command_string('Alt+P'),
					'description': [
						Markup('Turn visible whitespace on/off'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('28e3d10551e341e3a45ac159ec1c5ee3')[0]),
					'flag': helper.set_entry_command_string('Alt+V'),
					'description': [
						Markup('Enter next keystroke verbatim'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('207e6f212f114f5a9e59988b69770995')[0]),
					'flag': helper.set_entry_command_string('Ctrl+L'),
					'description': [
						Markup('Refresh the screen'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3f72f305e7784f0eb11915f290175ac9')[0]),
					'flag': helper.set_entry_command_string('Ctrl+Z'),
					'description': [
						Markup('Suspend nano'),
					],
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
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

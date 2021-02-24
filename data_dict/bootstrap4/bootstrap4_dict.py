import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

script_dir = os.path.dirname(__file__)
helper = Helpers('bootstrap4', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'v'
meta = {
	'title': 'Bootstrap4 Cheatsheet',
	'description': '',
	'keywords': 'frontend framework, css, css framework, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/bootstrap4/',

	'opengraph_title': 'Bootstrap4 Cheatsheet',
	'opengraph_description': '',
	'opengraph_image': '',
	'opengraph_url': 'https://www.cheatsheet.wtf/bootstrap4/',

	'twitter_title': 'Bootstrap4 Cheatsheet',
	'twitter_description': '',
	'twitter_image': '',
}
information = {
	'tool': 'Bootstrap 4',
	'title': 'Bootstrap 4 Cheatsheet',
	'subtitle': 'This site is a reference for Bootstrap',
	'description': 'Bootstrap is a high-level CSS framework directed at responsive frontend development. It is amongst the most starred projects at Github with more than 140k stars.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Bootstrap 4',
			[
				helper.characteristics.get('front-end'),
			])
	],
	'topic_uris': [
		'front-end',
	],
}
general_info_text = 'Notation'
general_info_text_lead = 'On The Use of Asterisks (*)'
general_info_links = {}
general_info = [
	Markup(
		'Whenever you see a class like <kbd>.float-*-*</kbd> the first asterisk is a replacement a class specifier (e.g. <kbd>left</kbd>) and the second is a breakpoint specifier (e.g. <kbd>md</kbd>). In action this is the same as <kbd>float-&lt;direction&gt;-&lt;breakpoint&gt;</kbd> e.g. <kbd>float-right-lg</kbd>'),
]
general_info_flag = True
see_also = [
	{
	},
]
cheatsheet = [
	{
		'heading': helper.set_folder('Breaking Points'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': 'e632eeac82e8456abd762bb7d5d3389f',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('70cf8592ed89475c8cbefc256847ec2e')[0]),
					'flag': helper.set_entry_command_string("Extra small"),
					'description': Markup('< 544px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('838884feed744c0da017875b25e5fc80')[0]),
					'flag': helper.set_entry_command_string("Small"),
					'description': Markup('≥ 544px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d0a92d49d5e64311ab5831e2450f0f5f')[0]),
					'flag': helper.set_entry_command_string("Medium"),
					'description': Markup('≥ 768px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1ddca08b6a1f4808915369a973ce28f0')[0]),
					'flag': helper.set_entry_command_string("Large"),
					'description': Markup('≥ 992px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6d6cf58c420b4d0fad81c655edb0cca4')[0]),
					'flag': helper.set_entry_command_string("Extra large"),
					'description': Markup('≥ 1200px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Colors'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': '005d5088763f4c25845a6528f3a6630e',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('87bb2cbbdb82495e8acef46331ac0be1')[0]),
					'flag': helper.set_entry_command_string("text-primary"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('127e535ff9f04e1aa4f0932c06e456e7')[0]),
					'flag': helper.set_entry_command_string("text-secondary"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c192de63afde45c59655d3e3da6bac6b')[0]),
					'flag': helper.set_entry_command_string("text-success"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('eb286bfa92de4becbec37a3b784d02ef')[0]),
					'flag': helper.set_entry_command_string("text-danger"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5be96d4adfe44089911781713f14f04f')[0]),
					'flag': helper.set_entry_command_string("text-warning"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e852f83f528044a5b07346767034d357')[0]),
					'flag': helper.set_entry_command_string("text-info"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('388643bde47a4c2e82b78898e9b63f17')[0]),
					'flag': helper.set_entry_command_string("text-light"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('de6e007b59934595bd3b84d79084aa9f')[0]),
					'flag': helper.set_entry_command_string("text-dark"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3ec06196144541a2843c9b298e585dfd')[0]),
					'flag': helper.set_entry_command_string("text-white"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a060fe83fb7f42c3a37d64c74083f6c7')[0]),
					'flag': helper.set_entry_command_string("bg-primary"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bf43393431be40a5be326234970cebcf')[0]),
					'flag': helper.set_entry_command_string("bg-secondary"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7624833fca994c5ea4a808a4cadfadc5')[0]),
					'flag': helper.set_entry_command_string("bg-success"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('856dfe092d5c44f78a33ec87e14b9fbb')[0]),
					'flag': helper.set_entry_command_string("bg-danger"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e1afac784ce14ca8bfbf2685770042e9')[0]),
					'flag': helper.set_entry_command_string("bg-warning"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2c473fa1979a40f887231b544eedda2b')[0]),
					'flag': helper.set_entry_command_string("bg-info"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bd25a378354248b787b7125ee44b3db4')[0]),
					'flag': helper.set_entry_command_string("bg-light"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d6e417c133fc4864bfc48182ebf2d333')[0]),
					'flag': helper.set_entry_command_string("bg-dark"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('99958e0489564396b590fb23b18dcb72')[0]),
					'flag': helper.set_entry_command_string("bg-white"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Buttons'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': 'c3bc5f69a59d4c3c95d8e6971d66a6e5',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ae36459b046b4d16a0a8f8aa303444e9')[0]),
					'flag': helper.set_entry_command_string("btn"),
					'description': Markup('Needs to be added to all buttons - sets margin and padding'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5dc8e89193d74d48a89c53f769ab4ad2')[0]),
					'flag': helper.set_entry_command_string("btn-*"),
					'description': Markup('Replace asterisks with any color. E.g. primary, secondary, dark. Adds color to the button'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('443931725c544405992b02a1908adcbc')[0]),
					'flag': helper.set_entry_command_string("btn-outline-*"),
					'description': Markup('Same as above but does not adds a background color to the button'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0355e4041a014b0eac62840f64dba859')[0]),
					'flag': helper.set_entry_command_string("btn-lg"),
					'description': Markup('A larger button with more padding'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4f24ac65d5564475b1c79664bc923fa1')[0]),
					'flag': helper.set_entry_command_string("btn-sm"),
					'description': Markup('A smaller button with less padding'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Typography'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': '5968dabf70d3431991f19845c8a34a5a',
		'content': {
			'descriptor': [
				'Classname',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('26b3f60e296c498f912a870b5e271eba')[0]),
					'flag': helper.set_entry_command_string("text-left"),
					'description': Markup('Left aligned text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2570653d99b649c889cd73570732e78a')[0]),
					'flag': helper.set_entry_command_string("text-center"),
					'description': Markup('Center aligned text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('334e5aa866db4ee9a7b9d7f159e99b1f')[0]),
					'flag': helper.set_entry_command_string("text-right"),
					'description': Markup('Right aligned text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2fa040c7a23f4255b5526efb05755fcd')[0]),
					'flag': helper.set_entry_command_string("text-justify"),
					'description': Markup('Justified text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e3461439c36c4698a845f6850dbe1425')[0]),
					'flag': helper.set_entry_command_string("text-nowrap"),
					'description': Markup('No wrap text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('66c7804da0b7462f9796a6deb95bc388')[0]),
					'flag': helper.set_entry_command_string("text-lowercause"),
					'description': Markup('Lowercase text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('384109e0ad1f430aa932a167ca741eb9')[0]),
					'flag': helper.set_entry_command_string("text-uppercase"),
					'description': Markup('Uppercase text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('22f1c99c1e5841eba1429e67fc737b0b')[0]),
					'flag': helper.set_entry_command_string("text-capitalize"),
					'description': Markup('Capitalized text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8cf5ce0275b54d87a30edb42bf4a0f9e')[0]),
					'flag': helper.set_entry_command_string("lead"),
					'description': Markup('Good for first paragraph of article'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5b43868375744a958667ed4ac7963f62')[0]),
					'flag': helper.set_entry_command_string("blockquote"),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('993e94b004fe47948704e2f409a0791f')[0]),
					'flag': helper.set_entry_command_string("h1 ... h6"),
					'description': Markup('This feature is useful for SEO when you want the size of a h3 header but your previous heading was a h2. Now you can accomplish that without weakening your SEO'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fd470f64cdfe4334ac7ac1438e0bc903')[0]),
					'flag': helper.set_entry_command_string("display-#"),
					'description': Markup('Display 1-4. If you need big headings. These are bigger than h1'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Lists'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': '5452db3aa5a74fbdaaa48439744f54d8',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e477e781b43342439d0de97f236f2412')[0]),
					'flag': helper.set_entry_command_string("list-unstyled"),
					'description': Markup('Removes default list margin'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d785fe7b38f649d8a4aa8038f2fa0756')[0]),
					'flag': helper.set_entry_command_string("dl-horizontal"),
					'description': Markup('Makes list items two columns'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8983edd07ea64a1e8c4cd12c6c3d646e')[0]),
					'flag': helper.set_entry_command_string("list-inline"),
					'description': Markup('Makes list items inline'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d68c5228722d43c284c7d1ab2ce417c7')[0]),
					'flag': helper.set_entry_command_string("list-inline-item"),
					'description': Markup('Added to each li'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Images'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': '55c967c7efc54e5dbdf8b12e029036a5',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('5f500ebaa76545c6abca9f0e5d33bb17')[0]),
					'flag': helper.set_entry_command_string("img-fluid"),
					'description': Markup('Make an image responsive'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('213c7250b3fc4ce28f43949a11ff4be8')[0]),
					'flag': helper.set_entry_command_string("rounded"),
					'description': Markup('Adds rounded corners to image'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c7f9c8a3a3054ad1acb6a5a8ee94cc25')[0]),
					'flag': helper.set_entry_command_string("rounded-circle"),
					'description': Markup('Crops image to be circle'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e633df5b70984caabfe035bd76a07f00')[0]),
					'flag': helper.set_entry_command_string("img-thumbnail"),
					'description': Markup('Adds rounded corner + border'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Floats'),
		'subtitle': '',
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_red': '342151637f104f62aa7747e335608c70',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2748bf105dc64160bb99688d34826c88')[0]),
					'flag': helper.set_entry_command_string("float-left"),
					'description': Markup('Floats item left'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('81c2fa10a1fe4168aacc7b65e7f60ff9')[0]),
					'flag': helper.set_entry_command_string("float-right"),
					'description': Markup('Floats item right'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1e7af54b7f074a0eab28b7a0603931ae')[0]),
					'flag': helper.set_entry_command_string("float-none"),
					'description': Markup('Removes float'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b609cad19c714c3985ae17865b8bb259')[0]),
					'flag': helper.set_entry_command_string("float-*-*"),
					'description': Markup('Add breakpoints if needed'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Starter Template'),
		'subtitle': '',
		'description': 'Copy this starter template and use it as a basis to get going instantly',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': '87ab43d3063141f5b9f2432e299db6d8',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/starter_template.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('0db8f191b9994f6e853f46d84b59b11f')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Navbar'),
		'subtitle': '',
		'description': 'Use this navbar as a starting point',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': '46575615ff8645b38c116c4cdaa58ddb',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/navbar.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('7271f44fa68d49bbbfe313041dbf6073')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Modal'),
		'subtitle': '',
		'description': 'Use this navbar as a starting point',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': 'ea9ce19172004ce4a66277d36b71ba4f',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/modal.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('2a15668b90cb4e5da7867d32ab73136e')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Forms'),
		'subtitle': '',
		'description': 'Use this navbar as a starting point',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': 'af68895ca83d46158fbc738a575a5b5a',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/forms.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('23a9e410bab9401b91b1f42d6db03f6c')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Carousel'),
		'subtitle': '',
		'description': '',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': '13cea461e37142dab558206dd2331792',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/carousel.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('fde34ab70df640c3a7be731c7ee1c004')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Responsive Embed'),
		'subtitle': '',
		'description': '',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': '41107cd61d8b4dc896ff3b648dd4a838',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/responsive-embed.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('304c1d71e7f9483e9c38e393e9f1a44e')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Tables'),
		'subtitle': '',
		'description': '',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': 'c2fdbaf5e2014fb5b4e7fe78dc7d4ed7',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/tables.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('820b1eeba1d5432ba00987a1d601ca55')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Cards'),
		'subtitle': '',
		'description': '',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': 'e3e34ae2aef2498abc6a6b6e5862ebfa',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/card.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('c59ffc8b16d04840b7f47c5afef62996')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Jumbotron'),
		'subtitle': '',
		'description': '',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': '680037e4d22d402e8c6c5ed4732725e7',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/jumbotron.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('91fc11bbffdd4e749d6fd3ed7dd9e6af')[0]),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Breadcrumbs'),
		'subtitle': '',
		'description': '',
		'columns': 'col-12',
		'language': 'html',
		'type': 'code_example',
		'uuid': helper.get_uuid(),
		'static_red': 'd3ac676ba18d444e879fa35b09242314',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'code_example': helper.read_file_content(file_path=os.path.join(script_dir, "full-width-example/breadcrumbs.html")),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_red': Markup(helper.set_entry_folder('a00fe3b70ecd4df9bc1355799bf837a3')[0]),
				},
			]
		}
	},
]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://websitesetup.org/wp-content/uploads/2020/03/Bootstrap-Cheat-Sheet-Summary-Full.png',
			'title': 'Bootstrap Cheatsheet Graphic',
			'description': Markup(''),
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

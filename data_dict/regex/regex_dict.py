import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('regex', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'regex'
meta = {
	'title': 'RegEx Cheatsheet',
	'description': '',
	'keywords': 'regex, regular expressions, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/regularexpressions/',

	'opengraph_title': 'RegEx Cheatsheet',
	'opengraph_description': '',
	'opengraph_image': '',
	'opengraph_url': 'https://www.cheatsheet.wtf/regularexpressions/',

	'twitter_title': 'RegEx Cheatsheet',
	'twitter_description': '',
	'twitter_image': '',
}
information = {
	'tool': 'Regular Expressions',
	'title': 'Regular Expressions Cheatsheet',
	'subtitle': 'This site is a reference for Regular Expressions (RegEx)',
	'description': 'Regular Expressions are powerful sequences of characters that define search patterns. Regular Expressions are used in search engines, text processing tools like Sed and Awk, for lexical analysis and a lot more. The concept of Regular Expressions arose around the 1950s and later saw heavy use with the introduction of UNIX text processing tools in the 1980s.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Regular Expressions',
			[
				helper.characteristics.get('tool'),
				helper.characteristics.get('text-processing'),
			])
	],
	'topic_uris': [
		'tool',
		'text-processing',
	],
}
general_info_text = 'Be Aware'
general_info_text_lead = Markup(
	'Syntax and Flavors')
general_info_links = {}
general_info = [
	'There are serveral flavors (different syntax) of RegExp with the two most common being POSIX and PCRE (Perl Compatible Regular Expressions). The IEEE POSIX standard has three sets of compliance which are Basic Regular Expression (BRE), Extended Regular Expressions (ERE) and Simple Regular Expressions (SRE).',
]
general_info_flag = True
see_also = [
	{
	},
]
cheatsheet = [
	{
		'heading': helper.set_folder('Regex Examples'),
		'subtitle': '',
		'description': 'Regular Expressions',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5ad5c9c7af724f208f8864ddffdb734e',
		'content': {
			'descriptor': [
				'Expression',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ce45adbceaea41e0b000a4b9ae4c3811')[0]),
					'flag': helper.set_entry_command_string('^(?:[\\t ]*(?:\\r?\\n|\\r))+'),
					'description': Markup('Match all empty lines'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Anchors'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '88e3a3330ec44ed0ab074d0fee360e41',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('4cbaaf7b826f44f89c2e1690137b8dab')[0]),
					'flag': helper.set_entry_command_string("^"),
					'description': Markup('Start of string, or start of line in multi-line pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8b5bd8ecdbf74cee889db282accafcee')[0]),
					'flag': helper.set_entry_command_string("\A"),
					'description': Markup('Start of string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6e6c0d2e9db34ad29ff946e07662c765')[0]),
					'flag': helper.set_entry_command_string("$"),
					'description': Markup('End of string, or end of line in multi-line pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bd83c4f2a10046eea813e00971e700f9')[0]),
					'flag': helper.set_entry_command_string("\Z"),
					'description': Markup('End of string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('434b5c6a14d74a2a960f01003e1ab751')[0]),
					'flag': helper.set_entry_command_string("\\b"),
					'description': Markup('Word boundary'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('03ca707f253d43eba16ad1ec876138d0')[0]),
					'flag': helper.set_entry_command_string("\B"),
					'description': Markup('Not word boundary'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8b90a3ad18fb48e68dc59a311cdf12f3')[0]),
					'flag': helper.set_entry_command_string("\<"),
					'description': Markup('Start of word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9ff54d7945ff4d76a9ac83a90125c90d')[0]),
					'flag': helper.set_entry_command_string("\>"),
					'description': Markup('End of word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Character Classes'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'e0752306c1e14b888850832ffaf0ba3a',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a7b9f7b3faf44336b4fcbe56d1dd92fe')[0]),
					'flag': helper.set_entry_command_string("\c"),
					'description': Markup('Control character'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('48c1107a0a6c4bf29376dbed6cbd715f')[0]),
					'flag': helper.set_entry_command_string("\s"),
					'description': Markup('White space'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5389949a719b4793ac447d5f354dbffe')[0]),
					'flag': helper.set_entry_command_string("\S"),
					'description': Markup('Not white space'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8aeabf29593f4bb8853b77420aca3e29')[0]),
					'flag': helper.set_entry_command_string("\d"),
					'description': Markup('Digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d92f72a319144c739e37f77ba05dc2f7')[0]),
					'flag': helper.set_entry_command_string("\D"),
					'description': Markup('Not digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5f900555e80b4c319807a009dc2ffe5f')[0]),
					'flag': helper.set_entry_command_string("\w"),
					'description': Markup('Word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cbce7122ac0d42839ce546a8d0c87057')[0]),
					'flag': helper.set_entry_command_string("\W"),
					'description': Markup('Not word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6b43a878594d4e45bfab9cec9699a9cd')[0]),
					'flag': helper.set_entry_command_string("\\x"),
					'description': Markup('Hexadecimal digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0041c33a0eb94ff8ac5eec9bea6f5efa')[0]),
					'flag': helper.set_entry_command_string("\O"),
					'description': Markup('Octal digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('POSIX'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '92fb5412621a4a55ad4c989fdcee4fb3',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('724891eb05354f649471ea1b2aabd92a')[0]),
					'flag': helper.set_entry_command_string("[:upper:]"),
					'description': Markup('Upper case letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1a6f402ffe814937a3758b06ef4193da')[0]),
					'flag': helper.set_entry_command_string("[:lower:]"),
					'description': Markup('Lower case letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('148393427bf04ee99b8f698af6469c07')[0]),
					'flag': helper.set_entry_command_string("[:alpha:]"),
					'description': Markup('All letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9b336b0eb73a472a936f9f1fa65b4f44')[0]),
					'flag': helper.set_entry_command_string("[:alnum:]"),
					'description': Markup('Digits and letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('27aa99ee42344e7ba410383b7b71d186')[0]),
					'flag': helper.set_entry_command_string("[:digit:]"),
					'description': Markup('Digits'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d3f47c9f45794e3c8907077bcfbf15c7')[0]),
					'flag': helper.set_entry_command_string("[:xdigit:]"),
					'description': Markup('Hexadecimal digits'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('222b4d33ea9941cfa25b068cfaeb94d6')[0]),
					'flag': helper.set_entry_command_string("[:punct:]"),
					'description': Markup('Punctuation'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dc863a0cb5bf4419b504fe93cd4ebe88')[0]),
					'flag': helper.set_entry_command_string("[:blank:]"),
					'description': Markup('Space and tab'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2b75a93eaa3e4c67a83aeac16da092d9')[0]),
					'flag': helper.set_entry_command_string("[:space:]"),
					'description': Markup('Blank characters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('742c002a81394d0993f5c3289d78894a')[0]),
					'flag': helper.set_entry_command_string("[:cntrl:]"),
					'description': Markup('Control characters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d3fd23d9d1304238aa06ecffa8a28c4b')[0]),
					'flag': helper.set_entry_command_string("[:graph:]"),
					'description': Markup('Printed characters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2e025bacf8ca422386e9f2b989cd7746')[0]),
					'flag': helper.set_entry_command_string("[:print:]"),
					'description': Markup('Printed characters and spaces'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('898e68f77a014e679604b265f033ec98')[0]),
					'flag': helper.set_entry_command_string("[:word:]"),
					'description': Markup('Digits, letters and underscore'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Assertions'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '84b9d28b85f5442b87843b7893b688ab',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('403e30ab81df416f884e6e4408575d53')[0]),
					'flag': helper.set_entry_command_string("?="),
					'description': Markup('Lookahead assertion'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('940f16165d7b4139ade5a5816361094f')[0]),
					'flag': helper.set_entry_command_string("?!"),
					'description': Markup('Negative lookahead'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2279ddca46b54d6092ffad7fe5a2d2f6')[0]),
					'flag': helper.set_entry_command_string("?<="),
					'description': Markup('Lookbehind assertion'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b63f72831e664a14983a0dd3ce585489')[0]),
					'flag': helper.set_entry_command_string("?!="),
					'description': Markup('Negative lookbehind'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f1078be0759b4f928a78e9629e260277')[0]),
					'flag': helper.set_entry_command_string("?<!"),
					'description': Markup('Negative lookbehind'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1124e20bdcaa4db68efef92cfafa1a80')[0]),
					'flag': helper.set_entry_command_string("?>"),
					'description': Markup('Once-only Subexpression'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d4580b534eb047c69079e2f8cf5e45b8')[0]),
					'flag': helper.set_entry_command_string("?()"),
					'description': Markup('Condition [if then]'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f78472b572a74ced8259f0c77ac6743c')[0]),
					'flag': helper.set_entry_command_string("?()|"),
					'description': Markup('Condition [if then else]'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2e57df9d031f4ccb8d4901069153dec7')[0]),
					'flag': helper.set_entry_command_string("?#"),
					'description': Markup('Comment'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Quanti­fiers'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '455861c58c3f47348a6f0bf2914873a4',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0f97fd41556243a4b12a930bce3bc1e8')[0]),
					'flag': helper.set_entry_command_string("*"),
					'description': Markup('0 or more'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fc7da0dff40548a9ad8c4e67f1070e36')[0]),
					'flag': helper.set_entry_command_string("+"),
					'description': Markup('1 or more'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fc5114297387477fad51afd36e45d8fb')[0]),
					'flag': helper.set_entry_command_string("?"),
					'description': Markup('0 or 1'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('52b942a25ffa4df0a70ce9f4426b1cb9')[0]),
					'flag': helper.set_entry_command_string("{3}"),
					'description': Markup('Exactly 3'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a6376a8f9a0d4ed285a8b92fef230c00')[0]),
					'flag': helper.set_entry_command_string("{3,}"),
					'description': Markup('3 or more'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0ae25644e6b34f2b8b6757350792ab9e')[0]),
					'flag': helper.set_entry_command_string("{,3}"),
					'description': Markup('Less than 3'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6b0e877f042b4686b6970d943adda17c')[0]),
					'flag': helper.set_entry_command_string("{3,5}"),
					'description': Markup('3, 4 or 5'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Escape Sequences'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': Markup(helper.set_entry_folder('621b958a54c64569887155a634eefa99')[0]),
		'info': {
		},
		'warning': {
			Markup('<kbd>^ [ . $ { * ( \ + ) | ? < ></kbd> are all special characters that need to be escaped if you wish to target (i.e. include) them in your search results'),
		},
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('78b956ff361045b9b79812ec4e0794cc')[0]),
					'flag': helper.set_entry_command_string("\\"),
					'description': Markup('Escape following character'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c011ee5e301b45dcbeb257c0f5606271')[0]),
					'flag': helper.set_entry_command_string("\Q"),
					'description': Markup('Begin literal sequence'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1446f64959bf46f7b151d1dcf5d78ead')[0]),
					'flag': helper.set_entry_command_string("\E"),
					'description': Markup('End literal sequence'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Special Characters'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '35042c8811784dff9a5a58a0f8cfcd6c',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a48b4df4841b42ec83e0426cf47d4a40')[0]),
					'flag': helper.set_entry_command_string("\\n"),
					'description': Markup('New line'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0eeb5f5f14d84655a98cafb0916f3155')[0]),
					'flag': helper.set_entry_command_string("\\r"),
					'description': Markup('Carriage return'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1fb2f8d0f90d47f1be02cfe4cf91a4ef')[0]),
					'flag': helper.set_entry_command_string("\\t"),
					'description': Markup('Tab'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d07798e8989b491298725cdff88d4912')[0]),
					'flag': helper.set_entry_command_string("\\v"),
					'description': Markup('Vertical tab'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('99150af2f0154b71a4bf6f4bb4750c2b')[0]),
					'flag': helper.set_entry_command_string("\\f"),
					'description': Markup('Form feed'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8492e5210fcc44bc828ce19655e112cd')[0]),
					'flag': helper.set_entry_command_string("\\xxx"),
					'description': Markup('Octal character xxx'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe83386c9dcc430dbecd1f03c60557b6')[0]),
					'flag': helper.set_entry_command_string("\\xhh"),
					'description': Markup('Hex character hh'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Groups and Ranges'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '49d54cf2b75f40448c64d8f866cb874a',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('51be690e614f4324a8ba528591d98f11')[0]),
					'flag': helper.set_entry_command_string("."),
					'description': Markup('Any character except new line (\n)'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7d75a87de9f046f796f31f18fa5cb881')[0]),
					'flag': helper.set_entry_command_string("(a|b)"),
					'description': Markup('A or b'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6beed5865164473d85d09624aa04afeb')[0]),
					'flag': helper.set_entry_command_string("(...)"),
					'description': Markup('Capture group'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6164efe30b8a4a6c89faac9d1a4505e0')[0]),
					'flag': helper.set_entry_command_string("(?:...)"),
					'description': Markup('Passive (non-capturing) group'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6a6391b80e9249f29e72f9d47546d39a')[0]),
					'flag': helper.set_entry_command_string("[abc]"),
					'description': Markup('Range (a or b or c)'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a8da6c98596446c7938f910986569cb5')[0]),
					'flag': helper.set_entry_command_string("[^abc]"),
					'description': Markup('Not (a or b or c)'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6cea9904d64e419aaaf221b0c33e007a')[0]),
					'flag': helper.set_entry_command_string("[a-q]"),
					'description': Markup('Lower case letter from a to q'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b1e1ffe487d245be81c26484f214e65e')[0]),
					'flag': helper.set_entry_command_string("[A-Q]"),
					'description': Markup('Upper case letter from A to Q'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a619b1d75cce4100bc5b3e311c0fc310')[0]),
					'flag': helper.set_entry_command_string("[0-7]"),
					'description': Markup('Digit from 0 to 7'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('db7b580ea7e1443c83a4ba805a294c15')[0]),
					'flag': helper.set_entry_command_string("\\x"),
					'description': Markup('Group/subpattern number "x"'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Pattern Modifiers'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'info': {
			Markup('All modifiers (except <kbd>g</kbd>) in this table are Perl Compliant Regex (PCRE) modifiers and not POSIX compliant'),
		},
		'uuid': helper.get_uuid(),
		'static_red': '0f7e353f51af4d42ac8ddedc5cf3b13d',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('432a06db43694683bab626a51e2872df')[0]),
					'flag': helper.set_entry_command_string("g"),
					'description': Markup('Global match'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3286eae8f84c4448895f57eb0000b901')[0]),
					'flag': helper.set_entry_command_string("i"),
					'description': Markup('Case-insensitive'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('337b243295a3408486be47f76dd966ef')[0]),
					'flag': helper.set_entry_command_string("m"),
					'description': Markup('Multiple lines'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('329bc4e1ca6e4cfe82c04b92a3ce6997')[0]),
					'flag': helper.set_entry_command_string("s"),
					'description': Markup('Treat string as single line'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2b36e43ed9174610b98d9a6383b2cd8d')[0]),
					'flag': helper.set_entry_command_string("x"),
					'description': Markup('Allow comments and whitespace in pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('10dbf6d3f6e54f8c83a4709550361bd8')[0]),
					'flag': helper.set_entry_command_string("e"),
					'description': Markup('Evaluate replacement'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('54a882ffdc5e41fb87161e2dcf90f3fc')[0]),
					'flag': helper.set_entry_command_string("U"),
					'description': Markup('Ungreedy pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('String Replacement'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '3c4325e48aae477e8fe537186a41f551',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0cd5eb426f574f83924e1e534a49f3db')[0]),
					'flag': helper.set_entry_command_string("$n"),
					'description': Markup('Nth non-pa­ssive group'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5a5c516999ae402ebd2cec442ca760e1')[0]),
					'flag': helper.set_entry_command_string("$2"),
					'description': Markup('"xyz" in /^(abc(xyz))$/'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ab870da397bc407abdca91e02a646cc7')[0]),
					'flag': helper.set_entry_command_string("$1"),
					'description': Markup('"xyz" in /^(?:abc)(xyz)$/'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('074c4b9479cd42d99c0cbd4565915b3c')[0]),
					'flag': helper.set_entry_command_string("$`"),
					'description': Markup('Before matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2721104fd47544d19f21d9b621d405e7')[0]),
					'flag': helper.set_entry_command_string("$'"),
					'description': Markup('After matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('75dcb2fc339b44a6b7abdd47a096ba79')[0]),
					'flag': helper.set_entry_command_string("$+"),
					'description': Markup('Last matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0a7fde406a004bc6a32152511ffcc84a')[0]),
					'flag': helper.set_entry_command_string("$&"),
					'description': Markup('Entire matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
]
resources = [
]
affiliate_products = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'title': Markup('Regular Expressions'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/0596528124/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0596528124&linkCode=as2&tag=cheatsheet0e-20&linkId=37513b0fdad1fdefef35880ffbd80b74"><img style="max-height:150px; max-width: 150px;"border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0596528124&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=0596528124" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Great addition to your library - pretty much a go-to for anything related to regular expressions!'),
			'description': '',
		}
	)
]
licensing = [
	Markup('')
]

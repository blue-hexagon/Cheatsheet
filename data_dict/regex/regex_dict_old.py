import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('regex', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'regex'
information = {
	'tool': 'Regular Expressions',
	'title': 'Regular Expressions Cheatsheet',
	'subtitle': 'This site is a reference for Regular Expressions (RegEx)',
	'description': 'Regular Expressions are powerful sequences of characters that define search patterns. Regular Expressions are used in search engines, text processing tools like Sed and Awk, for lexical analysis and a lot more. The concept of Regular Expressions arose around the 1950s and later saw heavy use with the introduction of UNIX text processing tools in the 1980s.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
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
		'heading': helper.set_folder('Anchors'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("^")[0]),
					'description': Markup('Start of string, or start of line in multi-line pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\A")[0]),
					'description': Markup('Start of string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$")[0]),
					'description': Markup('End of string, or end of line in multi-line pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\Z")[0]),
					'description': Markup('End of string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\b")[0]),
					'description': Markup('Word boundary'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\B")[0]),
					'description': Markup('Not word boundary'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\<")[0]),
					'description': Markup('Start of word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\>")[0]),
					'description': Markup('End of word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("\c")[0]),
					'description': Markup('Control character'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\s")[0]),
					'description': Markup('White space'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\S")[0]),
					'description': Markup('Not white space'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\d")[0]),
					'description': Markup('Digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\D")[0]),
					'description': Markup('Not digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\w")[0]),
					'description': Markup('Word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\W")[0]),
					'description': Markup('Not word'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\x")[0]),
					'description': Markup('Hexadecimal digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\O")[0]),
					'description': Markup('Octal digit'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("[:upper:]")[0]),
					'description': Markup('Upper case letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:lower:]")[0]),
					'description': Markup('Lower case letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:alpha:]")[0]),
					'description': Markup('All letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:alnum:]")[0]),
					'description': Markup('Digits and letters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:digit:]")[0]),
					'description': Markup('Digits'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:xdigit:]")[0]),
					'description': Markup('Hexadecimal digits'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:punct:]")[0]),
					'description': Markup('Punctuation'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:blank:]")[0]),
					'description': Markup('Space and tab'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:space:]")[0]),
					'description': Markup('Blank characters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:cntrl:]")[0]),
					'description': Markup('Control characters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:graph:]")[0]),
					'description': Markup('Printed characters'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:print:]")[0]),
					'description': Markup('Printed characters and spaces'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[:word:]")[0]),
					'description': Markup('Digits, letters and underscore'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("?=")[0]),
					'description': Markup('Lookahead assertion'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?!")[0]),
					'description': Markup('Negative lookahead'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?<=")[0]),
					'description': Markup('Lookbehind assertion'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?!=")[0]),
					'description': Markup('Negative lookbehind'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?<!")[0]),
					'description': Markup('Negative lookbehind'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?>")[0]),
					'description': Markup('Once-only Subexpression'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?()")[0]),
					'description': Markup('Condition [if then]'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?()|")[0]),
					'description': Markup('Condition [if then else]'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?#")[0]),
					'description': Markup('Comment'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("*")[0]),
					'description': Markup('0 or more'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("+")[0]),
					'description': Markup('1 or more'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("?")[0]),
					'description': Markup('0 or 1'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("{3}")[0]),
					'description': Markup('Exactly 3'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("{3,}")[0]),
					'description': Markup('3 or more'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("{,3}")[0]),
					'description': Markup('Less than 3'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("{3,5}")[0]),
					'description': Markup('3, 4 or 5'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
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
					'flag': Markup(helper.set_entry_folder("\\")[0]),
					'description': Markup('Escape following character'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\Q")[0]),
					'description': Markup('Begin literal sequence'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\E")[0]),
					'description': Markup('End literal sequence'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("\\n")[0]),
					'description': Markup('New line'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\r")[0]),
					'description': Markup('Carriage return'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\t")[0]),
					'description': Markup('Tab'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\v")[0]),
					'description': Markup('Vertical tab'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\f")[0]),
					'description': Markup('Form feed'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\xxx")[0]),
					'description': Markup('Octal character xxx'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\xhh")[0]),
					'description': Markup('Hex character hh'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(".")[0]),
					'description': Markup('Any character except new line (\n)'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("(a|b)")[0]),
					'description': Markup('A or b'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("(...)")[0]),
					'description': Markup('Capture group'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("(?:...)")[0]),
					'description': Markup('Passive (non-capturing) group'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[abc]")[0]),
					'description': Markup('Range (a or b or c)'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[^abc]")[0]),
					'description': Markup('Not (a or b or c)'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[a-q]")[0]),
					'description': Markup('Lower case letter from a to q'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[A-Q]")[0]),
					'description': Markup('Upper case letter from A to Q'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("[0-7]")[0]),
					'description': Markup('Digit from 0 to 7'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("\\x")[0]),
					'description': Markup('Group/subpattern number "x"'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("g")[0]),
					'description': Markup('Global match'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("i")[0]),
					'description': Markup('Case-insensitive'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("m")[0]),
					'description': Markup('Multiple lines'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("s")[0]),
					'description': Markup('Treat string as single line'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("x")[0]),
					'description': Markup('Allow comments and whitespace in pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("e")[0]),
					'description': Markup('Evaluate replacement'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("U")[0]),
					'description': Markup('Ungreedy pattern'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("$n")[0]),
					'description': Markup('Nth non-pa­ssive group'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$2")[0]),
					'description': Markup('"xyz" in /^(abc(xyz))$/'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$1")[0]),
					'description': Markup('"xyz" in /^(?:abc)(xyz)$/'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$`")[0]),
					'description': Markup('Before matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$'")[0]),
					'description': Markup('After matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$+")[0]),
					'description': Markup('Last matched string'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("$&")[0]),
					'description': Markup('Entire matched string'),
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
			'link': 'https://www.perlmonks.org/bare/?node_id=558868',
			'title': 'Perl Monks - The craziest RegExes you ever created',
			'description': Markup('Insane Regular Expressions'),
			'footer': Markup('Mentioning Perl and regex in the same sentence.. You know it\'s going to get crazy'),
			'screencapture': ''
		},
	)
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

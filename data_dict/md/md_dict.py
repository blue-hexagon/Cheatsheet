import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('md', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'md'
meta = {
	'title': 'Markdown Cheatsheet',
	'description': 'Headings · Emphasis · Links · Blockquotes · Code · Lists',
	'keywords': 'markdown, markup, md, readme.md, syntax, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/markdown/',

	'opengraph_title': 'Markdown Cheatsheet',
	'opengraph_description': 'Headings · Emphasis · Links · Blockquotes · Code · Lists',
	'opengraph_image': 'opengraph_markdown.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/markdown/',

	'twitter_title': 'Markdown Cheatsheet',
	'twitter_description': 'Headings · Emphasis · Links · Blockquotes · Code · Lists',
	'twitter_image': 'twitter_card_markdown.png',
}
information = {
	'tool': 'Markdown',
	'title': 'Markdown Cheatsheet',
	'subtitle': 'This site is a reference for Markdown',
	'description': 'Markdown is a lightweight markup language with plain-text-formatting syntax. It was created in 2004. Markdown, also referred to simply as md, are often used in readme files for writing messages on online-discussion forums and to create rich text in simple texteditors.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Markdown',
			[
				helper.characteristics.get('markup-language'),
			])
	],
	'topic_uris': [
		'markup-language',
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
cheatsheet = [
	{
		'heading': helper.set_folder('Heading'),
		'subtitle': 'How to Write Headings in Markdown',
		'description': 'Everything starts with proper sectioning of your content.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '8bbb5f9731c848a9b2c7734db232a355',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('7e1803020d83438bb46d76e942b029b6')[0]),
					'flag': Markup(helper.set_entry_command_string("# Heading")),
					'description': Markup('Equivalent to &lt;h1&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b825e12e7b214f3badb24895da06434c')[0]),
					'flag': Markup(helper.set_entry_command_string('## Sub heading')),
					'description': Markup('Equivalent to &lt;h2&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1866aa4620ef40a6aff74962a4196771')[0]),
					'flag': Markup(helper.set_entry_command_string('### Sub-sub heading')),
					'description': Markup('Equivalent to &lt;h3&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3cd4ed1ecb6a4bf0ab18797c5a58f5e4')[0]),
					'flag': Markup(helper.set_entry_command_string('#### Fourth level heading')),
					'description': Markup('Equivalent to &lt;h4&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b87598ddfbf24bef85d64e004c859a8b')[0]),
					'flag': Markup(helper.set_entry_command_string('##### Fifth level heading')),
					'description': Markup('Equivalent to &lt;h5&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1bf8aa8253064356b4ce6ede56f988d1')[0]),
					'flag': Markup(helper.set_entry_command_string('####### Sixth and last level')),
					'description': Markup('Equivalent to &lt;h6&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3ef9d153d2ae46008090300c617b9652')[0]),
					'flag': Markup(helper.set_entry_command_string('Woah, that\'s kewl</kbd><br><kbd>=================')),
					'description': Markup('Alternative level one heading'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f526119723c24ec59f2353425c0d8498')[0]),
					'flag': Markup(helper.set_entry_command_string('Pretty cool sub-heading!</kbd><br><kbd>------------------------')),
					'description': Markup('Alternative level two heading'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Emphasis'),
		'subtitle': '',
		'description': 'How to use emphasis in markdown',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f5916cf850b64850a94d1e550f24ae91',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6e0bae90b3ea4a70ad17f41c25bf9b4c')[0]),
					'flag': Markup(helper.set_entry_command_string('*text*')),
					'description': Markup('Makes the text italic'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bcb2f80883ee4caaac040c5ef6446e90')[0]),
					'flag': Markup(helper.set_entry_command_string('_text_')),
					'description': Markup('Makes the text italic'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3eaf4e13845e44d4ab95a748bef231fe')[0]),
					'flag': Markup(helper.set_entry_command_string('**text**')),
					'description': Markup('Makes the text bold'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0b0218be5ebf463989c39e4af5cb6ec0')[0]),
					'flag': Markup(helper.set_entry_command_string('__text__')),
					'description': Markup('Makes the text bold'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('800f5e85483d480bb0f419fa4c01bbf5')[0]),
					'flag': Markup(helper.set_entry_command_string('`code  text`')),
					'description': Markup('Used for emphasising code'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Lists'),
		'subtitle': '',
		'description': 'How to write lists in markdown',
		'columns': 'col-lg-6 col-md-12',
		'info': {
			'Lists can be nested.'
		},
		'uuid': helper.get_uuid(),
		'static_red': '9633fa3691f14cc9a4ac4f7ed4591a0d',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('db985fc74737410ebdd36791a1aba0b0')[0]),
					'flag': Markup(helper.set_entry_command_string('* List item')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bc8b3ea8da5e40b2a639cf24eeb334f9')[0]),
					'flag': Markup(helper.set_entry_command_string('- List item')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0e5fbd90b5d84fb79777d140abecfd28')[0]),
					'flag': Markup(helper.set_entry_command_string('- [ ] Checkbox (not checked)')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('31ec2b67a0934894b7103e350374c86a')[0]),
					'flag': Markup(helper.set_entry_command_string('- [x] Checkbox item (checked)')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('81f987b8c783455eb83cd41c284b3092')[0]),
					'flag': Markup(helper.set_entry_command_string('&lt;number&gt;. Numbered list item')),
					'description': Markup('Enumerated list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Images'),
		'subtitle': '.',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd72235051b9c44d5a8134f9603da7f19',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('d4ba4777676e495cae4b9bbf964eb839')[0]),
					'flag': Markup(helper.set_entry_command_string('![Image alt text](/path/to/img.jpg)')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0e987154a43e426c8ab202016e7fe21b')[0]),
					'flag': Markup(helper.set_entry_command_string('![Image alt text](/path/to/img.jpg "title")')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce9cb97e8db44d0b953c3a2c2e45690a')[0]),
					'flag': Markup(helper.set_entry_command_string('![Image alt text][img]')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4f0d6c376b924fa9b4c3351db999a294')[0]),
					'flag': Markup(helper.set_entry_command_string('[img]: http://foo.com/img.jpg')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Links'),
		'subtitle': 'Subheading.',
		'description': 'Description',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '100d85cef84e428fa9b521bf8b6e89fb',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('481b3845595644fe9e13e44512ab1735')[0]),
					'flag': Markup(helper.set_entry_command_string('[link](http://google.com)')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7e0c13e929a949e7bcbf84a83f64b626')[0]),
					'flag': Markup(helper.set_entry_command_string('[link][google]</kbd><br><kbd>[google]:&nbsp;http://google.com')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('04f0e95c47e64cdb87d29b663f3825e4')[0]),
					'flag': Markup(helper.set_entry_command_string('&lt;http://google.com&gt;')),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Horizontal Line'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'info': {
			'A minimum of three asterisks or dashes are required - use as many as you like. The asterisks and dashes may be seperated by spaces if you wish.'
		},
		'uuid': helper.get_uuid(),
		'static_red': '14cd5ca3899b479d986d3d4a2e3e5155',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('f665e891c01c40bcaeecbf474a1774e3')[0]),
					'flag': Markup(helper.set_entry_command_string('----')),
					'description': Markup('Makes a horizontal line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5f7b03fbcbe447cc857eafbb6a16b67d')[0]),
					'flag': Markup(helper.set_entry_command_string('****')),
					'description': Markup('Makes a horizontal line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Blockquote'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '600f6a30afcd402b84e6d6f05cdaf360',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('851d2ed14e1c491180b8310a7daccce5')[0]),
					'flag': Markup(helper.set_entry_command_string('>[>>>]')),
					'description': Markup('Used for blockquots. Starts with one and is increased by one > for each nested level.'),
					'example': helper.example_path(),
					'ext_link': '',
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
			'link': 'https://daringfireball.net/projects/markdown/syntax',
			'title': 'Caveats of Markdown',
			'description': Markup('A very detailed breakdown of various aspects'),
			'footer': Markup('Worth a read'),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

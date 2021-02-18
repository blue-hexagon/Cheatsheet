import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('md', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'md'
information = {
	'tool': 'Markdown',
	'title': 'Markdown Cheatsheet',
	'subtitle': 'This site is a reference for Markdown',
	'description': 'Markdown is a lightweight markup language with plain-text-formatting syntax. It was created in 2004. Markdown, also referred to simply as md, are often used in readme files for writing messages on online-discussion forums and to create rich text in simple texteditors.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '⚠',

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
	'',
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("# Heading")[0]),
					'description': Markup('Equivalent to &lt;h1&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('## Sub heading')[0]),
					'description': Markup('Equivalent to &lt;h2&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('### Sub-sub heading')[0]),
					'description': Markup('Equivalent to &lt;h3&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('#### Fourth level heading')[0]),
					'description': Markup('Equivalent to &lt;h4&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('##### Fifth level heading')[0]),
					'description': Markup('Equivalent to &lt;h5&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('####### Sixth and last level')[0]),
					'description': Markup('Equivalent to &lt;h6&gt; in HTML'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Woah, that\'s kewl</kbd><br><kbd>=================')[0]),
					'description': Markup('Alternative level one heading'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Pretty cool sub-heading!</kbd><br><kbd>------------------------')[0]),
					'description': Markup('Alternative level two heading'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('*text*')[0]),
					'description': Markup('Makes the text italic'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('_text_')[0]),
					'description': Markup('Makes the text italic'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('**text**')[0]),
					'description': Markup('Makes the text bold'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('__text__')[0]),
					'description': Markup('Makes the text bold'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('`code  text`')[0]),
					'description': Markup('Used for emphasising code'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('* List item')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('- List item')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('- [ ] Checkbox (not checked)')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('- [x] Checkbox item (checked)')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&lt;number&gt;. Numbered list item')[0]),
					'description': Markup('Enumerated list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('![Image alt text](/path/to/img.jpg)')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('![Image alt text](/path/to/img.jpg "title")')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('![Image alt text][img]')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[img]: http://foo.com/img.jpg')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('[link](http://google.com)')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[link][google]</kbd><br><kbd>[google]:&nbsp;http://google.com')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&lt;http://google.com&gt;')[0]),
					'description': Markup('Command description'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('----')[0]),
					'description': Markup('Makes a horizontal line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('****')[0]),
					'description': Markup('Makes a horizontal line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('&gt; This is a block quote</kbd><br><kbd>&gt; This is another line</kbd><br><kbd>&gt; This is another line</kbd><br><kbd>&gt;&gt; They can be nested</kbd><br><kbd>&gt;&gt; They can be nested</kbd>')[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
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

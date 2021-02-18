import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

script_dir = os.path.dirname(__file__)
helper = Helpers('bootstrap4', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'v'
information = {
	'tool': 'Bootstrap 4',
	'title': 'Bootstrap 4 Cheatsheet',
	'subtitle': 'This site is a reference for Bootstrap',
	'description': '',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '⚠',

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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("Extra small")[0]),
					'description': Markup('< 544px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Small")[0]),
					'description': Markup('≥ 544px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Medium")[0]),
					'description': Markup('≥ 768px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Large")[0]),
					'description': Markup('≥ 992px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Extra large")[0]),
					'description': Markup('≥ 1200px'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("text-primary")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-secondary")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-success")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-danger")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-warning")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-info")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-light")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-dark")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-white")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-primary")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-secondary")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-success")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-danger")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-warning")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-info")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-light")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-dark")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("bg-white")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("btn")[0]),
					'description': Markup('Needs to be added to all buttons - sets margin and padding'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("btn-*")[0]),
					'description': Markup('Replace asterisks with any color. E.g. primary, secondary, dark. Adds color to the button'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("btn-outline-*")[0]),
					'description': Markup('Same as above but does not adds a background color to the button'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("btn-lg")[0]),
					'description': Markup('A larger button with more padding'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("btn-sm")[0]),
					'description': Markup('A smaller button with less padding'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Classname',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("text-left")[0]),
					'description': Markup('Left aligned text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-center")[0]),
					'description': Markup('Center aligned text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-right")[0]),
					'description': Markup('Right aligned text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-justify")[0]),
					'description': Markup('Justified text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-nowrap")[0]),
					'description': Markup('No wrap text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-lowercause")[0]),
					'description': Markup('Lowercase text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-uppercase")[0]),
					'description': Markup('Uppercase text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("text-capitalize")[0]),
					'description': Markup('Capitalized text'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("lead")[0]),
					'description': Markup('Good for first paragraph of article'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("blockquote")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("h1 ... h6")[0]),
					'description': Markup('This feature is useful for SEO when you want the size of a h3 header but your previous heading was a h2. Now you can accomplish that without weakening your SEO'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("display-#")[0]),
					'description': Markup('Display 1-4. If you need big headings. These are bigger than h1'),
					'example': helper.example_path(),
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
		'description': '',
		'columns': '',
		'type': 'card_list',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("list-unstyled")[0]),
					'description': Markup('Removes default list margin'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("dl-horizontal")[0]),
					'description': Markup('Makes list items two columns'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("list-inline")[0]),
					'description': Markup('Makes list items inline'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("list-inline-item")[0]),
					'description': Markup('Added to each li'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("img-fluid")[0]),
					'description': Markup('Make an image responsive'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("rounded")[0]),
					'description': Markup('Adds rounded corners to image'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("rounded-circle")[0]),
					'description': Markup('Crops image to be circle'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("img-thumbnail")[0]),
					'description': Markup('Adds rounded corner + border'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Syntax',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("float-left")[0]),
					'description': Markup('Floats item left'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("float-right")[0]),
					'description': Markup('Floats item right'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("float-none")[0]),
					'description': Markup('Removes float'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("float-*-*")[0]),
					'description': Markup('Add breakpoints if needed'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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
		'static_ref': '',
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
					'static_ref': ''
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

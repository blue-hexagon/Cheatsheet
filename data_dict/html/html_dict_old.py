import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('html', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'html'
information = {
	'tool': 'HTML5',
	'title': 'HTML5 Cheatsheet',
	'subtitle': 'This site is a reference for HTML.',
	'description': 'HTML is a markup language used for webpages; it is the original language for designing webpages and can be (and most often is) assisted by technologies such as CSS (Cascading Style Sheets) and Javascript. It was initially released in 1993.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'HTML5',
			[
				helper.characteristics.get('markup-language'),
				helper.characteristics.get('web-development'),
			])
	],
	'topic_uris': [
		'markup-language',
		'web-development',
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
		'heading': helper.set_folder('Basic'),
		'subtitle': 'The most basic tags',
		'description': 'These are the most essential tags.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;!DOCTYPE&gt;")[0]),
					'description': Markup('Defines the document type'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;html&gt;")[0]),
					'description': Markup('Defines an HTML document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;head&gt;")[0]),
					'description': Markup('Contains metadata/information for the document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;title&gt;")[0]),
					'description': Markup('Defines a title for the document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;body&gt;")[0]),
					'description': Markup('Defines the document\'s body'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;p&gt;")[0]),
					'description': Markup('Defines a paragraph'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;h1&gt; ... &lt;h6&gt;")[0]),
					'description': Markup('Defines hiearchial headings; first heading should always be h1!'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;br&gt;")[0]),
					'description': Markup('Inserts a single line break'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;hr&gt;")[0]),
					'description': Markup('Horizontal ruler. Basically a horizontal border'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;!--your text--&gt;")[0]),
					'description': Markup('This is how you make a comment'),
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
		'heading': helper.set_folder('Formatting'),
		'subtitle': 'Formatting of text.',
		'description': 'Semantic tags for defining the text-elements. Good to know.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;abbr&gt;")[0]),
					'description': Markup('Defines an abbreviation or an acronym'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;address&gt;")[0]),
					'description': Markup('Defines contact information for the author/owner of a document/article'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;b&gt;")[0]),
					'description': Markup('Defines bold text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;bdi&gt;")[0]),
					'description': Markup('Isolates a part of text that might be formatted in a different direction from other text outside it'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;bdp&gt;")[0]),
					'description': Markup('Overrides the current text direction'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;blockquote&gt;")[0]),
					'description': Markup('Defines a section that is quoted from another source'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;cite&gt;")[0]),
					'description': Markup('Defines the title of a work'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;code&gt;")[0]),
					'description': Markup('Defines a piece of computer code'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;del&gt;")[0]),
					'description': Markup('Defines text that has been deleted from a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;dfn&gt;")[0]),
					'description': Markup('Specifies a term that is going to be defined within the content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;em&gt;")[0]),
					'description': Markup('Defines emphasized text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;i&gt;")[0]),
					'description': Markup('Defines a part of text in italics'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;ins&gt;")[0]),
					'description': Markup('Defines a text that has been inserted into a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;kbd&gt;")[0]),
					'description': Markup('Defines keyboard input'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;mark&gt;")[0]),
					'description': Markup('Defines marked/highlighted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;meter&gt;")[0]),
					'description': Markup('Defines a scalar measurement within a known range (a gauge)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;pre&gt;")[0]),
					'description': Markup('Defines preformatted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;progress&gt;")[0]),
					'description': Markup('Represents the progress of a task'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;q&gt;")[0]),
					'description': Markup('Defines a short quotation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;rp&gt;")[0]),
					'description': Markup('Defines what to show in browsers that do not support ruby annotations (see ruby tag, for what ruby is)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;rt&gt;")[0]),
					'description': Markup('Defines an explanation/pronunciation of characters (for East Asian typography)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;ruby&gt;")[0]),
					'description': Markup('Defines a ruby annotation. Ruby annotations are used for East Asian typography'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;s&gt;")[0]),
					'description': Markup('Defines a strikethrough text; used for marking something that is no longer correct'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;samp&gt;")[0]),
					'description': Markup('Defines sample output from a computer program'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;small&gt;")[0]),
					'description': Markup('Defines smaller-sized text for e.g. form-names laid above an input field'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;strong&gt;")[0]),
					'description': Markup('Defines important text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;sub&gt;")[0]),
					'description': Markup('Defines subscripted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;sup&gt;")[0]),
					'description': Markup('Defines superscripted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;template&gt;")[0]),
					'description': Markup('Defines a container for content that should be hidden when the page loads'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;time&gt;")[0]),
					'description': Markup('Defines a specific time (or datetime)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;u&gt;")[0]),
					'description': Markup('Defines some text that is unarticulated and styled differently from normal text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;var&gt;")[0]),
					'description': Markup('Defines a variable'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;wbr&gt;")[0]),
					'description': Markup('Defines a possible line-break'),
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
		'heading': helper.set_folder('Forms and Input'),
		'subtitle': 'Form and Input tags',
		'description': 'These elements are crucial in HTML',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;form&gt;")[0]),
					'description': Markup('Defines an HTML form for user input'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;input&gt;")[0]),
					'description': Markup('Defines an input control'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;textarea&gt;")[0]),
					'description': Markup('Defines a multiline input control (text area)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;button&gt;")[0]),
					'description': Markup('Defines a clickable button'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;select&gt;")[0]),
					'description': Markup('Defines a drop-down list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;optgroup&gt;")[0]),
					'description': Markup('Defines a group of related options in a drop-down list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;option&gt;")[0]),
					'description': Markup('Defines an option in a drop-down list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;label&gt;")[0]),
					'description': Markup('Defines a label for an &lt;input&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;fieldset&gt;")[0]),
					'description': Markup('Groups related elements in a form'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;legend&gt;")[0]),
					'description': Markup('Defines a caption for a &lt;fieldset&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;datalist&gt;")[0]),
					'description': Markup('Specifies a list of pre-defined options for input controls'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;output&gt;")[0]),
					'description': Markup('Defines the result of a calculation'),
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
		'heading': helper.set_folder('Frames'),
		'subtitle': 'How to Embed iFrame in HTML',
		'description': 'Artefact from previous HTML standards. Lets you embed a webpage inside another webpage.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;iframe&gt;")[0]),
					'description': Markup('Defines an inline frame'),
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
		'subtitle': 'Handling Graphics with HTML',
		'description': 'This is more than mere images - some of these tags are very powerful and useful',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;img&gt;")[0]),
					'description': Markup('Defines an image'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;map&gt;")[0]),
					'description': Markup('Defines a client-side image map'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;area&gt;")[0]),
					'description': Markup('Defines an area inside an image map'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;canvas&gt;")[0]),
					'description': Markup('Used to draw graphics, on the fly, via scripting (usually JavaScript)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;figcaption&gt;")[0]),
					'description': Markup('Defines a caption for a &gt;figure&lt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;figure&gt;")[0]),
					'description': Markup('Specifies self-contained content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;picture&gt;")[0]),
					'description': Markup('Defines a container for multiple image resources'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;svg&gt;")[0]),
					'description': Markup('Defines a container for SVG graphics'),
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
		'heading': helper.set_folder('Audio/Video'),
		'subtitle': 'Media in HTML',
		'description': 'Properly very niche',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;audio&gt;")[0]),
					'description': Markup('Defines sound content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;source&gt;")[0]),
					'description': Markup('Defines multiple media resources for media elements (&lt;video&gt;, &lt;audio&gt; and &lt;picture&gt;)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;video&gt;")[0]),
					'description': Markup('Defines a video or movie'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;track&gt;")[0]),
					'description': Markup('Defines text tracks for media elements (&lt;video&gt; and &lt;audio&gt;)'),
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
		'subtitle': 'How to make hyperlinks in HTML',
		'description': 'Crucial part of HTML is linking pages',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;a&gt;")[0]),
					'description': Markup('Defines a hyperlink'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;link&gt;")[0]),
					'description': Markup('Defines the relationship between a document and an external resource (most used to link to style sheets)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;nav&gt;")[0]),
					'description': Markup('Defines navigation links'),
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
		'heading': helper.set_folder('List'),
		'subtitle': 'How to use lists in HTML',
		'description': 'Very essential aspect of HTML is the use of ordered and unordered lists. In many CSS frameworks lists are used for menus.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;ul&gt;")[0]),
					'description': Markup('Defines an unordered list. You use &lt;li&gt; elements inside'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;ol&gt;")[0]),
					'description': Markup('Defines an ordered list. You use &lt;li&gt; elements inside'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;li&gt;")[0]),
					'description': Markup('Defines a list item. Must be encapsulated by &lt;ul&gt; or &lt;ol&gt; tags'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;dl&gt;")[0]),
					'description': Markup('Defines a description list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;dt&gt;")[0]),
					'description': Markup('Defines a term/name in a description list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;dd&gt;")[0]),
					'description': Markup('Defines a description of a term/name in a description list'),
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
		'heading': helper.set_folder('Tables'),
		'subtitle': 'How to make tables in HTML',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;table&gt;")[0]),
					'description': Markup('Defines a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;caption&gt;")[0]),
					'description': Markup('Defines a table caption'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;th&gt;")[0]),
					'description': Markup('Defines a header cell in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;tr&gt;")[0]),
					'description': Markup('Defines a row in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;td&gt;")[0]),
					'description': Markup('Defines a cell in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;thead&gt;")[0]),
					'description': Markup('Groups the header content in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;tbody&gt;")[0]),
					'description': Markup('Groups the body content in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;tfoot&gt;")[0]),
					'description': Markup('Groups the footer content in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;col&gt;")[0]),
					'description': Markup('Specifies column properties for each column within a &lt;colgroup&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;colgroup&gt;")[0]),
					'description': Markup('Specifies a group of one or more columns in a table for formatting'),
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
		'heading': helper.set_folder('Styles and Semantics'),
		'subtitle': 'Semantics of HTML',
		'description': 'Not so important as it used to be; grasping the essential structure however is beneficient.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;style&gt;")[0]),
					'description': Markup('Defines style information for a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;div&gt;")[0]),
					'description': Markup('Defines a section in a document. Used as a de-facto container for any type of content by adding CSS class names to the tag and encapsulating other elements'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;span&gt;")[0]),
					'description': Markup('Defines an inline-section in a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;header&gt;")[0]),
					'description': Markup('Defines a header for a document or section'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;footer&gt;")[0]),
					'description': Markup('Defines a footer for a document or section'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;main&gt;")[0]),
					'description': Markup('Specifies the main content of a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;section&gt;")[0]),
					'description': Markup('Defines a section in a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;article&gt;")[0]),
					'description': Markup('Defines an article'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;aside&gt;")[0]),
					'description': Markup('Defines content aside from the page content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;details&gt;")[0]),
					'description': Markup('Defines additional details that the user can view or hide'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;dialog&gt;")[0]),
					'description': Markup('Defines a dialog box or window'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;summary&gt;")[0]),
					'description': Markup('Defines a visible heading for a &lt;details&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;data&gt;")[0]),
					'description': Markup('Adds a machine-readable translation of a given content'),
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
		'heading': helper.set_folder('Meta Info'),
		'subtitle': 'Meta Tags and Information in HTML',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;head&gt;")[0]),
					'description': Markup('Defines information about the document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;meta&gt;")[0]),
					'description': Markup('Defines metadata about an HTML document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;base&gt;")[0]),
					'description': Markup('Specifies the base URL/target for all relative URLs in a document'),
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
		'heading': helper.set_folder('Programming'),
		'subtitle': 'The us of Objects and Scripts for Programming in HTML',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("&lt;script&gt;")[0]),
					'description': Markup('Defines a client-side script'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("&lt;noscript&gt;")[0]),
					'description': Markup('Defines an alternate content for users that do not support client-side scripts'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;embed&gt;")[0]),
					'description': Markup('Defines a container for an external (non-HTML) application'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;object&gt;")[0]),
					'description': Markup('Defines an embedded object'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("&lt;param&gt;")[0]),
					'description': Markup('Defines a parameter for an object'),
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
			'link': 'http://info.cern.ch/hypertext/WWW/TheProject.html',
			'title': 'World Wide Web',
			'description': Markup('The first website ever. Published in Aug. 1991 by Tim Berners-Lee; this is what the Internet looked like at the beginning'),
			'footer': Markup('Incredible 😎'),
			'screencapture': ''
		},

	)
]
licensing = [
	Markup('')
]

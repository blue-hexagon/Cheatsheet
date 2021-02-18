import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

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
		'heading':helper.set_folder('Basic'),
		'subtitle': 'The most basic tags',
		'description': 'These are the most essential tags.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '057013a100324e21bc1d6a541c6af383',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('31dc792e43734d2ab7db53fa96b634f5')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;!DOCTYPE&gt;")),

					'description': Markup('Defines the document type'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b1eb5c8a81584417b0005077d2a89d64')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;html&gt;")),

					'description': Markup('Defines an HTML document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('66cee421b9c1477eab7f14eede94826b')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;head&gt;")),

					'description': Markup('Contains metadata/information for the document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a20258b060d94a4491454ca05f58d809')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;title&gt;")),

					'description': Markup('Defines a title for the document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cdb20ebefee647bbaa18ee8e2981f700')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;body&gt;")),

					'description': Markup('Defines the document\'s body'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('965d034dd52b4b3fa956d7268e154b0e')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;p&gt;")),

					'description': Markup('Defines a paragraph'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b3e71b8543934ec88282523e819a5bbb')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;h1&gt; ... &lt;h6&gt;")),

					'description': Markup('Defines hiearchial headings; first heading should always be h1!'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cb32ceb2ef324131a0c54677eed6caa3')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;br&gt;")),

					'description': Markup('Inserts a single line break'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1fb608a512b94198a1f1c7a2c46f8425')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;hr&gt;")),

					'description': Markup('Horizontal ruler. Basically a horizontal border'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d7f88dd02cf145dc8a711fdf9f1c95f4')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;!--your text--&gt;")),

					'description': Markup('This is how you make a comment'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Formatting'),
		'subtitle': 'Formatting of text.',
		'description': 'Semantic tags for defining the text-elements. Good to know.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f3b03a709bfa4881ba7cec7751ca6365',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('718a50b664e14e26a0f2f1a44aace418')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;abbr&gt;")),

					'description': Markup('Defines an abbreviation or an acronym'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7cdb1acaf6ad4aaf926210632d5526b5')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;address&gt;")),

					'description': Markup('Defines contact information for the author/owner of a document/article'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a264d77e528740a5813540d05aff48ff')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;b&gt;")),

					'description': Markup('Defines bold text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a5e942dff9c541ab9c50b98590f999ee')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;bdi&gt;")),

					'description': Markup('Isolates a part of text that might be formatted in a different direction from other text outside it'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c53eefaf81154648b18915b93aa39113')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;bdp&gt;")),

					'description': Markup('Overrides the current text direction'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f7f5413a8f7a433bbfae539446fea977')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;blockquote&gt;")),

					'description': Markup('Defines a section that is quoted from another source'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('22360e9f7452473fb6bade765a079527')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;cite&gt;")),

					'description': Markup('Defines the title of a work'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5312ba33549d4ef0a8babbd5daefe33e')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;code&gt;")),

					'description': Markup('Defines a piece of computer code'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7903de957a0f40368b3f003696cf0cd9')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;del&gt;")),

					'description': Markup('Defines text that has been deleted from a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('970e3a3b39d64557986e01405c5ffcb8')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;dfn&gt;")),

					'description': Markup('Specifies a term that is going to be defined within the content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a99becc67cd94263833e7fb832295314')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;em&gt;")),

					'description': Markup('Defines emphasized text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ed5b339f5fe34f8e8ad3fe795e0f2f45')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;i&gt;")),

					'description': Markup('Defines a part of text in italics'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8ce2bfe723e14136bffe3434d022bfe5')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;ins&gt;")),

					'description': Markup('Defines a text that has been inserted into a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('448f3063ed4c42d4a3453394b7fba0d1')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;kbd&gt;")),

					'description': Markup('Defines keyboard input'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a771d621fde940e2a6bc25f3982837a8')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;mark&gt;")),

					'description': Markup('Defines marked/highlighted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a6b56116f13140829372974371cb333c')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;meter&gt;")),

					'description': Markup('Defines a scalar measurement within a known range (a gauge)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d20ad0bcaabe43278ef71973af13adfa')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;pre&gt;")),

					'description': Markup('Defines preformatted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fe119bd896614cf1b50253e5eb009c8f')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;progress&gt;")),

					'description': Markup('Represents the progress of a task'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d40ddc399df04d7f878a4efd9793ba43')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;q&gt;")),

					'description': Markup('Defines a short quotation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7452218ac0b74bac8f2d9a3e5278e748')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;rp&gt;")),

					'description': Markup('Defines what to show in browsers that do not support ruby annotations (see ruby tag, for what ruby is)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('92ef7fa3e18e441ebd4f7869554ad71a')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;rt&gt;")),

					'description': Markup('Defines an explanation/pronunciation of characters (for East Asian typography)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e07ebab79b1148069ce6976fbc68aa5d')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;ruby&gt;")),

					'description': Markup('Defines a ruby annotation. Ruby annotations are used for East Asian typography'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4a45a040c4d346758166cd0eda66c0cc')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;s&gt;")),

					'description': Markup('Defines a strikethrough text; used for marking something that is no longer correct'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7426cfc200af412ba562e033cf1f7bcc')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;samp&gt;")),

					'description': Markup('Defines sample output from a computer program'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1cb4c2efaf8d42699784d22243225f2f')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;small&gt;")),

					'description': Markup('Defines smaller-sized text for e.g. form-names laid above an input field'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('14309c5b8f6e4735b53e0b499ef17ba1')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;strong&gt;")),

					'description': Markup('Defines important text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('61b6381f7e424f9398287e934541f690')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;sub&gt;")),

					'description': Markup('Defines subscripted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f5b3768ce36f4edd8c199d910fb697ec')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;sup&gt;")),

					'description': Markup('Defines superscripted text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('712b341c7f504368aa7eb017d73f0e98')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;template&gt;")),

					'description': Markup('Defines a container for content that should be hidden when the page loads'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d122b662f8574dae8903a9d628f805f4')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;time&gt;")),

					'description': Markup('Defines a specific time (or datetime)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4b14dc1360324ac898becaa0ae79a980')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;u&gt;")),

					'description': Markup('Defines some text that is unarticulated and styled differently from normal text'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('aba89b3dee7a40dfa44eb2921257a6a1')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;var&gt;")),

					'description': Markup('Defines a variable'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('57c3bdd9bafb48fb9db8e9eff46e9b60')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;wbr&gt;")),

					'description': Markup('Defines a possible line-break'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Forms and Input'),
		'subtitle': 'Form and Input tags',
		'description': 'These elements are crucial in HTML',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '86ec359d968b4212b77c14a01dcefbff',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('dc99b586e39447ccacfd285b4366d1bb')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;form&gt;")),

					'description': Markup('Defines an HTML form for user input'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('838ce834da734329b5b1d771b2068117')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;input&gt;")),

					'description': Markup('Defines an input control'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7443bfb5578d4eee9a0c0f9c877f0c3c')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;textarea&gt;")),

					'description': Markup('Defines a multiline input control (text area)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e04a65d105f74deab37b07933fded609')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;button&gt;")),

					'description': Markup('Defines a clickable button'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6cf387a517a94ac98ec77af20b329275')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;select&gt;")),

					'description': Markup('Defines a drop-down list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2f7073d8b9834c0b86423650f6b91c40')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;optgroup&gt;")),

					'description': Markup('Defines a group of related options in a drop-down list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('78f99e1f252d43c3abc76935f4765fdb')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;option&gt;")),

					'description': Markup('Defines an option in a drop-down list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('89a0cfc9165949b7a3c985867f9b42a3')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;label&gt;")),

					'description': Markup('Defines a label for an &lt;input&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d314ca8faec645bb87a10a2c776f1ea0')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;fieldset&gt;")),

					'description': Markup('Groups related elements in a form'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b3107838e0dd419d8bd5bf63e93cb1d8')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;legend&gt;")),

					'description': Markup('Defines a caption for a &lt;fieldset&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5f226380567d432fb33d0875b1a2d6fd')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;datalist&gt;")),

					'description': Markup('Specifies a list of pre-defined options for input controls'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1645c490bbf94936a4f6b9e9900bd672')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;output&gt;")),

					'description': Markup('Defines the result of a calculation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Frames'),
		'subtitle': 'How to Embed iFrame in HTML',
		'description': 'Artefact from previous HTML standards. Lets you embed a webpage inside another webpage.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'e2edc4ffecb44229ad883658c4aa289e',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('980207212e60424499f684577e95ac06')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;iframe&gt;")),

					'description': Markup('Defines an inline frame'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Images'),
		'subtitle': 'Handling Graphics with HTML',
		'description': 'This is more than mere images - some of these tags are very powerful and useful',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '63db29d7e7e44d9fa11e93454bbff674',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ae1d25134e734883bc4a5066272ff4d1')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;img&gt;")),

					'description': Markup('Defines an image'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a36803b1952349e59d559a99f4971fe7')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;map&gt;")),

					'description': Markup('Defines a client-side image map'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('96f1eab51c2b4fd99ec81b44da5354a3')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;area&gt;")),

					'description': Markup('Defines an area inside an image map'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d5fad94ff9e14df390083d44c7b6ff2f')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;canvas&gt;")),

					'description': Markup('Used to draw graphics, on the fly, via scripting (usually JavaScript)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('18573b2281a345c292f8dfd179a6e84e')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;figcaption&gt;")),

					'description': Markup('Defines a caption for a &gt;figure&lt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('224da4c513d0499f83a99e1fdfe4e0b3')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;figure&gt;")),

					'description': Markup('Specifies self-contained content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cbfb4b2fb7904a78a1344387b80c92c9')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;picture&gt;")),

					'description': Markup('Defines a container for multiple image resources'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('43c6591c2dcf483d887638f26327f7dc')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;svg&gt;")),

					'description': Markup('Defines a container for SVG graphics'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Audio/Video'),
		'subtitle': 'Media in HTML',
		'description': 'Properly very niche',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '50e37592228145558115d28c9e7a3a51',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2e3d615c7be04b8481076226bd774ffc')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;audio&gt;")),

					'description': Markup('Defines sound content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('05f186ba405c4d03a7dabce378d56f09')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;source&gt;")),

					'description': Markup('Defines multiple media resources for media elements (&lt;video&gt;, &lt;audio&gt; and &lt;picture&gt;)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('760fe01a1c2f41f7b850fb826f9d655a')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;video&gt;")),

					'description': Markup('Defines a video or movie'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8d35c6e3cad74d78acec3c6745ea19e8')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;track&gt;")),

					'description': Markup('Defines text tracks for media elements (&lt;video&gt; and &lt;audio&gt;)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Links'),
		'subtitle': 'How to make hyperlinks in HTML',
		'description': 'Crucial part of HTML is linking pages',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5aa2f58338d641bb9d157bbae8355673',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ca061973abf34fd3bcb9aee8fad3cbc4')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;a&gt;")),

					'description': Markup('Defines a hyperlink'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('62c42cf551d54926984bf92b9b827644')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;link&gt;")),

					'description': Markup('Defines the relationship between a document and an external resource (most used to link to style sheets)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('83b0d17b66b84810a8b9dc1a9bf39c08')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;nav&gt;")),

					'description': Markup('Defines navigation links'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('List'),
		'subtitle': 'How to use lists in HTML',
		'description': 'Very essential aspect of HTML is the use of ordered and unordered lists. In many CSS frameworks lists are used for menus.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'e39f5aa4854f42daab2eb464ef18b81a',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('441493da509d43029ddad751ae5bbd63')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;ul&gt;")),

					'description': Markup('Defines an unordered list. You use &lt;li&gt; elements inside'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('c74713366a884f17a38eca69da9a5099')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;ol&gt;")),

					'description': Markup('Defines an ordered list. You use &lt;li&gt; elements inside'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d3bbbad53052407fba047fa48f750aa1')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;li&gt;")),

					'description': Markup('Defines a list item. Must be encapsulated by &lt;ul&gt; or &lt;ol&gt; tags'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ff41bf14fae14eae9ca289d26ca020b0')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;dl&gt;")),

					'description': Markup('Defines a description list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ab0ff1d4d8124ccd80aab8ac9257afb8')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;dt&gt;")),

					'description': Markup('Defines a term/name in a description list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1d58edcfb3cc4ed5b6c53ac56cbfcf3e')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;dd&gt;")),

					'description': Markup('Defines a description of a term/name in a description list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Tables'),
		'subtitle': 'How to make tables in HTML',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c4ddd97b862f4bd08d226279c47c99b0',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a2d61a73a399440fa383f48fef4ee32f')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;table&gt;")),

					'description': Markup('Defines a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('e165963a6a864e65a35c46e1d32434aa')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;caption&gt;")),

					'description': Markup('Defines a table caption'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9ae8d10eddd84a45970ddacf45f670ff')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;th&gt;")),

					'description': Markup('Defines a header cell in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ee4852402159461db85470f3c7b4f55f')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;tr&gt;")),

					'description': Markup('Defines a row in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('12ffc07b8e6343a289d8cb61a6122baa')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;td&gt;")),

					'description': Markup('Defines a cell in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ccf74687e62c4d9d985e383b82b7f14b')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;thead&gt;")),

					'description': Markup('Groups the header content in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('989269afd18e4735836128af9441c12a')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;tbody&gt;")),

					'description': Markup('Groups the body content in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('90bae7c07b584753a03dabebce44c061')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;tfoot&gt;")),

					'description': Markup('Groups the footer content in a table'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7ef9e982f01c4116b5547316d28238d9')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;col&gt;")),

					'description': Markup('Specifies column properties for each column within a &lt;colgroup&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7955b1747a374a24a9fba9e164d0c841')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;colgroup&gt;")),

					'description': Markup('Specifies a group of one or more columns in a table for formatting'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Styles and Semantics'),
		'subtitle': 'Semantics of HTML',
		'description': 'Not so important as it used to be; grasping the essential structure however is beneficient.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f2f0e26370154c269dfefb64cfb55432',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('60034166273c44d0be6935071702fb68')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;style&gt;")),

					'description': Markup('Defines style information for a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('b63a27b4e030479499d84b2aff377955')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;div&gt;")),

					'description': Markup('Defines a section in a document. Used as a de-facto container for any type of content by adding CSS class names to the tag and encapsulating other elements'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('db44f9a46df743e9b40c1b5609e0d905')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;span&gt;")),

					'description': Markup('Defines an inline-section in a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f738dafcbe3a4cfca9eedfb95fbcea7a')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;header&gt;")),

					'description': Markup('Defines a header for a document or section'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e783d716fb744d5592925ac25b218578')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;footer&gt;")),

					'description': Markup('Defines a footer for a document or section'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c5459c34cde147e990aaebae177f33f6')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;main&gt;")),

					'description': Markup('Specifies the main content of a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2872ff162b764ec79481405f2c45c661')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;section&gt;")),

					'description': Markup('Defines a section in a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ce8af7e368c34977b80bd62d1308b1f2')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;article&gt;")),

					'description': Markup('Defines an article'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1121f2e64b534aa7bc76b5ba0fdf08c0')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;aside&gt;")),

					'description': Markup('Defines content aside from the page content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e81539551b8244c5b104fe48dff4a241')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;details&gt;")),

					'description': Markup('Defines additional details that the user can view or hide'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e9c043d3796f4f009c6700e97a08f4f9')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;dialog&gt;")),

					'description': Markup('Defines a dialog box or window'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('db78773830294d61922f14654b1fc51a')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;summary&gt;")),

					'description': Markup('Defines a visible heading for a &lt;details&gt; element'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5f6b204b5797488eb0c8ecff4be81c8f')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;data&gt;")),

					'description': Markup('Adds a machine-readable translation of a given content'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Meta Info'),
		'subtitle': 'Meta Tags and Information in HTML',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '04e290bce75e4a68a5393a6a90661eda',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8870f9122336469299393dba7f6bfb71')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;head&gt;")),

					'description': Markup('Defines information about the document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('351800f9c09f4482b7f721b69e8de774')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;meta&gt;")),

					'description': Markup('Defines metadata about an HTML document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8167260307dd4973ab25cd82ac648ecc')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;base&gt;")),

					'description': Markup('Specifies the base URL/target for all relative URLs in a document'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading':helper.set_folder('Programming'),
		'subtitle': 'The us of Objects and Scripts for Programming in HTML',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'bb9732d31cbb48b4a550137753647989',
		'content': {
			'descriptor': [
				'Tag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('55cc53eceb224a478b2ee529f2874508')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;script&gt;")),

					'description': Markup('Defines a client-side script'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				}, {
					'static_red': Markup(helper.set_entry_folder('0a79c877d9a540c7b184fc92df89b7bd')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;noscript&gt;")),

					'description': Markup('Defines an alternate content for users that do not support client-side scripts'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6d58ac87b6924e608cd5271aa9ffa501')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;embed&gt;")),

					'description': Markup('Defines a container for an external (non-HTML) application'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('86f5070c2acd4697a1cbb4a66724e861')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;object&gt;")),

					'description': Markup('Defines an embedded object'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('562386f7404f4f75ae55611c3d529cfe')[0]),
					'flag': Markup(helper.set_entry_command_string("&lt;param&gt;")),

					'description': Markup('Defines a parameter for an object'),
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

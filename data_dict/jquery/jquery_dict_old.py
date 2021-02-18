import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('jquery', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'jquery'
information = {
	'tool': 'JQuery',
	'title': 'JQuery Cheatsheet',
	'subtitle': 'This site is a reference for JQuery',
	'description': 'JQuery is a popular JavaScript library used for the front-end in web applications.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'JQuery',
			[
				helper.characteristics.get('library'),
				helper.characteristics.get('front-end'),
				helper.characteristics.get('web-development'),
			])
	],
	'topic_uris': [
		'library',
		'front-end',
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

code_cards = [{

}]
# TODO: Make regex for links (find links at: https://overapi.com/jquery)
cheatsheet = [
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Attribute Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('[name|="value"]')[0]),
					'description': Markup('Selects elements that have the specified attribute with a value either equal to a given string or starting with that string followed by a hyphen (-)'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-contains-prefix-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name*="value"]')[0]),
					'description': Markup('Selects elements that have the specified attribute with a value containing a given substring'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-contains-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name~="value"]')[0]),
					'description': Markup('Selects elements that have the specified attribute with a value containing a given word, delimited by spaces'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-contains-word-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name$="value"]')[0]),
					'description': Markup('Selects elements that have the specified attribute with a value ending exactly with a given string. The comparison is case sensitive'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-ends-with-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name="value"]')[0]),
					'description': Markup('Selects elements that have the specified attribute with a value exactly equal to a certain value'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-equals-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name!="value"]')[0]),
					'description': Markup('Select elements that either don\'t have the specified attribute, or do have the specified attribute but not with a certain value'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-not-equal-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name^="value"]')[0]),
					'description': Markup('Selects elements that have the specified attribute with a value beginning exactly with a given string'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-starts-with-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name]')[0]),
					'description': Markup('Selects elements that have the specified attribute, with any value'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/has-attribute-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[name="value"][name2="value2"]')[0]),
					'description': Markup('Matches elements that match all of the specified attribute filters'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/multiple-attribute-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Form Selectors',
		'description': 'Form selectors. Used to select form elements.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(':button')[0]),
					'description': Markup('Selects all button elements and elements of type button'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/button-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':checkbox')[0]),
					'description': Markup('Selects all elements of type checkbox'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/checkbox-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':checked')[0]),
					'description': Markup('Matches all elements that are checked or selected'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/checked-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':disabled')[0]),
					'description': Markup('Selects all elements that are disabled'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/disabled-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':enabled')[0]),
					'description': Markup('Selects all elements that are enabled'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/enabled-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':focus')[0]),
					'description': Markup('Selects element if it is currently focused'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focus-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':file')[0]),
					'description': Markup('Selects all elements of type file'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/file-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':image')[0]),
					'description': Markup('Selects all elements of type image'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/image-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':input')[0]),
					'description': Markup('Selects all input, textarea, select and button elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/input-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':password')[0]),
					'description': Markup('Selects all elements of type password'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/password-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':radio')[0]),
					'description': Markup('Selects all elements of type radio'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/radio-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':reset')[0]),
					'description': Markup('Selects all elements of type reset'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/reset-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':selected')[0]),
					'description': Markup('Selects all elements that are selected'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/selected-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':submit')[0]),
					'description': Markup('Selects all elements of type submit'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/submit-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':text')[0]),
					'description': Markup('Selects all input elements of type text'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/text-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Basic Selectors',
		'description': 'Elementary JQuery selectors',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('*')[0]),
					'description': Markup('Selects all elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/all-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.class')[0]),
					'description': Markup('Selects all elements with the given class'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/class-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('element')[0]),
					'description': Markup('Selects all elements with the given tag name'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/element-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('#id')[0]),
					'description': Markup('Selects a single element with the given id attribute'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/id-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('selector1, selectorN, ...')[0]),
					'description': Markup('Selects the combined results of all the specified selectors'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/multiple-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Hidden Selectors',
		'description': 'Used to select all elements that are either hidden or visible',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(':hidden')[0]),
					'description': Markup('Selects all elements that are hidden'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hidden-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':visible')[0]),
					'description': Markup('Selects all elements that are visible'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/visible-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Basic Filter Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(':animated')[0]),
					'description': Markup('Select all elements that are in the progress of an animation at the time the selector is run'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/animated-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':eq()')[0]),
					'description': Markup('Select the element at index n within the matched set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/eq-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':even')[0]),
					'description': Markup('Selects even elements, zero-indexed'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/even-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':first')[0]),
					'description': Markup('Selects the first matched DOM element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/first-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':gt()')[0]),
					'description': Markup('Select all elements at an index greater than index within the matched set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/gt-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':header')[0]),
					'description': Markup('Selects all elements that are headers, like h1, h2, h3 and so on'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/header-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':last')[0]),
					'description': Markup('Selects the last matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/last-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':lt()')[0]),
					'description': Markup('Select all elements at an index less than index within the matched set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/lt-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':not()')[0]),
					'description': Markup('Selects all elements that do not match the given selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/not-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':odd')[0]),
					'description': Markup('Selects odd elements, zero-indexed'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/odd-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Child Filter Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(':first-child')[0]),
					'description': Markup('Selects all elements that are the first child of their parent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/first-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':last-child')[0]),
					'description': Markup('Selects all elements that are the last child of their parent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/last-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':nth-child()')[0]),
					'description': Markup('Selects all elements that are the nth-child of their parent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/nth-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':only-child')[0]),
					'description': Markup('Selects all elements that are the only child of their parent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/only-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Content Filter Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(':contains()')[0]),
					'description': Markup('Select all elements that contain the specified text'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/contains-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':empty')[0]),
					'description': Markup('Select all elements that have no children (including text nodes)'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/empty-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':has()')[0]),
					'description': Markup('Selects elements which contain at least one element that matches the specified selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/has-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':parent')[0]),
					'description': Markup('Select all elements that have at least one child node (either an element or text)'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parent-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Hierarchy Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('parent > child')[0]),
					'description': Markup('Selects all direct child elements specified by "child" of elements specified by "parent"'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('ancestor descendant')[0]),
					'description': Markup('Selects all elements that are descendants of a given ancestor'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/descendant-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('prev + next')[0]),
					'description': Markup('Selects all next elements matching "next" that are immediately preceded by a sibling "prev"'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/next-adjacent-Selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('prev ~ siblings')[0]),
					'description': Markup('Selects all sibling elements that follow after the "prev" element, have the same parent, and match the filtering "siblings" selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/next-siblings-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Basic Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.hide()')[0]),
					'description': Markup('Hide the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hide/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.show()')[0]),
					'description': Markup('Display the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/show/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.toggle()')[0]),
					'description': Markup('Display or hide the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toggle/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Custom Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.animate()')[0]),
					'description': Markup('Perform a custom animation of a set of CSS properties'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/animate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.clearQueue()')[0]),
					'description': Markup('Remove from the queue all items that have not yet been run'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/clearQueue',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.delay()')[0]),
					'description': Markup('Set a timer to delay execution of subsequent items in the queue'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/delay',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.dequeue()')[0]),
					'description': Markup('Execute the next function on the queue for the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/dequeue',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.dequeue()')[0]),
					'description': Markup('Execute the next function on the queue for the matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.dequeue/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.fx.interval')[0]),
					'description': Markup('The rate (in milliseconds) at which animations fire'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.fx.interval',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.fx.off')[0]),
					'description': Markup('Globally disable all animations'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.fx.off',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.queue()')[0]),
					'description': Markup('Show or manipulate the queue of functions to be executed on the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/queue',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.queue()')[0]),
					'description': Markup('Show or manipulate the queue of functions to be executed on the matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.queue/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.stop()')[0]),
					'description': Markup('Stop the currently-running animation on the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/stop',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Fading Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.fadeIn()')[0]),
					'description': Markup('Display the matched elements by fading them to opaque'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeIn/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.fadeOut()')[0]),
					'description': Markup('Hide the matched elements by fading them to transparent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeOut/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.fadeTo()')[0]),
					'description': Markup('Adjust the opacity of the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeTo/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.fadeToggle()')[0]),
					'description': Markup('Display or hide the matched elements by animating their opacity'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeToggle/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Sliding Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.slideDown()')[0]),
					'description': Markup('Display the matched elements with a sliding motion'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slideDown',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.slideToggle()')[0]),
					'description': Markup('Display or hide the matched elements with a sliding motion'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slideToggle',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.slideUp()')[0]),
					'description': Markup('Hide the matched elements with a sliding motion'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slideUp',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.attr()')[0]),
					'description': Markup('Get the value of an attribute for the first element in the set of matched elements or set one or more attributes for every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attr/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.prop()')[0]),
					'description': Markup('Get the value of a property for the first element in the set of matched elements or set one or more properties for every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.removeAttr()')[0]),
					'description': Markup('Remove an attribute from each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeAttr/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.removeProp()')[0]),
					'description': Markup('Remove a property for the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeProp/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.val()')[0]),
					'description': Markup('Get the current value of the first element in the set of matched elements or set the value of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/val/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'CSS Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.addClass()')[0]),
					'description': Markup('Adds the specified class(es) to each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/addClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.css()')[0]),
					'description': Markup('Get the value of a computed style property for the first element in the set of matched elements or set one or more CSS properties for every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/css/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.cssHooks')[0]),
					'description': Markup('Hook directly into jQuery to override how particular CSS properties are retrieved or set, normalize CSS property naming, or create custom properties'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.cssHooks/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.hasClass()')[0]),
					'description': Markup('Determine whether any of the matched elements are assigned the given class'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hasClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.removeClass()')[0]),
					'description': Markup('Remove a single class, multiple classes, or all classes from each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.toggleClass()')[0]),
					'description': Markup('Add or remove one or more classes from each element in the set of matched elements, depending on either the class\'s presence or the value of the state argument'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toggleClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Dimension Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.height()')[0]),
					'description': Markup('Get the current computed height for the first element in the set of matched elements or set the height of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/height/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.innerHeight()')[0]),
					'description': Markup('Get the current computed inner height (including padding but not border) for the first element in the set of matched elements or set the inner height of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/innerHeight/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.outerHeight()')[0]),
					'description': Markup('Get the current computed outer height (including padding, border, and optionally margin) for the first element in the set of matched elements or set the outer height of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/outerHeight/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.width()')[0]),
					'description': Markup('Get the current computed width for the first element in the set of matched elements or set the width of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/width/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.innerWidth()')[0]),
					'description': Markup('Get the current computed inner width (including padding but not border) for the first element in the set of matched elements or set the inner width of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/innerWidth/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.outerWidth()')[0]),
					'description': Markup('Get the current computed outer width (including padding, border, and optionally margin) for the first element in the set of matched elements or set the outer width of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/outerWidth/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Offset Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.offset()')[0]),
					'description': Markup('Get the current coordinates of the first element, or set the coordinates of every element, in the set of matched elements, relative to the document'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/offset/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.offsetParent()')[0]),
					'description': Markup('Get the closest ancestor element that is positioned'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/offsetParent/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.position()')[0]),
					'description': Markup('Get the current coordinates of the first element in the set of matched elements, relative to the offset parent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/position/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.scrollLeft()')[0]),
					'description': Markup('Get the current horizontal position of the scroll bar for the first element in the set of matched elements or set the horizontal position of the scroll bar for every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/scrollLeft/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.scrollTop()')[0]),
					'description': Markup('Get the current vertical position of the scroll bar for the first element in the set of matched elements or set the vertical position of the scroll bar for every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/scrollTop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Data Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery.data()')[0]),
					'description': Markup('Store arbitrary data associated with the specified element and/or return the value that was set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.data/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.data()')[0]),
					'description': Markup('Store arbitrary data associated with the matched elements or return the value at the named data store for the first element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/data/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.hasData()')[0]),
					'description': Markup('Determine whether an element has any jQuery data associated with it'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.hasData/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.removeData()')[0]),
					'description': Markup('Remove a previously-stored piece of data'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.removeData/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.removeData()')[0]),
					'description': Markup('Remove a previously-stored piece of data'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeData/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Utilities'),
		'subtitle': 'Utilities',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery.browser')[0]),
					'description': Markup('Contains flags for the useragent, read from navigator.userAgent. This property was removed in jQuery 1.9 and is available only through the jQuery.migrate plugin'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.browser/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.contains()')[0]),
					'description': Markup('Check to see if a DOM element is a descendant of another DOM element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.contains/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('each')[0]),
					'description': Markup('Iterate over a jQuery object, executing a function for each matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/each/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.each()')[0]),
					'description': Markup('A generic iterator function, which can be used to seamlessly iterate over both objects and arrays'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.each/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.extend()')[0]),
					'description': Markup('Merge the contents of two or more objects together into the first object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.extend/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.globalEval()')[0]),
					'description': Markup('Execute some JavaScript code globally'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.globalEval/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.grep()')[0]),
					'description': Markup('Finds the elements of an array which satisfy a filter function. The original array is not affected'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.grep/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.inArray()')[0]),
					'description': Markup('Search for a specified value within an array and return its index (or -1 if not found)'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.inArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isArray()')[0]),
					'description': Markup('Determine whether the argument is an array'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isEmptyObject()')[0]),
					'description': Markup('Check to see if an object is empty (contains no enumerable properties)'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isEmptyObject/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isFunction()')[0]),
					'description': Markup('Determines if its argument is callable as a function'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isFunction/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isNumeric()')[0]),
					'description': Markup('Determines whether its argument represents a JavaScript number'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isNumeric/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isPlainObject()')[0]),
					'description': Markup('Check to see if an object is a plain object (created using "{}" or "new Object")'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isPlainObject/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isWindow()')[0]),
					'description': Markup('Determine whether the argument is a window'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isWindow/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.isXMLDoc()')[0]),
					'description': Markup('Check to see if a DOM node is within an XML document (or is an XML document)'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isXMLDoc/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.makeArray()')[0]),
					'description': Markup('Convert an array-like object into a true JavaScript array'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.makeArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.map()')[0]),
					'description': Markup('Translate all items in an array or object to new array of items'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.map/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.merge()')[0]),
					'description': Markup('Merge the contents of two arrays together into the first array'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.merge/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.noop()')[0]),
					'description': Markup('An empty function'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.noop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.now()')[0]),
					'description': Markup('Return a number representing the current time'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.now/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.parseJSON()')[0]),
					'description': Markup('Takes a well-formed JSON string and returns the resulting JavaScript value'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.parseJSON/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.parseXML()')[0]),
					'description': Markup('Parses a string into an XML document'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.parseXML/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.proxy()')[0]),
					'description': Markup('Takes a function and returns a new one that will always have a particular context'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.proxy/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.support')[0]),
					'description': Markup('A collection of properties that represent the presence of different browser features or bugs. Intended for jQuery\'s internal use'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.support/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.trim()')[0]),
					'description': Markup('Remove the whitespace from the beginning and end of a string'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.trim/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.type()')[0]),
					'description': Markup('Determine the internal JavaScript [[Class]] of an object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.type/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.unique()')[0]),
					'description': Markup('Sorts an array of DOM elements, in place, with the duplicates removed. Note that this only works on arrays of DOM elements, not strings or numbers'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.unique/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'Copying',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.clone()')[0]),
					'description': Markup('Create a deep copy of the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/clone/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Insertion (Around)',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.wrap()')[0]),
					'description': Markup('Wrap an HTML structure around each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/wrap/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.wrapAll()')[0]),
					'description': Markup('Wrap an HTML structure around all elements in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/wrapAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.wrapInner()')[0]),
					'description': Markup('Wrap an HTML structure around the content of each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/wrapInner/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Insertion (Inside)',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.append()')[0]),
					'description': Markup('Insert content, specified by the parameter, to the end of each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/append/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.appendTo()')[0]),
					'description': Markup('Insert every element in the set of matched elements to the end of the target'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/appendTo/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.html()')[0]),
					'description': Markup('Get the HTML contents of the first element in the set of matched elements or set the HTML contents of every matched element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/html/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.prepend()')[0]),
					'description': Markup('Insert content, specified by the parameter, to the beginning of each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prepend/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.prependTo()')[0]),
					'description': Markup('Insert every element in the set of matched elements to the beginning of the target'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prependTo/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.text()')[0]),
					'description': Markup('Get the combined text contents of each element in the set of matched elements, including their descendants, or set the text contents of the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/text/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Insertion (Outside)',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.after()')[0]),
					'description': Markup('Insert content, specified by the parameter, after each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/after/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.before()')[0]),
					'description': Markup('Insert content, specified by the parameter, before each element in the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/before/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.insertAfter()')[0]),
					'description': Markup('Insert every element in the set of matched elements after the target'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/insertAfter/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.insertBefore()')[0]),
					'description': Markup('Insert every element in the set of matched elements before the target'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/insertBefore/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Removal',
		'description': 'Used to manipulate DOM elements from a selection of matched elements',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.detach()')[0]),
					'description': Markup('Remove the set of matched elements from the DOM'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/detach/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.empty()')[0]),
					'description': Markup('Remove all child nodes of the set of matched elements from the DOM'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/empty/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.remove()')[0]),
					'description': Markup('Remove the set of matched elements from the DOM'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/remove/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.unwrap()')[0]),
					'description': Markup('Remove the parents of the set of matched elements from the DOM, leaving the matched elements in their place'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/unwrap/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Replacement',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.replaceAll()')[0]),
					'description': Markup('Replace each target element with the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/replaceAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.replaceWith()')[0]),
					'description': Markup('Replace each element in the set of matched elements with the provided new content and return the set of elements that was removed'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/replaceWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Global Ajax Event Handlers',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.ajaxComplete()')[0]),
					'description': Markup('Register a handler to be called when Ajax requests complete'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxComplete/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.ajaxError()')[0]),
					'description': Markup('Register a handler to be called when Ajax requests complete with an error'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxError/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.ajaxSend()')[0]),
					'description': Markup('Attach a function to be executed before an Ajax request is sent'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxSend/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.ajaxStart()')[0]),
					'description': Markup('Register a handler to be called when the first Ajax request begins'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxStart/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.ajaxStop()')[0]),
					'description': Markup('Register a handler to be called when all Ajax requests have completed'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxStop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.ajaxSuccess()')[0]),
					'description': Markup('Attach a function to be executed whenever an Ajax request completes successfully'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxSuccess/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Ajax Helper Functions',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery.param()')[0]),
					'description': Markup('Create a serialized representation of an array, a plain object, or a jQuery object suitable for use in a URL query string or Ajax request'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.param/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.serialize()')[0]),
					'description': Markup('Encode a set of form elements as a string for submission'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/serialize/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.serializeArray()')[0]),
					'description': Markup('Encode a set of form elements as an array of names and values'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/serializeArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Ajax Low-Level Interface',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery.ajax()')[0]),
					'description': Markup('Perform an asynchronous HTTP (Ajax) request'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.ajax/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.ajaxSetup()')[0]),
					'description': Markup('Set default values for future Ajax requests. Its use is not recommended'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.ajaxSetup',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Ajax Shorthand Methods',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery.get()')[0]),
					'description': Markup('Load data from the server using a HTTP GET request'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.get/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.getJSON()')[0]),
					'description': Markup('Load JSON-encoded data from the server using a GET HTTP request'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.getJSON/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.getScript()')[0]),
					'description': Markup('Load a JavaScript file from the server using a GET HTTP request, then execute it'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.getScript/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.load()')[0]),
					'description': Markup('Load data from the server and place the returned HTML into the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/load/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.post()')[0]),
					'description': Markup('Send data to the server using a HTTP POST request'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.post/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Traversing'),
		'subtitle': 'Filter Traversing',
		'description': 'Used to filter traversed DOM elements that has been matched',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.eq()')[0]),
					'description': Markup('Reduce the set of matched elements to the one at the specified index'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/eq/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.filter()')[0]),
					'description': Markup('Reduce the set of matched elements to those that match the selector or pass the function\'s test'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/filter/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.first()')[0]),
					'description': Markup('Reduce the set of matched elements to the first in the set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/first/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.has()')[0]),
					'description': Markup('Reduce the set of matched elements to those that have a descendant that matches the selector or DOM element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/has/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.is()')[0]),
					'description': Markup('Check the current matched set of elements against a selector, element, or jQuery object and return true if at least one of these elements matches the given arguments'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/is/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.last()')[0]),
					'description': Markup('Reduce the set of matched elements to the final one in the set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/last/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.map()')[0]),
					'description': Markup('Pass each element in the current matched set through a function, producing a new jQuery object containing the return values'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/map/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.not()')[0]),
					'description': Markup('Remove elements from the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/not/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.slice()')[0]),
					'description': Markup('Reduce the set of matched elements to a subset specified by a range of indices'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slice/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Traversing'),
		'subtitle': 'Miscellaneous Traversing',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.add()')[0]),
					'description': Markup('Create a new jQuery object with elements added to the set of matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/add/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.andSelf()')[0]),
					'description': Markup('Add the previous set of elements on the stack to the current set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/andSelf/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.contents()')[0]),
					'description': Markup('Get the children of each element in the set of matched elements, including text and comment nodes'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/contents/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.end()')[0]),
					'description': Markup('End the most recent filtering operation in the current chain and return the set of matched elements to its previous state'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/end/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Traversing'),
		'subtitle': 'Tree Traversal',
		'description': 'Used to traverse the DOM tree',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.children()')[0]),
					'description': Markup('Get the children of each element in the set of matched elements, optionally filtered by a selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/children/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.closest()')[0]),
					'description': Markup('For each element in the set, get the first element that matches the selector by testing the element itself and traversing up through its ancestors in the DOM tree'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/closest/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.find()')[0]),
					'description': Markup('Get the descendants of each element in the current set of matched elements, filtered by a selector, jQuery object, or element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/find/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.next()')[0]),
					'description': Markup('Get the immediately following sibling of each element in the set of matched elements. If a selector is provided, it retrieves the next sibling only if it matches that selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/next/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.nextAll()')[0]),
					'description': Markup('Get all following siblings of each element in the set of matched elements, optionally filtered by a selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/nextAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.nextUntil()')[0]),
					'description': Markup('Get all following siblings of each element up to but not including the element matched by the selector, DOM node, or jQuery object passed'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/nextUntil/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.parent()')[0]),
					'description': Markup('Get the parent of each element in the current set of matched elements, optionally filtered by a selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parent/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.parents()')[0]),
					'description': Markup('Get the ancestors of each element in the current set of matched elements, optionally filtered by a selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parents/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.parentsUntil()')[0]),
					'description': Markup('Get the ancestors of each element in the current set of matched elements, up to but not including the element matched by the selector, DOM node, or jQuery object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parentsUntil/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.prev()')[0]),
					'description': Markup('Get the immediately preceding sibling of each element in the set of matched elements. If a selector is provided, it retrieves the previous sibling only if it matches that selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prev/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.prevAll()')[0]),
					'description': Markup('Get all preceding siblings of each element in the set of matched elements, optionally filtered by a selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prevAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.prevUntil()')[0]),
					'description': Markup('Get all preceding siblings of each element up to but not including the element matched by the selector, DOM node, or jQuery object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prevUntil/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.siblings()')[0]),
					'description': Markup('Get the siblings of each element in the set of matched elements, optionally filtered by a selector'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/siblings/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'jQuery Core Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery()')[0]),
					'description': Markup('Return a collection of matched elements either found in the DOM based on passed argument(s) or created by passing an HTML string'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.noConflict()')[0]),
					'description': Markup('Relinquish jQuery\'s control of the $ variable'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.noConflict/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.sub()')[0]),
					'description': Markup('Creates a new copy of jQuery whose properties and methods can be modified without affecting the original jQuery object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.sub/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.when()')[0]),
					'description': Markup('Provides a way to execute callback functions based on zero or more Thenable objects, usually Deferred objects that represent asynchronous events'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.when/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'DOM Element Methods',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.get()')[0]),
					'description': Markup('Retrieve the DOM elements matched by the jQuery object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/get/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.index()')[0]),
					'description': Markup('Search for a given element from among the matched elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/index/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.size()')[0]),
					'description': Markup('Return the number of elements in the jQuery object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/size/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('toArray()')[0]),
					'description': Markup('Retrieve all the elements contained in the jQuery set, as an array'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'Core Internals',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.jquery')[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/.jquery/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.context')[0]),
					'description': Markup('The DOM node context originally passed to jQuery(); if none was passed then context will likely be the document'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/context/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jQuery.error')[0]),
					'description': Markup('Takes a string and throws an exception containing it'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.error/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.length')[0]),
					'description': Markup('The number of elements in the jQuery object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/length/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.pushStack()')[0]),
					'description': Markup('Add a collection of DOM elements onto the jQuery stack'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/pushStack/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.selector')[0]),
					'description': Markup('A selector representing selector passed to jQuery(), if any, when creating the original set'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'Deferred Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('deferred.always()')[0]),
					'description': Markup('Add handlers to be called when the Deferred object is either resolved or rejected'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.always/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.done()')[0]),
					'description': Markup('Add handlers to be called when the Deferred object is resolved'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.done/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.fail()')[0]),
					'description': Markup('Add handlers to be called when the Deferred object is rejected'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.fail/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.isRejected()')[0]),
					'description': Markup('Determine whether a Deferred object has been rejected'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.isRejected/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.isResolved()')[0]),
					'description': Markup('Determine whether a Deferred object has been resolved'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.isResolved/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.notify()')[0]),
					'description': Markup('Call the progressCallbacks on a Deferred object with the given args'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.notify/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.notifyWith()')[0]),
					'description': Markup('Call the progressCallbacks on a Deferred object with the given context and args'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.notifyWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.pipe()')[0]),
					'description': Markup('Utility method to filter and/or chain Deferreds'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.pipe/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.progress()')[0]),
					'description': Markup('Add handlers to be called when the Deferred object generates progress notifications'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.progress/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.promise()')[0]),
					'description': Markup('Return a Deferred\'s Promise object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.promise/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.reject()')[0]),
					'description': Markup('Reject a Deferred object and call any failCallbacks with the given args'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.reject/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.rejectWith()')[0]),
					'description': Markup('Reject a Deferred object and call any failCallbacks with the given context and args'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.rejectWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.resolve()')[0]),
					'description': Markup('Resolve a Deferred object and call any doneCallbacks with the given args'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.resolve/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.resolveWith()')[0]),
					'description': Markup('Resolve a Deferred object and call any doneCallbacks with the given context and args'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.resolveWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.state()')[0]),
					'description': Markup('Determine the current state of a Deferred object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.state/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('deferred.then()')[0]),
					'description': Markup('Add handlers to be called when the Deferred object is resolved, rejected, or still in progress'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.then/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.promise()')[0]),
					'description': Markup('Return a Promise object to observe when all actions of a certain type bound to the collection, queued or not, have finished'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/promise/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'Callbacks Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('jQuery.Callbacks()')[0]),
					'description': Markup('A multi-purpose callbacks list object that provides a powerful way to manage callback lists'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.Callbacks/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.add()')[0]),
					'description': Markup('Add a callback or a collection of callbacks to a callback list'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.add/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.disable()')[0]),
					'description': Markup('Disable a callback list from doing anything more'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.disable/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.empty()')[0]),
					'description': Markup('Remove all of the callbacks from a list'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.empty/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.fire()')[0]),
					'description': Markup('Call all of the callbacks with the given arguments'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.fire/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.fired()')[0]),
					'description': Markup('Determine if the callbacks have already been called at least once'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.fired/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.fireWith()')[0]),
					'description': Markup('Call all callbacks in a list with the given context and arguments'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.fireWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.has()')[0]),
					'description': Markup('Determine whether or not the list has any callbacks attached. If a callback is provided as an argument, determine whether it is in a list'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.has/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.lock()')[0]),
					'description': Markup('Lock a callback list in its current state'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.lock/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.locked()')[0]),
					'description': Markup('Determine if the callbacks list has been locked'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.locked/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('callbacks.remove()')[0]),
					'description': Markup('Remove a callback or a collection of callbacks from a callback list'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.remove/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Event Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('event.currentTarget')[0]),
					'description': Markup('The current DOM element within the event bubbling phase'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.currentTarget/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.data')[0]),
					'description': Markup('An optional object of data passed to an event method when the current executing handler is bound'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.data/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.isDefaultPrevented()')[0]),
					'description': Markup('Returns whether event.preventDefault() was ever called on this event object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.isDefaultPrevented/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.isImmediatePropagationStopped()')[0]),
					'description': Markup('Returns whether event.stopImmediatePropagation() was ever called on this event object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.isImmediatePropagationStopped/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.isPropagationStopped()')[0]),
					'description': Markup('Returns whether event.stopPropagation() was ever called on this event object'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.isPropagationStopped/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.namespace')[0]),
					'description': Markup('The namespace specified when the event was triggered'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.namespace/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.pageX')[0]),
					'description': Markup('The mouse position relative to the left edge of the document'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.pageX/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.pageY')[0]),
					'description': Markup('The mouse position relative to the top edge of the document'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.pageY/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.preventDefault()')[0]),
					'description': Markup('If this method is called, the default action of the event will not be triggered'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.preventDefault/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.relatedTarget')[0]),
					'description': Markup('The other DOM element involved in the event, if any'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.relatedTarget/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.result')[0]),
					'description': Markup('The last value returned by an event handler that was triggered by this event, unless the value was undefined'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.result/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.stopImmediatePropagation()')[0]),
					'description': Markup('Keeps the rest of the handlers from being executed and prevents the event from bubbling up the DOM tree'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.stopImmediatePropagation/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.stopPropagation()')[0]),
					'description': Markup('Prevents the event from bubbling up the DOM tree, preventing any parent handlers from being notified of the event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.stopPropagation/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.target')[0]),
					'description': Markup('The DOM element that initiated the event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.target/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.timeStamp')[0]),
					'description': Markup('The difference in milliseconds between the time the browser created the event and January 1, 1970'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.timeStamp/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.type')[0]),
					'description': Markup('Describes the nature of the event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.type/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('event.which')[0]),
					'description': Markup('For key or mouse events, this property indicates the specific key or button that was pressed'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.which/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Mouse Events',
		'description': 'Used to bind an event handler to mouse clicks, hovering and focusing on elements',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.click()')[0]),
					'description': Markup('Bind an event handler to the "click" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/click/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.dblclick()')[0]),
					'description': Markup('Bind an event handler to the "dblclick" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/dblclick/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.focusin()')[0]),
					'description': Markup('Bind an event handler to the "focusin" event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focusin/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.focusout()')[0]),
					'description': Markup('Bind an event handler to the "focusout" JavaScript event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focusout/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.hover()')[0]),
					'description': Markup('Bind one or two handlers to the matched elements, to be executed when the mouse pointer enters and leaves the elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hover/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mousedown()')[0]),
					'description': Markup('Bind an event handler to the "mousedown" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mousedown/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mouseenter()')[0]),
					'description': Markup('Bind an event handler to be fired when the mouse enters an element, or trigger that handler on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseenter/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mouseleave()')[0]),
					'description': Markup('Bind an event handler to be fired when the mouse leaves an element, or trigger that handler on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseleave/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mousemove()')[0]),
					'description': Markup('Bind an event handler to the "mousemove" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mousemove/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mouseout()')[0]),
					'description': Markup('Bind an event handler to the "mouseout" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseout/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mouseover()')[0]),
					'description': Markup('Bind an event handler to the "mouseover" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseover/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.mouseup()')[0]),
					'description': Markup('Bind an event handler to the "mouseup" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseup/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.toggle()')[0]),
					'description': Markup('Bind two or more handlers to the matched elements, to be executed on alternate clicks'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toggle-event/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Browser Events',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.error()')[0]),
					'description': Markup('Bind an event handler to the "error" JavaScript event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/error/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.resize()')[0]),
					'description': Markup('Bind an event handler to the "resize" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/resize/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.scroll()')[0]),
					'description': Markup('Bind an event handler to the "scroll" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/scroll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Document Loading',
		'description': 'Used to bind event handlers to be fired upon loading the document f.e.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.holdReady()')[0]),
					'description': Markup('Holds or releases the execution of jQuery\'s ready event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.holdReady/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.load()')[0]),
					'description': Markup('Bind an event handler to the "load" JavaScript event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/load-event/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.ready()')[0]),
					'description': Markup('Specify a function to execute when the DOM is fully loaded'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ready/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.unload()')[0]),
					'description': Markup('Bind an event handler to the "unload" JavaScript event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/unload/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Event Handler Attachment',
		'description': 'Used to attach event handlers',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.bind()')[0]),
					'description': Markup('Attach a handler to an event for the elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/bind/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.delegate()')[0]),
					'description': Markup('Attach a handler to one or more events for all elements that match the selector, now or in the future, based on a specific set of root elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/delegate/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.die()')[0]),
					'description': Markup('Remove event handlers previously attached using .live() from the elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/die/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.live()')[0]),
					'description': Markup('Attach an event handler for all elements which match the current selector, now and in the future'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/live/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.off()')[0]),
					'description': Markup('Remove an event handler'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/off/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.on()')[0]),
					'description': Markup('Attach an event handler function for one or more events to the selected elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/on/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.one()')[0]),
					'description': Markup('Attach a handler to an event for the elements. The handler is executed at most once per element per event type'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/one/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.trigger()')[0]),
					'description': Markup('Execute all handlers and behaviors attached to the matched elements for the given event type'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/trigger/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.triggerHandler()')[0]),
					'description': Markup('Execute all handlers attached to an element for an event'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/triggerHandler/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.unbind()')[0]),
					'description': Markup('Remove a previously-attached event handler from the elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/unbind/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.undelegate()')[0]),
					'description': Markup('Remove a handler from the event for all elements which match the current selector, based upon a specific set of root elements'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/undelegate/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Form Events',
		'description': 'Used to bind event handlers to form elements',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.blur()')[0]),
					'description': Markup('Bind an event handler to the "blur" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/blur/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.change()')[0]),
					'description': Markup('Bind an event handler to the "change" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/change/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.focus()')[0]),
					'description': Markup('Bind an event handler to the "focus" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focus/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.select()')[0]),
					'description': Markup('Bind an event handler to the "select" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/select/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.submit()')[0]),
					'description': Markup('Bind an event handler to the "submit" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/submit/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Keyboard Events',
		'description': 'Used to bind event handlers to keyboard events such as pressing or releasing a key',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.keydown()')[0]),
					'description': Markup('Bind an event handler to the "keydown" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/keydown/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.keypress()')[0]),
					'description': Markup('Bind an event handler to the "keypress" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/keypress/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.keyup()')[0]),
					'description': Markup('Bind an event handler to the "keyup" JavaScript event, or trigger that event on an element'),
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/keyup/',
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
			'link': 'https://jquery.com/',
			'title': 'JQuery Website',
			'description': Markup('The official website for JQuery - the best documentation out there'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

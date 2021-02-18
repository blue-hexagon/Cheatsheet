import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('osint', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'osint'
information = {
	'tool': 'OSINT',
	'title': 'OSINT Cheatsheet',
	'subtitle': 'This site is a reference for Open Source Intelligence (OSINT)',
	'description': 'Open Source Intelligence deals with information gathered from publicly available sources that can be used in an intelligence context. This can vary widely and be anything from hashes, emails, newspaper articles or geo-locations.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'OSINT',
			[
				helper.characteristics.get('standard'),
			])
	],
	'topic_uris': [
		'standard',
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
		'heading': helper.set_folder('Tools'),
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
					'flag': Markup(helper.set_entry_folder("Maltego")[0]),
					'description': Markup('Powerfull tool to network topology mapping and much more'),
					'example': helper.example_path(),
					'ext_link': 'https://www.maltego.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("SpiderFoot")[0]),
					'description': Markup('A tool that automates OSINT collection'),
					'example': helper.example_path(),
					'ext_link': 'https://github.com/smicallef/spiderfoot',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("twint")[0]),
					'description': Markup('An advanced Twitter scraping & OSINT tool written in Python that doesn\'t use Twitter\'s API, allowing you to scrape a user\'s followers, following, Tweets and more while evading most API limitations'),
					'example': helper.example_path(),
					'ext_link': 'https://github.com/twintproject/twint',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Photon")[0]),
					'description': Markup('Incredibly fast crawler designed for OSINT'),
					'example': helper.example_path(),
					'ext_link': 'https://github.com/s0md3v/Photon',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("HaveIbeenPwned")[0]),
					'description': Markup('Search email addresses that has been subject to a data breach and get information about the data breach'),
					'example': helper.example_path(),
					'ext_link': 'https://haveibeenpwned.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Pipl")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': 'https://pipl.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Google Hacking Databse")[0]),
					'description': Markup('Dorks for querying sensitive information or vulnerable content'),
					'example': helper.example_path(),
					'ext_link': 'https://www.exploit-db.com/google-hacking-database',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Pipl")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': 'https://pipl.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Terms'),
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
					'flag': Markup(helper.set_entry_folder("Dorking")[0]),
					'description': Markup('Using search parameters to narrow down results in a Google search for information which is otherwise difficult to locate (see tools for a database of dorks)'),
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
		'heading': helper.set_folder('Archived Information'),
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
					'flag': Markup(helper.set_entry_folder("The Wayback Machine")[0]),
					'description': Markup('Archive of webpages throughout time as they change'),
					'example': helper.example_path(),
					'ext_link': 'http://archive.org/web/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Archive Today")[0]),
					'description': Markup('Another timecapsule for webpages'),
					'example': helper.example_path(),
					'ext_link': 'http://archive.vn/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Google and Bing")[0]),
					'description': Markup('Both offer cached versions of webpages'),
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
		'heading': helper.set_folder('Search Operators'),
		'subtitle': 'Google and Bing',
		'description': 'Also known as Google Dorking',
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
					'flag': Markup(helper.set_entry_folder("\"Search Term\"")[0]),
					'description': Markup('Search for the exact phase'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("TermA OR TermB")[0]),
					'description': Markup('Search for TermA or TermB'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("site:www.example.com")[0]),
					'description': Markup('Return results only from www.example.com'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("filetype:pdf")[0]),
					'description': Markup('Return results that are of filetype pdf'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("intitle:")[0]),
					'description': Markup('Search for sites with the given words in their title'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("inurl:")[0]),
					'description': Markup('Search for sites with the given words in their URL'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("intext:")[0]),
					'description': Markup('Search for sites with the given words in the text of the page'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("inanchor:")[0]),
					'description': Markup('Search for sites that have the given words in links pointing to them'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("cache:")[0]),
					'description': Markup('Show most recent cache of a webpage'),
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
			'link': 'https://osintframework.com/',
			'title': 'OSINT Framework',
			'description': Markup('A huge collection of resources to use when doing OSINT investigations'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://inteltechniques.com/',
			'title': 'Intel Techniques',
			'description': Markup('A truly exceptional resource for OSINT investigators'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

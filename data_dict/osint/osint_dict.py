import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('osint', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'osint'
meta = {
	'title': 'OSINT Cheatsheet',
	'description': 'Tools · Archived Information · Search Engines · Terminology · Search Operators',
	'keywords': 'osint, open source intelligence, sigint, humint, socmint, opsec, investigation, tools, online, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/OSINT/',

	'opengraph_title': 'OSINT Cheatsheet',
	'opengraph_description': 'Tools · Archived Information · Search Engines · Terminology · Search Operators',
	'opengraph_image': 'opengraph_osint.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/osint/',

	'twitter_title': 'OSINT Cheatsheet',
	'twitter_description': 'Tools · Archived Information · Search Engines · Terminology · Search Operators',
	'twitter_image': 'twitter_card_osint.png',
}
information = {
	'tool': 'OSINT',
	'title': 'OSINT Cheatsheet',
	'subtitle': 'This site is a reference for Open Source Intelligence (OSINT)',
	'description': 'Open Source Intelligence deals with information gathered from publicly available sources that can be used in an intelligence context. This can vary widely and be anything from hashes, emails, newspaper articles or geo-locations.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
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
		'description': 'Tools used for OSINT investigations',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '97847ac62f4b4d4197bdfa0c2e5f9ee2',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('16e2dcd41309443aaf48966fc075e431')[0]),
					'flag': helper.set_entry_command_string("Maltego"),
					'description': Markup('Powerfull tool to network topology mapping and much more'),
					'example': helper.example_path(),
					'ext_link': 'https://www.maltego.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('85c5d3ec7a6d4fee836b07b8c1efcb20')[0]),
					'flag': helper.set_entry_command_string("SpiderFoot"),
					'description': Markup('A tool that automates OSINT collection'),
					'example': helper.example_path(),
					'ext_link': 'https://github.com/smicallef/spiderfoot',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8f9d2dd7303e41c687a6a1961eb2d084')[0]),
					'flag': helper.set_entry_command_string("twint"),
					'description': Markup('An advanced Twitter scraping & OSINT tool written in Python that doesn\'t use Twitter\'s API, allowing you to scrape a user\'s followers, following, Tweets and more while evading most API limitations'),
					'example': helper.example_path(),
					'ext_link': 'https://github.com/twintproject/twint',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a11f54f1b8a44deba0d93cba16673b3d')[0]),
					'flag': helper.set_entry_command_string("Photon"),
					'description': Markup('Incredibly fast crawler designed for OSINT'),
					'example': helper.example_path(),
					'ext_link': 'https://github.com/s0md3v/Photon',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c54975a7fda749a1b294afaed4e9b2c1')[0]),
					'flag': helper.set_entry_command_string("HaveIbeenPwned"),
					'description': Markup('Search email addresses that has been subject to a data breach and get information about the data breach'),
					'example': helper.example_path(),
					'ext_link': 'https://haveibeenpwned.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('22381d88241b440f8c0258de5e006ed9')[0]),
					'flag': helper.set_entry_command_string("Pipl"),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': 'https://pipl.com/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d8760d9c96f74c62b2258a88c44a778f')[0]),
					'flag': helper.set_entry_command_string("Google Hacking Databse"),
					'description': Markup('Dorks for querying sensitive information or vulnerable content'),
					'example': helper.example_path(),
					'ext_link': 'https://www.exploit-db.com/google-hacking-database',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Terms'),
		'subtitle': '',
		'description': 'Terms used in relation to OSINT',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '80a4d867a020436391101b05f5c8f8b9',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('869400e9c91b45829e6a9084cda77416')[0]),
					'flag': helper.set_entry_command_string("Dorking"),
					'description': Markup('Using search parameters to narrow down results in a Google search for information which is otherwise difficult to locate (see tools for a database of dorks)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Archived Information'),
		'subtitle': '',
		'description': 'Search through cached and archived content',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '346d50a591714e6a844352ede8b197fa',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c81150d459614058a8c61ec66d2f000b')[0]),
					'flag': helper.set_entry_command_string("The Wayback Machine"),
					'description': Markup('Archive of webpages throughout time as they change'),
					'example': helper.example_path(),
					'ext_link': 'http://archive.org/web/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('777df9d6888b45eea356d65a9048ac3c')[0]),
					'flag': helper.set_entry_command_string("Archive Today"),
					'description': Markup('Another timecapsule for webpages'),
					'example': helper.example_path(),
					'ext_link': 'http://archive.vn/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6a2e69532e294553a993f14f7e96bb08')[0]),
					'flag': helper.set_entry_command_string("Google and Bing"),
					'description': Markup('Both offer cached versions of webpages'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '394883eed8994fc39f529c45ccba46d4',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c0e02104ed3a42a3a88b1afcdacb57bd')[0]),
					'flag': helper.set_entry_command_string("\"Search Term\""),
					'description': Markup('Search for the exact phase'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('927ffd3baaf94b7993536004fce8a9c5')[0]),
					'flag': helper.set_entry_command_string("TermA OR TermB"),
					'description': Markup('Search for TermA or TermB'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8621f3740a2f4c2f8abdaba39cf93177')[0]),
					'flag': helper.set_entry_command_string("site:www.example.com"),
					'description': Markup('Return results only from www.example.com'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('64d2a48beda146be888390290b0428ae')[0]),
					'flag': helper.set_entry_command_string("filetype:pdf"),
					'description': Markup('Return results that are of filetype pdf'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('85664d2781324b21a0a7de366ec867ac')[0]),
					'flag': helper.set_entry_command_string("intitle:"),
					'description': Markup('Search for sites with the given words in their title'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7d2243d882944f79a23375b91e926f79')[0]),
					'flag': helper.set_entry_command_string("inurl:"),
					'description': Markup('Search for sites with the given words in their URL'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('85398bf586344f9293b48a0194326a1b')[0]),
					'flag': helper.set_entry_command_string("intext:"),
					'description': Markup('Search for sites with the given words in the text of the page'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('526621609bb2466cb93725c59075cf45')[0]),
					'flag': helper.set_entry_command_string("inanchor:"),
					'description': Markup('Search for sites that have the given words in links pointing to them'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4798fbfd38164dda9f2e8d882221fc42')[0]),
					'flag': helper.set_entry_command_string("cache:"),
					'description': Markup('Show most recent cache of a webpage'),
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
		{
			'link': 'http://www.shodanhq.com/',
			'title': 'Shodan',
			'description': Markup('Discover various online devices (IoT, thermostats, printers, cameras)'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://haveibeenpwned.com/',
			'title': 'Have I Been Pwned',
			'description': Markup('Search email addresses to see if they have been involved in any known data breaches'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://github.com/qeeqbox/social-analyzer',
			'title': 'Social Analyzer',
			'description': Markup('API, CLI & Web App for analyzing & finding a person\'s profile across 350+ social media websites'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

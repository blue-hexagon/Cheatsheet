import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('http_status', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'http_status'
information = {
	'tool': 'HTTP',
	'title': 'HTTP Cheatsheet',
	'subtitle': 'This site is a reference for the HyperText-Transfer Protocol (HTTP)',
	'description': 'HTTP is the foundation for communication on the World Wide Web. The development of the protocol was initiated by Sir Tim Berners Lee in 1989 at CERN. Three version (HTTP/1. HTTP/2 and HTTP/3) exists. HTTP/1 is no longer widespread and adoption is moving towards HTTP/3 whereas HTTP/2 is virtually supported by all browsers at this point. HTTP/3 uses UDP instead of TCP for the underlying transport protocol. HTTP/3 is enabled by default on the latest MacOS releases and can be enabled in stable versions of Chrome and Firefox.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'HTTP',
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
		'heading': helper.set_folder('1xx'),
		'subtitle': 'Informational Responses',
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
					'flag': Markup(helper.set_entry_folder("100")[0]),
					'description': Markup('Continue'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/100',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("101")[0]),
					'description': Markup('Switching Protocols'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/101',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("102")[0]),
					'description': Markup('Processing'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/102',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('2xx'),
		'subtitle': 'Success Responses',
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
					'flag': Markup(helper.set_entry_folder("200")[0]),
					'description': Markup('OK'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/200',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("201")[0]),
					'description': Markup('Created'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/201',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("202")[0]),
					'description': Markup('Accepted'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/202',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("203")[0]),
					'description': Markup('Non-Authoritative Information'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/203',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("204")[0]),
					'description': Markup('No Content'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/204',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("205")[0]),
					'description': Markup('Reset Content'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/205',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("206")[0]),
					'description': Markup('Partial Content'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/206',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("207")[0]),
					'description': Markup('Multi-Status (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/207',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("208")[0]),
					'description': Markup('Already Reported (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/208',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("226")[0]),
					'description': Markup('IM Used'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/209',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},

			]
		}
	},
	{
		'heading': helper.set_folder('3xx'),
		'subtitle': 'Redirection Responses',
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
					'flag': Markup(helper.set_entry_folder("300")[0]),
					'description': Markup('Multiple Choices'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/300',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("301")[0]),
					'description': Markup('Moved Permanently'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/301',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("302")[0]),
					'description': Markup('Found'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/302',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("303")[0]),
					'description': Markup('See Other'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/303',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("304")[0]),
					'description': Markup('Not Modified'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/304',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("305")[0]),
					'description': Markup('Use Proxy'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/305',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("306")[0]),
					'description': Markup('(Unused)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/306',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("307")[0]),
					'description': Markup('Temporary Redirect'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/307',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("308")[0]),
					'description': Markup('Permanent Redirect (experimental)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/308',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('4xx'),
		'subtitle': 'Client Error Responses',
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
					'flag': Markup(helper.set_entry_folder("400")[0]),
					'description': Markup('Bad Request'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/400',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("401")[0]),
					'description': Markup('Unauthorized'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/401',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("402")[0]),
					'description': Markup('Payment Required'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/402',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("403")[0]),
					'description': Markup('Forbidden'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/403',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("404")[0]),
					'description': Markup('Not Found'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/404',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("405")[0]),
					'description': Markup('Method Not Allowed'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/405',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("406")[0]),
					'description': Markup('Not Acceptable'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/406',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("407")[0]),
					'description': Markup('Proxy Authentication Required'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/407',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("408")[0]),
					'description': Markup('Request Timeout'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/408',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("409")[0]),
					'description': Markup('Conflict'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/409',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("410")[0]),
					'description': Markup('Gone'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/410',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("411")[0]),
					'description': Markup('Length Required'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/411',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("412")[0]),
					'description': Markup('Precondition Failed'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/412',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("413")[0]),
					'description': Markup('Request Entity Too Large'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/413',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("414")[0]),
					'description': Markup('Request-URI Too Long'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/414',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("415")[0]),
					'description': Markup('Unsupported Media Type'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/415',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("416")[0]),
					'description': Markup('Requested Range Not Satisfiable'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/416',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("417")[0]),
					'description': Markup('Expectation Failed'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/417',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("418")[0]),
					'description': Markup('I\'m a teapot (RFC 2324)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/418',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("420")[0]),
					'description': Markup('Enhance Your Calm (Twitter)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/420',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("422")[0]),
					'description': Markup('Unprocessable Entity (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/422',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("423")[0]),
					'description': Markup('Locked (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/423',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("424")[0]),
					'description': Markup('Failed Dependency (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/424',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("425")[0]),
					'description': Markup('Reserved for WebDAV'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/425',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("426")[0]),
					'description': Markup('Upgrade Required'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/426',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("428")[0]),
					'description': Markup('Precondition Required'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/428',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("429")[0]),
					'description': Markup('Too Many Requests'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/429',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("431")[0]),
					'description': Markup('Request Header Fields Too Large'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/431',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("444")[0]),
					'description': Markup('No Response (Nginx)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/444',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("449")[0]),
					'description': Markup('Retry With (Microsoft)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/449',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("450")[0]),
					'description': Markup('Blocked by Windows Parental Controls (Microsoft)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/450',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("451")[0]),
					'description': Markup('Unavailable For Legal Reasons'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/451',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("499")[0]),
					'description': Markup('Client Closed Request (Nginx)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/499',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},

			]
		}
	},
	{
		'heading': helper.set_folder('5xx'),
		'subtitle': 'Server Error Responses',
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
					'flag': Markup(helper.set_entry_folder("500")[0]),
					'description': Markup('Internal Server Error'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/500',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("501")[0]),
					'description': Markup('Not Implemented'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/501',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("502")[0]),
					'description': Markup('Bad Gateway'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/502',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("503")[0]),
					'description': Markup('Service Unavailable'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/503',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("504")[0]),
					'description': Markup('Gateway Timeout'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/504',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("505")[0]),
					'description': Markup('HTTP Version Not Supported'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/505',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("506")[0]),
					'description': Markup('Variant Also Negotiates (Experimental)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/506',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("507")[0]),
					'description': Markup('Insufficient Storage (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/507',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("508")[0]),
					'description': Markup('Loop Detected (WebDAV)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/508',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("509")[0]),
					'description': Markup('Bandwidth Limit Exceeded (Apache)'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/509',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("510")[0]),
					'description': Markup('Not Extended'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/510',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("511")[0]),
					'description': Markup('Network Authentication Required'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/511',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("598")[0]),
					'description': Markup('Network read timeout error'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/598',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("599")[0]),
					'description': Markup('Network connect timeout error'),
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/599',
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
			'link': 'https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html',
			'title': 'W3 RFC2616',
			'description': Markup('A description of the HTTP status codes'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://httpstatuses.com/',
			'title': 'HTTP Statuses',
			'description': Markup('An overview of the various HTTP statuses with descriptions of each'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

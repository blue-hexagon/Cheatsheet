import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('gnu-utils', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'gnu-utils'
information = {
	'tool': 'DNS',
	'title': 'DNS Cheatsheet',
	'subtitle': 'This site is a reference for The Domain Name System (DNS)',
	'description': '',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Linux CLI',
			[
				helper.characteristics.get('tool'),
			])
	],
	'topic_uris': [
		'tool',
	],
	# TODO: Set topic and characteristics!
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
		'': '',
	},
]
cheatsheet = [
	{
		'heading':helper.set_folder('Records'),
		'subtitle': 'DNS Records',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '29c0c36ca6ce4ad69461c9152654e1ce',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ce47500d01fa45948fbbfd19b9265974')[0]),
					'flag': helper.set_entry_command_string("A"),

					'description': Markup('IPv4 address. E.g. www.example.com:80'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0fa511538a7e438194120f682c1e71a0')[0]),
					'flag': helper.set_entry_command_string("AAAA"),

					'description': Markup('IPv6 address'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('823e5cd877de4fb7b5107b8a31018d6d')[0]),
					'flag': helper.set_entry_command_string("MX"),

					'description': Markup('Mail exchanger aka. a MX record. Specifies the mail servers responsible for accepting email on behalf of your domain.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('db4400442d8b47769875eeed2677a46d')[0]),
					'flag': helper.set_entry_command_string("CNAME"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f0829cc80da74b358a3061c38ca7fdca')[0]),
					'flag': helper.set_entry_command_string("TXT"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('947b6f7d97cc4fbc944f2b28d22812fb')[0]),
					'flag': helper.set_entry_command_string("NS"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f8b115e733e744a4815e7110bb16df63')[0]),
					'flag': helper.set_entry_command_string("ANY"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8a8a783206c04c4f8da30da26321bb38')[0]),
					'flag': helper.set_entry_command_string("HINFO"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cfd858efd85b460197ce24f9b8b84ba4')[0]),
					'flag': helper.set_entry_command_string("WKS"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7b819fac9a5e45dbb632bec76e5af311')[0]),
					'flag': helper.set_entry_command_string("PTR"),

					'description': Markup('Reverse DNS / PTR'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cfb4677e8be04b33a7e224dead4c74a1')[0]),
					'flag': helper.set_entry_command_string("SPF"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ba67228122d241cb97c110c6bfadeaf5')[0]),
					'flag': helper.set_entry_command_string("SOA"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('03e69a4fcc7240f798cb719ed9e24bf0')[0]),
					'flag': helper.set_entry_command_string("SRV"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4588ca8dd2464154b2a968185ffaf96e')[0]),
					'flag': helper.set_entry_command_string("DKIM"),

					'description': Markup(''),
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
	# ResourceCollector.recieve_resources_from_dicts(
	#     {
	#         'link': 'https://github.com',
	#         'title': 'Github',
	#         'description': Markup('A collection of thousands of git-repositories from individual users'),
	#         'footer': Markup('You properly know it'),
	#         'screencapture': ''
	#     },
	# )
]
affiliate_products = [],
# style="max-height:150px; max-width: 150px;
licensing = [
	Markup('')
]

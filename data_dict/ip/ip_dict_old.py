import os
import pathlib
from datetime import datetime

from markdown import markdown
from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('ip', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'ip'
information = {
	'tool': 'IP',
	'title': 'IP',
	'subtitle': 'This site is a reference for IPv4 and IPv6',
	'description': 'The Internet Protocol (IP) currently resides at v4 and is moving towards v6 - and has been for decades. IP is the principal communications protocol for interconnected devices and established the Internet. IP has the tasks of delivering packets from the source to a host destination. At the current rate IPv6 will be fully implemented by 2148. The reasons for the slow gradual adoption is associated with expensive transistioning costs.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'IP',
			[
				helper.characteristics.get('standard'),
			])
	],
	'topic_uris': [
		'standard',
	],

}
general_info_text = 'Worth Knowing about IPv4'
general_info_text_lead = 'Address Space'
general_info_links = {}
general_info = [
	Markup(markdown('The Internet is running out of IPv4 addresses and have been for decades. To combat this decade old problem IPv6 was introduced back in 1995. IPv4 has a maximum of 32^2 (32-bit) addresses (approximately 4 billion) and as you know we are about 6 billion people on the Earth. ')),
	Markup(markdown(
		'With the introduction of IPv6 the address-space grew by an ufathomable amount and will properly be around when we reach the status of a fully intergalactive species. The address space of IPv6 is 128-bit; don\'t get fooled by the 4x - that is around 340 trillion trillion trillion IP addresses (1,329,227,995,784,910,000,000,000,000,000,000,000) which is among other things, one of the reasons IPv6 addresses uses base-16 (hex notation).')),
]
general_info_flag = True
see_also = [
	{
	},
]

cheatsheet = [
	{
		'heading': helper.set_folder('Glossary'),
		'subtitle': 'Terminology',
		'description': 'Terms important to the Internet Protocol',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("CIDR")[0]),
					'description': Markup('Classless interdomain routing. Developed to provide more granularity than legacy classful addressing; CIDR notation is expressed as /##'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("DHCP")[0]),
					'description': Markup('Used on subnets to dynamically (and temporarily) allocate IP addresses. IPv6 uses DHCPv6'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("ICMP")[0]),
					'description': Markup('Internet Control Message Protocol - aka. "ping". Is used for error reporting between routers. The IPv6 version is named accordingly: ICMPv6'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Packet")[0]),
					'description': Markup('A packet is a quantity of bytes send from a device to another. It has address and sender fields which is why it is a neat analogy'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Address Exhaustion")[0]),
					'description': Markup('A term used when talking about IPv4\'s limited address space. It is countered by the enourmous address space introduced with IPv6'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("IGMP")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("IPsec")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("OSI")[0]),
					'description': Markup('Open Systems Interconnection. A conceptual model that characterises the communication protocols in telecommunication'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Internet Layer")[0]),
					'description': Markup('The layer at which IP packets reside. It sits at layer 4 in the OSI model'),
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
		'heading': helper.set_folder('Classful Ranges IPv4'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("A")[0]),
					'description': Markup('0.0.0.0 – 127.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("B")[0]),
					'description': Markup('128.0.0.0 - 191.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("C")[0]),
					'description': Markup('192.0.0.0 - 223.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("D")[0]),
					'description': Markup('224.0.0.0 - 239.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("E")[0]),
					'description': Markup('240.0.0.0 - 255.255.255.255'),
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
		'heading': helper.set_folder('Reserved Ranges IPv4'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Reserved',
				'Range'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("Localhost")[0]),
					'description': Markup('127.0.0.0 - 127.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("RFC 1918")[0]),
					'description': Markup('10.0.0.0 - 10.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("RFC 1918")[0]),
					'description': Markup('172.16.0.0 - 172.31.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("RFC 1918")[0]),
					'description': Markup('192.168.0.0 - 192.168.255.255'),
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
		'heading': helper.set_folder('IPv4 Subnetting'),
		'subtitle': 'Subnets and Subnetmasking',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Subnet',
				'Addresses'
				'Netmask'
			],
			'data': [

				{
					'flag': Markup(helper.set_entry_folder("/31")[0]),
					'addresses': Markup('2'),
					'netmask': Markup('255.255.255.254'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/30")[0]),
					'addresses': Markup('4'),
					'netmask': Markup('255.255.255.252'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/29")[0]),
					'addresses': Markup('8'),
					'netmask': Markup('255.255.255.248'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/28")[0]),
					'addresses': Markup('16'),
					'netmask': Markup('255.255.255.240'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/27")[0]),
					'addresses': Markup('32'),
					'netmask': Markup('255.255.255.224'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/26")[0]),
					'addresses': Markup('64'),
					'netmask': Markup('255.255.255.192'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/25")[0]),
					'addresses': Markup('128'),
					'netmask': Markup('255.255.255.128'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/24")[0]),
					'addresses': Markup('256'),
					'netmask': Markup('255.255.255.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/23")[0]),
					'addresses': Markup('512'),
					'netmask': Markup('255.255.254.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/22")[0]),
					'addresses': Markup('1024'),
					'netmask': Markup('255.255.252.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/21")[0]),
					'addresses': Markup('2048'),
					'netmask': Markup('255.255.248.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/20")[0]),
					'addresses': Markup('4096'),
					'netmask': Markup('255.255.240.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/19")[0]),
					'addresses': Markup('8192'),
					'netmask': Markup('255.255.224.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/18")[0]),
					'addresses': Markup('16384'),
					'netmask': Markup('255.255.192.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/17")[0]),
					'addresses': Markup('32768'),
					'netmask': Markup('255.255.128.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/16")[0]),
					'addresses': Markup('65536'),
					'netmask': Markup('255.255.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/15")[0]),
					'addresses': Markup('131072'),
					'netmask': Markup('255.254.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/14")[0]),
					'addresses': Markup('262144'),
					'netmask': Markup('255.252.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/13")[0]),
					'addresses': Markup('524288'),
					'netmask': Markup('255.248.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/12")[0]),
					'addresses': Markup('1048576'),
					'netmask': Markup('255.240.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/11")[0]),
					'addresses': Markup('2097152'),
					'netmask': Markup('255.224.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/10")[0]),
					'addresses': Markup('4194304'),
					'netmask': Markup('255.192.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/9")[0]),
					'addresses': Markup('8388608'),
					'netmask': Markup('255.128.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/8")[0]),
					'addresses': Markup('16777216'),
					'netmask': Markup('255.0.0.0'),
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
		'heading': helper.set_folder('IPv6 Subnetting'),
		'subtitle': 'Subnets and Subnetmasking',
		'description': '',
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Subnet',
				'Addresses'
				'Amount of a /64'
			],
			'data': [

				{
					'flag': Markup(helper.set_entry_folder("/128")[0]),
					'addresses': Markup('1'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/127")[0]),
					'addresses': Markup('2'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/126")[0]),
					'addresses': Markup('4'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/125")[0]),
					'addresses': Markup('8'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/124")[0]),
					'addresses': Markup('16'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/123")[0]),
					'addresses': Markup('32'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/122")[0]),
					'addresses': Markup('64'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/121")[0]),
					'addresses': Markup('128'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/120")[0]),
					'addresses': Markup('256'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/119")[0]),
					'addresses': Markup('512'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/118")[0]),
					'addresses': Markup('1,024'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/117")[0]),
					'addresses': Markup('2,048'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/116")[0]),
					'addresses': Markup('4,096'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/115")[0]),
					'addresses': Markup('8,192'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/114")[0]),
					'addresses': Markup('16,384'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/113")[0]),
					'addresses': Markup('32,768'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/112")[0]),
					'addresses': Markup('65,536'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/111")[0]),
					'addresses': Markup('131,072'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/110")[0]),
					'addresses': Markup('262,144'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/109")[0]),
					'addresses': Markup('524,288'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/108")[0]),
					'addresses': Markup('1,048,576'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/107")[0]),
					'addresses': Markup('2,097,152'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/106")[0]),
					'addresses': Markup('4,194,304'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/105")[0]),
					'addresses': Markup('8,388,608'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/104")[0]),
					'addresses': Markup('16,777,216'),
					'amount': Markup('This is equivalent to an IPv4 Internet or IPv4 /8'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/103")[0]),
					'addresses': Markup('33,554,432'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/102")[0]),
					'addresses': Markup('67,108,864'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/101")[0]),
					'addresses': Markup('134,217,728'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/100")[0]),
					'addresses': Markup('268,435,456'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/99")[0]),
					'addresses': Markup('536,870,912'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/98")[0]),
					'addresses': Markup('1,073,741,824'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/97")[0]),
					'addresses': Markup('2,147,483,648'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/96")[0]),
					'addresses': Markup('4,294,967,296'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/95")[0]),
					'addresses': Markup('8,589,934,592'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/94")[0]),
					'addresses': Markup('17,179,869,184'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/93")[0]),
					'addresses': Markup('34,359,738,368'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/92")[0]),
					'addresses': Markup('68,719,476,736'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/91")[0]),
					'addresses': Markup('137,438,953,472'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/90")[0]),
					'addresses': Markup('274,877,906,944'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/89")[0]),
					'addresses': Markup('549,755,813,888'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/88")[0]),
					'addresses': Markup('1,099,511,627,776'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/87")[0]),
					'addresses': Markup('2,199,023,255,552'),
					'amount': Markup('1/8,388,608'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/86")[0]),
					'addresses': Markup('4,398,046,511,104'),
					'amount': Markup('1/4,194,304'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/85")[0]),
					'addresses': Markup('8,796,093,022,208'),
					'amount': Markup('1/2,097,152'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/84")[0]),
					'addresses': Markup('17,592,186,044,416'),
					'amount': Markup('1/1,048,576'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/83")[0]),
					'addresses': Markup('35,184,372,088,832'),
					'amount': Markup('1/524,288'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/82")[0]),
					'addresses': Markup('70,368,744,177,664'),
					'amount': Markup('1/262,144'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/81")[0]),
					'addresses': Markup('140,737,488,355,328'),
					'amount': Markup('1/131,072'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/80")[0]),
					'addresses': Markup('281,474,976,710,656'),
					'amount': Markup('1/65,536'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/79")[0]),
					'addresses': Markup('562,949,953,421,312'),
					'amount': Markup('1/32,768'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/78")[0]),
					'addresses': Markup('1,125,899,906,842,620'),
					'amount': Markup('1/16,384'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/77")[0]),
					'addresses': Markup('2,251,799,813,685,240'),
					'amount': Markup('1/8,192'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/76")[0]),
					'addresses': Markup('4,503,599,627,370,490'),
					'amount': Markup('1/4,096'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/75")[0]),
					'addresses': Markup('9,007,199,254,740,990'),
					'amount': Markup('1/2,048'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/74")[0]),
					'addresses': Markup('18,014,398,509,481,900'),
					'amount': Markup('1/1,024'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/73")[0]),
					'addresses': Markup('36,028,797,018,963,900'),
					'amount': Markup('1/512'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/72")[0]),
					'addresses': Markup('72,057,594,037,927,900'),
					'amount': Markup('1/256'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/71")[0]),
					'addresses': Markup('144,115,188,075,855,000'),
					'amount': Markup('1/128'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/70")[0]),
					'addresses': Markup('288,230,376,151,711,000'),
					'amount': Markup('1/64'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/69")[0]),
					'addresses': Markup('576,460,752,303,423,000'),
					'amount': Markup('1/32'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/68")[0]),
					'addresses': Markup('1,152,921,504,606,840,000'),
					'amount': Markup('1/16'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/67")[0]),
					'addresses': Markup('2,305,843,009,213,690,000'),
					'amount': Markup('1/8'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/66")[0]),
					'addresses': Markup('4,611,686,018,427,380,000'),
					'amount': Markup('1/4'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/65")[0]),
					'addresses': Markup('9,223,372,036,854,770,000'),
					'amount': Markup('1/2'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/64")[0]),
					'addresses': Markup('18,446,744,073,709,500,000'),
					'amount': Markup('This is the standard end user allocation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/63")[0]),
					'addresses': Markup('36,893,488,147,419,100,000'),
					'amount': Markup('2'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/62")[0]),
					'addresses': Markup('73,786,976,294,838,200,000'),
					'amount': Markup('4'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/61")[0]),
					'addresses': Markup('147,573,952,589,676,000,000'),
					'amount': Markup('8'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/60")[0]),
					'addresses': Markup('295,147,905,179,352,000,000'),
					'amount': Markup('16'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/59")[0]),
					'addresses': Markup('590,295,810,358,705,000,000'),
					'amount': Markup('32'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/58")[0]),
					'addresses': Markup('1,180,591,620,717,410,000,000'),
					'amount': Markup('64'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/57")[0]),
					'addresses': Markup('2,361,183,241,434,820,000,000'),
					'amount': Markup('128'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/56")[0]),
					'addresses': Markup('4,722,366,482,869,640,000,000'),
					'amount': Markup('256'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/55")[0]),
					'addresses': Markup('9,444,732,965,739,290,000,000'),
					'amount': Markup('512'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/54")[0]),
					'addresses': Markup('18,889,465,931,478,500,000,000'),
					'amount': Markup('1,024'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/53")[0]),
					'addresses': Markup('37,778,931,862,957,100,000,000'),
					'amount': Markup('2,048'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/52")[0]),
					'addresses': Markup('75,557,863,725,914,300,000,000'),
					'amount': Markup('4,096'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/51")[0]),
					'addresses': Markup('151,115,727,451,828,000,000,000'),
					'amount': Markup('8,192'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/50")[0]),
					'addresses': Markup('302,231,454,903,657,000,000,000'),
					'amount': Markup('16,384'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/49")[0]),
					'addresses': Markup('604,462,909,807,314,000,000,000'),
					'amount': Markup('32,768'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/48")[0]),
					'addresses': Markup('1,208,925,819,614,620,000,000,000'),
					'amount': Markup('65,536 This is the standard business allocation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/47")[0]),
					'addresses': Markup('2,417,851,639,229,250,000,000,000'),
					'amount': Markup('131,072'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/46")[0]),
					'addresses': Markup('4,835,703,278,458,510,000,000,000'),
					'amount': Markup('262,144'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/45")[0]),
					'addresses': Markup('9,671,406,556,917,030,000,000,000'),
					'amount': Markup('524,288'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/44")[0]),
					'addresses': Markup('19,342,813,113,834,000,000,000,000'),
					'amount': Markup('1,048,576'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/43")[0]),
					'addresses': Markup('38,685,626,227,668,100,000,000,000'),
					'amount': Markup('2,097,152'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/42")[0]),
					'addresses': Markup('77,371,252,455,336,200,000,000,000'),
					'amount': Markup('4,194,304'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/41")[0]),
					'addresses': Markup('154,742,504,910,672,000,000,000,000'),
					'amount': Markup('8,388,608'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/40")[0]),
					'addresses': Markup('309,485,009,821,345,000,000,000,000'),
					'amount': Markup('16,777,216'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/39")[0]),
					'addresses': Markup('618,970,019,642,690,000,000,000,000'),
					'amount': Markup('33,554,432'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/38")[0]),
					'addresses': Markup('1,237,940,039,285,380,000,000,000,000'),
					'amount': Markup('67,108,864'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/37")[0]),
					'addresses': Markup('2,475,880,078,570,760,000,000,000,000'),
					'amount': Markup('134,217,728'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/36")[0]),
					'addresses': Markup('4,951,760,157,141,520,000,000,000,000'),
					'amount': Markup('268,435,456'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/35")[0]),
					'addresses': Markup('9,903,520,314,283,040,000,000,000,000'),
					'amount': Markup('536,870,912'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/34")[0]),
					'addresses': Markup('19,807,040,628,566,000,000,000,000,000'),
					'amount': Markup('1,073,741,824'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/33")[0]),
					'addresses': Markup('39,614,081,257,132,100,000,000,000,000'),
					'amount': Markup('2,147,483,648'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/32")[0]),
					'addresses': Markup('79,228,162,514,264,300,000,000,000,000'),
					'amount': Markup('4,294,967,296 This is the standard ISP Allocation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/31")[0]),
					'addresses': Markup('158,456,325,028,528,000,000,000,000,000'),
					'amount': Markup('8,589,934,592'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/30")[0]),
					'addresses': Markup('316,912,650,057,057,000,000,000,000,000'),
					'amount': Markup('17,179,869,184'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/29")[0]),
					'addresses': Markup('633,825,300,114,114,000,000,000,000,000'),
					'amount': Markup('34,359,738,368'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/28")[0]),
					'addresses': Markup('1,267,650,600,228,220,000,000,000,000,000'),
					'amount': Markup('68,719,476,736'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/27")[0]),
					'addresses': Markup('2,535,301,200,456,450,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/26")[0]),
					'addresses': Markup('5,070,602,400,912,910,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/25")[0]),
					'addresses': Markup('10,141,204,801,825,800,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/24")[0]),
					'addresses': Markup('20,282,409,603,651,600,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/23")[0]),
					'addresses': Markup('40,564,819,207,303,300,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/22")[0]),
					'addresses': Markup('81,129,638,414,606,600,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/21")[0]),
					'addresses': Markup('162,259,276,829,213,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/20")[0]),
					'addresses': Markup('324,518,553,658,426,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/19")[0]),
					'addresses': Markup('649,037,107,316,853,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/18")[0]),
					'addresses': Markup('1,298,074,214,633,700,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/17")[0]),
					'addresses': Markup('2,596,148,429,267,410,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/16")[0]),
					'addresses': Markup('5,192,296,858,534,820,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/15")[0]),
					'addresses': Markup('10,384,593,717,069,600,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/14")[0]),
					'addresses': Markup('20,769,187,434,139,300,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/13")[0]),
					'addresses': Markup('41,538,374,868,278,600,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/12")[0]),
					'addresses': Markup('83,076,749,736,557,200,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/11")[0]),
					'addresses': Markup('166,153,499,473,114,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/10")[0]),
					'addresses': Markup('332,306,998,946,228,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/9")[0]),
					'addresses': Markup('664,613,997,892,457,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("/8")[0]),
					'addresses': Markup('1,329,227,995,784,910,000,000,000,000,000,000,000'),
					'amount': Markup(''),
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
			'link': 'https://github.com',
			'title': 'Github',
			'description': Markup('A collection of thousands of git-repositories from individual users'),
			'footer': Markup('You properly know it'),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

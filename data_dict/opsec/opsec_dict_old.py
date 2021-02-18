import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('opsec', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'opsec'
information = {
	'tool': 'OpSec',
	'title': 'OpSec Cheatsheet',
	'subtitle': 'This site is a reference for Operational Security (OPSEC)',
	'description': 'Operations Security deals with identification of critical information, analysis of threats, analysis of vulnerabilities, assessment of risks and application of appropriate OpSec measures. This page concerns itself mainly with the latter alongside preventive measuers.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'OpSec',
			[
				helper.characteristics.get('standard'),
			])
	],
	'topic_uris': [
		'standard',
	],

}
general_info_text = ''
general_info_text_lead = 'Take Care of Your Threat Surface and Stay Cautious'
general_info_links = {}
general_info = [
	Markup(
		'Facebook exemplifies the axiom that if a product is free, you aren’t the customer. You are the product<br> - Micahel Bazzell'),
]
general_info_flag = True
see_also = [
	{
	},
]

cheatsheet = [
	{
		'heading': helper.set_folder('Phishing'),
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
					'flag': Markup(helper.set_entry_folder("phishing")[0]),
					'description': Markup('A general term for fradulent attempts to obtain sensitive information or data such as usernames, passwords, account details and so on. The term phishing has roots in the word phreaking'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Catphishing/catfishing")[0]),
					'description': Markup('Online deception that involces getting to know someone closely in order to extract sensitive information or data from them'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Email phishing")[0]),
					'description': Markup('Malicious emails that targets an individual or a multitude of people. Often contains a link to a malicious webpage or a piece of malware such as ransomware'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Sphearphishing")[0]),
					'description': Markup('Highly targeted phishing'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Angler phishing")[0]),
					'description': Markup('A relatively new attack vector. Essentially the same as smishing but constrained to Social Media platforms'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("vishing")[0]),
					'description': Markup('Phone phishing'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("smishing")[0]),
					'description': Markup('In line with vishing. Textual phishing. Can be either SMS or any other textual communication type such as Telegram, Messenger etc'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("whaling")[0]),
					'description': Markup('Term used to describe phishing against high-profile (business) targets'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		},
	},
	{
		'heading': helper.set_folder('Digital Extortion'),
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
					'flag': Markup(helper.set_entry_folder("Sextortion")[0]),
					'description': Markup('A woman (most often) initiating sexual contact over a webcam or similar while screencapturing the sexual acts and using the material to extort the target'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Ransomware")[0]),
					'description': Markup('A type of malware gaining traction in recent years. Works by holding your data ransom until you pay for a de-cryption key. Sometimes you get to have your data back, other times you do not'),
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
		'heading': helper.set_folder('Password Protection'),
		'subtitle': 'Protection against cracking and bruteforce attacks',
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
					'flag': Markup(helper.set_entry_folder("Password manager")[0]),
					'description': Markup('A password manager helps you manage logins and enables the use of complex random passwords for all your logins as you do not have to rely on memory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Cracking")[0]),
					'description': Markup('Reusing the same password makes cracking possible if you happend to ever fall victim to a databreach'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Data breach")[0]),
					'description': Markup('Sensitive information such as password hashes being leaked because of a security hole'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Bruteforcing")[0]),
					'description': Markup('Attempting to crack a password hash from a target whose data was leaked in a databreach'),
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
		'heading': helper.set_folder('Social Engineering'),
		'subtitle': '',
		'description': 'A practice dating back many years.',
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
					'flag': Markup(helper.set_entry_folder("Phreak")[0]),
					'description': Markup('A phone "phreaker". A type of social engineerer that gains entrance into telecommunication networks by use of social engineering tactics. Kevin Mitnick (formerly FBIs most wanted hacker) is well known for phreaking'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("2FA")[0]),
					'description': Markup('2-Factor Authentication. People have lost their life savings because of weak 2FA such as SMSs which can be either intercepted or in the case of social engineering redirected to a new cellphone own by the social engineer'),
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
		'heading': helper.set_folder('2-Factor Authentication'),
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
					'flag': Markup(helper.set_entry_folder("SMS")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Mobile Apps")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("RSA Keys")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Hardware Keys")[0]),
					'description': Markup('Yubi keys for example'),
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
		'heading': helper.set_folder('Attack Vectors'),
		'subtitle': '',
		'description': 'An attack vector is a threat-surface upon which an attacker may exploit a target device',
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
					'flag': Markup(helper.set_entry_folder("Phone")[0]),
					'description': Markup('Biometric IDs can sometimes be bypassed by a printed image. Your camera can be exploited. GPS can be exploited by webpages. Lots of scare stuff is possible'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("IOT")[0]),
					'description': Markup('Internet of things. This is a topic in and of itself'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Computer")[0]),
					'description': Markup('Computers are exceptionally prone to malware if used by people that have no clue about operational security practices'),
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
		'heading': helper.set_folder('Darknets'),
		'subtitle': '',
		'description': 'Parts of the Internet that run on seperate networks/protocols and thus are not indexed by regular search engines.',
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
					'flag': Markup(helper.set_entry_folder("I2P")[0]),
					'description': Markup('See link'),
					'example': helper.example_path(),
					'ext_link': 'https://geti2p.net/en/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Freenet")[0]),
					'description': Markup('A peer-to-peer platform for censorship-resistant communication and publishing'),
					'example': helper.example_path(),
					'ext_link': 'https://freenetproject.org/index.html',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Tor")[0]),
					'description': Markup('The Onion Router. A well-known darknet'),
					'example': helper.example_path(),
					'ext_link': 'https://www.torproject.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('SSH'),
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
					'flag': Markup(helper.set_entry_folder("Fingerprints")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("X11 forwarding")[0]),
					'description': Markup('Can be used to anonymize your computer through a VPS container whereby you can run a "clean slate"-browser session'),
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
		'heading': helper.set_folder('VPN'),
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
					'flag': Markup(helper.set_entry_folder("Logfiles")[0]),
					'description': Markup('Be aware of logfiles and 5/9/14-eyes agreeements'),
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
		'heading': helper.set_folder('Storage'),
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
					'flag': Markup(helper.set_entry_folder("Veracrypt")[0]),
					'description': Markup('Tool for encrypting portable media devices. You should use full-disk encryption on your PC. Veracrypt also has a neat feature for creating hidden encrypted volumes'),
					'example': helper.example_path(),
					'ext_link': 'https://www.veracrypt.fr/code/VeraCrypt/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Password Manager")[0]),
					'description': Markup('A tool for storing unique user-password combinations so that you do not have to rely on memory'),
					'example': helper.example_path(),
					'ext_link': 'https://keepassxc.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Full Disk Encryption")[0]),
					'description': Markup('A technique for encrypting a harddrive. For windows use Bitlocker. For Linux there are LUKS and Dm-cryot. It is possible on Android as well'),
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
		'heading': helper.set_folder('International Agreements'),
		'subtitle': '',
		'description': 'These alliances share sensitive information with each other. Sensitive information could for example be regular requests of VPN log files from service provider.',
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
					'flag': Markup(helper.set_entry_folder("5-eyes")[0]),
					'description': Markup('Formed in the 1940s between UK-USA. New Zealand, Canada and Australia later joined'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("9-eyes")[0]),
					'description': Markup('An expansion of the 5-eyes alliance. Cooperation is less intense. The Netherlands, France, Denmark and Norway are part of this alliance as well as the rest of the 5-eye countries'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("14-eyes")[0]),
					'description': Markup('An expansion of the 9-eyes alliance. Cooperation is less intense than the 9-eyes alliance. Countries added are Belgium, Italy, Germany, Spain and Sweden'),
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
		'heading': helper.set_folder('IRC'),
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
					'flag': Markup(helper.set_entry_folder("Cloaking")[0]),
					'description': Markup('IRC is by no means anonymous. You can however on many networks request a cloak which hides your identity'),
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
		'heading': helper.set_folder('Operating Systems'),
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
					'flag': Markup(helper.set_entry_folder("Tails")[0]),
					'description': Markup('A thumbdrive bootable OS with security features that runs TOR by default'),
					'example': helper.example_path(),
					'ext_link': 'https://tails.boum.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Qubes")[0]),
					'description': Markup('Https://www.qubes-os.org/'),
					'example': helper.example_path(),
					'ext_link': 'https://www.qubes-os.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}, {
					'flag': Markup(helper.set_entry_folder("Whonix")[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': 'https://www.whonix.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Email'),
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
					'flag': Markup(helper.set_entry_folder("Burner Email")[0]),
					'description': Markup('Multiple services exists to create one-time email addresses. Beware these are not usable by other people aswell. You can setup forwarding to an intermediate email address which then forwards to your regular email address'),
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
		'heading': helper.set_folder('Tracking'),
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
					'flag': Markup(helper.set_entry_folder("Cryptocurrency")[0]),
					'description': Markup('All transactions on Bitcoin for example are stored on public ledgers and can thus be traced easily. Some cryptocurrencies have made attempts to curcumvent this feature (e.g. Monero)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("SS7 Hijacking")[0]),
					'description': Markup('A vulnerability that allows hackers to read texts, listen to calls and track their locations. Has been used on. This vulerability have been used against populations and army-staff aswell as political targets'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Hot Wallet")[0]),
					'description': Markup('A bitcoin wallet that is online and connected'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Cold Wallet")[0]),
					'description': Markup('An offline wallet that is stored on a hardware device'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Fingerprinting")[0]),
					'description': Markup('A nasty technique. Read example'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Cookies")[0]),
					'description': Markup('Read example'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("Super Cookies")[0]),
					'description': Markup('Read example'),
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
			'link': 'https://keepassxc.org/',
			'title': 'KeePassXC',
			'description': Markup('Perhaps the best password manager out there. Easy to use and plain-dead simple'),
			'screencapture': '',
		},

	)

]

affiliate_products = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'title': Markup('Extreme Privacy: What It Takes to Disappear'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/B0898YGR58/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0898YGR58&linkCode=as2&tag=cheatsheet0e-20&linkId=fda7ae4519db3248ed0ea8cb8191befc"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B0898YGR58&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B0898YGR58" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Written by an expert on the topic (Michael Bazzell)'),
			'description': '',
		},
		{
			'title': Markup('Smartphone/webcam Camera Blocker'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/B083QGCFY8/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B083QGCFY8&linkCode=as2&tag=cheatsheet0e-20&linkId=710987f88ebbd41efb5af11d71cc53df"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B083QGCFY8&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B083QGCFY8" border="0" alt="" height="150"  style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('Faraday Bag for Your Devices'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/B08K2Q9RCK/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B08K2Q9RCK&linkCode=as2&tag=cheatsheet0e-20&linkId=5faf2b63b312405df92bdccb9eaa85bf"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B08K2Q9RCK&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B08K2Q9RCK" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('Yubikey 5Ci'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/B07WGJ1DNJ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07WGJ1DNJ&linkCode=as2&tag=cheatsheet0e-20&linkId=aeb6e679106a0d92cacfb0e0a0700018"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07WGJ1DNJ&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B07WGJ1DNJ" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('The Art of Invisibility'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/0316380520/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0316380520&linkCode=as2&tag=cheatsheet0e-20&linkId=432e70cfe6a170c327a8c71d1a83cc12"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0316380520&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=0316380520" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Written by Kevin Mitnick'),
			'description': 'Details his years as FBIs most wanted hacker. An interesting read in regards of OpSec',
		},
		{
			'title': Markup('Ghost in The Wires'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/0316037729/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0316037729&linkCode=as2&tag=cheatsheet0e-20&linkId=9a0ca0214f0cda8d07959bbf514ef04b"><img  style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0316037729&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=0316037729"  height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Written by Kevin Mitnick'),
			'description': 'Details his adventures as one of the most prolific phreakers',
		},
		{
			'title': Markup('Phishing Dark Waters'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/1118958470/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1118958470&linkCode=as2&tag=cheatsheet0e-20&linkId=1a3e8f70eb43fee5d4c074f75c6699aa"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1118958470&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=1118958470" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Great and very interesting read about phishing'),
			'description': '',
		},
		{
			'title': Markup('Microphone blocker'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/B07V9T14N3/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07V9T14N3&linkCode=as2&tag=cheatsheet0e-20&linkId=89cd6c2c44e83d12528d9070f778408d"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07V9T14N3&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B07V9T14N3" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Useful for important meetings'),
			'description': '',
		},
	)
]
licensing = [
	'',
]

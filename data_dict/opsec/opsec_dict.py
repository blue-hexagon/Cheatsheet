import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('opsec', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'opsec'
meta = {
	'title': 'OpSec Cheatsheet',
	'description': '',
	'keywords': 'opsec, security, operational security, intelligence, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/opsec/',

	'opengraph_title': 'OpSec Cheatsheet',
	'opengraph_description': '',
	'opengraph_image': '',
	'opengraph_url': 'https://www.cheatsheet.wtf/opsec/',

	'twitter_title': 'OpSec Cheatsheet',
	'twitter_description': '',
	'twitter_image': '',
}
information = {
	'tool': 'OpSec',
	'title': 'OpSec Cheatsheet',
	'subtitle': 'This site is a reference for Operational Security (OPSEC)',
	'description': 'Operations Security deals with identification of critical information, analysis of threats, analysis of vulnerabilities, assessment of risks and application of appropriate OpSec measures. This page concerns itself mainly with the latter alongside preventive measuers.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
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
general_info_text_lead = ''
general_info_links = {}
general_info = [
	Markup(
		'Facebook exemplifies the axiom that if a product is free, you aren’t the customer. You are the product.<br> - Micahel Bazzell'),
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
		'description': 'Phishing is type of social engineering attack. It occurs when an attacker masquerading as a trusted entity dupes a victim into opening an email, clicking a link or sharing sensitive information ',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '06bb3ca845284f76a8b18f8f1107fd87',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('350d17348c7e4d779cf0f30d42ca72a9')[0]),
					'flag': helper.set_entry_command_string("phishing"),
					'description': Markup('A general term for fradulent attempts to obtain sensitive information or data such as usernames, passwords, account details and so on. The term phishing has roots in the word phreaking'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3aa9ded4d7cb4f81bc33ad0cdad6b816')[0]),
					'flag': helper.set_entry_command_string("Catphishing/catfishing"),
					'description': Markup('Online deception that involces getting to know someone closely in order to extract sensitive information or data from them'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('907fc7cfcbed46eda6e5af0061d9d49d')[0]),
					'flag': helper.set_entry_command_string("Email phishing"),
					'description': Markup('Malicious emails that targets an individual or a multitude of people. Often contains a link to a malicious webpage or a piece of malware such as ransomware'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e6f159f3a7224866a3d218b0147570e4')[0]),
					'flag': helper.set_entry_command_string("Sphearphishing"),
					'description': Markup('Highly targeted phishing'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8dc27dc67cab49ef986798c5c19d355e')[0]),
					'flag': helper.set_entry_command_string("Angler phishing"),
					'description': Markup('A relatively new attack vector. Essentially the same as smishing but constrained to Social Media platforms'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bd5731de6360485d982110e13ce78b73')[0]),
					'flag': helper.set_entry_command_string("vishing"),
					'description': Markup('Phone phishing'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('28814fb1bf7c4ac18f379ba40572d5aa')[0]),
					'flag': helper.set_entry_command_string("smishing"),
					'description': Markup('In line with vishing. Textual phishing. Can be either SMS or any other textual communication type such as Telegram, Messenger etc'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dd4807b31f9d415c949c6c13375f52a6')[0]),
					'flag': helper.set_entry_command_string("whaling"),
					'description': Markup('Term used to describe phishing against high-profile (business) targets'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '14c59c7749fe47639cbf1f7cbd3598a8',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9b1d29d442c341e9bc44efb6b4e5c3cf')[0]),
					'flag': helper.set_entry_command_string("Sextortion"),
					'description': Markup('A woman (most often) initiating sexual contact over a webcam or similar while screencapturing the sexual acts and using the material to extort the target'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fef06ddaefbb408aa2cfa3525ee17d4c')[0]),
					'flag': helper.set_entry_command_string("Ransomware"),
					'description': Markup('A type of malware gaining traction in recent years. Works by holding your data ransom until you pay for a de-cryption key. Sometimes you get to have your data back, other times you do not'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '76f1ae932973441eb3a636c0d88a7e41',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('43851276faad4e45823b17fd7aac7397')[0]),
					'flag': helper.set_entry_command_string("Password manager"),
					'description': Markup('A password manager helps you manage logins and enables the use of complex random passwords for all your logins as you do not have to rely on memory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('72beaaa8d12f4795bf814e29c2737b28')[0]),
					'flag': helper.set_entry_command_string("Cracking"),
					'description': Markup('Reusing the same password makes cracking possible if you happend to ever fall victim to a databreach'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3e3e44bfcb694d6e9cdc479879dc054b')[0]),
					'flag': helper.set_entry_command_string("Data breach"),
					'description': Markup('Sensitive information such as password hashes being leaked because of a security hole'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e6df709355b0410a835fcb2fefba19b6')[0]),
					'flag': helper.set_entry_command_string("Bruteforcing"),
					'description': Markup('Attempting to crack a password hash from a target whose data was leaked in a databreach'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '50a5dabfd87a487fa316efe0e4fc0e89',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('361b1c4ce7594c17bf3e34697eb54061')[0]),
					'flag': helper.set_entry_command_string("Phreak"),
					'description': Markup('A phone "phreaker". A type of social engineerer that gains entrance into telecommunication networks by use of social engineering tactics. Kevin Mitnick (formerly FBIs most wanted hacker) is well known for phreaking'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cb3aafa9f49d4a66a5272d91bed619ee')[0]),
					'flag': helper.set_entry_command_string("2FA"),
					'description': Markup('2-Factor Authentication. People have lost their life savings because of weak 2FA such as SMSs which can be either intercepted or in the case of social engineering redirected to a new cellphone own by the social engineer'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '3aa7170ccfcd4046ae79258df119682f',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('5f05651bbd7b41f386fba0989ad7af21')[0]),
					'flag': helper.set_entry_command_string("SMS"),
					'description': Markup('One time passwords through SMS; susceptible to SIM-swapping fraud.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8f1e53be97334d59920ea9c58f08beb5')[0]),
					'flag': helper.set_entry_command_string("Mobile Apps"),
					'description': Markup('One time codes through apps like Google Authenticator for example.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ac348f697ef24c748adf1a772a0fcffa')[0]),
					'flag': helper.set_entry_command_string("Hardware Keys"),
					'description': Markup('Hardware authentication device like a YubiKey for example.'),
					'example': helper.example_path(),
					'ext_link': 'https://en.wikipedia.org/wiki/YubiKey',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': 'd8392414ff294720a0ab4ae90f1cf5f6',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8a6f6314d5d4493ca13bc3e2460dd725')[0]),
					'flag': helper.set_entry_command_string("Phone"),
					'description': Markup('Biometric IDs can sometimes be bypassed by a printed image. Your camera can be exploited. GPS location can be obtained by webpages.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('de41f1538ccc464cb32ded350146e986')[0]),
					'flag': helper.set_entry_command_string("IOT"),
					'description': Markup('Internet of things-devices are known for their weak, hardcoded or guessable passwords, insecure default settings, lack of secure update mechanisms and a lot more.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9c3018287bc4464f84ec8192d42bf8a4')[0]),
					'flag': helper.set_entry_command_string("Computer"),
					'description': Markup('Computers are exceptionally prone to malware if used by people that have no clue about common security practices'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2c3a18d87bc2464f84ecf19fda2bf8a4')[0]),
					'flag': helper.set_entry_command_string("BYOD"),
					'description': Markup('Bring Your Own Device (BYOD) comes with a lot risks. Data-theft, lost devices and malware infiltration are perhaps the most significant.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '29587536e62d495cae2ee1aa22ac6f33',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8bcaf4f88a3140768c54b315bf1cee4c')[0]),
					'flag': helper.set_entry_command_string("I2P"),
					'description': Markup('The (I)nvisible (I)nternet (P)roject. A fully encrypted private network layer.'),
					'example': helper.example_path(),
					'ext_link': 'https://geti2p.net/en/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b62e79f973734b0494198e5f190d4bb5')[0]),
					'flag': helper.set_entry_command_string("Freenet"),
					'description': Markup('A peer-to-peer platform for censorship-resistant communication and publishing'),
					'example': helper.example_path(),
					'ext_link': 'https://freenetproject.org/index.html',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0728af5fffb648809f4e697cd26aa3c1')[0]),
					'flag': helper.set_entry_command_string("Tor"),
					'description': Markup('The Onion Router. Perhaps the most well known darknet'),
					'example': helper.example_path(),
					'ext_link': 'https://www.torproject.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('SSH'),
		'subtitle': '',
		'description': 'SSH (Secure Shell) is a protocol used for secure remote access',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '711d11b000724236b795bfb213347282',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8856e565f48e46489ef4edce27925708')[0]),
					'flag': helper.set_entry_command_string("Fingerprints"),
					'description': Markup('If an SSH fingerprint changes it either means the machine you are connecting to has changed their public key or that you are connecting to a different machine than what you think.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3c9fb69d706e4b6584b540ef2a1d7c99')[0]),
					'flag': helper.set_entry_command_string("X11 forwarding"),
					'description': Markup('Can be used to anonymize your computer through a VPS container whereby you can run a "clean slate"-browser session'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('VPN'),
		'subtitle': '',
		'description': 'VPN (Virtual Private Network) provides privacy, anonymity and security to users by creating a connection to a private network across a public network like the Internet',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '7d3799e98d1a465e8cc0ca4451795c56',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('78bb7dcd239f4383aa1dcb660da31a2d')[0]),
					'flag': helper.set_entry_command_string("Logfiles"),
					'description': Markup('Be aware if your provider saves logfiles or not (they might have their hand forced at some point if they do), or just assume all communication is secretly tapped.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Disk Storage'),
		'subtitle': '',
		'description': 'Drive storage refers to the physical storage of information on personal computers, laptops or phones',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6a0ad919ac3d4ed0855e05b7506a074b',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('adbca3b021e3411dadbb1540c73f690a')[0]),
					'flag': helper.set_entry_command_string("Veracrypt"),
					'description': Markup('Tool for encrypting portable media devices. You should use full-disk encryption on your PC. Veracrypt also has a neat feature for creating hidden encrypted volumes'),
					'example': helper.example_path(),
					'ext_link': 'https://www.veracrypt.fr/code/VeraCrypt/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cc37f5fba1c44e6991c0a1097c58481b')[0]),
					'flag': helper.set_entry_command_string("Password Manager"),
					'description': Markup('A tool for storing unique user-password combinations so that you do not have to rely on memory'),
					'example': helper.example_path(),
					'ext_link': 'https://keepassxc.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e84e763785cf4bba839fc98cc48e357f')[0]),
					'flag': helper.set_entry_command_string("Full Disk Encryption"),
					'description': Markup('A technique for encrypting a harddrive. For windows use Bitlocker. For Linux there are LUKS and Dm-cryot. It can be done on Android as well'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': 'ec012dbbf2f24055b674ddc5a8c6af5c',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c208cc47a62c468c97d8edf6367a30e4')[0]),
					'flag': helper.set_entry_command_string("5-eyes"),
					'description': Markup('Formed in the 1940s between UK-USA. New Zealand, Canada and Australia later joined'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fd4b1ee423a440809151fdc90e70c543')[0]),
					'flag': helper.set_entry_command_string("9-eyes"),
					'description': Markup('An expansion of the 5-eyes alliance. Cooperation is less intense. The Netherlands, France, Denmark and Norway are part of this alliance as well as the rest of the 5-eye countries'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d12ba3fe99654ce7918724ddf7280d39')[0]),
					'flag': helper.set_entry_command_string("14-eyes"),
					'description': Markup('An expansion of the 9-eyes alliance. Cooperation is less intense than the 9-eyes alliance. Countries added are Belgium, Italy, Germany, Spain and Sweden'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('IRC'),
		'subtitle': 'Internet Relay Chat',
		'description': 'An application layer protocol that facilitates text communication through a client-server model',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '1f8506fff1e941efb24eb232542eb8b1',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('10f02b91fb534a15946bd2e0d82464fe')[0]),
					'flag': helper.set_entry_command_string("Cloaking"),
					'description': Markup('An IRC hostmask cloak replaces your IP address or hostname with a cloak.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '9d49ff232cfd4c18ba2398e2061d03c8',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('f1f1597ae3874575a520427e499a36a6')[0]),
					'flag': helper.set_entry_command_string("Tails"),
					'description': Markup('An encrypted thumbdrive bootable OS with security features that runs TOR by default.'),
					'example': helper.example_path(),
					'ext_link': 'https://tails.boum.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cee0f98414d24d9e910a98bf1faef263')[0]),
					'flag': helper.set_entry_command_string("Qubes OS"),
					'description': Markup('Security focused operating system that relies on compartmentalization (security by isolation); effectively spinning up isolated instances of VMs for each application.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.qubes-os.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('11cf85e67cf642ea96194a3885b77708')[0]),
					'flag': helper.set_entry_command_string("Whonix"),
					'description': Markup('Another security-focused Linux distribution with some neat features like keystroke anonymization, kernel modules for overwriting TCP ISNs, hardening the OS and more.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.whonix.org/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('82678d37193a47d4884d5d86751b897b')[0]),
					'flag': helper.set_entry_command_string("Hardening"),
					'description': Markup('OS hardening is a process of reducing the attack surface by various means such as closing down ports, containerization/virtualization of applications, IPS/IDS, relevant kernel modules and much more.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '8b614fae554f42dda96adc611f12f325',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b11f24066bab4f30b573460a854e3bf4')[0]),
					'flag': helper.set_entry_command_string("Burner Email"),
					'description': Markup('Multiple services exists to create one-time email addresses. Beware these are not usable by other people aswell. You can setup forwarding to an intermediate email address which then forwards to your regular email address'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4493e00ec0804f818edadb419efa831b')[0]),
					'flag': helper.set_entry_command_string("Email spoofing"),
					'description': Markup('Creation of email messages with forged headers that results in a forged sender address'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': 'e2289827745a4fbb886628b8624ecf5e',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('91d41341975a44d78954b50114b3eb92')[0]),
					'flag': helper.set_entry_command_string("Cryptocurrency"),
					'description': Markup('All transactions on Bitcoin for example are stored on public ledgers and can thus be traced easily. Some cryptocurrencies have made attempts to curcumvent this feature (e.g. Monero)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1a91925d6f924ce9bf940e2dd398b40f')[0]),
					'flag': helper.set_entry_command_string("SS7 Hijacking"),
					'description': Markup('A vulnerability that allows hackers to read texts, listen to calls and track their locations. This vulerability have been used against populations and army-staff aswell as political targets'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d14d6ff1b932475a92c787b5a27f3c6c')[0]),
					'flag': helper.set_entry_command_string("Hot Wallet"),
					'description': Markup('A bitcoin wallet that is online and connected'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('acea6283c9224dfaad13cbc2b6f90dbf')[0]),
					'flag': helper.set_entry_command_string("Cold Wallet"),
					'description': Markup('An offline wallet that is stored on a hardware device'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b60ff5d846fb4ba5a33e7904c2cf24b7')[0]),
					'flag': helper.set_entry_command_string("Fingerprinting"),
					'description': Markup('A nasty set of techniques to identify, track and collect information on users without their consent.'),
					'example': helper.example_path(),
					'ext_link': 'https://en.wikipedia.org/wiki/Device_fingerprint',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('83aaedf31dc24528ba449aa225ec90ba')[0]),
					'flag': helper.set_entry_command_string("Cookies"),
					'description': Markup('A small piece of data stored on an end-users computer by a web browser. Used to remember stateful information and exploited by advertising companies to track and identify users.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('edfa733af60443d398e3e9eb05a80c56')[0]),
					'flag': helper.set_entry_command_string("Zombie Cookie"),
					'description': Markup('A cookie that is automatically recreated after being deleted. Accomplished by storing the cookies content in multiple locations client-side as well as server-side.'),
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
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/B0898YGR58/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0898YGR58&linkCode=as2&tag=cheatsheet0e-20&linkId=fda7ae4519db3248ed0ea8cb8191befc"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B0898YGR58&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B0898YGR58" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Written by an expert on the topic (Michael Bazzell)'),
			'description': '',
		},
		{
			'title': Markup('Smartphone/webcam Camera Blocker'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/B083QGCFY8/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B083QGCFY8&linkCode=as2&tag=cheatsheet0e-20&linkId=710987f88ebbd41efb5af11d71cc53df"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B083QGCFY8&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B083QGCFY8" border="0" alt="" height="150"  style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('Faraday Bag for Your Devices'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/B08K2Q9RCK/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B08K2Q9RCK&linkCode=as2&tag=cheatsheet0e-20&linkId=5faf2b63b312405df92bdccb9eaa85bf"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B08K2Q9RCK&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B08K2Q9RCK" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('Yubikey 5Ci'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/B07WGJ1DNJ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07WGJ1DNJ&linkCode=as2&tag=cheatsheet0e-20&linkId=aeb6e679106a0d92cacfb0e0a0700018"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07WGJ1DNJ&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B07WGJ1DNJ" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('The Art of Invisibility'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/0316380520/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0316380520&linkCode=as2&tag=cheatsheet0e-20&linkId=432e70cfe6a170c327a8c71d1a83cc12"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0316380520&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=0316380520" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Written by Kevin Mitnick'),
			'description': 'Details his years as FBIs most wanted hacker. An interesting read in regards of OpSec',
		},
		{
			'title': Markup('Ghost in The Wires'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/0316037729/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0316037729&linkCode=as2&tag=cheatsheet0e-20&linkId=9a0ca0214f0cda8d07959bbf514ef04b"><img  style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0316037729&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=0316037729"  height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Written by Kevin Mitnick'),
			'description': 'Details his adventures as one of the most prolific phreakers',
		},
		{
			'title': Markup('Phishing Dark Waters'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/1118958470/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1118958470&linkCode=as2&tag=cheatsheet0e-20&linkId=1a3e8f70eb43fee5d4c074f75c6699aa"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1118958470&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=1118958470" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Great and very interesting read about phishing'),
			'description': '',
		},
		{
			'title': Markup('Microphone blocker'),
			'affiliate_link': Markup(
				'<a target="_blank" alt="Amazon affiliate product"  href="https://www.amazon.com/gp/product/B07V9T14N3/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07V9T14N3&linkCode=as2&tag=cheatsheet0e-20&linkId=89cd6c2c44e83d12528d9070f778408d"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07V9T14N3&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B07V9T14N3" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Useful for important meetings'),
			'description': '',
		},
	)
]
licensing = [
	'',
]

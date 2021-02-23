import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('gnu_coreutils', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'gnu_coreutils'
information = {
	'tool': 'Linux CLI',
	'title': 'GNU/Linux CLI Cheatsheet',
	'subtitle': 'This site is a reference for GNU Core Utils',
	'description': 'What many would refer to as Linux CLI or maybe even Bash is a powerful toolset known as GNU core utility tools.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Linux CLI',
			[
				helper.characteristics.get('tool'),
				helper.characteristics.get('sys-admin'),
				helper.characteristics.get('dev-ops'),
			])
	],
	'topic_uris': [
		'tool',
		'sys-admin',
		'dev-ops',
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
affiliate_products = [{
	Markup(''),
	Markup(''),
	Markup(''),
}],
cheatsheet = [
	{
		'heading': helper.set_folder('Output of Entire Files'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd6d00400be834c4398204fa54c3efe6a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b681fbfb427f4dab9b6234a8ac00a435')[0]),
					'flag': helper.set_entry_command_string("cat"),
					'description': Markup('Concatenate and write files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('57b8ad3c41774a3c990f05544f9a838f')[0]),
					'flag': helper.set_entry_command_string("tac"),
					'description': Markup('Concatenate and write files in reverse.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tac-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('57b35efc7dbd42c6bcd8ae100a5fe7b9')[0]),
					'flag': helper.set_entry_command_string("nl"),
					'description': Markup('Number lines and write files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nl-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('23e58e0f7467462a9a4746ed18d46b0f')[0]),
					'flag': helper.set_entry_command_string("od"),
					'description': Markup('Write files in octal or other formats.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#od-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bc478cd613b74b018495abff381125e1')[0]),
					'flag': helper.set_entry_command_string("base32"),
					'description': Markup('Transform data into printable data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#base32-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d31b1b7e57e542878ded49b760c63311')[0]),
					'flag': helper.set_entry_command_string("base64"),
					'description': Markup('Transform data into printable data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#base64-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a0e1bb6ca30430998b298aa1c344ac5')[0]),
					'flag': helper.set_entry_command_string("basenc"),
					'description': Markup('Transform data into printable data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#basenc-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Formatting File Contents'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4e02331f4f3c4203bf36ed8ff280fc4f',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2e0a3f6434d04e9b8b67a03ef357cc73')[0]),
					'flag': helper.set_entry_command_string("fmt"),
					'description': Markup('Reformat paragraph text.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#fmt-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('49d3fa1a93f04474b606f2eff05795ec')[0]),
					'flag': helper.set_entry_command_string("pr"),
					'description': Markup('Paginate or columnate files for printing.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#pr-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b62608d0b5a84be78b6a33870556c669')[0]),
					'flag': helper.set_entry_command_string("fold"),
					'description': Markup('Wrap input lines to fit in specified width.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#fold-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Output of Parts of Files'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'b94076b0d91d471283f0fc24b42fe822',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c26c55296e80402f8d97fde456979e94')[0]),
					'flag': helper.set_entry_command_string("head"),
					'description': Markup('Output the first part of files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#head-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce3d9eacfd084e5ea9e6b82a273ee9eb')[0]),
					'flag': helper.set_entry_command_string("tail"),
					'description': Markup('Output the last part of files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tail-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7ef011d2f0e84a709983cfa54f515cf6')[0]),
					'flag': helper.set_entry_command_string("split"),
					'description': Markup('Split a file into pieces.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#split-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('73a6f76bfb5141e89d117db7fcd05e58')[0]),
					'flag': helper.set_entry_command_string("csplit"),
					'description': Markup('Split a file into context-determined pieces.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#csplit-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Summarizing Files'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '89498b82d02b4c1d8f31ee7ec6801a9d',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('367129eeb7f6485b91b93bac725bc40c')[0]),
					'flag': helper.set_entry_command_string("wc"),
					'description': Markup('Print newline, word, and byte counts.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#wc-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce8e1e716cdf4ec98481567ac03839b5')[0]),
					'flag': helper.set_entry_command_string("sum"),
					'description': Markup('Print checksum and block counts.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0e12a0e5016047c7a06a9f1e4ca03543')[0]),
					'flag': helper.set_entry_command_string("cksum"),
					'description': Markup('Print CRC checksum and byte counts.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cksum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8c0cab23ef4e4a2e895e1c82272ade19')[0]),
					'flag': helper.set_entry_command_string("b2sum"),
					'description': Markup('Print or check BLAKE2 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#b2sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7af5c10c184a48dea84a7eec1d683db8')[0]),
					'flag': helper.set_entry_command_string("md5sum"),
					'description': Markup('Print or check MD5 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#md5sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b96d5afedcdf4bab9ec6758b7a270433')[0]),
					'flag': helper.set_entry_command_string("sha1sum"),
					'description': Markup('Print or check SHA-1 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sha1sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('113cb831a3c243fe99006e2db724631d')[0]),
					'flag': helper.set_entry_command_string("sha224sum sha256sum sha384sum sha512sum"),
					'description': Markup('Print or check SHA-2 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Operating on Sorted Files'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'b38d6c80a2e5460e87591412b84233b2',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6a34a379b01c4b76bb57e61833816334')[0]),
					'flag': helper.set_entry_command_string("sort"),
					'description': Markup('Sort text files.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('594feb928d8b4af483a085028eeddcc5')[0]),
					'flag': helper.set_entry_command_string("shuf"),
					'description': Markup('Shuffle text files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#shuf-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2f3a8fe5e3464342917b45332250230c')[0]),
					'flag': helper.set_entry_command_string("uniq"),
					'description': Markup('Uniquify files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#uniq-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4ced7ddaa81a4a339f83abc1144a4d10')[0]),
					'flag': helper.set_entry_command_string("comm"),
					'description': Markup('Compare two sorted files line by line.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#comm-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b161a04ca8014aacb512706721936a60')[0]),
					'flag': helper.set_entry_command_string("ptx"),
					'description': Markup('Produce a permuted index of file contents.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#ptx-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b5fbd6360db34f6fa1b14456a7d706c9')[0]),
					'flag': helper.set_entry_command_string("tsort"),
					'description': Markup('Topological sort'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tsort-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Operating on Fields'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'a58051ef4bf3419ca3b93e9261f8ef5a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('cf168ca4e6ba4414a4a02fa8ec8eb765')[0]),
					'flag': helper.set_entry_command_string("cut"),
					'description': Markup('Print selected parts of lines.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cut-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7b0e4120572a4f3a9c6573a35abdd3ea')[0]),
					'flag': helper.set_entry_command_string("paste"),
					'description': Markup('Merge lines of files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#paste-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1eb6f4e19fda4893b480bf5123aa3374')[0]),
					'flag': helper.set_entry_command_string("join"),
					'description': Markup('Join lines on a common field.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#join-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Operating on Characters'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '25a4f9b2816945f2b0bb9539338520b6',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e4c6be8c4a464f739adc0a3bdefe04d0')[0]),
					'flag': helper.set_entry_command_string("tr"),
					'description': Markup('Translate, squeeze, and/or delete characters.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tr-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3ebd32e6f3fc4193ae693e943a572a58')[0]),
					'flag': helper.set_entry_command_string("expand"),
					'description': Markup('Convert tabs to spaces.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#expand-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6593ecd8d9f24c16a61b6e277ac47fb8')[0]),
					'flag': helper.set_entry_command_string("unexpand"),
					'description': Markup('Convert spaces to tabs.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#unexpand-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Directory Listing'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f69c6c10eeb040bba6d1100f61e04bcc',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e909abf55b00487a8bdd2988616c50ae')[0]),
					'flag': helper.set_entry_command_string("ls"),
					'description': Markup('List directory contents.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#ls-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5cea5889c12244e2b93f9b98043b0910')[0]),
					'flag': helper.set_entry_command_string("dir"),
					'description': Markup('Briefly ls.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c9cf223f64c94f5dba00b2c7bfc65095')[0]),
					'flag': helper.set_entry_command_string("vdir"),
					'description': Markup('Verbosely ls.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#vdir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b8d999163ca646379a0087d6a7a91229')[0]),
					'flag': helper.set_entry_command_string("dircolors"),
					'description': Markup('Color setup for ls, etc.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dircolors-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Basic File Operations'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '81f09ea8883c4315bef9b4e2ac2a9f0c',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('262a45b327484fa1ad9352538ad995c3')[0]),
					'flag': helper.set_entry_command_string("cp"),
					'description': Markup('Copy files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cp-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e1182d196d81463fb153c0bf438f6e02')[0]),
					'flag': helper.set_entry_command_string("dd"),
					'description': Markup('Convert and copy a file.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dd-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3c6736edaf834bc2ab7414e5c3062d31')[0]),
					'flag': helper.set_entry_command_string("install"),
					'description': Markup('Copy files and set attributes.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#install-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8af70a54f8404039b7ad6fc33095f2e8')[0]),
					'flag': helper.set_entry_command_string("mv"),
					'description': Markup('Move (rename) files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mv-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e59d2aa173a54c3cb8fa326a1280809c')[0]),
					'flag': helper.set_entry_command_string("rm"),
					'description': Markup('Remove files or directories.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#rm-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('afe0a80fa3514317a59c02bf24889666')[0]),
					'flag': helper.set_entry_command_string("shred"),
					'description': Markup('Remove files more securely.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#shred-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Special Filetypes'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '272035d14e2a4f62878743c558405d30',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2f96c8bea2a544ebaa244569441442cd')[0]),
					'flag': helper.set_entry_command_string("link"),
					'description': Markup('Make a hard link via the link syscall'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#link-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('57c509ad0c4e4084be0271b98f9d7ce3')[0]),
					'flag': helper.set_entry_command_string("ln"),
					'description': Markup('Make links between files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#ln-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9ebeb8a0d7cb4b9790c8106f0098a86e')[0]),
					'flag': helper.set_entry_command_string("mkdir"),
					'description': Markup('Make directories.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mkdir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ad496745d8614f32a272a42d1cc81dce')[0]),
					'flag': helper.set_entry_command_string("mkfifo"),
					'description': Markup('Make FIFOs (named pipes).'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mkfifo-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e14f1f8643f645a898e1003a98c32fd6')[0]),
					'flag': helper.set_entry_command_string("mknod"),
					'description': Markup('Make block or character special files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mknod-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dd1e7d98afdf4b988e20ec0f6c3dae29')[0]),
					'flag': helper.set_entry_command_string("readlink"),
					'description': Markup('Print value of a symlink or canonical file name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#readlink-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b7b7561f2bf7463fae3328d91e33c879')[0]),
					'flag': helper.set_entry_command_string("rmdir"),
					'description': Markup('Remove empty directories.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#rmdir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d4947a24c1314c52ac99b20bc3bbe6d4')[0]),
					'flag': helper.set_entry_command_string("unlink"),
					'description': Markup('Remove files via the unlink syscall'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#unlink-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Changing File Attributes'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5809667b3e534456adbbdae29fc36565',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('3c57650e770047438d4d7c580442ea55')[0]),
					'flag': helper.set_entry_command_string("chown"),
					'description': Markup('Change file owners and groups.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chown-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('72f6cc5f23d848d5a5b5304d4bfab628')[0]),
					'flag': helper.set_entry_command_string("chgrp"),
					'description': Markup('Change file groups.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chgrp-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1466a4fa2b664150bf48c9d18efab715')[0]),
					'flag': helper.set_entry_command_string("chmod"),
					'description': Markup('Change access permissions.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chmod-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4a302dee334a4e10aeb6473a14c62e34')[0]),
					'flag': helper.set_entry_command_string("touch"),
					'description': Markup('Change file timestamps.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#touch-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Disk Usage'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '206e9c2374d64b848b0b2f7cfbdf602f',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('4aa0475677754e6ebc80ca7ec990aa33')[0]),
					'flag': helper.set_entry_command_string("df"),
					'description': Markup('Report file system disk space usage.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#df-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2466b876cf0f44e3848af9824be74417')[0]),
					'flag': helper.set_entry_command_string("du"),
					'description': Markup('Estimate file space usage.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#du-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('28611a051baa43d2926e5f5a2f292144')[0]),
					'flag': helper.set_entry_command_string("stat"),
					'description': Markup('Report file or file system status.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#stat-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d6aee50c1eba4685a318bb6fc07cb467')[0]),
					'flag': helper.set_entry_command_string("sync"),
					'description': Markup('Synchronize cached writes to persistent storage.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sync-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3ea752f1b4954450b26c154e4fda9cce')[0]),
					'flag': helper.set_entry_command_string("truncate"),
					'description': Markup('Shrink or extend the size of a file.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#truncate-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Printing text'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'cccb2a3e564a4df49f53ecfc09c96b33',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('47c28c8a14534773aa22a85e2a92334b')[0]),
					'flag': helper.set_entry_command_string("echo"),
					'description': Markup('Print a line of text.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#echo-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('01c2caf63bc84225aead1e2d36db1c1a')[0]),
					'flag': helper.set_entry_command_string("printf"),
					'description': Markup('Format and print data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#printf-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce6b46176d55435789fff8dad67c3dda')[0]),
					'flag': helper.set_entry_command_string("yes"),
					'description': Markup('Print a string until interrupted.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#yes-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Conditions'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6cef0c4cba7c484d996e052fb8dacb7b',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('3367afec94c94d5c8812e426dba446c4')[0]),
					'flag': helper.set_entry_command_string("false"),
					'description': Markup('Do nothing, unsuccessfully.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#false-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('62d454587ae6457792086f8d8d051566')[0]),
					'flag': helper.set_entry_command_string("true"),
					'description': Markup('Do nothing, successfully.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#true-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('871634619ea74d2b88761d3dcbc82139')[0]),
					'flag': helper.set_entry_command_string("test"),
					'description': Markup('Check file types and compare values.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#test-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('59d0eb7fb8234e0b9998f523560e4231')[0]),
					'flag': helper.set_entry_command_string("expr"),
					'description': Markup('Evaluate expressions.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#expr-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Redirection'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '180dcc83887b427388a7334f07a6ad38',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('810c41d4cb0249f995c21d89e70b597c')[0]),
					'flag': helper.set_entry_command_string("tee"),
					'description': Markup('Redirect output to multiple files or processes.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tee-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Filename Manipulation'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'ccda998446784232b9a813ef290e80ac',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0e21d940c5b14697958842dff67750af')[0]),
					'flag': helper.set_entry_command_string("basename"),
					'description': Markup('Strip directory and suffix from a file name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#basename-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d7cf0c3399324ec2a270bdd1bcd37961')[0]),
					'flag': helper.set_entry_command_string("dirname"),
					'description': Markup('Strip last file name component.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dirname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('23f588981b29403c85881a47b09fe6fa')[0]),
					'flag': helper.set_entry_command_string("pathchk"),
					'description': Markup('Check file name validity and portability.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#pathchk-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('123dae0d4c754c5f8e45e7b71db0f278')[0]),
					'flag': helper.set_entry_command_string("mktemp"),
					'description': Markup('Create temporary file or directory.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mktemp-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('31c345f3c2454f60b067830b23de5401')[0]),
					'flag': helper.set_entry_command_string("realpath"),
					'description': Markup('Print resolved file names.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#realpath-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Working Context'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4183f63d8b0a4197b9dc9b5da7af6373',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('23eaa034e8924937bf85dd78840cda12')[0]),
					'flag': helper.set_entry_command_string("pwd"),
					'description': Markup('Print working directory.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#pwd-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('16329b7baafa4ea2bf35ff87cf996b10')[0]),
					'flag': helper.set_entry_command_string("stty"),
					'description': Markup('Print or change terminal characteristics.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#stty-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a1bd5edb75714d758ecfd4ac8f275430')[0]),
					'flag': helper.set_entry_command_string("printenv"),
					'description': Markup('Print environment variables.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#printenv-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('46666dcbfb1846bcbb94e98532c75bb3')[0]),
					'flag': helper.set_entry_command_string("tty"),
					'description': Markup('Print file name of terminal on standard input.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tty-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('User Information'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5cd6ead969ae4c9580de6e40dbeacd36',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('80efa470c6e0416d8b28bfbeaad3de42')[0]),
					'flag': helper.set_entry_command_string("id"),
					'description': Markup('Print user identity.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#id-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e0224947fe1b4688a27d758adbc67277')[0]),
					'flag': helper.set_entry_command_string("logname"),
					'description': Markup('Print current login name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#logname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9c52a7a6af1341db9c9d3affe9fc10e8')[0]),
					'flag': helper.set_entry_command_string("whoami"),
					'description': Markup('Print effective user ID'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#whoami-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b89242b237b74e5398ded81ac201ce51')[0]),
					'flag': helper.set_entry_command_string("groups"),
					'description': Markup('Print group names a user is in'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#groups-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fb8ff69ecf4e4178b1de447e5cd80df5')[0]),
					'flag': helper.set_entry_command_string("users"),
					'description': Markup('Print login names of users currently logged in.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#users-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6824b7798bcc41309b639729e1ba00a1')[0]),
					'flag': helper.set_entry_command_string("who"),
					'description': Markup('Print who is currently logged in'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#who-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('System Context'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'db0a9fc261594d6e858000601adeea52',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('cbc67406a59b48a9b46c384853c1db87')[0]),
					'flag': helper.set_entry_command_string("date"),
					'description': Markup('Print or set system date and time.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#date-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('416f89707f0d42c79a757e9bd6085700')[0]),
					'flag': helper.set_entry_command_string("arch"),
					'description': Markup('Print machine hardware name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#arch-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8542b0bf61be4136b7b7ca2fc85db717')[0]),
					'flag': helper.set_entry_command_string("nproc"),
					'description': Markup('Print the number of processors.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nproc-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('56d98482114142d68f04badf0fd10ced')[0]),
					'flag': helper.set_entry_command_string("uname"),
					'description': Markup('Print system information.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#uname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9c72f13fca9a40df8910e47d96d323e3')[0]),
					'flag': helper.set_entry_command_string("hostname"),
					'description': Markup('Print or set system name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#hostname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('507e2c4fa7ec41dca50881bffe32f1e2')[0]),
					'flag': helper.set_entry_command_string("hostid"),
					'description': Markup('Print numeric host identifier.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#hostid-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('91d8ac4f2d2b45d58e037b7c3f5363a7')[0]),
					'flag': helper.set_entry_command_string("uptime"),
					'description': Markup('Print system uptime and load.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#uptime-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('SELinux Context'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '1a2b4019224e4bb1bfd0fffd2c9e32a7',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b3b5f756f70149b1868421795f1db0c9')[0]),
					'flag': helper.set_entry_command_string("chcon"),
					'description': Markup('Change SELinux context of file'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chcon-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('56a0bb7544084f479a634c5e05fd82fa')[0]),
					'flag': helper.set_entry_command_string("runcon"),
					'description': Markup('Run a command in specified SELinux context'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#runcon-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Modified Command Invocation'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '060cf22b583a4d7aa5245484c7fd87c6',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b0209e1678494f638dc65aacaef44470')[0]),
					'flag': helper.set_entry_command_string("chroot"),
					'description': Markup('Modify the root directory'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chroot-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0a1e26fd58744bcf9acd643bf1af1cdb')[0]),
					'flag': helper.set_entry_command_string("env"),
					'description': Markup('Modify environment variables.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#env-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('17e19d1beb79420db0879d324fe7ddc4')[0]),
					'flag': helper.set_entry_command_string("nice"),
					'description': Markup('Modify niceness.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nice-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f786957e2eb14e2885f05af0b499dbeb')[0]),
					'flag': helper.set_entry_command_string("nohup"),
					'description': Markup('Immunize to hangups.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nohup-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('78b5d7f8150e4735b4f3a7e21ef01183')[0]),
					'flag': helper.set_entry_command_string("stdbuf"),
					'description': Markup('Modify buffering of standard streams.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#stdbuf-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7523577df0e74f24b15c5ecf5242d8ad')[0]),
					'flag': helper.set_entry_command_string("timeout"),
					'description': Markup('Run with time limit'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#timeout-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Process Control'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4e3fb69da9a74f7fb318fefc1c123169',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6c91da60b41c4322b192af4fcecf0027')[0]),
					'flag': helper.set_entry_command_string("kill"),
					'description': Markup('Sending a signal to processes.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#kill-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Delaying'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '2eddb02523ac47e28c1a7f4df3ce70ee',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('1b0f02d0a11a4c68b7284152bc9ff3b0')[0]),
					'flag': helper.set_entry_command_string("sleep"),
					'description': Markup('Delay for a specified time.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sleep-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Numeric Operations'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4456b84cdba54adda53ffea1ff94fc6e',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('39878afc008344f1ba495814c66b55ad')[0]),
					'flag': helper.set_entry_command_string("factor"),
					'description': Markup('Show factors of numbers.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#factor-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7bc75cacce6a476e9c76977ee1debad3')[0]),
					'flag': helper.set_entry_command_string("numfmt"),
					'description': Markup('Reformat numbers'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#numfmt-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e57f74f133d84509b5311ed4ab0eb64b')[0]),
					'flag': helper.set_entry_command_string("seq"),
					'description': Markup('Print sequences of numbers'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#seq-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
]
resources = [
]
affiliate_products = [],
# style="max-height:150px; max-width: 150px;
licensing = [
	Markup('')
]

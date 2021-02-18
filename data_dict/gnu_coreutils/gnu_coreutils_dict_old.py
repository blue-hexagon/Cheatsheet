import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('gnu_coreutils', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'gnu_coreutils'
information = {
	'tool': 'Linux CLI',
	'title': 'GNU/Linux CLI Cheatsheet',
	'subtitle': 'This site is a reference for GNU Core Utils',
	'description': 'What many would refer to as Linux CLI or maybe even Bash is a powerful toolset known as GNU core utility tools.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("cat")[0]),
					'description': Markup('Concatenate and write files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("tac")[0]),
					'description': Markup('Concatenate and write files in reverse.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tac-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("nl")[0]),
					'description': Markup('Number lines and write files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nl-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("od")[0]),
					'description': Markup('Write files in octal or other formats.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#od-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("base32")[0]),
					'description': Markup('Transform data into printable data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#base32-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("base64")[0]),
					'description': Markup('Transform data into printable data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#base64-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("basenc")[0]),
					'description': Markup('Transform data into printable data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#basenc-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("fmt")[0]),
					'description': Markup('Reformat paragraph text.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#fmt-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("pr")[0]),
					'description': Markup('Paginate or columnate files for printing.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#pr-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("fold")[0]),
					'description': Markup('Wrap input lines to fit in specified width.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#fold-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("head")[0]),
					'description': Markup('Output the first part of files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#head-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("tail")[0]),
					'description': Markup('Output the last part of files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tail-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("split")[0]),
					'description': Markup('Split a file into pieces.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#split-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("csplit")[0]),
					'description': Markup('Split a file into context-determined pieces.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#csplit-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("wc")[0]),
					'description': Markup('Print newline, word, and byte counts.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#wc-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("sum")[0]),
					'description': Markup('Print checksum and block counts.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("cksum")[0]),
					'description': Markup('Print CRC checksum and byte counts.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cksum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("b2sum")[0]),
					'description': Markup('Print or check BLAKE2 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#b2sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("md5sum")[0]),
					'description': Markup('Print or check MD5 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#md5sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("sha1sum")[0]),
					'description': Markup('Print or check SHA-1 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sha1sum-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("sha224sum sha256sum sha384sum sha512sum")[0]),
					'description': Markup('Print or check SHA-2 digests.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("sort")[0]),
					'description': Markup('Sort text files.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("shuf")[0]),
					'description': Markup('Shuffle text files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#shuf-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("uniq")[0]),
					'description': Markup('Uniquify files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#uniq-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("comm")[0]),
					'description': Markup('Compare two sorted files line by line.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#comm-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("ptx")[0]),
					'description': Markup('Produce a permuted index of file contents.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#ptx-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("tsort")[0]),
					'description': Markup('Topological sort'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tsort-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("cut")[0]),
					'description': Markup('Print selected parts of lines.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cut-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("paste")[0]),
					'description': Markup('Merge lines of files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#paste-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("join")[0]),
					'description': Markup('Join lines on a common field.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#join-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("tr")[0]),
					'description': Markup('Translate, squeeze, and/or delete characters.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tr-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("expand")[0]),
					'description': Markup('Convert tabs to spaces.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#expand-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("unexpand")[0]),
					'description': Markup('Convert spaces to tabs.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#unexpand-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("ls")[0]),
					'description': Markup('List directory contents.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#ls-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("dir")[0]),
					'description': Markup('Briefly ls.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("vdir")[0]),
					'description': Markup('Verbosely ls.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#vdir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("dircolors")[0]),
					'description': Markup('Color setup for ls, etc.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dircolors-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("cp")[0]),
					'description': Markup('Copy files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#cp-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("dd")[0]),
					'description': Markup('Convert and copy a file.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dd-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("install")[0]),
					'description': Markup('Copy files and set attributes.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#install-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("mv")[0]),
					'description': Markup('Move (rename) files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mv-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("rm")[0]),
					'description': Markup('Remove files or directories.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#rm-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("shred")[0]),
					'description': Markup('Remove files more securely.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#shred-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("link")[0]),
					'description': Markup('Make a hard link via the link syscall'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#link-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("ln")[0]),
					'description': Markup('Make links between files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#ln-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("mkdir")[0]),
					'description': Markup('Make directories.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mkdir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("mkfifo")[0]),
					'description': Markup('Make FIFOs (named pipes).'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mkfifo-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("mknod")[0]),
					'description': Markup('Make block or character special files.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mknod-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("readlink")[0]),
					'description': Markup('Print value of a symlink or canonical file name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#readlink-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("rmdir")[0]),
					'description': Markup('Remove empty directories.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#rmdir-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("unlink")[0]),
					'description': Markup('Remove files via the unlink syscall'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#unlink-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("chown")[0]),
					'description': Markup('Change file owners and groups.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chown-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("chgrp")[0]),
					'description': Markup('Change file groups.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chgrp-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("chmod")[0]),
					'description': Markup('Change access permissions.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chmod-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("touch")[0]),
					'description': Markup('Change file timestamps.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#touch-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("df")[0]),
					'description': Markup('Report file system disk space usage.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#df-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("du")[0]),
					'description': Markup('Estimate file space usage.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#du-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("stat")[0]),
					'description': Markup('Report file or file system status.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#stat-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("sync")[0]),
					'description': Markup('Synchronize cached writes to persistent storage.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sync-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("truncate")[0]),
					'description': Markup('Shrink or extend the size of a file.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#truncate-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("echo")[0]),
					'description': Markup('Print a line of text.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#echo-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("printf")[0]),
					'description': Markup('Format and print data.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#printf-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("yes")[0]),
					'description': Markup('Print a string until interrupted.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#yes-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("false")[0]),
					'description': Markup('Do nothing, unsuccessfully.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#false-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("true")[0]),
					'description': Markup('Do nothing, successfully.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#true-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("test")[0]),
					'description': Markup('Check file types and compare values.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#test-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("expr")[0]),
					'description': Markup('Evaluate expressions.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#expr-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("tee")[0]),
					'description': Markup('Redirect output to multiple files or processes.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tee-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("basename")[0]),
					'description': Markup('Strip directory and suffix from a file name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#basename-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("dirname")[0]),
					'description': Markup('Strip last file name component.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#dirname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("pathchk")[0]),
					'description': Markup('Check file name validity and portability.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#pathchk-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("mktemp")[0]),
					'description': Markup('Create temporary file or directory.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#mktemp-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("realpath")[0]),
					'description': Markup('Print resolved file names.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#realpath-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("pwd")[0]),
					'description': Markup('Print working directory.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#pwd-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("stty")[0]),
					'description': Markup('Print or change terminal characteristics.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#stty-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("printenv")[0]),
					'description': Markup('Print environment variables.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#printenv-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("tty")[0]),
					'description': Markup('Print file name of terminal on standard input.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#tty-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("id")[0]),
					'description': Markup('Print user identity.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#id-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("logname")[0]),
					'description': Markup('Print current login name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#logname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("whoami")[0]),
					'description': Markup('Print effective user ID'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#whoami-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("groups")[0]),
					'description': Markup('Print group names a user is in'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#groups-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("users")[0]),
					'description': Markup('Print login names of users currently logged in.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#users-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("who")[0]),
					'description': Markup('Print who is currently logged in'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#who-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("date")[0]),
					'description': Markup('Print or set system date and time.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#date-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("arch")[0]),
					'description': Markup('Print machine hardware name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#arch-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("nproc")[0]),
					'description': Markup('Print the number of processors.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nproc-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("uname")[0]),
					'description': Markup('Print system information.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#uname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("hostname")[0]),
					'description': Markup('Print or set system name.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#hostname-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("hostid")[0]),
					'description': Markup('Print numeric host identifier.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#hostid-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("uptime")[0]),
					'description': Markup('Print system uptime and load.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#uptime-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("chcon")[0]),
					'description': Markup('Change SELinux context of file'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chcon-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("runcon")[0]),
					'description': Markup('Run a command in specified SELinux context'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#runcon-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("chroot")[0]),
					'description': Markup('Modify the root directory'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#chroot-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("env")[0]),
					'description': Markup('Modify environment variables.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#env-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("nice")[0]),
					'description': Markup('Modify niceness.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nice-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("nohup")[0]),
					'description': Markup('Immunize to hangups.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#nohup-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("stdbuf")[0]),
					'description': Markup('Modify buffering of standard streams.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#stdbuf-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("timeout")[0]),
					'description': Markup('Run with time limit'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#timeout-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("kill")[0]),
					'description': Markup('Sending a signal to processes.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#kill-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("sleep")[0]),
					'description': Markup('Delay for a specified time.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#sleep-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("factor")[0]),
					'description': Markup('Show factors of numbers.'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#factor-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("numfmt")[0]),
					'description': Markup('Reformat numbers'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#numfmt-invocation',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("seq")[0]),
					'description': Markup('Print sequences of numbers'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/coreutils/manual/coreutils.html#seq-invocation',
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
# style="max-height:150px; max-width: 150px;
licensing = [
	Markup('')
]

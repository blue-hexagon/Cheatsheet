import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('bash', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'bash'

information = {
	'tool': 'Bash',
	'title': 'Bash Cheatsheet',
	'subtitle': 'This site is a reference for the scripting language Bash',
	'description': 'Bash (Bourne Again Shell) is a shell language build on-top of the orignal Bourne Shell which was distributed with V7 Unix in 1979 and became the standard for writing shell scripts. Today it is primary to most Linux distributions, MacOS and it has even recently been enabled to run on Windows through something called WSL (Windows Subsystem for Linux).',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '✔',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Bash',
			[
				helper.characteristics.get('domain-specific-language'),
				helper.characteristics.get('scripting-language'),
				helper.characteristics.get('command-language'),
				helper.characteristics.get('imperative-programming'),
				helper.characteristics.get('dev-ops'),
				helper.characteristics.get('sys-admin'),
			]),
	],
	'topic_uris': [
		'domain-specific-language',
		'scripting-language',
		'command-language',
		'imperative-programming',
		'dev-ops',
		'sys-admin',
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
		'': '',
	},
]

cheatsheet = [
	{
		'heading': helper.set_folder('File Test Operators'),
		'subtitle': 'Used for testing of files files in shellscripts',
		'description': 'Testing files in scripts is easy and straight forward. This is where shell scripting starts to show its glory! In Bash you can do file testing for permissions, size, date, filetype or existence.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('-e')[0]),
					'description': Markup('File exists'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-a')[0]),
					'description': Markup('File exists (identical to -e but is deprecated and outdated)'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-f')[0]),
					'description': Markup('File is a regular file (not a directory or device file)'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup('https://www.youtube.com/embed/m8Cz5NhO-mE'),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-s')[0]),
					'description': Markup('File is not zero size'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''

				},
				{
					'flag': Markup(helper.set_entry_folder('-d')[0]),
					'description': Markup('File is a directory'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''

				},
				{
					'flag': Markup(helper.set_entry_folder('-b')[0]),
					'description': Markup('File is a block device'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-c')[0]),
					'description': Markup('File is a character device'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-p')[0]),
					'description': Markup('File is a pipe'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-h')[0]),
					'description': Markup('File is a symbolic link'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-L')[0]),
					'description': Markup('File is a symbolic link'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-S')[0]),
					'description': Markup('File is a socket'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-t')[0]),
					'description': Markup('File (descriptor) is associated with a terminal device'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-r')[0]),
					'description': Markup('File has read permission (for the user running the test)'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-w')[0]),
					'description': Markup('File has write permission (for the user running the test)'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-x')[0]),
					'description': Markup('File has execute permission (for the user running the test)'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-g')[0]),
					'description': Markup('Set-group-id (sgid) flag set on file or directory'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-u')[0]),
					'description': Markup('Set-user-id (suid) flag set on file'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-k')[0]),
					'description': Markup('Sticky bit set'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-O')[0]),
					'description': Markup('You are owner of file'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-G')[0]),
					'description': Markup('Group-id of file same as yours'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-N')[0]),
					'description': Markup('File modified since it was last read'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('f1&nbsp;-nt&nbsp;f2')[0]),
					'description': Markup('File f1 is newer than f2'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('f1&nbsp;-ot&nbsp;f2')[0]),
					'description': Markup('File f1 is older than f2'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('f1&nbsp;-ef&nbsp;f2')[0]),
					'description': Markup('Files f1 and f2 are hard links to the same file'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!')[0]),
					'description': Markup('Not operator, will reverse the any test and return true if a condition is absent'),
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}
			]
		}
	},
	{
		'heading': helper.set_folder('String Comparison'),
		'subtitle': 'Used for string comparison in Bash',
		'description': 'This section describes how to compare strings in Bash.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('=')[0]),
					'description': Markup('Is equal to'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''

				},
				{
					'flag': Markup(helper.set_entry_folder('==')[0]),
					'description': Markup('Same as above, except the use of double equal symbols'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!=')[0]),
					'description': Markup('Is not equal to'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('<')[0]),
					'description': Markup('Is less than ASCII alphabetical order'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('>')[0]),
					'description': Markup('Is greater than ASCII alphabetical order'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-z')[0]),
					'description': Markup('String is null (i.e. zero length)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-n')[0]),
					'description': Markup('String is not null (i.e. !zero length)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}
			]
		}
	},
	{
		'heading': helper.set_folder('Integer Comparison'),
		'subtitle': 'Used for comparing numbers',
		'description': 'How to compare integers or arithmetic expressions in shell scripts.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('-eq')[0]),
					'description': Markup('Is equal to'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-ne')[0]),
					'description': Markup('Is not equal to'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-gt')[0]),
					'description': Markup('Is greater than'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-ge')[0]),
					'description': Markup('Is greater than or equal to'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-lt')[0]),
					'description': Markup('Is less than'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-le')[0]),
					'description': Markup('Is less than or equal to'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('<')[0]),
					'description': Markup('Is less than – place within double parentheses'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('<=')[0]),
					'description': Markup('Is less than or equal to (same rule as previous row)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('>')[0]),
					'description': Markup('Is greater than (same rule as previous row)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('>=')[0]),
					'description': Markup('Is greater than or equal to (same rule as previous row)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}
			]
		}
	},
	{
		'heading': helper.set_folder('Compound Operators'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'info': {
			Markup('Useful for boolean expressions and is similar to <kbd>&&</kbd> and <kbd>||</kbd>'),
			Markup('The compound operators work with the <kbd>test</kbd> command or may occur within single brackets <kbd>[ &lt;expr&gt; ]</kbd>'),
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('-a')[0]),
					'description': Markup('Logical and'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-o')[0]),
					'description': Markup('Logical or'),
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
		'heading': helper.set_folder('List Constructs'),
		'subtitle': '',
		'description': 'Provides a means of processing commands consecutively and in effect is able to replace complex if/then/case structures.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Construct',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('&&')[0]),
					'description': Markup('And construct'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('||')[0]),
					'description': Markup('Or construct'),
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
		'heading': helper.set_folder('Job Identifiers'),
		'subtitle': '',
		'description': 'Job control allows you to selectively stop (suspend) the execution of processes and continue their execution at a later point in time.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Notation',
				'Description'
			],
			'data': [
				{
					'notation': Markup('%N'),
					'description': Markup('Job number [N]'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'notation': Markup('%S'),
					'description': Markup('Invocation (command-line) of job begins with string S'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'notation': Markup('%?S'),
					'description': Markup('Invocation (command-line) of job contains within it string S'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'notation': Markup('%%'),
					'description': Markup('"current" job (last job stopped in foreground or started in background)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'notation': Markup('%+'),
					'description': Markup('"current" job (last job stopped in foreground or started in background)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'notation': Markup('%-'),
					'description': Markup('Last job'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'notation': Markup('%!'),
					'description': Markup('Last background process'),
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
		'heading': helper.set_folder('Signals'),
		'subtitle': 'System V Signals',
		'description': 'UNIX System V Signals.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Name',
				'Number',
				'Action',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('SIGHUP')[0]),
					'number': Markup('1'),
					'action': Markup('Exit'),
					'description': Markup('Hangs up'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGINT')[0]),
					'number': Markup('2'),
					'action': Markup('Exit'),
					'description': Markup('Interrupts'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGQUIT')[0]),
					'number': Markup('3'),
					'action': Markup('core dump'),
					'description': Markup('Quits'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGILL')[0]),
					'number': Markup('4'),
					'action': Markup('core dump'),
					'description': Markup('Illegal instruction'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGTRAP')[0]),
					'number': Markup('5'),
					'action': Markup('core dump'),
					'description': Markup('Trace trap'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGIOT')[0]),
					'number': Markup('6'),
					'action': Markup('core dump'),
					'description': Markup('IOT instruction'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGEMT')[0]),
					'number': Markup('7'),
					'action': Markup('core dump'),
					'description': Markup('MT instruction'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGFPE')[0]),
					'number': Markup('8'),
					'action': Markup('core dump'),
					'description': Markup('Floating point exception'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGKILL')[0]),
					'number': Markup('9'),
					'action': Markup('exit'),
					'description': Markup('Kills (cannot be caught or ignored)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGBUS')[0]),
					'number': Markup('10'),
					'action': Markup('core dump'),
					'description': Markup('Bus error'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGSEGV')[0]),
					'number': Markup('11'),
					'action': Markup('core dump'),
					'description': Markup('Segmentation violation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGSYS')[0]),
					'number': Markup('12'),
					'action': Markup('core dump'),
					'description': Markup('Bad argument to system call'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGPIPE')[0]),
					'number': Markup('13'),
					'action': Markup('exit'),
					'description': Markup('Writes on a pipe with no one to read it'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGALRM')[0]),
					'number': Markup('14'),
					'action': Markup('exit'),
					'description': Markup('Alarm clock'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('SIGTERM')[0]),
					'number': Markup('15'),
					'action': Markup('exit'),
					'description': Markup('Software termination signal'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				}
			]
		}
	},
	{
		'heading': helper.set_folder('Reserved Exit Codes'),
		'subtitle': '',
		'description': 'Useful for debugging a script. Exit takes integer args in the range 0-255. ',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Exit Code No.',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('1')[0]),
					'description': Markup('Catchall for general errors'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('2')[0]),
					'description': Markup('Misuse of shell builtins'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('126')[0]),
					'description': Markup('Command invoked cannot execute'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('127')[0]),
					'description': Markup('Command not found'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('128')[0]),
					'description': Markup('Invalid argument to exit'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('128+n')[0]),
					'description': Markup('Fatal error signal "n"'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('130')[0]),
					'description': Markup('Script terminated by Control-C'),
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
		'heading': helper.set_folder('Sending Control Signals'),
		'subtitle': '',
		'description': 'You can use these key-combinations to send signals or control the output. Check your stty settings. Suspend and resume of output is usually disabled if you are using "modern" terminal emulations. The standard xterm supports Ctrl+S and Ctrl+Q by default.',
		'warning': {
			'Check your stty settings. Suspend and resume of output is usually disabled if you are using "modern" terminal emulations. The standard xterm supports Ctrl+S and Ctrl+Q by default.'
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Key Combo',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+C')[0]),
					'description': Markup('The interrupt signal, sends SIGINT to the job running in the foreground'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+Y')[0]),
					'description': Markup(
						'The delayed suspend character. Causes a running process to be stopped when it attempts to read input from the terminal. Control is returned to the shell, the user can foreground, background or kill the process. Delayed suspend is only available on operating systems supporting this feature.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl+Z')[0]),
					'description': Markup('The suspend signal, sends a SIGTSTP to a running program, thus stopping it and returning control to the shell.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + s')[0]),
					'description': Markup('Stops the output to the screen (for long running verbose command)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + q')[0]),
					'description': Markup('Allow output to the screen (if previously stopped using command above)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + l')[0]),
					'description': Markup('Clear the screen'),
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
		'heading': helper.set_folder('Command Editing'),
		'subtitle': 'Keyboard Shortcuts',
		'description': 'Shortcuts to use in the CLI for swiftly editing a command. These shortcuts are provided by the GNU Readline library.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Key Combo',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + a')[0]),
					'description': Markup('Go to the start of the command line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + e')[0]),
					'description': Markup('Go to the end of the command line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + k')[0]),
					'description': Markup('Delete from cursor to the end of the command line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + u')[0]),
					'description': Markup('Delete from cursor to the start of the command line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + w ')[0]),
					'description': Markup('Delete from cursor to start of word (i.e. delete backwards one word)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + y')[0]),
					'description': Markup('Paste word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + xx')[0]),
					'description': Markup('Move between start of command line and current cursor position (and back again)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + b')[0]),
					'description': Markup('Move backward one word (or go to start of word the cursor is currently on)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + f')[0]),
					'description': Markup('Move forward one word (or go to end of word the cursor is currently on)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + d')[0]),
					'description': Markup('Delete to end of word starting at cursor (whole word if cursor is at the beginning of word)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + c')[0]),
					'description': Markup('Capitalize to end of word starting at cursor (whole word if cursor is at the beginning of word)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + u')[0]),
					'description': Markup('Make uppercase from cursor to end of word'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + l')[0]),
					'description': Markup('Make lowercase from cursor to end of word'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Alt + t')[0]),
					'description': Markup('Swap current word with previous'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + f')[0]),
					'description': Markup('Move forward one character'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + b')[0]),
					'description': Markup('Move backward one character'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + d')[0]),
					'description': Markup('Delete character under the cursor'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + h')[0]),
					'description': Markup('Delete character before the cursor'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('Ctrl + t ')[0]),
					'description': Markup('Swap character under cursor with the previous one'),
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
		'heading': helper.set_folder('File Types'),
		'subtitle': '',
		'description': 'This is very different from Windows but straight forward once you get it.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Symbol',
				'Meaning'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('-')[0]),
					'description': Markup('Regular file'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('d')[0]),
					'description': Markup('Directory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('l')[0]),
					'description': Markup('(Symbolic) Link'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('c')[0]),
					'description': Markup('Character device'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('s')[0]),
					'description': Markup('Socket'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('p')[0]),
					'description': Markup('Named pipe'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('b')[0]),
					'description': Markup('Block device'),
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
		'heading': helper.set_folder('Special Files'),
		'subtitle': '',
		'description': 'Files that are read by the shell. Listed in order of their execution.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'File',
				'Info'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('/etc/profile')[0]),
					'description': Markup('Executed automatically at login'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('~.bash_profile</kbd><br><kbd>~/.bash_login</kbd><br><kbd>~.profile')[0]),
					'description': Markup('Whichever is found first is executed at login'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('~/.bashrc')[0]),
					'description': Markup('Is read by every nonlogin shell'),
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
		'heading': helper.set_folder('Permissions'),
		'subtitle': '',
		'description': 'Now you may know what that arcane looking string rwxrwxrwx is when you invoke ls -l',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Code',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('s')[0]),
					'description': Markup('Setuid when in user column'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('s')[0]),
					'description': Markup('Setgid when in group column'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('t')[0]),
					'description': Markup('Sticky bit'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('0</kbd><br><kbd>-')[0]),
					'description': Markup('The access right that is supposed to be on this place is not granted.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('4</kbd><br><kbd>r')[0]),
					'description': Markup('Read access is granted to the user category defined in this place'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('2</kbd><br><kbd>w')[0]),
					'description': Markup('Write permission is granted to the user category defined in this place'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('1</kbd><br><kbd>x')[0]),
					'description': Markup('Execute permission is granted to the user category defined in this place'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('u')[0]),
					'description': Markup('User permissions'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('g')[0]),
					'description': Markup('Group permissions'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('o')[0]),
					'description': Markup('Others permissions'),
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
		'heading': helper.set_folder('String Manipulation'),
		'subtitle': '',
		'description': 'Bash supports a surprisingly big number of string operations! Unfortunately, these tools lack a unified focus. Some are a subset of parameter substitution, and others fall under the functionality of the UNIX expr command. This results in inconsistent command syntax and overlap of functionality.',
		'warning': {
			'MacOS built-in bash is from 2007 and won\'t support many of these.',
		},
		'danger': {
		},
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': [
				'Pattern',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('${#var}')[0]),
					'description': Markup('Find the length of the string'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var%pattern}')[0]),
					'description': Markup('Remove from shortest rear (end) pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var%%pattern}')[0]),
					'description': Markup('Remove from longest rear (end) pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var:position}')[0]),
					'description': Markup('Extract substring from $var at $position'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var:num1:num2}')[0]),
					'description': Markup('Substring'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var#pattern}')[0]),
					'description': Markup('Remove from shortest front pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var##pattern}')[0]),
					'description': Markup('Remove from longest front pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var/pattern/string}')[0]),
					'description': Markup('Find and replace (only replace first occurrence)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var//pattern/string}')[0]),
					'description': Markup('Find and replace all occurrences'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${!prefix*}')[0]),
					'description': Markup('Expands to the names of variables whose names begin with prefix.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var,}</kbd><br><kbd>${var,pattern}')[0]),
					'description': Markup('Convert first character to lowercase'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var,,}</kbd><br><kbd>${var,,pattern}')[0]),
					'description': Markup('Convert all characters to lowercase'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var^}</kbd><br><kbd>${var^pattern}')[0]),
					'description': Markup('Convert first character to uppercase'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${var^^}</kbd><br><kbd>${var^^pattern}')[0]),
					'description': Markup('Convert all character to uppercase'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${string/substring/replacement}')[0]),
					'description': Markup('Replace first match of $substring with $replacement'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${string//substring/replacement}')[0]),
					'description': Markup('Replace all matches of $substring with $replacement'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${string/#substring/replacement}')[0]),
					'description': Markup('If $substring matches front end of $string, substitute $replacement for $substring'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${string/%substring/replacement}')[0]),
					'description': Markup('If $substring matches back end of $string, substitute $replacement for $substring'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("expr match \"$string\" '$substring'")[0]),
					'description': Markup('Length of matching $substring* at beginning of $string'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder("expr \"$string\" : '$substring'")[0]),
					'description': Markup('Length of matching $substring* at beginning of $string'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('expr index \"$string\" $substring')[0]),
					'description': Markup('Numerical position in $string of first character in $substring* that matches [0 if no match, first character counts as position 1]'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('expr substr $string $position $length')[0]),
					'description': Markup('Extract $length characters from $string starting at $position [0 if no match, first character counts as position 1]'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('expr match "$string" \'\($substring\)\'')[0]),
					'description': Markup('Extract $substring*, searching from beginning of $string'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('expr "$string" : \'\($substring\)\'')[0]),
					'description': Markup('Extract $substring* , searching from beginning of $string'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('expr match "$string" \'.*\($substring\)\'')[0]),
					'description': Markup('Extract $substring*, searching from end of $string'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('expr "$string" : \'.*\($substring\)\'')[0]),
					'description': Markup('Extract $substring*, searching from end of $string'),
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
		'heading': helper.set_folder('Quoting'),
		'subtitle': '',
		'description': 'The following text shows characters or that need to be quoted if you want to use their literal symbols and not their special meaning.',
		'warning': {
			'Everything between "..." is taken literally, except $ (dollar) ` (backtick) and " (double-quotation).',
			'Everything between \'...\' is taken literally, except \' (single-quote).',
			'The characters following \ is taken literally. Use \ to escape anything in "..." or \'...\'',
		},
		'danger': {
			'Using $ before "..." or \'...\' causes some special behavior. $"..." is the same as "..." except that locale translation is done. Likewise, $\'...\' is similar to $\'...\' except that the quoted string is processed for escape sequences.',
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Symbol',
				'Literal Meaning'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(';')[0]),
					'description': Markup('Command seperator'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&')[0]),
					'description': Markup('Background execution'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('()')[0]),
					'description': Markup('Command grouping'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('|')[0]),
					'description': Markup('Pipe'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('< > &')[0]),
					'description': Markup('Redirection symbols'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('* ? [ ] ~ + - @ !')[0]),
					'description': Markup('Filename metacharacters'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('" \' \\')[0]),
					'description': Markup('Used in quoting characters'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$')[0]),
					'description': Markup('Variable, command or arithmetic substituion'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('#')[0]),
					'description': Markup('Start a command that ends on a linebreak'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('space tab newline')[0]),
					'description': Markup('Word seperators'),
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
		'heading': helper.set_folder('Command Parameters'),
		'subtitle': '',
		'description': 'Command parameters, also known as arguments, are used when invoking a Bash script.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Command',
				'Description'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('$0')[0]),
					'description': Markup('Name of the script itself'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$1 … $9')[0]),
					'description': Markup('Parameter 1 ... 9'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${10} ... ${nn}')[0]),
					'description': Markup('Positional parameter 10 or greater'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$*')[0]),
					'description': Markup('Expands to the positional parameters, starting from one'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$-')[0]),
					'description': Markup('Current options'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$_')[0]),
					'description': Markup('Contains the absolute file name of the shell or script being executed'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$$')[0]),
					'description': Markup('Process id of the shell'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$?')[0]),
					'description': Markup('Exit status of the most recently executed command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$@')[0]),
					'description': Markup('All arguments as separate words'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$#')[0]),
					'description': Markup('Number of arguments'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$!')[0]),
					'description': Markup('PID of most recently backgrounded process'),
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
		'heading': helper.set_folder('History Expansion'),
		'subtitle': '',
		'description': 'Enables use and manipulation of previous commands.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Command',
				'Description'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('!')[0]),
					'description': Markup('Starts a history substitution'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!!')[0]),
					'description': Markup('Refers to the last command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!n')[0]),
					'description': Markup('Refers to the <n>-th command line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!-n')[0]),
					'description': Markup('Refers to the current command line minus <n>'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!string')[0]),
					'description': Markup('Refers to the most recent command starting with <string>'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!string:p')[0]),
					'description': Markup('Print out the command that !string would run (also adds it as the latest command in the command history)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!$')[0]),
					'description': Markup('The last word of the previous command (same as Alt + .)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!$:p')[0]),
					'description': Markup('Print out the word that !$ would substitute'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!*')[0]),
					'description': Markup('The previous command except for the last word (e.g. if you type ‘_find somefile.txt /’, then !* would give you ‘_find somefile.txt’)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!*:p')[0]),
					'description': Markup('Print out what !* would substitute'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!?string?')[0]),
					'description': Markup('Refers to the most recent command containing <string> (the ending ? is optional)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('^string1^string2^')[0]),
					'description': Markup('Quick substitution. Repeats the last command, replacing <string1> with <string2>'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!#')[0]),
					'description': Markup('Refers to the entire command line typed so far'),
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
		'heading': helper.set_folder('Variable Operations'),
		'subtitle': 'Parameter Expansions',
		'description': '',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Expression',
				'Set and not Null',
				'Set but Null',
				'Unset',
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('${parameter:-word}')[0]),
					'description': {
						Markup('Substitute parameter'),
						Markup('Substitute word'),
						Markup('Substitute word'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter-word}')[0]),
					'description': {
						Markup('Substitute parameter'),
						Markup('Substitute null'),
						Markup('Substitute word'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter:=word}')[0]),
					'description': {
						Markup('Substitute parameter'),
						Markup('Assign word'),
						Markup('Assign word'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter=word}')[0]),
					'description': {
						Markup('Substitute parameter'),
						Markup('Substitute null'),
						Markup('Assign word'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter:?word}')[0]),
					'description': {
						Markup('Substitute parameter'),
						Markup('Error, exit'),
						Markup('Error, exit'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter?word}')[0]),
					'description': {
						Markup('Substitute parameter'),
						Markup('Substitute null'),
						Markup('Error, exit'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter:+word}')[0]),
					'description': {
						Markup('Substitute word'),
						Markup('Substitute null'),
						Markup('Substitute null'),
					},
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${parameter+word}')[0]),
					'description': {
						Markup('Substitute word'),
						Markup('Substitute word'),
						Markup('Substitute null'),
					},
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
		'heading': helper.set_folder('Bash Globbing'),
		'subtitle': '',
		'description': 'Bash cannot recognize RegEx but understand globbing. Globbing is done to filenames by the shell while RegEx is used for searching text.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Glob',
				'Description'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('*')[0]),
					'description': Markup('Matches zero or more occurences of a given pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('?')[0]),
					'description': Markup('Matches zero or one occurences of a given pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('+')[0]),
					'description': Markup('Matches one or more occurences of a given pattern'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('!')[0]),
					'description': Markup('Negates any pattern matches — reverses the pattern so to speak'),
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
		'heading': helper.set_folder('Character Classes in BRE'),
		'subtitle': '',
		'description': 'A character class is a pattern you can use instead of a regular expression. They are easier to remember and work with.',
		'warning': {
		},
		'danger': {
		},
		'info': {
			Markup('Character classes has the format <kbd>[:CharClass:]</kbd>'),
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Character Class',
				'Equivalent',
				'Explanation'
			},
			'data': [
				{
					'character_class': Markup('[:lower:]'),
					'ere_equivalent': Markup('[a-z]'),
					'explanation': 'Lowercase letters.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:upper:]'),
					'ere_equivalent': Markup('[A-Z]'),
					'explanation': 'Uppercase letters.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:alpha:]'),
					'ere_equivalent': Markup('[A-Za-z]'),
					'explanation': 'Alphabetic letters, both upper- and lowercase.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:digit:]'),
					'ere_equivalent': Markup('[0-9]'),
					'explanation': 'Numbers 0-9.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:alnum:]'),
					'ere_equivalent': Markup('[a-zA-Z0-9]'),
					'explanation': 'Alphanumeric: both letters (upper- + lowercase) and digits.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:xdigit:]'),
					'ere_equivalent': Markup('[0-9A-Fa-f]'),
					'explanation': 'Hexadecimal digits.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:space:]'),
					'ere_equivalent': Markup('[ \\t\\n\\r\\f\\v]'),
					'explanation': 'Whitespace. Spaces, tabs, newline and similar.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:punct:]'),
					'ere_equivalent': Markup(''),
					'explanation': 'Symbols (minus digits and letters).',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:print:]'),
					'ere_equivalent': Markup('[[:graph] ]'),
					'explanation': 'Printable characters (spaces included).',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:blank:]'),
					'ere_equivalent': Markup('[ \\t]'),
					'explanation': 'Space and tab characters only.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:graph:]'),
					'ere_equivalent': Markup('[^ [:cntrl:]]'),
					'explanation': 'Graphically printable characters excluding space.',
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'character_class': Markup('[:cntrl:]'),
					'ere_equivalent': Markup(''),
					'explanation': 'Control characters. Non-printable characters.',
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
		'heading': helper.set_folder('Regular Expressions'),
		'subtitle': 'Extended Regular Expressions (ERE)',
		'description': '',
		'warning': {
			'Always use quotes in your RegEx to avoid globbing',
			Markup(
				'In basic regular expressions the metacharacters <kbd>?</kbd>, <kbd>+</kbd>, <kbd>{</kbd>, <kbd>|</kbd>, <kbd>(</kbd>, and <kbd>)</kbd> lose their special meaning; instead use the backslash versions <kbd>\?</kbd> ... <kbd>\)</kbd>. Check in your system documentation whether commands using regular expressions support extended expressions'),
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Operator',
				'Effect'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('.')[0]),
					'description': Markup('Matches any single character'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('?')[0]),
					'description': Markup('The preceding item is optional and will be matched, at most, once'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('*')[0]),
					'description': Markup('The preceding item will be matched zero or more times'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('+')[0]),
					'description': Markup('The preceding item will be matched one or more times'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('{N}')[0]),
					'description': Markup('The preceding item is matched exactly N times'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('{N,}')[0]),
					'description': Markup('The preceding item is matched N or more times'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('{N,M}')[0]),
					'description': Markup('The preceding item is matched at least N times, but not more than M times'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-')[0]),
					'description': Markup('Represents the range if it\'s not first or last in a list or the ending point of a range in a list.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('^')[0]),
					'description': Markup('Matches the empty string at the beginning of a line; also represents the characters not in the range of a list.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$')[0]),
					'description': Markup('Matches the empty string at the end of a line'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[aoeiAOEI]')[0]),
					'description': Markup('Matches any 1 character from the list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[^AOEIaoei]')[0]),
					'description': Markup('Matches any 1 character, not in the list!'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[a-f]')[0]),
					'description': Markup('Matches any 1 character in the range a-f'),
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
		'heading': helper.set_folder('Flow Control'),
		'subtitle': '',
		'description': 'Flow control structures in Bash are straight forward, albeit Bash is unforgiving if you get the syntax wrong.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Keyword',
				'Description'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('if')[0]),
					'description': Markup('Test a condition.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('else')[0]),
					'description': Markup('Test a condition and use a fallback if the test fails.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('elif')[0]),
					'description': Markup('Provides additional testing plus a fallback if all tests fail. You may skip the elif conditions or add as many in-between as you like. Similarly, you may skip the else fallback'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('for')[0]),
					'description': Markup('Iterate over a sequence, a list or anything as far as the imagination goes'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('while')[0]),
					'description': Markup('While a condition is true - repeat until that condition is no longer true'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('until')[0]),
					'description': Markup('The inverse of the while loop - as long as the test-command fails, the until-loop continues'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('select')[0]),
					'description': Markup('Used for easy menu generation. Any statement within can be another select construct, thus enabling sub-menu creation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('case')[0]),
					'description': Markup('Alternative if-branching. Each case is an expression which matches a given pattern (i.e., a case)'),
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
		'heading': helper.set_folder('Overview of Bash Symbols'),
		'subtitle': '',
		'description': 'Here we have gathered a collection of all arcane syntax along with a brief description. A bunch of these symbols are repeated from earlier but many are new - this is a good starting point if you are new to the language.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Builtin',
				'Description'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder('#')[0]),
					'description': Markup('Used for comments'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$')[0]),
					'description': Markup('Used for parameters and variables. Has a bunch of edge cases'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('( )')[0]),
					'description': Markup('Is used for running commands in a subshell'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$( )')[0]),
					'description': Markup('Is used for saving output of commands that are send to run in a subshell'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('(( ))')[0]),
					'description': Markup('Is used for arithmetic'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$(( ))')[0]),
					'description': Markup('Is used for retrieving the output of arithmetic expressions, either for usage with a command or to save the output in a variable.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('$[]')[0]),
					'description': Markup('Deprecated integer expansion construct which is replaced by $(( )). Evaluates integers between the square brackets'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[ ]')[0]),
					'description': Markup('Is used for testing and is a built-in. Is useful in some cases for filename expansion and string manipulation.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[[ ]]')[0]),
					'description': Markup('Is used for testing. This is the one you should use unless you can think of a reason not to.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('<( )')[0]),
					'description': Markup('Used for process substitution and is similar to a pipe. Can be used whenever a command expects a file and you can use multiple at once.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('{ }')[0]),
					'description': Markup('Is used for expansion of sequences'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('${ }')[0]),
					'description': Markup('Is used for variable interpolation and string manipulation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('|')[0]),
					'description': Markup('Is a pipe which is used for chaining commands together'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('<')[0]),
					'description': Markup('Used for feeding input to commands from a file'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('>')[0]),
					'description': Markup('Used for sending output to a file and erasing any previous content in that file.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('||')[0]),
					'description': Markup('Logical or'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&&')[0]),
					'description': Markup('Logical and'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('-')[0]),
					'description': Markup('Used for option prefixes'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('--')[0]),
					'description': Markup('Used for the long-option prefixes'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&')[0]),
					'description': Markup('Used to send a job to the background'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&lt;&lt;WORD</kbd><br><kbd>&lt;&lt;-WORD</kbd><br><kbd>&lt;&lt;\'WORD\'</kbd><br><kbd>&lt;&lt;-\'WORD\' ')[0]),
					'description': Markup('Is used for heredocs'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&lt;&lt;&lt;')[0]),
					'description': Markup('Is used for herestrings'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('&gt;&gt;')[0]),
					'description': Markup('Is used to append output to a file'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('\' \'')[0]),
					'description': Markup('Single quotes are used to preserve the literal value'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('" "')[0]),
					'description': Markup('Double quotes are used to preserve the literal value of all characters except $, ` ` and \\'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('\\')[0]),
					'description': Markup('Backslash is used to escape otherwise interpreted symbols/characters which has a special meaning'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('/')[0]),
					'description': Markup('Used for seperating the components of a filename'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(':')[0]),
					'description': Markup('Similar to a NOP – a do nothing operation. It is a shell builtin with an exit status of true'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(';')[0]),
					'description': Markup('Used to seperate commands intended to run sequentally'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder(',')[0]),
					'description': Markup('Used for linking together arithmetic operations. All are evalutated but only the last is returned'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.')[0]),
					'description': Markup('Represents the current directory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('..')[0]),
					'description': Markup('Represents parent directory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('~')[0]),
					'description': Markup('Expands to home directory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('` `')[0]),
					'description': Markup('Is deprecated and should not be used. Read further in its respective section'),
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
		'heading': helper.set_folder('Bash Builtins'),
		'subtitle': '',
		'description': 'Shell builins are built into Bash are often very (if not extremely) fast compared to external programs. Some of the builtins are inherited from the Bourne Shell (sh) — these inherited commands will also work in the original Bourne Shell.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': {
			'descriptor': {
				'Symbol',
				'Usage'
			},
			'data': [
				{
					'flag': Markup(helper.set_entry_folder(':')[0]),
					'description': Markup('Equivalent to true'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('.')[0]),
					'description': Markup('Reads and executes commands from a designated file in the current shell'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('[')[0]),
					'description': Markup('Is a synonym for test but requires a final argument of ]'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('alias')[0]),
					'description': Markup('Defines an alias for the specified command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('bg')[0]),
					'description': Markup('Resumes a job in background mode'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('bind')[0]),
					'description': Markup('Binds a keyboard sequence to a read line function or macro'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('break')[0]),
					'description': Markup('Exits from a for, while, select, or until loop'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('builtin')[0]),
					'description': Markup('Executes the specified shell built-in command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('caller')[0]),
					'description': Markup('Returns the context of any active subroutine call'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('case')[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('cd')[0]),
					'description': Markup('Changes the current directory to the specified directory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('command')[0]),
					'description': Markup('Executes the specified command without the normal shell lookup'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('compgen')[0]),
					'description': Markup('Generates possible completion matches for the specified word'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('complete')[0]),
					'description': Markup('Displays how the specified words would be completed'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('comopt')[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('continue')[0]),
					'description': Markup('Resumes the next iteration of a for, while, select, or until loop'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('declare')[0]),
					'description': Markup('Declares a variable or variable type'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('dirs')[0]),
					'description': Markup('Displays a list of currently remembered directories'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('disown')[0]),
					'description': Markup('Removes the specified jobs from the jobs table for the process'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('echo')[0]),
					'description': Markup('Displays the specified string to STDOUT'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('enable')[0]),
					'description': Markup('Enables or disables the specified built-in shell command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('eval')[0]),
					'description': Markup('Concatenates the specified arguments into a single command, and executes the command.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('exec')[0]),
					'description': Markup('Replaces the shell process with the specified command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('exit')[0]),
					'description': Markup('Forces the shell to exit with the specified exit status'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('export')[0]),
					'description': Markup('Sets the specified variables to be available for child shell processes'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('fc')[0]),
					'description': Markup('Selects a list of commands from the history list'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('fg')[0]),
					'description': Markup('Resumes a job in foreground mode'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('getopts')[0]),
					'description': Markup('Parses the specified positional parameters'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('hash')[0]),
					'description': Markup('Finds and remembers the full pathname of the specified command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('help')[0]),
					'description': Markup('Displays a help file'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('history')[0]),
					'description': Markup('Displays the command history'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('if')[0]),
					'description': Markup('Used for branching'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('jobs')[0]),
					'description': Markup('Lists active jobs'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('kill')[0]),
					'description': Markup('Sends a system signal to the specified process ID (PID)'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('let')[0]),
					'description': Markup('Evaluates each argument in a mathematical expression'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('local')[0]),
					'description': Markup('Creates a limited-scope variable in a function'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('logout')[0]),
					'description': Markup('Exits a login shell'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('mapfile')[0]),
					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('popd')[0]),
					'description': Markup('Removes entries from the directory stack'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('printf')[0]),
					'description': Markup('Displays text using formatted strings'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('pushd')[0]),
					'description': Markup('Adds a directory to the directory stack'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('pwd')[0]),
					'description': Markup('Displays the pathname of the current working directory'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('read')[0]),
					'description': Markup('Reads one line of data from STDIN, and assigns it to a variable'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('readonly')[0]),
					'description': Markup('Reads one line of data from STDIN, and assigns it to a variable that can’t be changed.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('return')[0]),
					'description': Markup('Forces a function to exit with a value that can be retrieved by the calling script'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('set')[0]),
					'description': Markup('Sets and displays environment variable values and shell attributes'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('shift')[0]),
					'description': Markup('Rotates positional parameters down one position'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('shopt')[0]),
					'description': Markup('Toggles the values of variables controlling optional shell behavior'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('source')[0]),
					'description': Markup('Reads and executes commands from a designated file in the current shell'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('suspend')[0]),
					'description': Markup('Suspends the execution of the shell until a SIGCONT signal is received'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('test')[0]),
					'description': Markup('Returns an exit status of 0 or 1 based on the specified condition'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('times')[0]),
					'description': Markup('Displays the accumulated user and system shell time'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('trap')[0]),
					'description': Markup('Executes the specified command if the specified system signal is received'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('type')[0]),
					'description': Markup('Displays how the specified words would be interpreted if used as a command'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('typeset')[0]),
					'description': Markup('Declares a variable or variable type'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('ulimit')[0]),
					'description': Markup('Sets a limit on the specific resource for system users'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('umask')[0]),
					'description': Markup('Sets default permissions for newly created files and directories'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('unalias')[0]),
					'description': Markup('Removes specified alias'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('unset')[0]),
					'description': Markup('Removes the specified environment variable or shell attribute'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('until')[0]),
					'description': Markup('Loop that is very similar to the while-loop except that it executes until the test-command executes succesfully. As long as the test-command fails, the until-loop continues.'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('wait')[0]),
					'description': Markup('Make the shell wait for a job to finish'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('while')[0]),
					'description': Markup('Waits for the specified process to complete, and returns the exit status'),
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
			'link': 'https://en.wikipedia.org/wiki/Shellshock_(software_bug)',
			'title': 'Shellshock',
			'description': Markup('A group of severe privilege escalation vulnerabilities existing in the wild for about 25 years'),
			'footer': Markup('According to Wikipedia, security companies recorded millions of attacks and probes related to the bugs in the days following the disclosure'),
		},
		{
			'link': 'http://mywiki.wooledge.org/BashGuide',
			'title': 'Greg\'s Wiki 🧠',
			'description': Markup('A lot of great articles teaching good practices and how to avoid pitfalls'),
			'screencapture': 'resources/graphic/link_screen_captures/mywiki_wooledge_org_bash_pitfalls.png'
		},
		{
			'link': 'https://www.shellcheck.net/',
			'title': 'Shellcheck',
			'description': Markup('A linter to check your shellscripts. Extremely useful'),
			'screencapture': 'resources/graphic/link_screen_captures/www_shellcheck_net.png'
		},
		{
			'link': 'https://explainshell.com/',
			'title': 'Explain Shell 🐚',
			'description': Markup('If you have wondered how a fork-bomb or any similar obscure command is parsed and executed'),
			'screencapture': 'resources/graphic/link_screen_captures/www_explainshell_com.png'
		},
		{
			'link': 'https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html',
			'title': 'GNU Bash Manual',
			'description': Markup('Perhaps the most comphehensive manual out there'),
			'screencapture': 'resources/graphic/link_screen_captures/gnu_org_savannah_checkouts_gnu_bash_manual_bash.png',
			'footer': 'Everything you need really.'
		},
		{
			'link': 'https://google.github.io/styleguide/shellguide.html',
			'title': 'Shell Style Guide',
			'description': Markup('Google\'s style guide for shellscripts'),
			'screencapture': 'resources/graphic/link_screen_captures/google_github_io_styleguide_shellguide.png',
		},
		{
			'link': 'https://apenwarr.ca/log/20110228',
			'title': 'Insufficiently known POSIX shell features',
			'screencapture': 'resources/graphic/link_screen_captures/apenwarr_ca.png',
		},
		{
			'link': 'http://www.pixelbeat.org/programming/shell_script_mistakes.html',
			'title': 'Shellscript Mistakes',
			'screencapture': 'resources/graphic/link_screen_captures/pixelbeat_org.png',
		},
	)

]

affiliate_products = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'title': Markup('Bash Pocket Guide'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/1491941596/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491941596&linkCode=as2&tag=cheatsheet0e-20&linkId=8747a5d4f92197e5fa552191d44ad4c8"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1491941596&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=1491941596" height="150" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Concise little reference book that has it all'),
			'description': '',
		},
		{
			'title': Markup('UNIX and Linux System Administration Handbook'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/0134277554/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0134277554&linkCode=as2&tag=cheatsheet0e-20&linkId=2afebdc9ae97dd173c1bf23fc4fb5a57"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0134277554&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=0134277554" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Quality book. A bit pricy however'),
			'description': '',
		},
		{
			'title': Markup('Linux Command Line & Shell Scripting Bible'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/111898384X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=111898384X&linkCode=as2&tag=cheatsheet0e-20&linkId=d1d26240e70373f8913f149455fdde3f"><img style="max-height:150px; max-width: 150px;"  border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=111898384X&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=111898384X" width="100px" border="0" alt="" style="border:none !important; margin:0px !important; max-width: 100px;" />'),
			'footer': Markup('Great for beginners. New edition is on the horizon'),
			'description': '',
		}
	)
]

licensing = [
	Markup('https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02')
]

import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('jinja', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'jinja'
information = {
	'tool': 'Jinja2',
	'title': 'Jinja2 Cheatsheet',
	'subtitle': 'This site is a reference for Jinja2',
	'description': 'Jinja is a ',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Git',
			[
				helper.characteristics.get('template-language'),
			])
	],
	'topic_uris': [
		'template-language',
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
affiliate_products = [{
	Markup(''),
	Markup(''),
	Markup(''),
}],
cheatsheet = [
	{
		'heading': helper.set_folder('Branch'),
		'subtitle': 'How to use Branches',
		'description': 'Everything starts with a branch',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'ab898bdba50a4094ba6b5fa54e6c2e14',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a3fbe41b3c194971a980b671446e9258')[0]),
					'flag': helper.set_entry_command_string("git branch"),
					'description': Markup('List all local branches.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1d2f578b3ae64a9f9e8942f222cdfe25')[0]),
					'flag': helper.set_entry_command_string('git branch -a'),
					'description': Markup(' 	List remote and local branches.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a99e276d4c9948959de245474ddb524d')[0]),
					'flag': helper.set_entry_command_string('git checkout -b branch_name'),
					'description': Markup('Create a local branch and switch to it.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ae8bee499f4b4dbba8fac240ce212bef')[0]),
					'flag': helper.set_entry_command_string('git checkout branch_name'),
					'description': Markup('Switch to an existing branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d75ee871370545959125742f8f6428b4')[0]),
					'flag': helper.set_entry_command_string('git push origin branch_name'),
					'description': Markup('Push branch to remote.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e557991bebd64786a16afd55247e084b')[0]),
					'flag': helper.set_entry_command_string('git branch -m new_name'),
					'description': Markup('Rename current branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ae5d69ef35d543d2b6e497539cecaaad')[0]),
					'flag': helper.set_entry_command_string(Markup('git branch -d branch_name')),
					'description': Markup('Delete a local branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5eff23ea2ee84ef7bb0bee67bc24571d')[0]),
					'flag': helper.set_entry_command_string(Markup('git push origin :branch_name')),
					'description': Markup('Delete a remote branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Logs'),
		'subtitle': '..',
		'description': '..',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'fe42386d7834491a8c9d39ef0324cbf1',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e0fdafea297b445fa96147a932edf539')[0]),
					'flag': helper.set_entry_command_string(Markup('git log --oneline')),
					'description': Markup('Show commit history in single lines.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3999634e0ba645ffb38d8a1df109836a')[0]),
					'flag': helper.set_entry_command_string(Markup('git log -2')),
					'description': Markup('Show commit history for last N commits.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2d1635725ee64b179d228e0575719ae2')[0]),
					'flag': helper.set_entry_command_string(Markup('git log -p -2')),
					'description': Markup('Show commit history for last N commits with diff.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('84ed206940064e75b442cb2fbfdbd127')[0]),
					'flag': helper.set_entry_command_string(Markup('git diff')),
					'description': Markup('Show all local file changes in the working tree.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2dfb99b7152f4642af02a7818de16b83')[0]),
					'flag': helper.set_entry_command_string(Markup('git diff myfile')),
					'description': Markup('Show changes made to a file.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0b7d263d80b548f0938058d8fea2b636')[0]),
					'flag': helper.set_entry_command_string(Markup('git blame myfile')),
					'description': Markup('Show who changed what & when in a file.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('69bea2beab974b53ac2906d74c22a6ec')[0]),
					'flag': helper.set_entry_command_string(Markup('git remote show origin')),
					'description': Markup('Show remote branches and their mapping to local.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Cleanup'),
		'subtitle': '..',
		'description': '..',
		'columns': 'col-lg-6 col-md-12',
		'info': {
			'Some info ...'
		},
		'uuid': helper.get_uuid(),
		'static_red': '7423c8957e5247e0914511adc685ef4a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('1828962810df4d0b91c1b709c5a5a18a')[0]),
					'flag': helper.set_entry_command_string(Markup('git clean -f')),
					'description': Markup('Delete all untracked files.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('077522518c8c474cbc4568f200c65c1c')[0]),
					'flag': helper.set_entry_command_string(Markup('git clean -df')),
					'description': Markup('Delete all untracked files and directories.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('11a02f60b5344897a264a360dd2ce1c8')[0]),
					'flag': helper.set_entry_command_string(Markup('git checkout -- .')),
					'description': Markup('Undo local modifications to all files.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('65637e05e7734d7a879ea993eb417351')[0]),
					'flag': helper.set_entry_command_string(Markup('git reset HEAD myfile')),
					'description': Markup('Unstage a file.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Tags'),
		'subtitle': '.',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f76dbb6407304143ab5a921341469bee',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('68f6f9f63e5d48eeb21432b0cc7cc3c7')[0]),
					'flag': helper.set_entry_command_string(Markup('git pull --tags')),
					'description': Markup('Get remote tags.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('339948867ed6459f9114b1f779047e42')[0]),
					'flag': helper.set_entry_command_string(Markup('git checkout tag_name')),
					'description': Markup('Switch to an existing tag.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a296d080eeef46f0ae99b14b3e4d2ce3')[0]),
					'flag': helper.set_entry_command_string(Markup('git tag')),
					'description': Markup('List all tags.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9677e35a4b31434ea8d49ccbf8f34c02')[0]),
					'flag': helper.set_entry_command_string(Markup('git tag -a tag_name -m "tag message"')),
					'description': Markup('Create a new tag.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ec6cea0c51a44c8bb65bba8fdd82a77e')[0]),
					'flag': helper.set_entry_command_string(Markup('git push --tags')),
					'description': Markup('Push all tags to remote repo.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Stashes'),
		'subtitle': '...',
		'description': '..',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6c3812bfa51b4803abba68f8a7dfbcb8',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ccddcb2d5ce44438b9988a6413a2202b')[0]),
					'flag': helper.set_entry_command_string(Markup('git stash save "stash name" && git stash')),
					'description': Markup('Save changes to a stash.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('20326ea931834389a11157ed999e2653')[0]),
					'flag': helper.set_entry_command_string(Markup('git stash list')),
					'description': Markup('List all stashes.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d41ad8bb124c463ba1b1db2760111904')[0]),
					'flag': helper.set_entry_command_string(Markup('git stash pop')),
					'description': Markup('Apply a stash and delete it from stash list.'),
					'example': helper.example_path(),
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
			'link': 'https://github.com',
			'title': 'Github',
			'description': Markup('A collection of thousands of git-repositories from individual users.'),
			'footer': Markup('You properly know it.'),
			'screencapture': ''
		},
	)
]
licensing = [
	Markup('')
]

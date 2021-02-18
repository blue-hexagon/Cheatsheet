import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('git', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'git'
information = {
	'tool': 'Git',
	'title': 'Git Cheatsheet',
	'subtitle': 'This site is a reference for Git',
	'description': 'Git is a popular VCS (Versioning Control System) developed by Linus Torvalds and released in 2005. It is a distributed version-control system for tracking changes in any set of files. It was developed to allow programmers coordinating their work on source code during software development. Imagine where we would be without! Other VCS exists but Git has gained an enormous adoption since its release.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Git',
			[
				helper.characteristics.get('cvs'),
			])
	],
	'topic_uris': [
		'cvs',
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
		'heading': helper.set_folder('Branch'),
		'subtitle': 'How to use Branches',
		'description': 'Everything starts with a branch',
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
					'flag': Markup(helper.set_entry_folder("git branch")[0]),
					'description': Markup('List all local branches'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git branch -a')[0]),
					'description': Markup('List remote and local branches'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git checkout -b branch_name')[0]),
					'description': Markup('Create a local branch and switch to it'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git checkout branch_name')[0]),
					'description': Markup('Switch to an existing branch'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git push origin branch_name')[0]),
					'description': Markup('Push branch to remote'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git branch -m new_name')[0]),
					'description': Markup('Rename current branch'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git branch -d branch_name')[0]),
					'description': Markup('Delete a local branch'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git push origin :branch_name')[0]),
					'description': Markup('Delete a remote branch'),
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
		'heading': helper.set_folder('Logs'),
		'subtitle': 'Using Git Logs to Your Advantage',
		'description': 'Show commit history, changes done to a file, who changed what and when and more.',
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
					'flag': Markup('git log --oneline')[0],
					'description': Markup('Show commit history in single lines'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git log -2')[0],
					'description': Markup('Show commit history for last N commits'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git log -p -2')[0],
					'description': Markup('Show commit history for last N commits with diff'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git diff')[0],
					'description': Markup('Show all local file changes in the working tree'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git diff myfile')[0],
					'description': Markup('Show changes made to a file'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git blame myfile')[0],
					'description': Markup('Show who changed what & when in a file'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git remote show origin')[0],
					'description': Markup('Show remote branches and their mapping to local'),
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
		'heading': helper.set_folder('Cleanup'),
		'subtitle': 'How To Cleanup with Git',
		'description': 'Delete untracked files, undo local changes and unstaging files.',
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
					'flag': Markup('git clean -f')[0],
					'description': Markup('Delete all untracked files'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git clean -df')[0],
					'description': Markup('Delete all untracked files and directories'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git checkout -- .')[0],
					'description': Markup('Undo local modifications to all files'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git reset HEAD myfile')[0],
					'description': Markup('Unstage a file'),
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
		'heading': helper.set_folder('Tags'),
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
					'flag': Markup('git pull --tags')[0],
					'description': Markup('Get remote tags'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git checkout tag_name')[0],
					'description': Markup('Switch to an existing tag'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git tag')[0],
					'description': Markup('List all tags'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git tag -a tag_name -m "tag message"')[0],
					'description': Markup('Create a new tag'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git push --tags')[0],
					'description': Markup('Push all tags to remote repo'),
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
		'heading': helper.set_folder('Stashes'),
		'subtitle': '...',
		'description': '..',
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
					'flag': Markup('git stash save "stash name" && git stash')[0],
					'description': Markup('Save changes to a stash'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git stash list')[0],
					'description': Markup('List all stashes'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git stash pop')[0],
					'description': Markup('Apply a stash and delete it from stash list'),
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

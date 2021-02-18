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
	'state': '❌',
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
	'',
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup(helper.set_entry_folder("git branch")[0]),
					'description': Markup('List all local branches.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git branch -a')[0]),
					'description': Markup(' 	List remote and local branches.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git checkout -b branch_name')[0]),
					'description': Markup('Create a local branch and switch to it.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git checkout branch_name')[0]),
					'description': Markup('Switch to an existing branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git push origin branch_name')[0]),
					'description': Markup('Push branch to remote.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup(helper.set_entry_folder('git branch -m new_name')[0]),
					'description': Markup('Rename current branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git branch -d branch_name'),
					'description': Markup('Delete a local branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git push origin :branch_name'),
					'description': Markup('Delete a remote branch.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('git log --oneline'),
					'description': Markup('Show commit history in single lines.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git log -2'),
					'description': Markup('Show commit history for last N commits.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git log -p -2'),
					'description': Markup('Show commit history for last N commits with diff.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git diff'),
					'description': Markup('Show all local file changes in the working tree.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git diff myfile'),
					'description': Markup('Show changes made to a file.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git blame myfile'),
					'description': Markup('Show who changed what & when in a file.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git remote show origin'),
					'description': Markup('Show remote branches and their mapping to local.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('git clean -f'),
					'description': Markup('Delete all untracked files.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git clean -df'),
					'description': Markup('Delete all untracked files and directories.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git checkout -- .'),
					'description': Markup('Undo local modifications to all files.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git reset HEAD myfile'),
					'description': Markup('Unstage a file.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
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
		'static_ref': '',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'flag': Markup('git pull --tags'),
					'description': Markup('Get remote tags.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git checkout tag_name'),
					'description': Markup('Switch to an existing tag.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git tag'),
					'description': Markup('List all tags.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git tag -a tag_name -m "tag message"'),
					'description': Markup('Create a new tag.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git push --tags'),
					'description': Markup('Push all tags to remote repo.'),
					'example': helper.example_path(),
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
					'flag': Markup('git stash save "stash name" && git stash'),
					'description': Markup('Save changes to a stash.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git stash list'),
					'description': Markup('List all stashes.'),
					'example': helper.example_path(),
					'video': Markup(''),
					'uuid': helper.get_uuid(),
					'static_ref': ''
				},
				{
					'flag': Markup('git stash pop'),
					'description': Markup('Apply a stash and delete it from stash list.'),
					'example': helper.example_path(),
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
			'description': Markup('A collection of thousands of git-repositories from individual users.'),
			'footer': Markup('You properly know it.'),
			'screencapture': ''
		},
	)
]

licensing = [
	Markup('')
]

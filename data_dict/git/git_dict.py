import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('git', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'git'
meta = {
	'title': 'Git Cheatsheet',
	'description': 'Branches · Clean · Tags · Logs · Stashes',
	'keywords': 'git, vcs, github, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/Git/',

	'opengraph_title': 'Git Cheatsheet',
	'opengraph_description': 'Branches · Clean · Tags · Logs · Stashes',
	'opengraph_image': 'opengraph_git.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/git/',

	'twitter_title': 'Git Cheatsheet',
	'twitter_description': 'Branches · Clean · Tags · Logs · Stashes',
	'twitter_image': 'twitter_card_git.png',
}
information = {
	'tool': 'Git',
	'title': 'Git Cheatsheet',
	'subtitle': 'This site is a reference for Git',
	'description': 'Git is a popular VCS (Versioning Control System) developed by Linus Torvalds and released in 2005. It is a distributed version-control system for tracking changes in any set of files. It was developed to allow programmers coordinating their work on source code during software development. Imagine where we would be without! Other VCS exists but Git has gained an enormous adoption since its release.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
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
		'description': 'Branches are unique versions of your repository which are used to work on the codebase independently from other changes, e.g. a feature branch, a hotfix branch, experimental feature branch.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6bbc9b44071744e4bf4386a7038a8b5a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e8646f33a6ec4ca9aa137ae674d2ca69')[0]),
					'flag': helper.set_entry_command_string("git branch"),
					'description': [
						Markup('List all local branches'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7c2cd123c87a498fb58d4fdde0312a70')[0]),
					'flag': helper.set_entry_command_string('git branch -a'),
					'description': [
						Markup('List remote and local branches'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1e90a08c462b4e55a97dc0b7ec6b5ac6')[0]),
					'flag': helper.set_entry_command_string('git checkout -b branch_name'),
					'description': [
						Markup('Create a local branch and switch to it'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e433d23123c5424c829f246e5b68d48c')[0]),
					'flag': helper.set_entry_command_string('git checkout branch_name'),
					'description': [
						Markup('Switch to an existing branch'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('286876fca7d24bd6a82afd694162f604')[0]),
					'flag': helper.set_entry_command_string('git push origin branch_name'),
					'description': [
						Markup('Push branch to remote'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('89a2f1e0bc8c40af805d37bb9acc28ed')[0]),
					'flag': helper.set_entry_command_string('git branch -m new_name'),
					'description': [
						Markup('Rename current branch'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d526e67ffde341a8b9d8ad07a48f0370')[0]),
					'flag': helper.set_entry_command_string('git branch -d branch_name'),
					'description': [
						Markup('Delete a local branch'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('779f3523414d479b846621528ec67a2c')[0]),
					'flag': helper.set_entry_command_string('git push origin :branch_name'),
					'description': [
						Markup('Delete a remote branch'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '19da3b6b2ea74d3297ead4551e879d9d',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ca8ef8dcbe424bd3b5bb33e01ed4a790')[0]),
					'flag': helper.set_entry_command_string('git log --oneline'),
					'description': [
						Markup('Show commit history in single lines'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b5b1b2fd50a445fe827a9aa89437527a')[0]),
					'flag': helper.set_entry_command_string('git log -2'),
					'description': [
						Markup('Show commit history for last N commits'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('753daf3ee091421795cab7c063fe3c3b')[0]),
					'flag': helper.set_entry_command_string('git log -p -2'),
					'description': [
						Markup('Show commit history for last N commits with diff'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7b9a56bb34a94d15a4beafa05a9eda6d')[0]),
					'flag': helper.set_entry_command_string('git diff'),
					'description': [
						Markup('Show all local file changes in the working tree'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('99003de4c28043a99e11e59805aac85e')[0]),
					'flag': helper.set_entry_command_string('git diff myfile'),
					'description': [
						Markup('Show changes made to a file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('92624b9bef634d349d95822aba9e6aaa')[0]),
					'flag': helper.set_entry_command_string('git blame myfile'),
					'description': [
						Markup('Show who changed what & when in a file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9e91c651a37d40509b9cc2bc993b328c')[0]),
					'flag': helper.set_entry_command_string('git remote show origin'),
					'description': [
						Markup('Show remote branches and their mapping to local'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
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
		'static_red': '3ebebf5b62d6415e98cb95d0554d92dc',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('50141aed87a249a58dea6649babe39fc')[0]),
					'flag': helper.set_entry_command_string('git clean -f'),
					'description': [
						Markup('Delete all untracked files'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2ecbb746fdf445cd9e1c6ad1e02e71fc')[0]),
					'flag': helper.set_entry_command_string('git clean -df'),
					'description': [
						Markup('Delete all untracked files and directories'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('25b2b93f535142cd9913904ec8de9bd9')[0]),
					'flag': helper.set_entry_command_string('git checkout -- .'),
					'description': [
						Markup('Undo local modifications to all files'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7473de76a1d943a1b3b6209ce04bb529')[0]),
					'flag': helper.set_entry_command_string('git reset HEAD myfile'),
					'description': [
						Markup('Unstage a file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Tags'),
		'subtitle': '',
		'description': 'Tagging is used to capture a point in the commit history, such as a realease version.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'fa03465c437345769f2be798f38db07f',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('44bfa2cf107543c486c748557e6a13dd')[0]),
					'flag': helper.set_entry_command_string('git pull --tags'),
					'description': [
						Markup('Get remote tags'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('18b5df67353e4ce79c3b8b852dbc2eda')[0]),
					'flag': helper.set_entry_command_string('git checkout tag_name'),
					'description': [
						Markup('Switch to an existing tag'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a85eefeafc284bdbbd2e6c2c80f9285b')[0]),
					'flag': helper.set_entry_command_string('git tag'),
					'description': [
						Markup('List all tags'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8f09ed8b1aa34e159efccdf108ed273c')[0]),
					'flag': helper.set_entry_command_string('git tag -a tag_name -m "tag message"'),
					'description': [
						Markup('Create a new tag'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6106ea045a974d17a38d742a9fabe973')[0]),
					'flag': helper.set_entry_command_string('git push --tags'),
					'description': [
						Markup('Push all tags to remote repo'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Stashes'),
		'subtitle': 'Stash your changes temporarily',
		'description': 'Stashes take your uncomitted (staged or unstaged) changes and saves them away for later use. ',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '87b26f69dd4a4f3a94307b84cfc91694',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e797dbd7fe364c7eaf07f00619b33859')[0]),
					'flag': helper.set_entry_command_string('git stash save "stash name" && git stash'),
					'description': [
						Markup('Save changes to a stash'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('18a8bfe98f6e4c52be9e862b4a6f533c')[0]),
					'flag': helper.set_entry_command_string('git stash list'),
					'description': [
						Markup('List all stashes'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('aca472a93b454fd6a8a74c9048a249c2')[0]),
					'flag': helper.set_entry_command_string('git stash pop'),
					'description': [
						Markup('Apply a stash and delete it from stash list'),
					],
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
			'link': 'https://github.com',
			'title': 'Github',
			'description': Markup('A collection of thousands of git-repositories from individual users'),
			'footer': Markup('You properly know it'),
			'screencapture': ''
		},
		{
			'link': 'https://sethrobertson.github.io/GitFixUm/fixup.html',
			'title': 'On undoing, fixing or removing commits',
			'description': Markup('When you got a mess on your hands, this article might help you out'),
			'footer': Markup('For when you mess up'),
			'screencapture': ''
		},
		{
			'link': 'https://www.internalpointers.com/post/squash-commits-into-one-git',
			'title': 'Squashing Commits',
			'description': Markup('A little guide on how to squash commits in Git'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://learngitbranching.js.org/',
			'title': 'Interactive Git Tutorial',
			'description': Markup('Much more than branching...'),
			'footer': Markup('Use it to learn Git'),
			'screencapture': ''
		},
		{
			'link': 'https://git-scm.com/',
			'title': 'Git Documentation',
			'description': Markup('Through and good documentation'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]

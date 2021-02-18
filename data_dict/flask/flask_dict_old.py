import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.data_dict.helper_functions import Helpers
from static.data_dict.resource_collector import ResourceCollector

helper = Helpers('flask', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'flask'
information = {
	'tool': 'Flask',
	'title': 'Flask Cheatsheet',
	'subtitle': 'This site is a reference for Flask',
	'description': 'Flask is a popular micro framework written in Python and used for building web applications. It supports extensions that can add application features as if they were implemented in Flask itself.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Flask',
			[
				helper.characteristics.get('framework'),
				helper.characteristics.get('back-end'),
				helper.characteristics.get('web-development'),
			])
	],
	'topic_uris': [
		'framework',
		'back-end',
		'web-development',
	],
}
general_info_text = ''
general_info_text_lead = ''
general_info_links = {

}
general_info_flag = False
general_info = [
	'',  # Markup(flask_cheatsheet.cheatsheet),
]
see_also = [
	{
	},
]

code_cards = [{

}]
cheatsheet = [
	{
		'heading': helper.set_folder('Skeleton Application'),
		'subtitle': 'How to create a bare-bones application',
		'description': 'This example shows you how the minimal code required to setup a functional Flask app',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
from flask import Flask
app = Flask(__name__)
# Make a route accessible, i.e. www.example.com/hello-world/
@app.route('/hello-world/')
def hello():
   # Method which is executed when user accesses www.example.com/hello-world/
   return 'Hello, World!'

if __name__ == '__main__':
   app.run(debug=True)         
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Routing Basics'),
		'subtitle': 'Creating URL routes',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
@app.route('/&lt;string:name&gt;/&lt;int:age&gt;')
def hello(name, age):
	return 'Hello ' + name + ', ' + 'you are ' + age + ' years old!'

# Other route converters
# string -> The default. Accepts any text without a slash.
# float -> A floating point integer, i.e. 4.32137
# int -> An integer, i.e. 7
# path -> Like a string but also accepts slash.
# uuid -> Accepts UUIDs (universally unique identifiers); think hexcode on steroids.
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Request Methods'),
		'subtitle': 'Handling user requests',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
@app.route('/test') # Accepts 'GET' by default and no other.
@app.route('/test', methods=['POST']) # Allows only 'POST'.
@app.route('/test', methods=['POST','PUT']) # Allows 'PUT' and 'POST' and no other.
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Configuration'),
		'subtitle': 'Setting configuration values',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
app.config['CONFIG_NAME'] = 'config value' # E.g. app.config['SECRET_KEY'] = '832dcb4c00910ad5de1db300488e26d9'
app.config.from_envvar('ENV_VAR_NAME') # Gets the value from an environment value. Useful for API keys and similar information.
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Templates'),
		'subtitle': 'Using Flask+Jinja2 to render dynamic templates',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
from flask import render_template
@app.route('/')def index():
	return render_template('template_file.html', var1=value1, ...) # Specify as many vars as you want to, to pass down to the template.    
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('JSON Responses'),
		'subtitle': 'Returning JSON instead of HTML',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
import jsonify
@app.route('/returnstuff')
def returnstuff():
	num_list = [1,2,3,4,5]
	num_dict = {'numbers' : num_list, 'name' : 'Numbers'}
	return jsonify({'output' : num_dict})
# Usefull if you f.e. want to create a REST API for connecting the backend to the frontend.    
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Request Data (Access)'),
		'subtitle': 'Accessing user data with the request object',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
request.args['name'] # Query string arguments
request.form['name'] # Form data
request.method # Used to determine the request type. Can be used to check if user is POST'ing, PUT'ting, GET'ting etc.
request.cookies.get('cookie_name') # Getting a cookie, by name 'cookie_name'
request.files['name'] # Retrieving a file    
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Redirection'),
		'subtitle': 'Redirecting a route in Flask',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
from flask import url_for, redirect
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/redirect')
def redirect_example():
	return redirect(url_for('home')) # Redirects the user to /home
	# url_for('') retrieves route and method for whatever method you give it.    
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Aborting and Errorhandling'),
		'subtitle': 'Handling a 404 Not Found error',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
from flask import abort()
@app.route('/')
def index():
	abort(404) # Returns 404 error. Use the errorhandler below to catch http codes, i.e. redirecting to your own 404 page.
	render_template('index.html') # This never gets executed

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html', title='404: Missing Page'), 404    
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Setting Cookies'),
		'subtitle': '',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
from flask import make_response
@app.route('/')
def index():
	res = make_response(render_template('index.html'))
	res.set_cookie('cookie_name', 'cookie_value')
	return res    
				"""
			],
		],
	},
	{
		'heading': helper.set_folder('Sessions'),
		'subtitle': '',
		'description': '',
		'uuid': helper.get_uuid(),
		'static_ref': '',
		'content': [
			[
				"""
import session
app.config['SECRET_KEY'] = 'any random string' # Secret key must always be set to use sessions

# Set a session
@app.route('/login_success')
def login_success():
	session['key_name'] = 'key_value' #stores a secure cookie in browser
return redirect(url_for('index'))

# Read a session
@app.route('/')
def index():
	if 'key_name' in session: # Session exists and has key named 'key_name'
		session_var = session['key_value']    
				"""
			],
		],
	},
]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://prettyprinted.com/',
			'title': 'Pretty Printed',
			'description': Markup('Flask, Django, Python and more. He also has a handful of free mini-courses on topics such as SQLAlchemy and Flask.'),
			'footer': Markup('Brilliant tutor.'),
			'screencapture': ''
		},
	)
]
affiliate_products = [
	''
]
licensing = [
	Markup('')
]

import os
import flask

from flask import request, render_template

from src.items import create_random_item, to_view

app = flask.Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route('/')
def display_items():

	num = 10
	if 'num' in request.args:
		num = int(request.args['num'])
		
	items = [to_view(create_random_item()) for _ in range(num)]
	return render_template('items.html', items=items)

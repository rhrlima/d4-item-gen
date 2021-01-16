from src.items import create_random_item, to_view

import flask
from flask import request, render_template

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def display_items():

	if 'num' in request.args:
		num = int(request.args['num'])
	else:
		num = 10
	items = [to_view(create_random_item()) for _ in range(num)]
	return render_template('items.html', items=items)

from src.items import create_random_item, to_view

import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/home')
def single_item():

	item = create_random_item()
	item_dict = to_view(item)
	return render_template('test.html', item=item_dict)


@app.route('/items')
def display_items():

	if 'num' in request.args:
		num = int(request.args['num'])
	else:
		num = 10
	items = [to_view(create_random_item()) for _ in range(num)]
	return render_template('items.html', items=items)


if __name__ == '__main__':
	
	app.run()

import os
from flask import Flask, request, render_template
from people import get_people, add_people, edit_people, delete_people, get_people_filtered


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api/')
def api_base():
    return request.args


methods = ['GET', 'POST', 'PUT', 'DELETE']
@app.route('/api/people', methods=methods)
@app.route('/api/people/<id>', methods=methods)
def api_people(id=None):

    if request.method == "POST":
        data = request.get_json()
        return add_people(data)

    elif request.method == "PUT":
        data = request.get_json()
        return edit_people(data)

    elif request.method == "DELETE":
        data = request.get_json()
        return delete_people(data)
    else:
        requests = len(request.args)

        if requests > 0:
            return get_people_filtered(request.args)
        else:
            return get_people(id)


@app.route('/api/systems')
def api_systems():
    return 'system results here'


@app.route('/api/planets')
def api_planets():
    return 'planets results here'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

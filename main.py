from flask import Flask, request
from utilities import create_table, phone_create, phone_read, phone_update, phone_delete

app = Flask(__name__)


@app.route("/create_table/")
def new_table():
    create_table()
    return 'table_created'


@app.route("/phones/create/")
def create_phone():
    phone_id = request.args['id']
    name = request.args['name']
    number = request.args['phone']
    phone_create(phone_id, name, number)
    return 'phone_create'


@app.route("/phones/read/")
def read_phones():
    result = phone_read()
    return str(result)


@app.route("/phones/update/")
def update_phone():
    phone_id = request.args['id']
    name = request.args['name']
    number = request.args['phone']
    phone_update(phone_id, name, number)
    return 'phone_update'


@app.route("/phones/delete/")
def delete_phone():
    id_phone = request.args['id']
    phone_delete(id_phone)
    return 'phone_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

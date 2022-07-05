import os
from flask import Flask, request, send_from_directory, send_file
from flask_cors import CORS, cross_origin
import string
import random

app = Flask(__name__)
cors = CORS(app)


cur_path = os.getcwd()
UPLOAD_FOLDER =  os.path.join(app.root_path,'Downloads')
print ("ULOAD", UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3','wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['GET'])
def dev():
    if request.args:
        key = list(request.args)[0]
        return send_from_directory(f"{os.getcwd()}/app/dist/app", key)
    else:
        return send_from_directory(f"{os.getcwd()}/app/dist/app", "index.html")


# @app.route("/", methods=['GET'])
# def dev():
#     print("inside Main ")
#     # if request.args:
#     #     key = list(request.args)[0]
#     #     return send_from_directory(f"{os.getcwd()}/dist/demo", key)
#     # else:
#     # print("******", f"{os.getcwd()}dist/demo")
#     return send_from_directory(f"{os.getcwd()}/app/dist/demo", "index.html")

@app.route('/save', methods=['POST'])   
def save():
    print("** Insie Save Method ** ")
    file = request.files['file']
    print ("\n\n")
    print (request.files)
    print("\n\n")

    # res = ''.join(random.choices(string.ascii_uppercase + string.digits, k =7))
    res = 'output'
    fl_name = res + '.wav'
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fl_name))
    return "success"




# ======================================
if __name__ == '__main__':
    print('Angular frontend enabled on localhost port 8080')
    app.run(debug=True, host='127.0.0.1', port=8080)

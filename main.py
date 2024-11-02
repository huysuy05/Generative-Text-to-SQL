from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS 
# from flask_wtf import FlaskForm
# from wtforms import FileField, SubmitField
# from wtforms.validators import DataRequired
# CORS lets you be able to access Flask from different domains
# CORS stands for Cross-Origin Resource Sharing
from meta.get_schema import get_schema
from nl2sql.gen_query import gen_sql_query, glob_context
from nl2sql.exec_query import execute_query
# from werkzeug.utils import secure_filename
# import os


app = Flask(__name__)
CORS(app)



# app.config["SECRET_KEY"] = "huysuy05"
# app.config["UPLOAD_FOLDER"] = "input_dir"


# class FileUpload(FlaskForm): #Setting buttons for the file
#     file = FileField('File', validators=[DataRequired()])
#     submit = SubmitField('Upload File')


# @app.route("/", methods=["GET", "POST"])
# @app.route("/get_file", methods=["GET", "POST"])
# # # Upload the button to the html template
# def get_file():
#     form = FileUpload()
#     if form.validate_on_submit():
#         file = form.file.data #Lấy file được chọn
#         filename = secure_filename(file.filename)  
#         upload_path = app.config["UPLOAD_FOLDER"]
#         if not os.path.exists(upload_path):
#             os.makedirs(upload_path)
#         file.save(os.path.join(upload_path, filename))
#         return "File has been saved"
#     return render_template("index.html", form=form)


# Route the generated query to the app

@app.route("/set_schema", methods=["POST"])
def set_schema():
    global context
    schema_context = request.form.get("schema")
    if not schema_context:
        return jsonify({'error': "no schema found"}), 400
    
    context = get_schema(schema_context)
    glob_context(context)
    return jsonify({'message': 'schema received successfully'}), 200


@app.route("/gen_query", methods=['POST'])
def gen_query():
    data = request.get_json() #Lấy request từ flask app
    if not data:
        return jsonify({"error": "could not achieve data"}), 400
    
    print("Request data: ", data)
    question = data.get("question")
    if not question:
        return jsonify({"error": "no question received"}), 400


    query = gen_sql_query(question)

    if not query:
        return jsonify({"error": "No query returned"}), 400
    return jsonify({"query": query}), 200

# Route the executed query to the app
@app.route("/exec_query", methods=['POST'])
def exec_query():
    data = request.get_json()
    query  = data.get("query")
    print(query)
    if not query:
        return jsonify({"error": "No query returned"}), 400
    
    try:
        res = execute_query(query)
        return jsonify({"result": res}), 200
    except Exception as e:
        return jsonify({"error": f"Error occured at {e}"}), 500
    

if __name__ == "__main__":
    app.run(debug=True, port=5500)

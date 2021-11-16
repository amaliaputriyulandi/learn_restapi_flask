# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


# Inisiasi object flask
app = Flask(__name__)

# Inisiasi objeck flask_restful
api = Api(app)

# Inisiasi objeck flask_cors
CORS(app)

# Inisiasi variabel kosong bertipe dictionary
identitas = {}  # variabel global, dictionary = json

# membuat class Resource


class ContohResource(Resource):
    # Metode get and post
    def get(self):
        # response = {"msg":"Hallo dunia, ini app restful pertamaku di flask"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        #print("COBA PRINT", nama)
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg": "Data berhasil dimasukkan",
                    "nama": nama,
                    "umur": umur}
        return response


# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)

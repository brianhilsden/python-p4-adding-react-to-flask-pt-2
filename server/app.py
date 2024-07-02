from flask import Flask,make_response,request,jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db,Movie

app = Flask(__name__)
CORS(app)
migrate = Migrate(app,db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.json.compact = False

@app.route("/movies",methods = ["GET"])
def movies():
    if request.method == "GET":
        movies = Movie.query.all()
        return make_response(jsonify([movie.to_dict() for movie in movies]),200)
    
    return make_response({"text":"Method not Allowed"})
 

if __name__ == '__main__':
    app.run(port=5555,debug=True)
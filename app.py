from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://BlAcKkNiGhT47:Nagumalai47@cluster0.fflbwsc.mongodb.net/")
    app.db = client.Microblog


    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method=="POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.Entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.Entries.find({})
        ]


        return render_template("home.html", entries=entries_with_date)
    
    return app
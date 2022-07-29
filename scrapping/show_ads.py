from flask import Flask
from flask import render_template
import psycopg2
from sqlalchemy import create_engine

app = Flask(__name__)
@app.route("/")

def main():
    db_name = 'sreality_db'
    db_user = 'sokovninn'
    db_pass = 'sreality_db'
    db_host = 'db'
    db_port = '5432'
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    db = create_engine(db_string)

    with app.app_context():
        query = "SELECT (title,imageurl)  " + \
                "FROM flats "
        cursor = db.execute(query)
        results = cursor.fetchall()
        results = [list(eval(result[0])) for result in results]
        results = list(enumerate(results))
        return render_template("results.html", results = results)


if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=8080)

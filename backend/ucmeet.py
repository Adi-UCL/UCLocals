from flask import Flask, request
import mysql.connector as sql

app = Flask(__name__)


def get_db_conn():
    # noinspection SpellCheckingInspection
    user = "ucmeet"
    # noinspection SpellCheckingInspection
    password = "Porticode15"
    # noinspection SpellCheckingInspection
    database = "ucmeet"
    host = "localhost"
    return sql.connect(user = user, password = password, host = host, database = database)


def get_col_heads():
    db = get_db_conn()
    cur = db.cursor()
    # noinspection SpellCheckingInspection
    cur.execute("SHOW COLUMNS FROM ucmeet")
    columns = cur.fetchall()
    db.close()
    return [column[0] for column in columns]


def ghost(args, record):
    if not args.get("ghosts"):
        return record[8] == 0
    else:
        return args.get("ghosts").lower() == "true"


def year(args, record):
    if not args.get("year"):
        return True
    else:
        return record[3] == int(args.get("year"))


def course(args, record):
    if not args.get("course"):
        return True
    else:
        return args.get("course").lower() in record[4].lower()


def societies(args, record):
    if not args.get("societies"):
        return True
    else:
        return args.get("societies").lower() in record[5].lower()


def status(args, record):
    if not args.get("status"):
        return True
    else:
        return record[6].lower() == args.get("status").lower()


def location(args, record):
    if not args.get("location"):
        return True
    else:
        return args.get("location").lower() in record[7].lower()


def show_record(a, r):
    return ghost(a, r) and year(a, r) and course(a, r) and societies(a, r) and status(a, r) and location(a, r)


def formatted_value(i, value):
    if i == 3:
        return f"Year {value}"
    elif i == 8:
        if value == 1:
            return "Ghost Mode On"
        else:
            return "Ghost Mode Off"
    else:
        return str(value)


def filtered_records(records):
    table = ""
    for record in records:
        if show_record(request.args, record):
            values = []
            for i, value in enumerate(record):
                values.append(formatted_value(i, value))
            table += "\t".join(values)
            table += "\n"
    return table


@app.route("/search")
def search():
    db = get_db_conn()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM ucmeet")
    records = cur.fetchall()
    db.close()
    return filtered_records(records)


@app.route("/insert")
def insert():
    db = get_db_conn()
    cur = db.cursor()
    col_heads = get_col_heads()[1:]
    placeholders = ["%s" for _ in range(len(col_heads))]
    sql_query = f"INSERT INTO ucmeet ({', '.join(col_heads)}) VALUES ({', '.join(placeholders)})"
    # noinspection DuplicatedCode
    record = [request.args.get(col_head) for col_head in col_heads]
    try:
        cur.execute(sql_query, record)
        db.commit()
    except sql.Error as error:
        db.close()
        return str(error)
    db.close()
    return "true"


@app.route("/update/<int:record_id>")
def update(record_id):
    db = get_db_conn()
    cur = db.cursor()
    col_heads = get_col_heads()[1:]
    fields = [f"{col_head} = %s" for col_head in col_heads]
    sql_query = f"UPDATE ucmeet SET {', '.join(fields)} WHERE {get_col_heads()[0]} = {record_id}"
    # noinspection DuplicatedCode
    record = [request.args.get(col_head) for col_head in col_heads]
    try:
        cur.execute(sql_query, record)
        db.commit()
    except sql.Error as error:
        db.close()
        return str(error)
    db.close()
    return "true"


app.run()

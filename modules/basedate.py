import configparser
import sqlite3

t = None


def new_base():
    try:
        conn = sqlite3.connect('.//base_date/vegetables.db')
        cursor = conn.cursor()
        # Если не существует таблиц, их нужно создать (первый запуск)
        vegetable = """
              create table if not exists
                vegetable (
                    id INT Primary Key,
                    name TEXT,
                    super_class TEXT,
                    main_class TEXT,
                    child_class TEXT,
                    growing_season BOOLEAN,
                    hybrid BOOLEAN,
                    thermophilic BOOLEAN,
                    light_loving BOOLEAN,
                    hydrophilous BOOLEAN,
                    coord_x INT,
                    coord_y INT,
                    period1 TEXT,
                    period2 TEXT,
                    recommended_date TEXT,
                    temperature INT,
                    state BOOLEAN,
                    fact_date TEXT,
                    comment TEXT,
                    path_img TEXT
                );
            """

        cursor.execute(vegetable)
        conn.commit()
        conn.close()
    except:
        pass


def save_base(ident,name=t, super_class=t, main_class=t, child_class=t, growing_season=t, hybrid=t, thermophilic=t,
              light_loving=t, hydrophilous=t, coord_x=t, coord_y=t,period1=t,period2=t, recommended_date=t, temperature=t, state=t,
              fact_date=t, comment=t, path_img=t):
    try:

        config = configparser.ConfigParser()
        conn = sqlite3.connect('.//base_date/vegetables.db')
        cur = conn.cursor()
        config.read('conf.ini')
        tmp = (ident, name, super_class, main_class, child_class, growing_season, hybrid, thermophilic,
               light_loving, hydrophilous, coord_x, coord_y, recommended_date, temperature, state,
               fact_date, comment, path_img)
        req = """INSERT INTO vegetable (id, name, super_class, main_class, child_class, growing_season,
        hybrid, thermophilic, light_loving, hydrophilous, coord_x, coord_y, period1, period2, recommended_date, temperature, state,
        fact_date, comment,path_img) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        cur.execute(req, tmp)
        conn.commit()
        conn.close()
        config['DEFAULT']['id'] = str(ident)
        with open('conf.ini', 'w') as configfile:
            config.write(configfile)
        return True
    except:
        return False


def number_of_rows():
    try:
        conn = sqlite3.connect('.//base_date/vegetables.db')
        cur = conn.cursor()
        tmp = cur.execute("SELECT Count(1) FROM vegetable").fetchall()
        conn.close()
        return tmp[0][0]
    except:
        return False


def instance(current_vegetable):
    try:
        conn = sqlite3.connect('.//base_date/vegetables.db')
        cur = conn.cursor()
        tmp = cur.execute(f"SELECT *  from vegetable WHERE id= {str(current_vegetable)}").fetchall()
        tmp = tmp[0]
        conn.close()
        return tmp
    except:
        return False


def list_all_id():
    try:
        conn = sqlite3.connect('.//base_date/vegetables.db')
        cur = conn.cursor()
        tmp = cur.execute("SELECT id FROM vegetable").fetchall()
        conn.close()
        tmp2 = [int(i[0]) for i in tmp]
        return tmp2
    except:
        return []


def del_v(data):
    try:
        conn = sqlite3.connect('.//base_date/vegetables.db')
        cur = conn.cursor()
        tmp = cur.execute(f"DELETE FROM vegetable where id={data}")
        conn.commit()

        conn.close()
        return True
    except:
        return False
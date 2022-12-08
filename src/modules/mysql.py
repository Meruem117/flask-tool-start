import pymysql


def show_database():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db="bili")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show databases"
    cursor.execute(sql)
    database_list = cursor.fetchall()

    cursor.close()
    con.close()

    return database_list


def show_tables(database_name):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db="bili")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show tables from %s"
    cursor.execute(sql % database_name)
    table_list = cursor.fetchall()

    cursor.close()
    con.close()

    return table_list


def show_table_columns(table_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db="bili")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show full columns from %s"
    cursor.execute(sql % table_name)
    column_list = cursor.fetchall()

    cursor.close()
    con.close()

    return column_list


def select_table_data(table_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db="bili")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from %s"
    cursor.execute(sql % table_name)
    data_list = cursor.execute()

    cursor.close()
    con.close()

    return data_list


if __name__ == '__main__':
    show_database()
    # show_tables("bili")
    # show_table_columns("up")
    # select_table_data("up")

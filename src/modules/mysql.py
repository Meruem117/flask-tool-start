import pymysql


def show_database():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show databases"
    cursor.execute(sql)
    database_list = cursor.fetchall()
    filter_list = ["information_schema", "performance_schema", "sys"]
    result = [item for item in database_list if item["Database"] not in filter_list]

    cursor.close()
    con.close()

    return result


def show_tables(database_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show tables from %s"
    cursor.execute(sql % database_name)
    table_list = cursor.fetchall()

    cursor.close()
    con.close()

    return table_list


def show_table_columns(database_name: str, table_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db=database_name)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show full columns from %s"
    cursor.execute(sql % table_name)
    column_list = cursor.fetchall()

    cursor.close()
    con.close()

    return column_list


def select_table_data(database_name: str, table_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db=database_name)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from %s"
    cursor.execute(sql % table_name)
    data_list = cursor.fetchall()

    cursor.close()
    con.close()

    return data_list


if __name__ == '__main__':
    show_database()
    # show_tables("bili")
    # show_table_columns("bili", "up")
    # select_table_data("bili", "up")

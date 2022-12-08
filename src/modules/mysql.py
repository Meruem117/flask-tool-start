import pymysql


def show_table_columns(table_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db="bili")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "show full columns from %s"
    cursor.execute(sql % table_name)
    columns = cursor.fetchall()

    cursor.close()
    con.close()

    return columns


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
    describe_table("up")
    # select_table_data("up")

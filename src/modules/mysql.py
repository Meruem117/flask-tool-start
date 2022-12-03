import pymysql


def select_table_data(table_name: str):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="abc123", charset="utf8", db="bili")
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from %s"
    cursor.execute(sql % table_name)
    data_list = cursor.fetchall()

    cursor.close()
    con.close()

    return data_list


if __name__ == '__main__':
    select_table_data("up")

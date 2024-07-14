import time
import sqlite3
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, title, price,  text, url):
        try:
            self.__cur.execute("SELECT COUNT() as `count` FROM posts WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Статья с таким url уже существует")
                return False


            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES (NULL,?, ?, ?, ?, ?)", (title, price, text, url, tm,))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return True



    def get_post(self, alias):
        try:
            self.__cur.execute(f"SELECT title, price, text FROM posts WHERE url='{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса в БД " + str(e))

        return False, False, False

    def get_posts_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, price, text, url  FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курсов из БД " + str(e))

        return []















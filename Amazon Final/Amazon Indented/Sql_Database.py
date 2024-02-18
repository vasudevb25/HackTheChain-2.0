import mysql.connector as mysql
import csv

sql = mysql.connect(user="root", host="localhost", password="Arduino1")
cursor = sql.cursor()
f = open("Sql_Database.csv", "r")


def checkdatabase():
    cursor.execute("show databases")
    m = cursor.fetchall()
    if ("amazon",) not in m:
        cursor.execute("create database amazon")
        cursor.execute("use amazon")
        cursor.execute("Create Table Users_List(user_id integer auto_increment primary key,name varchar(30),password varchar(1000),email varchar(100) unique,shopowner integer default 0,admin integer default 0,history varchar(1000) default '[]')")
        cursor.execute("Create Table bannedusers(email varchar(100) primary key)")
        cursor.execute("insert Into Users_List(name,password,email,shopowner,admin) values('elza','1425^193 107^-102 94^-201 87^182 101^-141 117^131 -1090^-103 970^103','admin101@admin1',1,1)")
        cursor.execute("Create Table total_items(id  integer auto_increment primary key,item varchar(1000),sellerid integer,category varchar(1000),sub_category varchar(1000),stock integer default 0,cost integer default 0,description varchar(1000),keyword varchar(1000),banned integer default 0,review varchar(2000) not null default '[]')")
        re = csv.reader(f)
        for g in re:
            if g[0] != "item":
                item = g[0]
                seller = int(g[1])
                cat = g[2]
                subc = g[3]
                stock = int(g[4])
                cost = int(g[5])
                des = g[6]
                key = g[7]
                ban = g[8]
                cursor.execute("insert into total_items (item,sellerid,category,sub_category,stock,cost,description,keyword,banned) values('{}',{},'{}','{}',{},{},'{}','{}',{})".format(item, seller, cat, subc, stock, cost, des, key, ban))
                sql.commit()
checkdatabase()

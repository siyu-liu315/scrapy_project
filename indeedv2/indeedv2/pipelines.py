# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class Indeedv2Pipeline:
    def __init__(self):
        self.connect_sqlite()

    def connect_sqlite(self):
        self.conn = sqlite3.connect("indeedv2.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""create table if not exists indeed_v2(
                         time date,
                         title text,
                         location text,
                         company text,
                         jd text,
                         url text,
                         primary key(title, location, company))""")


    def process_item(self, item, spider):
        self.store_date(item)
        print("Done :" +item['title'])
        return item

    def store_date(self,item):
        self.cur.execute("""insert or ignore into indeed_v2 values(?,?,?,?,?,?)""",(
            item['date'],
            item['title'],
            item['location'],
            item['company'],
            item['jd'],
            item['url']
        ))

        self.conn.commit()

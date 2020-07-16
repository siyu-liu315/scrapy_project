# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3


class IndeedPipeline:
    def __init__(self):
        self.open_connection()

    def open_connection(self):
        self.conn = sqlite3.connect("indeed.db")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS indeed 
                            (title text, 
                            company text,
                            jd text, 
                            address text,
                            url text,
                            primary key(title, company, address))""")

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline : " + item['title'])
        return item

    def store_db(self,item):
        self.curr.execute("""INSERT OR IGNORE INTO indeed VALUES(?,?,?,?,?)""",(
            item['title'],
            item['company'],
            item['description'],
            item['address'],
            item['url']


        ))
        self.conn.commit()


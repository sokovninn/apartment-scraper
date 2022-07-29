from sqlalchemy import create_engine
import scrapy
import json

db_name = 'sreality_db'
db_user = 'sokovninn'
db_pass = 'sreality_db'
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


class FlatSpider(scrapy.Spider):
    name = "flats"

    def start_requests(self):
        db.execute("TRUNCATE TABLE flats")
        url = 'https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&locality_country_id=10001&per_page=500'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        estates = json.loads(response.text)["_embedded"]["estates"]
        for estate in estates:
            name = estate["name"]
            image_url = estate["_links"]["image_middle2"][0]["href"]
            print(name)
            print(image_url)

            db.execute("INSERT INTO flats (title,imageurl) "+\
            	"VALUES ("+\
            	"'" + name + "'," + \
            	"'" + image_url + "');")

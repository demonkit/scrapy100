# Scrapy settings for scrapy100 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy100'

SPIDER_MODULES = ['scrapy100.spiders']
NEWSPIDER_MODULE = 'scrapy100.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy100 (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['scrapy100.pipelines.Scrapy100Pipeline']


DB_DRIVERNAME = 'mysql'
DB_HOST = ''
DB_PORT = 3306
DB_USERNAME = 'root'
DB_PASSWORD = '....'
DB_NAME = 'scrapy100'
DB_CHARSET = 'utf8'


DB_DIALECT = "%s://%s:%s@%s:%s/%s?charset=%s" % (
    DB_DRIVERNAME,
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_CHARSET,
)

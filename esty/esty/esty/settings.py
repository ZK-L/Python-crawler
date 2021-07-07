# Scrapy settings for esty project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'esty'

SPIDER_MODULES = ['esty.spiders']
NEWSPIDER_MODULE = 'esty.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'esty (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
  'Cookie':'uaid=RsyZML55lXVpaaL5rrfDeTuqwOpjZACChKcKdjC6Wqk0MTNFyUrJqNAyo8oz36yi2NDMOzy0IN0l1yIg3d3cMigvRamWAQA.; user_prefs=9dr1ZmETaUYjVPWXn1BhdvfkjeFjZACChKcKdjA6Wskx1EVJJ680J0dHKTVP191JSQcoBBUxglC4iFgGAA..; fve=1625628734.0; utm_lps=google__cpc; _gcl_au=1.1.1456660858.1625628736; _ga=GA1.2.370309823.1625628736; _gid=GA1.2.2128795574.1625628736; ua=531227642bc86f3b5fd7103a0c0b4fd6; _gcl_aw=GCL.1625628737.CjwKCAjw_o-HBhAsEiwANqYhp3j5OoMxVBT00rVIaH9MLrjkn4J1c5jnkeguAypZzkfLIzb_pWY3CBoCruQQAvD_BwE; _gac_UA-2409779-1=1.1625628737.CjwKCAjw_o-HBhAsEiwANqYhp3j5OoMxVBT00rVIaH9MLrjkn4J1c5jnkeguAypZzkfLIzb_pWY3CBoCruQQAvD_BwE; ken_gclid=CjwKCAjw_o-HBhAsEiwANqYhp3j5OoMxVBT00rVIaH9MLrjkn4J1c5jnkeguAypZzkfLIzb_pWY3CBoCruQQAvD_BwE; _pin_unauth=dWlkPU5tRmxPREkxTmpjdE1qa3haaTAwTm1Wa0xUbG1OVEF0TURBeU9ERmlaR1prTkRoaQ; search_options={\"prev_search_term\":\"earring\",\"item_language\":null,\"language_carousel\":null}; last_browse_page=https%3A%2F%2Fwww.etsy.com%2Fau%2Fshop%2FLuckyJewUS; _uetsid=ed845f90ded311eb8406d1634c8c3b7e; _uetvid=ed848160ded311eba324e99b83005967; QSI_HistorySession=https%3A%2F%2Fwww.etsy.com%2Fau%2Fsearch%3Fq%3Dearring%26page%3D1~1625633035116%7Chttps%3A%2F%2Fwww.etsy.com%2Flisting%2F816387372%2Fcartilage-hoop-nose-hoop-tragus-hoop%3Fga_order%3Dmost_relevant%26ga_search_type%3Dall%26ga_view_type%3Dgallery%26ga_search_query%3Dearring%26ref%3Dsr_gallery-1-1%26organic_search_click%3D1%26pro%3D1%26frs%3D1~1625633080988; pla_spr=1',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'esty.middlewares.EstySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'esty.middlewares.EstyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'esty.pipelines.EstyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

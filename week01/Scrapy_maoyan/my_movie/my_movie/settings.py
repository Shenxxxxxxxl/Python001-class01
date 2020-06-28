# Scrapy settings for my_movie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'my_movie'

SPIDER_MODULES = ['my_movie.spiders']
NEWSPIDER_MODULE = 'my_movie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = ''

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
# DEFAULT_REQUEST_HEADERS = {
#    'Content-Type': 'text/plain; charset=UTF-8',
#     'Origin': 'https://maoyan.com',
#     'Referer': 'https://maoyan.com/films?showType=3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
#     'Cookie': 'uuid_n_v=v1; uuid=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; mojo-uuid=5626779d6b188ad9cb357370abebe4a6; _lxsdk_cuid=172f4a90b2ac8-08c40deb6c77f7-f7d123e-144000-172f4a90b2ac8; _lxsdk=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; _csrf=ab509b8b2c599bd493ff3148994b5fe53475d33ee77fe3f17b87c1afeefe020f; mojo-session-id={"id":"21e8156aec037c18c3de76bf5294b379","time":1593357315508}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593272389,1593273208,1593349783,1593357316; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593357548; __mta=208974381.1593242618761.1593357536653.1593357548961.14; mojo-trace-id=7; _lxsdk_s=172fb7f2a42-ca9-00e-972%7C%7C11'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'my_movie.middlewares.MyMovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html\

RANDOM_UA_TYPE = 'random'

DOWNLOADER_MIDDLEWARES = {
    'my_movie.customMiddleware.CustomerUserAgent':10,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
#    'my_movie.middlewares.MyMovieDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'my_movie.pipelines.MyMoviePipeline': 300,
}

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

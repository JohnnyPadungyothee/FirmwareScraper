# Scrapy settings for firmware project

BOT_NAME = 'firmware'

SPIDER_MODULES = ['firmware.spiders']
NEWSPIDER_MODULE = 'firmware.spiders'

FILES_STORE = 'firmware_files/'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

#increased timeout from 320 to 420
DOWNLOAD_TIMEOUT = 420

#increased size from 1024MB default to 2GB, in bytes
DOWNLOAD_MAXSIZE = 2147483648
#increase size from 32MB default to 1GB, in bytes
DOWNLOAD_WARNSIZE = 1073741824

#halved default values to get clean shutdown for avm_gpl
#CONCURRENT_ITEMS = 50
#CONCURRENT_REQUESTS = 8
#CONCURRENT_REQUESTS_PER_DOMAIN = 4

LOG_LEVEL = 'DEBUG'

FTP_USER = 'anonymous'
FTP_PASSWORD = 'guest'

DOWNLOAD_HANDLERS = {
    'ftp': 'firmware.handlers.FTPHandler'
}

DOWNLOADER_MIDDLEWARES = {
    'firmware.middlewares.FirmwareDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
    'firmware.pipelines.HpPipeline': 300,
    'firmware.pipelines.AsusPipeline': 300,
    'firmware.pipelines.AvmPipeline': 1,
    'firmware.pipelines.LinksysPipeline': 1,
    
    #'scrapy.pipelines.files.FilesPipeline': 1,
}

# Enable to run with Selenium. Set to the driver executable path
SELENIUM_DRIVER_EXECUTABLE_PATH = '/usr/local/bin/geckodriver'
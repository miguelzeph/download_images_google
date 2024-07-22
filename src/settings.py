from klein_config import get_config
import logging

config = get_config()

####### Driver Settings ########
DRIVER_PATH = config.get("browser_driver.path")
DOWNLOAD_IMAGE_PATH = config.get("browser_driver.download_image_path")

####### Google Settings ########
GOOGLE_IMAGE_URL = config.get("google.image_url")
GOOGLE_IMAGE_CLASS = config.get("google.image_class")

####### User Agent ########
usr_agent = {
    "User-Agent": config.get("usr_agent.user-agent"),
    "Accept": config.get("usr_agent.accept"),
    "Accept-Charset": config.get("usr_agent.accept-charset"),
    "Accept-Encoding": config.get("usr_agent.accept-encoding"),
    "Accept-Language": config.get("usr_agent.accept-language"),
    "Connection": config.get("usr_agent.connection")
}

######### Logger ##########

logging.basicConfig(
    level=config.get("logger.level"),
    handlers=[
        logging.StreamHandler(),
    ],
)

def get_logger(module_name: str) -> logging.Logger:
    """Get a logger instance for the specified module.

    This function initializes a logger for the specified module name and returns
    the logger instance. The logger can be used to output log messages to various
    destinations, such as the console, files, or other handlers configured in
    the logging system.
    """
    return logging.getLogger(module_name)

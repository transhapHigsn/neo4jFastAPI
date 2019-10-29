import os
import io

from configparser import ConfigParser
from functools import lru_cache


CONF_FILES = {
	'dev': 'dev.ini'
}


@lru_cache(maxsize=None)
def read_config_file(filename):
	config = ConfigParser()
	config_filepath = os.path.join(os.path.dirname(__file__), filename)
	config.read(config_filepath)
	return config


@lru_cache(maxsize=None)
def get_config(section, key):
	env = os.environ.get('ENV',  'dev')
	config_file = CONF_FILES[env]
	config = read_config_file(config_file)
	return config[section][key]


def load_config_file():
	env = os.environ.get('ENV',  'dev')
	config_file = CONF_FILES[env]
	read_config_file(config_file)
	return
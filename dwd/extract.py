"""
File extractor classes
Encapsulate the location, retrieval and caching of file based online data
"""
import os
import logging
import requests
from io import BytesIO

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class extractor:
    """
    Generic url file extractor
    """

    def __init__(self, base_url):
        logger.debug('generic file extractor instanciated')
        self.__base_url = base_url
        self.__files = dict()

    def __get_url(self, filename):
        return os.path.join(self.__base_url, filename)

    def __download_file(self, filename):
        try:
            self.__files[filename] = requests.get(self.__get_url(filename)).content
        except requests.exceptions.RequestException as e:
            logger.error (f'failed to download {filename}')
            raise SystemExit(e)

    def _get_file(self, filename):
        if filename not in self.__files:
            logger.info(f'downloading {filename}')
            self.__download_file(filename)
        return self.__files[filename]

class dwd_extractor(extractor):
    """
    Specific Deutscher Wetterdienst (dwd) file extractor
    """

    BASE_URL = 'https://tinyurl.com/54puhkrx'
    BASE_FILENAME = 'regional_averages_tm_{}.txt'

    def __init__(self):
        super().__init__(self.BASE_URL)
        self.__filenames = { month: self.BASE_FILENAME.format(str(month).zfill(2)) for month in range(1,13) }

    def get_file_for_month(self, month):
        return BytesIO(self._get_file(self.__filenames[month]))
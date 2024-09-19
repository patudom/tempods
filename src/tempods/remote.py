from cosmicds.utils import CDSJSONEncoder
from contextlib import closing
from io import BytesIO
import json
from astropy.io import fits
from cosmicds.remote import BaseAPI
from cosmicds.logger import setup_logger
from typing import List

logger = setup_logger("API")


class LocalAPI(BaseAPI):
    """
    This class would interact with the CDS API to load data into the project state.
    """

    pass


LOCAL_API = LocalAPI()

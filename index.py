from __future__ import print_function
from crhelper import CfnResource
import logging

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120, ssl_verify=None)

@helper.create
def create(event, context):
    logger.info("Got Create")

@helper.update
def update(event, context):
    logger.info("Got Update")

@helper.delete
def delete(event, context):
    logger.info("Got Delete")

def handler(event, context):
    helper(event, context)

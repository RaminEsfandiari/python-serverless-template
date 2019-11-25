from aws_lambda_decorators import cors, log, response_body_as_json
from src.common import hello_func
from src.logger import get_logger


LOGGER = get_logger(__name__)


@cors()
@log(parameters=True, response=True)
@response_body_as_json
def handler(event, context):  # pylint:disable=unused-argument
    LOGGER.info("Some info message")
    return {
        "statusCode": 200,
        "body": hello_func("a_lambda")
    }

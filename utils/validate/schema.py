import allure
from jsonschema import validate
from loguru import logger


@allure.step('Validating schema')
def validate_schema(instance: dict, schema: dict) -> None:
    logger.debug(f"Comparing actual {instance} response with expected {schema}")
    validate(instance=instance, schema=schema)

from fastapi import Depends
from services.ecwid import EcwidClient, set_selected_environment
from models.environment import Environment, EnvironmentHeader


def use_environment(
    environment: EnvironmentHeader = Environment.production,
) -> Environment:
    set_selected_environment(environment)
    return environment


def get_ecwid_client(
    environment: Environment = Depends(use_environment),
) -> EcwidClient:
    return EcwidClient(environment)

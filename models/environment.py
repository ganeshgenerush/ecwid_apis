from enum import Enum
from typing import Annotated

from fastapi import Header


class Environment(str, Enum):
    test = "test"
    production = "production"


EnvironmentHeader = Annotated[
    Environment,
    Header(
        alias="environment",
        description="Choose which Ecwid store this request should use.",
    ),
]

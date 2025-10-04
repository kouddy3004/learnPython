from pydantic import BaseModel
from typing import List

class TestCase(BaseModel):
    id: str
    scenario: str
    steps: List[str]
    expected_result: str
    type: str

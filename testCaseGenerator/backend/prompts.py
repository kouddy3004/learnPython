TESTCASE_PROMPT = """
You are a QA engineer. Generate **functional test cases** for the requirement:

Requirement: "{requirement}"

Rules:
- Provide both POSITIVE and NEGATIVE test cases.
- Output must be strictly valid JSON array.
- Each test case should include:
  - id (TC### format)
  - scenario
  - steps (list of steps)
  - expected_result
  - type (positive or negative)
"""

from fastapi import FastAPI
from pydantic import BaseModel
import openai,os
import json
from prompts import TESTCASE_PROMPT
import openpyxl
from models import TestCase

app = FastAPI()


class Requirement(BaseModel):
    text: str


@app.post("/generate_testcases")
def generate_testcases(req: Requirement):
    prompt = TESTCASE_PROMPT.format(requirement=req.text)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message["content"]

    try:
        testcases = json.loads(content)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned from LLM", "raw": content}

    return {"testcases": testcases}


# ... existing endpoints ...

@app.post("/export_excel")
def export_excel(testcases: list[TestCase]):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    ws.append(["ID", "Scenario", "Steps", "Expected Result", "Type"])

    for tc in testcases:
        steps_str = "\n".join(tc.steps)
        ws.append([tc.id, tc.scenario, steps_str, tc.expected_result, tc.type])

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    wb.save(tmp.name)
    tmp.close()

    response = FileResponse(
        path=tmp.name,
        filename="testcases.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    @response.call_on_close
    def cleanup():
        os.unlink(tmp.name)

    return response


@app.post("/export_csv")
def export_csv(testcases: list[TestCase]):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", newline="")
    writer = csv.writer(tmp)

    # Header
    writer.writerow(["ID", "Scenario", "Steps", "Expected Result", "Type"])

    # Rows
    for tc in testcases:
        steps_str = " | ".join(tc.steps)
        writer.writerow([tc.id, tc.scenario, steps_str, tc.expected_result, tc.type])

    tmp.close()

    response = FileResponse(
        path=tmp.name,
        filename="testcases.csv",
        media_type="text/csv"
    )

    @response.call_on_close
    def cleanup():
        os.unlink(tmp.name)

    return response

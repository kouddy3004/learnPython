# FastAPI Backend Snippet: Serving Test Reports and Artifacts

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from typing import List, Dict, Any, Optional
import os
import json

router = APIRouter()


# --- Pydantic Models for Output Structure (Simplified for routing logic) ---
# NOTE: These models reflect the required content for the final report.

class TestArtifacts(Dict[str, str]):
    """Represents the required step-level artifacts paths."""
    screenshot_path: Optional[str] = None
    dom_snapshot_path: Optional[str] = None
    console_log_path: Optional[str] = None
    network_capture_path: Optional[str] = None


class TestResult(Dict[str, Any]):
    """Represents the validated output for a single test."""
    verdict: str
    evidence: TestArtifacts
    reproducibility_stats: float
    triage_notes: str


class FinalReport(Dict[str, Any]):
    """The comprehensive final report structure, which must be in JSON format."""
    run_id: str
    execution_timestamp: str
    total_tests_executed: int
    results: List[TestResult]  # Results from the 10 selected tests


# --- Placeholder Report Storage and Artifact Directory Setup ---

# In a real project, this would be a database connection.
# noinspection PyTypeChecker
REPORT_DATABASE: Dict[str, FinalReport] = {}
ARTIFACTS_DIR = "test_artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# Simulate a completed report that the AnalyzerAgent would produce
SAMPLE_REPORT_ID = "run_demo_001"
# noinspection PyTypeChecker
REPORT_DATABASE[SAMPLE_REPORT_ID] = {
    "run_id": SAMPLE_REPORT_ID,
    "execution_timestamp": "2024-05-15T12:00:00Z",
    "total_tests_executed": 10,  # Selected top 10 tests
    "results": [
        {
            "verdict": "PASS",
            "evidence": {
                # These paths link directly to the artifact serving endpoint
                "screenshot_path": f"{ARTIFACTS_DIR}/{SAMPLE_REPORT_ID}/test_1/step_1.png",
                "dom_snapshot_path": f"{ARTIFACTS_DIR}/{SAMPLE_REPORT_ID}/test_1/step_1.html",
            },
            "reproducibility_stats": 0.95,
            "triage_notes": "Game logic path confirmed correct."
        },
        {
            "verdict": "FAIL",
            "evidence": {
                "screenshot_path": f"{ARTIFACTS_DIR}/{SAMPLE_REPORT_ID}/test_5/step_3_failure.png",
                "console_log_path": f"{ARTIFACTS_DIR}/{SAMPLE_REPORT_ID}/test_5/console.log",
            },
            "reproducibility_stats": 0.75,
            "triage_notes": "Inputting negative numbers crashed the game state."
        }
        # ... 8 more results processed by the AnalyzerAgent ...
    ]
}


# --- Utility to create placeholder files for demo ---
def create_placeholder_artifact(file_path: str):
    """Ensures a file exists so the FileResponse doesn't immediately fail."""
    full_path = file_path
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(f"Placeholder content for artifact: {file_path}")


# Initialize placeholder files corresponding to the sample report
for result in REPORT_DATABASE[SAMPLE_REPORT_ID]['results']:
    for path in result['evidence'].values():
        if path:
            create_placeholder_artifact(path)


# --- FastAPI Endpoints ---

@router.get("/reports/{run_id}", response_model=FinalReport, tags=["Reports"])
async def get_report(run_id: str):
    """
    Endpoint for the minimal UI to retrieve the final JSON report.
    """
    if run_id not in REPORT_DATABASE:
        raise HTTPException(status_code=404, detail=f"Report {run_id} not found.")

    # In a production system, you would load this from storage
    return REPORT_DATABASE[run_id]


@router.get("/artifacts/{artifact_path:path}", tags=["Reports"])
async def get_artifact(artifact_path: str):
    """
    Endpoint to serve captured step-level artifacts (screenshots, DOM, console logs, etc.).
    This supports the required demo of 'opening a sample report with artifacts'.
    """
    full_path = artifact_path  # Assuming artifact_path already includes the directory

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail=f"Artifact not found at path: {artifact_path}")

    # Determine media type based on extension
    if full_path.endswith('.png'):
        media_type = 'image/png'
    elif full_path.endswith('.html'):
        media_type = 'text/html'
    elif full_path.endswith('.log'):
        media_type = 'text/plain'
    else:
        media_type = 'application/octet-stream'

    return FileResponse(full_path, media_type=media_type)

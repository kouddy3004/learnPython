Multi-Agent Game Tester Proof of Concept (POC)

1. Project Objective and Overview
   This repository contains the Proof of Concept (POC) for a Multi-Agent Game Tester system
   . The primary objective is to build a working, runnable system within a 5-day limit
   .
   The system is designed to automatically test a specific web number/math puzzle game (target
   game: https://play.ezygamers.com/)
   .
   Key System Capabilities
   The agent system is built to handle the full testing lifecycle:
   • Planning: Uses LangChain to generate at least 20 candidate test cases (PlannerAgent)
   .
   • Ranking: Ranks candidates with a RankerAgent and automatically selects the top 10 for execution
   .
   • Execution: Executes the selected test cases using multiple ExecutorAgents coordinated by an OrchestratorAgent
   .
   • Artifact Capture: Captures crucial step-level artifacts, including screenshots, DOM snapshots, console logs, and
   network captures
   .
   • Validation: Validates results using an AnalyzerAgent which performs repeat and cross-agent validations
   .
   • Reporting: Produces a final report (JSON) containing verdicts, evidence, reproducibility stats, and triage notes
   .
2. Technology Stack
   • Backend Framework: FastAPI (The backend must be FastAPI)
   .
   • Planning/Agent Orchestration: LangChain
   .
   • Web Interaction: (e.g., Selenium or Playwright) for ExecutorAgents to interact with the target game.
3. Installation and Setup
   Prerequisites
   • Python 3.x
   • A package manager (e.g., pip)
   Setup Steps
   1. Clone the Repository:
      2. Install Dependencies: Install all required libraries, including FastAPI and LangChain:
      3. Run the Backend Server: The system uses main.py to launch the FastAPI application:
      4. (The server should start running, typically at http://127.0.0.1:8000).
      4. Usage and Workflow
         The system is designed to be interacted with via the minimal UI provided in the ui/ folder, which triggers the three
         main phases of the multi-agent workflow:
         Step 1: Trigger Planning
            1. Access the minimal UI (ui/index.html) in your browser.
            2. Click the "Trigger Planning" button (which sends a request to /api/v1/plan).
            3. The PlannerAgent generates 20+ tests
               , and the RankerAgent selects the top 10
               .
            4. The API returns a unique job_id.

         Step 2: Initiate Execution
            1. Input the received job_id into the execution section of the minimal UI.
            2. Click the "Start Execution" button (which sends a request to /api/v1/execute/{job_id}).
            3. The OrchestratorAgent coordinates the ExecutorAgents to run the top 10 tests
               .
            4. Artifacts (screenshots, logs, etc.) are captured at the step level
               .
            5. The AnalyzerAgent performs validation using repeat and cross-agent checks
               .
            6. Upon completion, the execution endpoint returns the final report_id.
   
         Step 3: View Report
            1. Input the received report_id into the report viewer section of the minimal UI.
            2. Click "View Report" (which queries /api/v1/report/{report_id}).
            3. The system serves the final report (JSON)
               , which includes verdicts, evidence links, reproducibility stats, and triage notes.
   5. Project Structure Summary
      The repository is organized to cleanly separate the core backend logic from the UI and outputs:   
        game-tester-poc/
            ??? main.py # FastAPI Server Launcher
            ??? requirements.txt # Dependencies (FastAPI, LangChain, etc.)
            ??? ui/ # Minimal UI (HTML, CSS, JS)
            ??? app/
            ??? agents/ # Implementation of Planner, Ranker, Orchestrator, Executor, Analyzer
            ??? api/ # FastAPI route handlers
            ??? data/
            ??? artifacts/ # Storage for captured artifacts (screenshots, logs, etc.) [3]
            ??? reports/ # Storage for final JSON reports [3]

    6. Deliverables
        The following two items are required for the final evaluation:
        1. Public GitHub link with the complete working repository .
       2. Short demo video (screen capture) showing: plan generation, execution (top 10 runs mentioned, or top 3 quick demo),
          and opening a sample report that includes artifacts              .
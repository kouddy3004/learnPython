import { useState } from "preact/hooks";
import { generateTestcases, exportExcel, exportCSV } from "./api";

export default function App() {
  const [req, setReq] = useState("");
  const [cases, setCases] = useState([]);
  const [filter, setFilter] = useState("all");

  const handleSubmit = async () => {
    const data = await generateTestcases(req);
    if (data.testcases) {
      setCases(data.testcases);
    }
  };

  const handleExportExcel = async () => {
    if (cases.length === 0) return alert("No test cases to export!");
    await exportExcel(filteredCases);
  };

  const handleExportCSV = async () => {
    if (cases.length === 0) return alert("No test cases to export!");
    await exportCSV(filteredCases);
  };

  // Apply filter
  const filteredCases =
    filter === "all" ? cases : cases.filter((tc) => tc.type === filter);

  return (
    <div class="container">
      <h1>LLM Test Case Generator</h1>

      <textarea
        value={req}
        onInput={(e) => setReq(e.target.value)}
        placeholder="Enter your requirement here..."
      />

      <button onClick={handleSubmit}>Generate</button>

      <div class="actions">
        <button onClick={handleExportExcel} disabled={filteredCases.length === 0}>
          Export to Excel
        </button>
        <button onClick={handleExportCSV} disabled={filteredCases.length === 0}>
          Export to CSV
        </button>

        <select value={filter} onChange={(e) => setFilter(e.target.value)}>
          <option value="all">All</option>
          <option value="positive">Positive</option>
          <option value="negative">Negative</option>
        </select>
      </div>

      {filteredCases.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Scenario</th>
              <th>Steps</th>
              <th>Expected Result</th>
              <th>Type</th>
            </tr>
          </thead>
          <tbody>
            {filteredCases.map((tc) => (
              <tr key={tc.id}>
                <td>{tc.id}</td>
                <td>{tc.scenario}</td>
                <td>
                  <ul>
                    {tc.steps.map((s, i) => (
                      <li key={i}>{s}</li>
                    ))}
                  </ul>
                </td>
                <td>{tc.expected_result}</td>
                <td>{tc.type}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

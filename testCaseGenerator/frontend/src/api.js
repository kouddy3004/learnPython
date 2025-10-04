export async function generateTestcases(requirement) {
  const res = await fetch("http://localhost:8000/generate_testcases", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: requirement }),
  });
  return await res.json();
}

async function downloadFile(endpoint, filename, data) {
  const res = await fetch(`http://localhost:8000/${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    alert(`Failed to export ${filename}`);
    return;
  }

  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  window.URL.revokeObjectURL(url);
}

export async function exportExcel(testcases) {
  await downloadFile("export_excel", "testcases.xlsx", testcases);
}

export async function exportCSV(testcases) {
  await downloadFile("export_csv", "testcases.csv", testcases);
}

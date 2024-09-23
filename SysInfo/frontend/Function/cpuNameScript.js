async function fetchCpuName() {
  try {
    const response = await fetch("http://127.0.0.1:5001/cpu-name");
    if (!response.ok) {
      throw new Error("Unable to fetch CPU name.");
    }
    const data = await response.json();

    const cpuNameDiv = document.getElementById("cpu-name-info");
    cpuNameDiv.innerHTML = `<strong>CPU Name:</strong> ${data.cpu_name}`;
  } catch (error) {
    const cpuNameDiv = document.getElementById("cpu-name-info");
    cpuNameDiv.innerHTML = `<div class="error">${error.message}</div>`;
  }
}
document.addEventListener("DOMContentLoaded", fetchCpuName());

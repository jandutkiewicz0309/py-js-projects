async function fetchDiskData() {
  try {
    const response = await fetch("http://127.0.0.1:5001/disk");
    const data = await response.json();

    const cpuInfoDiv = document.getElementById("disk-info");
    cpuInfoDiv.innerHTML = "";

    const memoryInfoDiv = document.getElementById("disk-info");
    memoryInfoDiv.innerHTML = `
        <strong>Total Memory:</strong> ${data.total} <br>
        <strong>Used Memory:</strong> ${data.used} <br>
        <strong>Free Memory:</strong> ${data.free} <br>
        `;
  } catch (error) {
    console.error("Error fetching disk data:", error);
  }
}

window.onload = setInterval(fetchDiskData(), 5000);

async function fetchMemoryData() {
  try {
    const response = await fetch("http://127.0.0.1:5001/memory");
    const data = await response.json();

    const memoryInfoDiv = document.getElementById("memory-info");
    memoryInfoDiv.innerHTML = `
        <strong>Total Memory:</strong> ${data.total} <br>
        <strong>Used Memory:</strong> ${data.used} <br>
        <strong>Free Memory:</strong> ${data.free} <br>
        <strong>Memory Usage:</strong> ${data.percent} <br>
      `;
  } catch (error) {
    console.error("Error fetching memory data:", error);
  }
}

window.onload = setInterval(fetchMemoryData(), 5000);

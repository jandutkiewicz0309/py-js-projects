async function fetchGpuData() {
  try {
    const response = await fetch("http://127.0.0.1:5001/gpu");
    if (!response.ok) {
      throw new Error("Unable to fetch GPU data.");
    }
    const data = await response.json();

    const gpuInfoDiv = document.getElementById("gpu-info");
    gpuInfoDiv.innerHTML = `
          <strong>GPU Usage:</strong> ${data.gpu_usage || "N/A"}<br>
          <strong>GPU Temperature:</strong> ${data.gpu_temperature || "N/A"}°C
        `;
  } catch (error) {
    const gpuInfoDiv = document.getElementById("gpu-info");
    gpuInfoDiv.innerHTML = `<div class="error">${error.message}</div>`;
  }
}

window.onload = fetchGpuData();

async function fetchCpuTemperature() {
  try {
    const response = await fetch("http://127.0.0.1:5001/cpu-temperature");
    if (!response.ok) {
      throw new Error(
        "Temperature sensors not available or CPU temperature not found."
      );
    }
    const data = await response.json();

    const temperatureInfoDiv = document.getElementById("temperature-info");
    temperatureInfoDiv.innerHTML = "";
    data.cpu_temperatures.forEach((temp) => {
      const tempDiv = document.createElement("div");
      tempDiv.classList.add("temperature");
      tempDiv.innerHTML = `
        <strong>${temp.sensor}:</strong> ${temp.temperature_celsius}°C
      `;
      temperatureInfoDiv.appendChild(tempDiv);
    });
  } catch (error) {
    const temperatureInfoDiv = document.getElementById("temperature-info");
    temperatureInfoDiv.innerHTML = `<div class="error">${error.message}</div>`;
  }
}

window.onload = setInterval(fetchCpuTemperature(), 5000);

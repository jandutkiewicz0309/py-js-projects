async function fetchCpuData() {
  try {
    const response = await fetch("http://127.0.0.1:5001/cpu");
    const data = await response.json();

    const cpuInfoDiv = document.getElementById("cpu-info");
    cpuInfoDiv.innerHTML = "";

    const physicalCoresDiv = document.createElement("div");
    physicalCoresDiv.innerHTML = "<h3>Physical Cores</h3>";
    data.physical_cores.forEach((core) => {
      const coreDiv = document.createElement("div");
      coreDiv.innerHTML = `<strong>Core ${core.core}:</strong> ${core.usage}% | Frequency: ${core.frequency} MHz`;
      physicalCoresDiv.appendChild(coreDiv);
    });
    cpuInfoDiv.appendChild(physicalCoresDiv);

    const logicalCoresDiv = document.createElement("div");
    logicalCoresDiv.innerHTML = "<h3>Logical Cores</h3>";
    data.logical_cores.forEach((core) => {
      const coreDiv = document.createElement("div");
      coreDiv.innerHTML = `<strong>Core ${core.core}:</strong> ${core.usage}% | Frequency: ${core.frequency} MHz`;
      logicalCoresDiv.appendChild(coreDiv);
    });
    cpuInfoDiv.appendChild(logicalCoresDiv);
  } catch (error) {
    console.error("Error fetching CPU data:", error);
  }
}

window.onload = setInterval(fetchCpuData(), 5000);

async function fetchMotherboardName() {
  try {
    const response = await fetch("http://127.0.0.1:5001/motherboard-name");
    if (!response.ok) {
      throw new Error("Unable to fetch motherboard name.");
    }
    const data = await response.json();

    const motherboardInfoDiv = document.getElementById("motherboard-info");
    motherboardInfoDiv.innerHTML = `<strong>Motherboard Name:</strong> ${data.motherboard_name}`;
  } catch (error) {
    const motherboardInfoDiv = document.getElementById("motherboard-info");
    motherboardInfoDiv.innerHTML = `<div class="error">${error.message}</div>`;
  }
}

window.onload = fetchMotherboardName();

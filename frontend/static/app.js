document.getElementById("voting-form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const votes = document.getElementById("votes").value;
  const messages = document.getElementById("messages");
  const loadingGif = document.getElementById("loading-gif");

  messages.innerHTML = "";  // limpia antes de mostrar
  loadingGif.classList.remove("hidden"); // muestra el gif

  const res = await fetch("/votar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ votes: parseInt(votes) })
  });

  const data = await res.json();

  // Ocultar el gif apenas lleguen mensajes
  loadingGif.classList.add("hidden");

  if (data.logs && Array.isArray(data.logs)) {
    data.logs.forEach(msg => {
      const p = document.createElement("p");
      p.textContent = msg;
      messages.appendChild(p);
    });
  } else {
    messages.innerHTML += `<p>${data.mensaje}</p>`;
  }
});

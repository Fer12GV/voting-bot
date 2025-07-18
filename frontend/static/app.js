document.getElementById("voting-form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const votes = document.getElementById("votes").value;
  const messages = document.getElementById("messages");
  messages.innerHTML += `<p>🔁 Iniciando proceso de votación con ${votes} intento(s)...</p>`;

  const res = await fetch("/votar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ votes: parseInt(votes) })
  });

  const data = await res.json();
  messages.innerHTML += `<p>${data.mensaje}</p>`;
});

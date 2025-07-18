document.getElementById("voting-form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const votes = document.getElementById("votes").value;
  const messages = document.getElementById("messages");
  messages.innerHTML = "";  // limpia antes de mostrar

  const res = await fetch("/votar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ votes: parseInt(votes) })
  });

  const data = await res.json();

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

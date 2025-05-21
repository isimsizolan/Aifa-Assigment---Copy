const chatBox = document.getElementById("chat-box");

document.addEventListener("DOMContentLoaded", () => {
  const chatBox = document.getElementById("chat-box");
  const input = document.getElementById("user-input");

  window.sendMessage = async function () {
    const message = input.value;
    if (!message) return;

    chatBox.innerHTML += `<div><b>You:</b> ${message}</div>`;
    input.value = "";

    const res = await fetch("/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    console.log(data);
    chatBox.innerHTML += `<div><b>Bot:</b> ${data.response?.toString?.() || JSON.stringify(data.response)}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  };
});
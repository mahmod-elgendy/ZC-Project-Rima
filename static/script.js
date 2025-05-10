async function sendMessage() {
  const inputField = document.getElementById("user-input");
  const message = inputField.value;
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user-msg">${message}</div>`;

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: message }),
  });
  const data = await res.json();

  chatBox.innerHTML += `
    <div class="bot-msg">
      <img src="/static/images/rima.png" class="avatar" />
      <span>${data.answer}</span>
    </div>`;
  inputField.value = "";
}
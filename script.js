// script.js
window.Telegram.WebApp.ready();

// Get user data
const user = window.Telegram.WebApp.initDataUnsafe?.user || {};

// Display user name (if available)
document.body.insertAdjacentHTML(
  'afterbegin',
  `<p>Hello, ${user.first_name || 'User'}!</p>`
);

// Add event listener to send a message back to the bot
document.getElementById('sendMessageButton').addEventListener('click', () => {
    window.Telegram.WebApp.sendData("Hello from my web app!");
});

// Ensure the web app is ready
window.Telegram.WebApp.ready();

// Function to handle the submit button click
document.getElementById('submitButton').addEventListener('click', () => {
    // Get the values from the form
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const gender = document.querySelector('input[name="gender"]:checked')?.value || 'Not specified';

    // Display the user's information
    if (name && age && gender) {
        document.getElementById('userInfo').style.display = 'block';
        document.getElementById('userName').innerText = `Name: ${name}`;
        document.getElementById('userAge').innerText = `Age: ${age}`;
        document.getElementById('userGender').innerText = `Gender: ${gender}`;
    } else {
        alert('Please fill in all fields.');
    }
});

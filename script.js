/* Set the global font style to sans-serif */
body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #ffffff;
    color: #333;
    font-size: 16px;
}

/* Style the header */
h1 {
    text-align: center;
    color: #444;
    margin-top: 20px;
}

/* Style the form container */
.profile-form {
    width: 90%; /* Allows the form to take up 90% of the screen width */
    max-width: 500px; /* Sets an upper limit for the width on larger screens */
    margin: 20px auto; /* Centers the form horizontally and gives top/bottom space */
    background-color: #CEFBDA; /* Sets the background color to white */
    padding: 20px; /* Adds inner padding for the content */
    border-radius: 8px; /* Rounds the corners for a softer look */
}

.profile-form div {
    display: flex;
    align-items: center; /* Vertically aligns radio buttons/checkboxes with labels */
    gap: 8px; /* Adds space between radio button/checkbox and label */
    margin-bottom: 10px; /* Adds space between each option group */
}

.profile-form label {
    font-family: sans-serif; /* Applies a sans-serif font for readability */
}


/* Style form headings */
h2 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
}

/* Label and input styles */
label {
    font-weight: bold;
    margin-top: 10px;
    display: block;
}

input[type="radio"],
input[type="checkbox"] {
    margin-right: 5px;
}

/* Dropdown styles for skill levels */
select {
    margin-top: 10px;
    margin-bottom: 10px;
    width: 100%;
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Style the submit button */
button {
    display: inline-block;
    width: auto;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold; /* Make the text bold */
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 7px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}


button:hover {
    background-color: #0056b3;
}

/* User information display section */
#userInfo {
    max-width: 500px;
    margin: 20px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    color: #333;
}

#userInfo p {
    margin: 10px 0;
}

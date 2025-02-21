const express = require('express');
const { Client } = require('pg'); // PostgreSQL client

const app = express();
const port = 3000;

app.use(express.json()); // To parse JSON data from the request body

// Set up your PostgreSQL connection
const client = new Client({
    user: 'u74paoavmds30r',
    host: 'c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com',
    database: 'd196r0fv8p6tii',
    password: 'pf5baba4878a23ad2fa9729b32256b75aa27c1aa49e4fad94e6243afd15ddfae1',
    port: 5432,
    ssl: {
        rejectUnauthorized: false // This allows self-signed certificates
    }
    
});
client.connect();

app.post('/submit-profile', (req, res) => {
    console.log("Received request at /submit-profile");
    console.log("Request body:", req.body); // Log incoming request data

    const { chat_id, age, gender, sports, location } = req.body;

    if (!age || !gender || !sports || !location) {
        return res.status(400).json({ success: false, message: "Missing required fields" });
    }

    const query = 'INSERT INTO users (chat_id, age, gender, sports, location) VALUES ($1, $2, $3, $4, $5)';
    const values = [chat_id, age, gender, JSON.stringify(sports), location];

    client.query(query, values, (err, result) => {
        if (err) {
            console.error("Database error:", err);
            return res.status(500).json({ success: false, message: 'Database error', error: err.message });
        }

        console.log("Profile submitted successfully!");
        res.status(200).json({ success: true, message: 'Profile submitted successfully!' });
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

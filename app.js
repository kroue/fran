const express = require('express');
const connectToDatabase = require('./server/mongodb');

const app = express();

// Middleware
app.use(express.json());

// Routes
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// Connect to MongoDB and start the server
(async () => {
    try {
        await connectToDatabase();
        console.log('Backend is starting...');
        const PORT = process.env.PORT || 3000;
        app.listen(PORT, () => {
            console.log(`Server is running on port ${PORT}`);
        });
    } catch (error) {
        console.error('Error during backend startup:', error);
    }
})();
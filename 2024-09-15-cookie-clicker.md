---
layout: base
title: Cookie Clicker
hide: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        button {
            font-size: 18px;
            padding: 10px 20px;
            margin: 10px;
            cursor: pointer;
        }
        button:hover {
            background-color: #ddd;
        }
        .cookie {
            width: 300px; 
            height: auto; 
            display: block; 
            margin: 0 auto 20px auto; 
            border: 5px solid #000;  
        }
    </style>
</head>
<body>
    <div class="image">
        <img src="https://clipart-library.com/newhp/3-34513_cookies-clipart-transparent-background-cookies-clipart.png" alt="Cookie" class="cookie">
    </div>
    <div class="container">
        <h1>Cookie Clicker</h1>
        <div class="cookie-info">
            <p>Cookies: <span id="cookie-count">0</span></p>
            <p>Multiplier: <span id="multiplier">1</span></p>
        </div>
        <button id="click-button">Click for Cookies</button>
        <button id="multiplier-button">Apply Multiplier (requires 25 cookies)</button>
    </div>
    <script>
        let cookies = 0;
        let cookiesPerClick = 1;
        let multiplier = 1;
        const cookieCountElement = document.getElementById('cookie-count');
        const multiplierElement = document.getElementById('multiplier');
        const clickButton = document.getElementById('click-button');
        const multiplierButton = document.getElementById('multiplier-button');
        clickButton.addEventListener('click', () => {
            cookies += cookiesPerClick * multiplier;
            updateDisplay();
        });
        multiplierButton.addEventListener('click', () => {
            if (cookies >= 25) {
                cookies -= 25; 
                multiplier += 1; 
            } else {
                alert('You need at least 25 cookies to apply a multiplier. Keep playing! :)');
            }
            updateDisplay();
        });
        function updateDisplay() {
            cookieCountElement.textContent = cookies;
            multiplierElement.textContent = multiplier;
        }
        updateDisplay();
    </script>
</body>
</html>

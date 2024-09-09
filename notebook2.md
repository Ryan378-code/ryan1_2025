---
layout: base
title: MKath Jokes
description: Click the button below to see a random math joke. 
hide: false
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Math Joke</title>
</head>
<body>
    <p id="mathJoke">Click the button to see a random math joke!</p>
    <button
        onclick="generateJoke()"
        style="background: linear-gradient(to right, #00c6ff, #0072ff);
               padding: 15px 30px;
               font-size: 18px;
               color: white;
               border: none;
               border-radius: 20px;
               cursor: pointer;">
        Get a Math Joke
    </button>
    <script>
        var mathJokeList = [
            "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else.",
            "Why did the mathematician break up with his girlfriend? She had too many problems.",
            "How do you stay warm in a cold room? Go to the corner, it’s always 90 degrees.",
            "Why was the math book sad? It had too many problems.",
            "Why was the fraction apprehensive about marrying the decimal? Because he would have to convert.",
            "Why did the two fours skip lunch? They already eight.",
            "What is a math teacher’s favorite place in NYC? Times Square.",
            "Why was the student eating his math homework? Because his teacher said it was a piece of cake.",
            "What do you call a number that can't keep still? A roamin' numeral.",
            "Why was the obtuse triangle always so sad? Because it was never right."
        ];
        function generateJoke() {
            var randomIndex = Math.floor(Math.random() * mathJokeList.length);
            var selectedJoke = mathJokeList[randomIndex];
            document.getElementById("mathJoke").innerText = "Math Joke #" + (randomIndex + 1) + ": " + selectedJoke;
        }
    </script>
</body>
</html>

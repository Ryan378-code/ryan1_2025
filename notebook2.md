---
layout: base
title: Skittles Facts
description: Click the button below to see a random Skittles fact. 
hide: false
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skittles Facts</title>
</head>
<body>
    <p id="skittlesFact">Click the button to see something about Skittles!</p>
    <button
        onclick="generateFact()"
        style="background: linear-gradient(to right, #00c6ff, #0072ff);
               padding: 15px 30px;
               font-size: 18px;
               color: white;
               border: none;
               border-radius: 20px;
               cursor: pointer;">
        Get a Skittles Fact
    </button>
    <script>
        var skittlesFactList = [
            "Skittles were first produced in 1974 in the UK and were introduced to the United States in 1982.",
            "The sugar shell of Skittles is made from a combination of sugar, corn syrup, and hydrogenated palm kernel oil, giving them their distinct shiny appearance.",
            "In 2007, astronauts on the Space Shuttle Atlantis took Skittles to space as part of their food supplies!",
            "In 2013, the company changed the green Skittle from lime to green apple, sparking debates among fans!",
            "Over the years, Skittles has released numerous limited-edition flavors and varieties, such as Skittles Sour, Skittles Wild Berry, and even Skittles Gummies."
        ];
        function generateFact() {
            var randomIndex = Math.floor(Math.random() * skittlesFactList.length);
            var selectedFact = skittlesFactList[randomIndex];
            document.getElementById("skittlesFact").innerText = "Skittles Fact #" + (randomIndex + 1) + ": " + selectedFact;
        }
    </script>
</body>
</html>


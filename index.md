---
layout: base
title: Student Home 
description: Home Page
hide: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #ffffff;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }
        .subnav {
            background-color: hsl(204, 80%, 75%);
            padding: 10px;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .subnav button {
            background-color: #555;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
        }
        .subnav button:hover {
            background-color: #666;
        }
        .content {
            margin: 20px;
        }
        h1 {
            color: #ffffff;
        }
        p {
            margin: 10px 0;
        }
    </style>
</head>
<body>

    <div class="subnav">
        <button onclick="redirect()">Types of Skittles</button>
        <button onclick="oops()">Opinions on Original Skittles</button>
    </div>

    <div class="content">
        <div id="types">
            <h1>Types of Skittles (Ordered by Color):</h1>
            <p><strong>Red: Strawberry</strong> Insert text here.</p>
            <p><strong>Orange: Orange</strong> Insert text here.</p>
            <p><strong>Yellow: Lemon</strong> Insert text here.</p>
            <p><strong>Green: Lime</strong> Insert text here.</p>
            <p><strong>Purple: Grape</strong> Insert text here.</p>
        </div>
    </div>

    <div class="content"
        <div id ="opinions">
            <h1>My Opinions on Each of the Original Skittles Flavors:</h1>
            <p><strong>Red: Strawberry</strong> Insert text here.</p>
            <p><strong>Orange: Orange</strong> Insert text here.</p>
            <p><strong>Yellow: Lemon</strong> Insert text here.</p>
            <p><strong>Green: Lime</strong> Insert text here.</p>
            <p><strong>Purple: Grape</strong> Insert text here.</p>
        </div>

    <script>
        function redirect() {
            document.getElementById('types').scrollIntoView({ behavior: "smooth"});
        }
        function oops() {
            document.getElementById('oops').scrollIntoView({behavior:"smooth"});
        }
    </script>
</body>
</html>


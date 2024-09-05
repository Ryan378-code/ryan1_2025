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
            background-color: #333; 
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

<p>Information about Skittles below.</p>

<body>
    <div class="subnav">
        <button onclick="redirect()">Types of Skittles</button>
        <button onclick="oops()">Opinions on Original Skittles</button>
        <button onclick="more()">Other Types of Skittles</button>
    </div>
    <header id="color">
        <h1>Types of Skittles (Ordered by Color):</h1>
    </header>

    <div class="content">
        <div id="types">
            <p><strong>Red (Strawberry):</strong> Insert text here.</p>
            <p><strong>Orange (Orange):</strong> Insert text here.</p>
            <p><strong>Yellow (Lemon):</strong> Insert text here.</p>
            <p><strong>Green (Lime):</strong> Insert text here.</p>
            <p><strong>Purple (Grape):</strong> Insert text here.</p>
        </div>
    </div>

    <header id="header">
        <h1>My Opinions On Skittles Flavors:</h1>
    </header>

    <div class="content">
        <div id="opinions">
            <p><strong>Red (Strawberry):</strong> Insert text here.</p>
            <p><strong>Orange (Orange):</strong> Insert text here.</p>
            <p><strong>Yellow (Lemon):</strong> Insert text here.</p>
            <p><strong>Green (Lime):</strong> Insert text here.</p>
            <p><strong>Purple (Grape):</strong> Insert text here.</p>
        </div>
    </div>

    <header id="other">
        <h1>Other Types of Skittles</h1>
    </header>

    <div class="content">
        <div id="Other">
            <p><strong>Skittles Gummies:</strong> Insert text here.</p>
            <p><strong>Wild Berry:</strong> Insert text here.</p>
            <p><strong>Sour Skittles:</strong> Insert text here.</p>
            <p><strong>Brightside:</strong>Insert text here.</p>
        </div>
    </div>

    <script>
        function redirect() {
            document.getElementById('color').scrollIntoView({ behavior: "smooth" });
        }
        function oops() {
            document.getElementById('header').scrollIntoView({ behavior: "smooth" });
        }
        function more() {
            document.getElementById("Other").scrollintoView({behavior: "smooth"});
        }
        var types = document.getElementById('types')
            types.style.marginBottom ='10px'
        var opinions = document.getElementById('opinions')
            opinions.style.marginBottom = '10px'
        var Other = document.getElementById('Other')
            types.style.marginBottom = '10px'
    </script>
</body>
</html>

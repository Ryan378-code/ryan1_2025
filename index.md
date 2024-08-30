---
layout: base
title: Student Home 
description: Home Page
hide: true
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skittles Flavors</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .menu {
            display: flex;
            background-color: #f0f0f0;
            padding: 10px;
            border-bottom: 2px solid #ddd;
        }
        .menu button {
            background: none;
            border: none;
            padding: 10px;
            cursor: pointer;
            font-size: 16px;
        }
        .menu button:hover {
            background-color: #ddd;
        }
        .content {
            padding: 20px;
        }
        .content div {
            display: none;
        }
        .content div.active {
            display: block;
        }
    </style>
</head>
<body>

    <div class="menu">
        <button onclick="showContent('original')">Original Flavors</button>
        <button onclick="showContent('limited')">Limited Edition Flavors</button>
        <button onclick="showContent('international')">International Flavors</button>
    </div>

    <div class="content">
        <div id="original" class="active">
            <h2>Original Flavors</h2>
            <p>Skittles' original flavors include:</p>
            <ul>
                <li><strong>Strawberry:</strong> A sweet and fruity taste reminiscent of ripe strawberries.</li>
                <li><strong>Grape:</strong> A bold, juicy grape flavor that stands out.</li>
                <li><strong>Green Apple:</strong> A tangy, crisp apple flavor that is both refreshing and sweet.</li>
                <li><strong>Lemon:</strong> A zesty, citrusy taste that is sharp and invigorating.</li>
                <li><strong>Orange:</strong> A bright and fruity flavor that captures the essence of oranges.</li>
            </ul>
        </div>
        <div id="limited">
            <h2>Limited Edition Flavors</h2>
            <p>Skittles has released numerous limited edition flavors, including:</p>
            <ul>
                <li><strong>Skittles Wild Berry:</strong> A mix of berry flavors like Berry Punch, Strawberry, Melon Berry, Wild Cherry, and Raspberry.</li>
                <li><strong>Skittles Sour:</strong> Features sour versions of classic flavors like Sour Apple, Sour Cherry, Sour Grape, Sour Lemon, and Sour Orange.</li>
                <li><strong>Skittles Darkside:</strong> Includes mysterious flavors like Forbidden Fruit, Midnight Lime, Pomegranate, Blood Orange, and Dark Berry.</li>
            </ul>
        </div>
        <div id="international">
            <h2>International Flavors</h2>
            <p>Different countries offer unique Skittles flavors such as:</p>
            <ul>
                <li><strong>Skittles Tropical (Various Countries):</strong> Flavors include Banana Berry, Kiwi Lime, Mango Tangelo, Pineapple Passionfruit, and Straw-Bana.</li>
                <li><strong>Skittles Brazil (Brazil):</strong> Includes flavors like Guaraná, Açaí, Cashew, Mango, and Pineapple.</li>
                <li><strong>Skittles Japan (Japan):</strong> Offers unique flavors such as Wasabi, Sweet Corn, and Green Tea.</li>
            </ul>
        </div>
    </div>

    <script>
        function showContent(id) {
            const contents = document.querySelectorAll('.content div');
            contents.forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(id).classList.add('active');
        }
    </script>

</body>
</html>

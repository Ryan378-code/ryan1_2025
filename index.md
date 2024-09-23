---
layout: base
title: Ryan and Skittles 
description: Here you'll find information about me, my programming journey, and Skittles!
hide: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Calibri', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .submenu {
            background-color: lightgray;
            padding: 10px;
            margin: 10px 0;
        }
        .submenu a, .submenu button {
            display: block;
            color: rgb(0, 0, 0);
            padding: 10px;
            text-decoration: none;
            border: none;
            background: none;
            font-size: 18px;
            cursor: pointer;
        }
        .submenu a:hover, .submenu button:hover {
            background-color: #ddd;
            color: #000;
        }
        .mario {
            position: absolute;
            top: 20px;
            left: -150px; 
            width: 100px; 
            height: auto;
            animation: runAcross 10s linear infinite;
        }
        @keyframes runAcross {
            0% {
                left: -150px; 
            }
            100% {
                left: 100%; 
            }
        }
        .gum {
            width: 300px; 
            height: auto; 
            display: block; 
            margin-left: 10px; 
            border: 5px solid #9e7171;
        }
        .games {
            background-color: lightgray;
            padding: 10px;
            margin: 10px 0
        }
        .games a {
            display: block;
            color: rgb(0, 0, 0);
            padding: 10px;
            text-decoration: none;
        }
        button {
            font-size: 18px;
            padding: 10px 20px;
            margin: 10px;
            cursor: pointer;
            color: black; 
            background-color: transparent; 
            border: 1px solid black; 
        }
        button:hover {
            background-color: #ddd;
        }
    </style>
</head>
<body>
    <div>
        <p>The first button takes you to the official Skittles website. The other is a mystery. Click it and find out what's in it!</p>
    </div>
    <div>
        <button>This button doesn't do anything. :]</button>
    </div>
    <div class="submenu">
        <a href="https://www.skittles.com/">Skittles Website</a>
        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Mystery Button</a>
    </div>

    <p>Have fun exploring my pages!</p>
    <div class="gummies">
        <p>These are currently on my mind! I would love to have these right now!</p>
        <img src="https://www.skittles.com/cdn-cgi/image/width=472,height=472,f=auto,quality=90/sites/g/files/fnmzdf586/files/migrate-product-files/qb3lrole0uywupm6pzfl.png" alt="Gummy Skittles" class="gum">
    </div>

    <h1>Jupyter Notebook (Emoji!)</h1>
    <div class="submenu">
        <button><a href="https://github.com/Ryan378-code/ryan1_2025/blob/main/2024-09-15-jupyter-notebook-python.ipynb">Emoji Notebook (Hack #1)</a></button>
    </div>

    <h1>(Other) Notebooks</h1>
    <div class="submenu">
        <button><a href="notebook1.html">Notebook 1</a></button>
        <button><a href="notebook2.html">Notebook 2</a></button>
        <button><a href="notebook3.html">Notebook 3</a></button>
    </div>

    <div id="interesting">
        <h1>Games:</h1>
    </div>

    <div class="games">
        <a href="2024-09-15-cookie-clicker.html">Cookie Clicker</a>
        <a href="2024-9-16-binary-calculator.html">Binary Calculator</a>
        <a href="snake-game.html">Snake Game</a>
    </div>
    
    <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4ddabef1-8390-424a-a828-f61e4df3d499/daraj8q-744f0563-d3f2-4a25-98a7-377abba7dc7b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzRkZGFiZWYxLTgzOTAtNDI0YS1hODI4LWY2MWU0ZGYzZDQ5OVwvZGFyYWo4cS03NDRmMDU2My1kM2YyLTRhMjUtOThhNy0zNzdhYmJhN2RjN2IuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.KpbFWvWcQbuGNwF9TtupLcDKwLRFW8DAZLx404K5bAU" alt="Mario Running" class="mario">

    <table>
        <tr>
            <td><a href="{{site.baseurl}}/2024-9-22-python">Python Emojis</a></td>
        </tr>
    </table>
    

    <script src="https://utteranc.es/client.js"
        repo="Ryan378-code/ryan1_2025"
        issue-term="pathname"
        theme="github-dark"
        crossorigin="anonymous"
        async>
    </script>
    <script>
        var gummies = document.querySelector('.gummies');
        gummies.style.marginBottom = '20px';
    </script>
</body>
</html>

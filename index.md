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
            font-family: 'Calibri,' Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .navbar {
            background-color: #333;
            overflow: hidden;
        }
        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 17px;
        }
        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        .submenu {
            background-color: #444;
            padding: 10px;
        }
        .submenu a {
            display: block;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            font-size: 16px;
        }
        .submenu a:hover {
            background-color: #666;
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
    </style>
</head>
<body>
    <div class="submenu">
        <a href="navigation/skittles.html">Skittles</a>
        <a href="navigation/tools.html">Tools and Journey</a>
        <a href="http://127.0.0.1:4200/ryan1_2025/about/">About</a>
    </div>

    <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4ddabef1-8390-424a-a828-f61e4df3d499/daraj8q-744f0563-d3f2-4a25-98a7-377abba7dc7b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzRkZGFiZWYxLTgzOTAtNDI0YS1hODI4LWY2MWU0ZGYzZDQ5OVwvZGFyYWo4cS03NDRmMDU2My1kM2YyLTRhMjUtOThhNy0zNzdhYmJhN2RjN2IuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.KpbFWvWcQbuGNwF9TtupLcDKwLRFW8DAZLx404K5bAU" alt="Mario Running" class="mario">
</body>
</html>






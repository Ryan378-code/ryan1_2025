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
    <title>Submenu Example with Mario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            overflow-x: hidden; 
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
            display: none;
            position: absolute;
            background-color: #333;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .submenu a {
            float: none;
            color: white;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            text-align: left;
        }
        .submenu a:hover {
            background-color: #ddd;
            color: black;
        }
        .navbar .dropdown {
            float: left;
            overflow: hidden;
        }
        .navbar .dropdown:hover .submenu {
            display: block;
        }
        /* Mario animation */
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
    <div class="navbar">
        <div class="dropdown">
            <a href="#" class="dropbtn">Menu</a>
            <div class="submenu">
                <a href="navigation/skittles.html">Skittles</a>
            </div>
        </div>
    </div>
    <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4ddabef1-8390-424a-a828-f61e4df3d499/daraj8q-744f0563-d3f2-4a25-98a7-377abba7dc7b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzRkZGFiZWYxLTgzOTAtNDI0YS1hODI4LWY2MWU0ZGYzZDQ5OVwvZGFyYWo4cS03NDRmMDU2My1kM2YyLTRhMjUtOThhNy0zNzdhYmJhN2RjN2IuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.KpbFWvWcQbuGNwF9TtupLcDKwLRFW8DAZLx404K5bAU" alt="Mario Running" class="mario">

    <div style="padding:20px;">
        <h1>Welcome! This page is centered around Skittles and some of its variants.</h1>
        <p>Click on the buttons above to learn more about Skittles, me, or my tools and setup.</p>
    </div>
</body>
</html>





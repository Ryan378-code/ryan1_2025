---
layout: base
title: Snake Game 
description: Have fun playing this cheap knock-off of snakes!
hide: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        canvas {
            background-color: #4CAF50;
            border: 2px solid #000;
        }
    </style>
</head>
<body>
    <canvas id="snakeGame" width="400" height="400"></canvas>
    <script>
        const canvas = document.getElementById("snakeGame");
        const ctx = canvas.getContext("2d");
        const box = 20;
        let snake = [{ x: 9 * box, y: 9 * box }];
        let food = { x: Math.floor(Math.random() * 20) * box, y: Math.floor(Math.random() * 20) * box };
        let d;
        document.addEventListener("keydown", direction);
        function direction(event) {
            if (event.keyCode == 37 && d != "RIGHT") d = "LEFT";
            else if (event.keyCode == 38 && d != "DOWN") d = "UP";
            else if (event.keyCode == 39 && d != "LEFT") d = "RIGHT";
            else if (event.keyCode == 40 && d != "UP") d = "DOWN";
        }
        function collision(head, array) {
            return array.some(segment => head.x === segment.x && head.y === segment.y);
        }
        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "red";
            ctx.fillRect(food.x, food.y, box, box);
            for (let i = 0; i < snake.length; i++) {
                ctx.fillStyle = (i === 0) ? "darkgreen" : "green";
                ctx.fillRect(snake[i].x, snake[i].y, box, box);
            }
            let snakeX = snake[0].x;
            let snakeY = snake[0].y;
            if (d === "LEFT") snakeX -= box;
            if (d === "UP") snakeY -= box;
            if (d === "RIGHT") snakeX += box;
            if (d === "DOWN") snakeY += box;
            if (snakeX === food.x && snakeY === food.y) {
                food = { x: Math.floor(Math.random() * 20) * box, y: Math.floor(Math.random() * 20) * box };
            } else {
                snake.pop();
            }
            let newHead = { x: snakeX, y: snakeY };
            if (snakeX < 0 || snakeY < 0 || snakeX >= canvas.width || snakeY >= canvas.height || collision(newHead, snake)) {
                clearInterval(game);
                alert("Game Over!");
            }
            snake.unshift(newHead);
        }
        let game = setInterval(draw, 100);
    </script>
</body>
</html>



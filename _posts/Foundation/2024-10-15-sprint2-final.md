<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sprint 2 Final Hacks</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .link {
            color: blue; /* Link color */
            text-decoration: underline; /* Underline the link */
        }
        #gameCanvas {
            border: 4px solid rgb(102, 4, 4);
        }
    </style>
</head>
<body>
    <h2>Sprint 2 Final Hacks:</h2>
    <p>Check out the link for more information:</p>
    <a class="link" href="https://nighthawkcoders.github.io/portfolio_2025/csse/javascript/fundamentals/for-loops/" target="_blank">
        Mort's Link
    </a>
    <canvas id="gameCanvas" width="600" height="400"></canvas>
    <script>
        // Sprite metadata for lamp
        const lampSprite = {
            name: 'lamp',
            src: 'https://target.scene7.com/is/image/Target/GUEST_43f55026-adf3-4fce-aed3-817994ff6d0e?wid=488&hei=488&fmt=pjpeg',
            position: { x: 50, y: 50 } // Position of the lamp sprite
        };
        class CanvasDrawSprite {
            constructor(sprite) {
                this.sprite = sprite;
                this.canvas = document.getElementById('gameCanvas');
                this.ctx = this.canvas.getContext('2d');
                this.spriteImage = new Image();
                this.spriteImage.src = sprite.src;

                // Ensure the draw function is called only after the image loads
                this.spriteImage.onload = () => this.draw();
                this.spriteImage.onerror = () => console.error('Failed to load image:', this.sprite.src);
            }
            draw() {
                const { x, y } = this.sprite.position;
                this.ctx.drawImage(this.spriteImage, x, y);
                console.log(`Drawing sprite: ${this.sprite.name} at position (${x}, ${y})`);
            }
        }
        // Initialize and draw the lamp sprite
        new CanvasDrawSprite(lampSprite);
    </script>
</body>
</html>

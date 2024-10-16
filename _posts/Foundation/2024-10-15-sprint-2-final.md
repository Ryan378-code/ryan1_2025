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
    <p>
        <a class="link" href="https://nighthawkcoders.github.io/portfolio_2025/csse/javascript/fundamentals/for-loops/" target="_blank">
            Mort's Link
        </a>
    </p>
    <canvas id="gameCanvas" width="600" height="400"></canvas>
    <script>
        // Sprite metadata for lamp
        const lampSprite = {
            name: 'lamp',
            src: 'https://target.scene7.com/is/image/Target/GUEST_43f55026-adf3-4fce-aed3-817994ff6d0e?wid=488&hei=488&fmt=pjpeg',
            position: { x: 50, y: 50 }, // Initial position of the lamp sprite
            size: { width: 50, height: 50 }, // Size of the sprite
            brightnessLevels: [0.1, 0.5, 1.0], // Array of brightness levels
            currentBrightness: 1.0 // Current brightness level
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
            // Method to change position based on conditions
            updatePosition() {
                const { x, y } = this.sprite.position;
                const canvasWidth = this.canvas.width;
                const canvasHeight = this.canvas.height;

                // Move the sprite only if it is within bounds
                if (x < canvasWidth - this.sprite.size.width && y < canvasHeight - this.sprite.size.height) {
                    // Move the sprite down and to the right
                    this.sprite.position.x += 10; // Move right by 10
                    this.sprite.position.y += 10; // Move down by 10
                } else {
                    // If out of bounds, reset position
                    console.log(`Sprite is out of bounds. Resetting position.`);
                    this.sprite.position.x = 50;
                    this.sprite.position.y = 50;
                }
            }
            // Method to draw the sprite
            draw() {
                this.updatePosition(); // Update position before drawing
                const { x, y } = this.sprite.position;

                // Set the opacity based on brightness
                this.ctx.globalAlpha = this.sprite.currentBrightness;

                // Clear the canvas before drawing the sprite
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

                // Draw the sprite
                this.ctx.drawImage(this.spriteImage, x, y, this.sprite.size.width, this.sprite.size.height);
                console.log(`Drawing sprite: ${this.sprite.name} at position (${x}, ${y}) with brightness ${this.sprite.currentBrightness}`);
            }

            // Method to change brightness
            changeBrightness(levelIndex) {
                if (levelIndex >= 0 && levelIndex < this.sprite.brightnessLevels.length) {
                    this.sprite.currentBrightness = this.sprite.brightnessLevels[levelIndex];
                    console.log(`Changed brightness to ${this.sprite.currentBrightness}`);
                } else {
                    console.error(`Invalid brightness level index: ${levelIndex}`);
                }
            }
        }
        // Initialize and draw the lamp sprite
        const lamp = new CanvasDrawSprite(lampSprite);

        // Example of changing brightness after 1 second
        setTimeout(() => {
            lamp.changeBrightness(1); // Change to 50% brightness
            lamp.draw(); // Redraw with updated brightness
        }, 1000);

        // Example of changing brightness again after another second
        setTimeout(() => {
            lamp.changeBrightness(2); // Change to 100% brightness
            lamp.draw(); // Redraw with updated brightness
        }, 2000);
    </script>
</body>
</html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            size: { width: 50, height: 50 }, // Size of the sprite
            brightnessLevels: [0.1, 0.5, 1.0], // Array of brightness levels
            currentBrightness: 1.0 // Current brightness level
        };
        class CanvasDrawSprite {
            constructor(sprite, position) {
                this.sprite = sprite;
                this.position = position; // Position passed as parameter
                this.canvas = document.getElementById('gameCanvas');
                this.ctx = this.canvas.getContext('2d');
                this.spriteImage = new Image();
                this.spriteImage.src = sprite.src;
                // Ensure the draw function is called only after the image loads
                this.spriteImage.onload = () => this.startAnimation();
                this.spriteImage.onerror = () => console.error('Failed to load image:', this.sprite.src);
            }
            // Method to draw the sprite
            draw() {
                // Set the opacity based on brightness
                this.ctx.globalAlpha = this.sprite.currentBrightness;
                // Draw the sprite
                this.ctx.drawImage(this.spriteImage, this.position.x, this.position.y, this.sprite.size.width, this.sprite.size.height);
                console.log(`Drawing sprite: ${this.sprite.name} at position (${this.position.x}, ${this.position.y}) with brightness ${this.sprite.currentBrightness}`);
            }
            // Method to start animation loop
            startAnimation() {
                const animate = () => {
                    this.draw(); // Draw the sprite
                    requestAnimationFrame(animate); // Request the next animation frame
                };
                animate(); // Start the animation loop
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
        // Create a 2D array to hold the positions of sprites
        const positions = [
            [{ x: 50, y: 50 }, { x: 150, y: 50 }, { x: 250, y: 50 }],
            [{ x: 50, y: 150 }, { x: 150, y: 150 }, { x: 250, y: 150 }],
            [{ x: 50, y: 250 }, { x: 150, y: 250 }, { x: 250, y: 250 }]
        ];
        // Initialize and draw multiple lamp sprites based on the 2D array
        const lamps = [];
        for (let row = 0; row < positions.length; row++) {
            for (let col = 0; col < positions[row].length; col++) {
                lamps.push(new CanvasDrawSprite(lampSprite, positions[row][col]));
            }
        }
        // Example of changing brightness after 1 second
        setTimeout(() => {
            lamps.forEach(lamp => lamp.changeBrightness(1)); // Change to 50% brightness
        }, 1000);
        // Example of changing brightness again after another second
        setTimeout(() => {
            lamps.forEach(lamp => lamp.changeBrightness(2)); // Change to 100% brightness
        }, 2000);
    </script>
</body>
</html>


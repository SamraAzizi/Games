const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const GRID_SIZE = 20;
const GRID_WIDTH = canvas.width / GRID_SIZE;
const GRID_HEIGHT = canvas.height / GRID_SIZE;

// Game state
let isPaused = false;
let gameSpeed = 100; // milliseconds between updates
let lastRenderTime = 0;
let score = 0;

class Snake {
    constructor() {
        this.reset();
    }

    reset() {
        this.length = 1;
        this.positions = [
            {
                x: Math.floor(GRID_WIDTH / 2) * GRID_SIZE,
                y: Math.floor(GRID_HEIGHT / 2) * GRID_SIZE
            }
        ];
        this.direction = this.randomDirection();
    }

    randomDirection() {
        const directions = ['UP', 'DOWN', 'LEFT', 'RIGHT'];
        return directions[Math.floor(Math.random() * directions.length)];
    }

    move() {
        const head = { ...this.positions[0] };

        switch (this.direction) {
            case 'UP':
                head.y -= GRID_SIZE;
                break;
            case 'DOWN':
                head.y += GRID_SIZE;
                break;
            case 'LEFT':
                head.x -= GRID_SIZE;
                break;
            case 'RIGHT':
                head.x += GRID_SIZE;
                break;
        }

        // Wrap around the screen
        head.x = (head.x + canvas.width) % canvas.width;
        head.y = (head.y + canvas.height) % canvas.height;

        // Check collision with self
        if (this.checkCollision(head)) {
            this.reset();
            score = 0;
            updateScore();
            return;
        }

        this.positions.unshift(head);
        if (this.positions.length > this.length) {
            this.positions.pop();
        }
    }

    checkCollision(head) {
        return this.positions.some(segment =>
            segment.x === head.x && segment.y === head.y
        );
    }

    draw() {
        ctx.fillStyle = '#4ecca3'; // Updated snake color to match theme
        this.positions.forEach((position, index) => {
            // Make head slightly larger
            const size = index === 0 ? GRID_SIZE : GRID_SIZE - 2;
            ctx.fillRect(position.x, position.y, size - 2, size - 2);
        });
    }
}

class Food {
    constructor() {
        this.position = { x: 0, y: 0 };
        this.randomize();
    }

    randomize() {
        this.position = {
            x: Math.floor(Math.random() * GRID_WIDTH) * GRID_SIZE,
            y: Math.floor(Math.random() * GRID_HEIGHT) * GRID_SIZE
        };
    }

    draw() {
        ctx.fillStyle = '#ff6b6b'; // Updated food color
        ctx.beginPath();
        const centerX = this.position.x + GRID_SIZE / 2;
        const centerY = this.position.y + GRID_SIZE / 2;
        ctx.arc(centerX, centerY, (GRID_SIZE - 4) / 2, 0, 2 * Math.PI);
        ctx.fill();
    }
}

let snake = new Snake();
let food = new Food();

function updateScore() {
    document.getElementById('score').textContent = `Score: ${score}`;
}

function drawPauseScreen() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = '#4ecca3';
    ctx.font = '30px "Press Start 2P"';
    ctx.textAlign = 'center';
    ctx.fillText('PAUSED', canvas.width / 2, canvas.height / 2);
    ctx.font = '16px "Press Start 2P"';
    ctx.fillText('Press SPACE to resume', canvas.width / 2, canvas.height / 2 + 40);
}

function gameLoop(currentTime) {
    window.requestAnimationFrame(gameLoop);

    // Convert to seconds
    const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000;

    // If paused, just draw pause screen and return
    if (isPaused) {
        drawPauseScreen();
        return;
    }

    // Only update if enough time has passed
    if (secondsSinceLastRender < gameSpeed / 1000) return;

    lastRenderTime = currentTime;

    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Update game state
    snake.move();

    // Check if snake ate food
    if (snake.positions[0].x === food.position.x && 
        snake.positions[0].y === food.position.y) {
        snake.length++;
        score += 10;
        updateScore();
        food.randomize();
        // Increase game speed slightly
        gameSpeed = Math.max(50, gameSpeed - 1);
    }

    // Draw everything
    snake.draw();
    food.draw();
}

// Input handling
document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'ArrowUp':
            if (snake.direction !== 'DOWN') snake.direction = 'UP';
            break;
        case 'ArrowDown':
            if (snake.direction !== 'UP') snake.direction = 'DOWN';
            break;
        case 'ArrowLeft':
            if (snake.direction !== 'RIGHT') snake.direction = 'LEFT';
            break;
        case 'ArrowRight':
            if (snake.direction !== 'LEFT') snake.direction = 'RIGHT';
            break;
        case ' ': // Space bar
            isPaused = !isPaused;
            break;
    }
});

// Start the game
gameLoop();

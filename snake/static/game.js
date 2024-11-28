const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const GRID_SIZE = 20;
const GRID_WIDTH = canvas.width / GRID_SIZE;
const GRID_HEIGHT = canvas.height / GRID_SIZE;

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
        ctx.fillStyle = 'white';
        this.positions.forEach(position => {
            ctx.fillRect(position.x, position.y, GRID_SIZE - 2, GRID_SIZE - 2);
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
        ctx.fillStyle = 'red';
        ctx.fillRect(this.position.x, this.position.y, GRID_SIZE - 2, GRID_SIZE - 2);
    }
}

let snake = new Snake();
let food = new Food();
let score = 0;

function updateScore() {
    document.getElementById('score').textContent = `Score: ${score}`;
}

function gameLoop() {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    snake.move();
    
    // Check for food collision
    if (snake.positions[0].x === food.position.x && snake.positions[0].y === food.position.y) {
        snake.length++;
        food.randomize();
        score++;
        updateScore();
    }

    snake.draw();
    food.draw();
}

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
    }
});

// Start the game
setInterval(gameLoop, 100);

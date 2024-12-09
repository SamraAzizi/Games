const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreElement = document.getElementById('score');

// Game constants
const GRAVITY = 0.25;
const FLAP_SPEED = -4.6;
const PIPE_SPEED = 2;
const PIPE_SPAWN_INTERVAL = 1500;
const GROUND_HEIGHT = canvas.height * 0.8;
const PIPE_WIDTH = 52;
const PIPE_GAP = 120;
const MIN_PIPE_HEIGHT = 50;  // Minimum height for pipes
const MAX_PIPE_HEIGHT = canvas.height - GROUND_HEIGHT - PIPE_GAP - MIN_PIPE_HEIGHT;  // Maximum height considering gap and ground

// Game state
let score = 0;
let frames = 0;
let gameStarted = false;
let gameOver = false;

// Bird object
const bird = {
    x: 50,
    y: 150,
    width: 34,
    height: 24,
    velocity: 0,
    rotation: 0,  // Added for rotation animation
    
    flap() {
        this.velocity = FLAP_SPEED;
        this.rotation = -25;  // Rotate upward when flapping
    },
    
    update() {
        this.velocity += GRAVITY;
        this.y += this.velocity;
        
        // Update rotation based on velocity
        if (this.velocity >= FLAP_SPEED) {
            this.rotation += 2;
            if (this.rotation > 90) this.rotation = 90;
        }
        
        // Ground collision
        if (this.y + this.height >= GROUND_HEIGHT) {
            this.y = GROUND_HEIGHT - this.height;
            gameOver = true;
        }
        
        // Ceiling collision
        if (this.y <= 0) {
            this.y = 0;
            this.velocity = 0;
        }
    },
    
    draw() {
        ctx.save();
        ctx.translate(this.x + this.width/2, this.y + this.height/2);
        ctx.rotate(this.rotation * Math.PI/180);
        
        // Bird body
        ctx.fillStyle = '#f4d03f';
        ctx.beginPath();
        ctx.ellipse(-this.width/2, -this.height/2, this.width/2, this.height/2, 0, 0, 2 * Math.PI);
        ctx.fill();
        
        // Wing
        ctx.fillStyle = '#f1c40f';
        ctx.beginPath();
        ctx.ellipse(-this.width/4, -this.height/4, this.width/4, this.height/4, 0, 0, 2 * Math.PI);
        ctx.fill();
        
        // Eye
        ctx.fillStyle = 'white';
        ctx.beginPath();
        ctx.arc(this.width/4, -this.height/4, 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = 'black';
        ctx.beginPath();
        ctx.arc(this.width/4, -this.height/4, 2, 0, 2 * Math.PI);
        ctx.fill();
        
        ctx.restore();
    }
};

// Pipes array
let pipes = [];

class Pipe {
    constructor() {
        this.width = PIPE_WIDTH;
        this.x = canvas.width;
        this.gap = PIPE_GAP;
        
        // Calculate a fixed height for top pipe between MIN and MAX
        this.topHeight = MIN_PIPE_HEIGHT + Math.random() * (MAX_PIPE_HEIGHT - MIN_PIPE_HEIGHT);
        this.bottomY = this.topHeight + this.gap;
    }
    
    update() {
        this.x -= PIPE_SPEED;
    }
    
    draw() {
        // Gradient for pipes
        let gradientTop = ctx.createLinearGradient(this.x, 0, this.x + this.width, 0);
        gradientTop.addColorStop(0, '#2ecc71');
        gradientTop.addColorStop(0.5, '#27ae60');
        gradientTop.addColorStop(1, '#2ecc71');
        
        // Top pipe
        ctx.fillStyle = gradientTop;
        ctx.fillRect(this.x, 0, this.width, this.topHeight);
        
        // Pipe cap (top)
        ctx.fillStyle = '#27ae60';
        ctx.fillRect(this.x - 3, this.topHeight - 20, this.width + 6, 20);
        
        // Bottom pipe
        ctx.fillStyle = gradientTop;
        ctx.fillRect(this.x, this.bottomY, this.width, canvas.height - this.bottomY);
        
        // Pipe cap (bottom)
        ctx.fillStyle = '#27ae60';
        ctx.fillRect(this.x - 3, this.bottomY, this.width + 6, 20);
    }
    
    collidesWith(bird) {
        return !(bird.x + bird.width < this.x || 
                bird.x > this.x + this.width || 
                bird.y > this.topHeight && bird.y + bird.height < this.bottomY);
    }
}

// Event listeners
document.addEventListener('keydown', (e) => {
    if (e.code === 'Space' || e.code === 'ArrowUp') {
        if (!gameStarted) {
            gameStarted = true;
        }
        if (!gameOver) {
            bird.flap();
        } else {
            resetGame();
        }
    }
});

document.addEventListener('click', () => {
    if (!gameStarted) {
        gameStarted = true;
    }
    if (!gameOver) {
        bird.flap();
    } else {
        resetGame();
    }
});

function resetGame() {
    // Reset game state
    score = 0;
    frames = 0;
    gameOver = false;
    pipes = [];
    scoreElement.textContent = '0';
    
    // Reset bird position
    bird.y = 150;
    bird.velocity = 0;
}

// Game loop
function update() {
    frames++;
    
    if (gameStarted && !gameOver) {
        bird.update();
        
        // Spawn new pipes
        if (frames % 100 === 0) {
            pipes.push(new Pipe());
        }
        
        // Update pipes
        pipes.forEach(pipe => {
            pipe.update();
            
            // Check collision
            if (pipe.collidesWith(bird)) {
                gameOver = true;
            }
            
            // Score point
            if (pipe.x + pipe.width < bird.x && !pipe.passed) {
                score++;
                scoreElement.textContent = score;
                pipe.passed = true;
            }
        });
        
        // Remove off-screen pipes
        pipes = pipes.filter(pipe => pipe.x + pipe.width > 0);
    }
}

function draw() {
    // Clear canvas
    ctx.fillStyle = '#71c5cf';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw pipes
    pipes.forEach(pipe => pipe.draw());
    
    // Draw ground
    ctx.fillStyle = '#dec07a';
    ctx.fillRect(0, GROUND_HEIGHT, canvas.width, canvas.height - GROUND_HEIGHT);
    
    // Draw bird
    bird.draw();
    
    // Draw game over message
    if (gameOver) {
        ctx.fillStyle = 'black';
        ctx.font = '48px Arial';
        ctx.fillText('Game Over!', canvas.width/2 - 100, canvas.height/2);
        ctx.font = '24px Arial';
        ctx.fillText('Click to restart', canvas.width/2 - 60, canvas.height/2 + 40);
    }
    
    // Draw start message
    if (!gameStarted) {
        ctx.fillStyle = 'black';
        ctx.font = '24px Arial';
        ctx.fillText('Click to start', canvas.width/2 - 60, canvas.height/2);
    }
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();

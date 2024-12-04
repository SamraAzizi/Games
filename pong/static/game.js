const socket = io();
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Game constants
const PADDLE_WIDTH = 15;
const PADDLE_HEIGHT = 90;
const BALL_SIZE = 30;
const PADDLE_SPEED = 6;
const WINNING_SCORE = 5;
const POWER_UP_INTERVAL = 15000;

// Game state
let gameState = {
    ball: { x: 400, y: 300, dx: 3, dy: 3 },
    paddles: { left: 300, right: 300 },
    scores: { left: 0, right: 0 },
    powerUp: { active: false, x: 0, y: 0, type: null },
    paddleSizes: { left: PADDLE_HEIGHT, right: PADDLE_HEIGHT },
    gameOver: false,
    winner: null
};

// Input handling
const keys = {
    w: false,
    s: false,
    ArrowUp: false,
    ArrowDown: false
};

// Simple key handler
window.addEventListener('keydown', (e) => {
    if (e.key === ' ' || e.code === 'Space') {
        if (gameState.gameOver) {
            console.log('Space pressed - Resetting game');
            resetGame();
        }
        return;
    }
    
    if (keys.hasOwnProperty(e.key)) {
        keys[e.key] = true;
    }
});

window.addEventListener('keyup', (e) => {
    if (keys.hasOwnProperty(e.key)) {
        keys[e.key] = false;
    }
});

// Socket events
socket.on('connect', () => {
    console.log('Connected to server');
    socket.emit('join_game', { game_id: 'default' });
});

socket.on('game_state', (state) => {
    if (!gameState.gameOver || state.gameOver !== gameState.gameOver) {
        Object.assign(gameState, state);
    }
});

// Add power-up spawning
setInterval(() => {
    if (!gameState.powerUp.active && !gameState.gameOver) {
        gameState.powerUp = {
            active: true,
            x: Math.random() * (canvas.width - 100) + 50,
            y: Math.random() * (canvas.height - 100) + 50,
            type: Math.random() < 0.5 ? 'speed' : 'size'
        };
    }
}, POWER_UP_INTERVAL);

function checkPowerUpCollision() {
    if (gameState.powerUp.active) {
        const ballCenter = {
            x: gameState.ball.x + BALL_SIZE / 2,
            y: gameState.ball.y + BALL_SIZE / 2
        };
        
        const powerUpRect = {
            x: gameState.powerUp.x - 15,
            y: gameState.powerUp.y - 15,
            width: 30,
            height: 30
        };

        if (ballCenter.x > powerUpRect.x && 
            ballCenter.x < powerUpRect.x + powerUpRect.width &&
            ballCenter.y > powerUpRect.y && 
            ballCenter.y < powerUpRect.y + powerUpRect.height) {
            
            applyPowerUp(gameState.ball.dx > 0 ? 'right' : 'left');
            gameState.powerUp.active = false;
        }
    }
}

function applyPowerUp(side) {
    if (gameState.powerUp.type === 'speed') {
        gameState.ball.dx *= 1.5;
        gameState.ball.dy *= 1.5;
    } else if (gameState.powerUp.type === 'size') {
        gameState.paddleSizes[side] = Math.min(PADDLE_HEIGHT * 1.5, gameState.paddleSizes[side] * 1.5);
        setTimeout(() => {
            gameState.paddleSizes[side] = PADDLE_HEIGHT;
        }, 5000); // Power-up lasts 5 seconds
    }
}

function resetGame() {
    console.log('Resetting game state');
    
    const newState = {
        ball: { 
            x: canvas.width / 2 - BALL_SIZE / 2,
            y: canvas.height / 2 - BALL_SIZE / 2,
            dx: 3 * (Math.random() > 0.5 ? 1 : -1),
            dy: 3 * (Math.random() > 0.5 ? 1 : -1)
        },
        paddles: { 
            left: canvas.height / 2 - PADDLE_HEIGHT / 2,
            right: canvas.height / 2 - PADDLE_HEIGHT / 2
        },
        scores: { left: 0, right: 0 },
        powerUp: { active: false, x: 0, y: 0, type: null },
        paddleSizes: { left: PADDLE_HEIGHT, right: PADDLE_HEIGHT },
        gameOver: false,
        winner: null
    };
    
    Object.assign(gameState, newState);
    
    socket.emit('reset_game', { game_id: 'default' });
    
    console.log('Game state reset complete');
}

// Game loop
function update() {
    if (gameState.gameOver) {
        draw();
        return;
    }
    // Update paddle positions based on input
    if (keys.w && gameState.paddles.left > 0) {
        gameState.paddles.left -= PADDLE_SPEED;
        socket.emit('paddle_move', { 
            game_id: 'default',
            paddle: 'left',
            position: gameState.paddles.left
        });
    }
    if (keys.s && gameState.paddles.left < canvas.height - gameState.paddleSizes.left) {
        gameState.paddles.left += PADDLE_SPEED;
        socket.emit('paddle_move', {
            game_id: 'default',
            paddle: 'left',
            position: gameState.paddles.left
        });
    }
    if (keys.ArrowUp && gameState.paddles.right > 0) {
        gameState.paddles.right -= PADDLE_SPEED;
        socket.emit('paddle_move', {
            game_id: 'default',
            paddle: 'right',
            position: gameState.paddles.right
        });
    }
    if (keys.ArrowDown && gameState.paddles.right < canvas.height - gameState.paddleSizes.right) {
        gameState.paddles.right += PADDLE_SPEED;
        socket.emit('paddle_move', {
            game_id: 'default',
            paddle: 'right',
            position: gameState.paddles.right
        });
    }

    // Update ball position
    gameState.ball.x += gameState.ball.dx;
    gameState.ball.y += gameState.ball.dy;

    // Ball collision with top and bottom
    if (gameState.ball.y <= 0 || gameState.ball.y + BALL_SIZE >= canvas.height) {
        gameState.ball.dy *= -1;
    }

    // Ball collision with paddles
    const leftPaddleRect = {
        x: 50,
        y: gameState.paddles.left,
        width: PADDLE_WIDTH,
        height: gameState.paddleSizes.left
    };

    const rightPaddleRect = {
        x: canvas.width - 50 - PADDLE_WIDTH,
        y: gameState.paddles.right,
        width: PADDLE_WIDTH,
        height: gameState.paddleSizes.right
    };

    if (checkCollision(gameState.ball, leftPaddleRect) || 
        checkCollision(gameState.ball, rightPaddleRect)) {
        gameState.ball.dx *= -1;
    }

    // Score points
    if (gameState.ball.x <= 0) {
        gameState.scores.right += 1;
        resetBall();
    }
    if (gameState.ball.x + BALL_SIZE >= canvas.width) {
        gameState.scores.left += 1;
        resetBall();
    }

    // Check for game over
    if (gameState.scores.left >= WINNING_SCORE) {
        gameState.gameOver = true;
        gameState.winner = 'Left';
    } else if (gameState.scores.right >= WINNING_SCORE) {
        gameState.gameOver = true;
        gameState.winner = 'Right';
    }

    checkPowerUpCollision();

    socket.emit('update_ball', {
        game_id: 'default',
        ball: gameState.ball,
        scores: gameState.scores,
        powerUp: gameState.powerUp,
        paddleSizes: gameState.paddleSizes,
        gameOver: gameState.gameOver,
        winner: gameState.winner
    });

    draw();
    requestAnimationFrame(update);
}

function checkCollision(ball, paddle) {
    return ball.x < paddle.x + paddle.width &&
           ball.x + BALL_SIZE > paddle.x &&
           ball.y < paddle.y + paddle.height &&
           ball.y + BALL_SIZE > paddle.y;
}

function resetBall() {
    gameState.ball.x = canvas.width / 2;
    gameState.ball.y = canvas.height / 2;
    gameState.ball.dx = 3 * (Math.random() > 0.5 ? 1 : -1);
    gameState.ball.dy = 3 * (Math.random() > 0.5 ? 1 : -1);
}

function draw() {
    // Clear canvas with a slight gradient
    const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
    gradient.addColorStop(0, '#1a1a1a');
    gradient.addColorStop(1, '#0a0a0a');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw paddles with glow effect
    ctx.shadowBlur = 10;
    ctx.shadowColor = 'rgba(255, 255, 255, 0.5)';
    ctx.fillStyle = '#fff';
    
    // Left paddle
    ctx.beginPath();
    ctx.roundRect(50, gameState.paddles.left, PADDLE_WIDTH, gameState.paddleSizes.left, 5);
    ctx.fill();
    
    // Right paddle
    ctx.beginPath();
    ctx.roundRect(canvas.width - 50 - PADDLE_WIDTH, gameState.paddles.right, PADDLE_WIDTH, gameState.paddleSizes.right, 5);
    ctx.fill();

    // Draw ball with glow
    ctx.beginPath();
    ctx.arc(gameState.ball.x + BALL_SIZE/2, gameState.ball.y + BALL_SIZE/2, BALL_SIZE/2, 0, Math.PI * 2);
    ctx.fill();

    // Reset shadow for other elements
    ctx.shadowBlur = 0;

    // Draw power-up if active
    if (gameState.powerUp.active) {
        ctx.beginPath();
        ctx.arc(gameState.powerUp.x, gameState.powerUp.y, 15, 0, Math.PI * 2);
        ctx.fillStyle = gameState.powerUp.type === 'speed' ? '#ff4444' : '#44ff44';
        ctx.fill();
        // Add glow effect to power-ups
        ctx.strokeStyle = gameState.powerUp.type === 'speed' ? '#ff6666' : '#66ff66';
        ctx.lineWidth = 3;
        ctx.stroke();
    }

    // Draw center line with dots
    ctx.setLineDash([5, 15]);
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, 0);
    ctx.lineTo(canvas.width / 2, canvas.height);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.stroke();

    // Draw scores with glow
    ctx.font = '48px "Press Start 2P"';
    ctx.textAlign = 'center';
    ctx.fillStyle = '#fff';
    ctx.shadowBlur = 10;
    ctx.shadowColor = 'rgba(255, 255, 255, 0.5)';
    ctx.fillText(gameState.scores.left, canvas.width / 4, 80);
    ctx.fillText(gameState.scores.right, 3 * canvas.width / 4, 80);

    // Draw game over screen
    if (gameState.gameOver) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.85)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.font = '48px "Press Start 2P"';
        ctx.fillStyle = '#fff';
        ctx.textAlign = 'center';
        ctx.shadowBlur = 15;
        ctx.shadowColor = 'rgba(255, 255, 255, 0.7)';
        ctx.fillText(`${gameState.winner} WINS!`, canvas.width / 2, canvas.height / 2 - 50);
        
        ctx.font = '24px "Press Start 2P"';
        ctx.fillStyle = '#aaa';
        ctx.shadowBlur = 5;
        ctx.fillText('PRESS SPACE TO RESTART', canvas.width / 2, canvas.height / 2 + 50);
    }
}

// Start the game
update();

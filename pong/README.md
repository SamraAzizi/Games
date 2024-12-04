# Modern Pong Game
---------------------------
A modern implementation of the classic Pong game using Flask and WebSocket for real-time multiplayer functionality. This version features a sleek design, power-ups, and smooth gameplay.

## Features
-------------------------
- **Real-time Multiplayer**: Built with Flask and WebSocket for smooth, lag-free gameplay
- **Modern UI**: Clean, minimalist design with retro-inspired elements
- **Power-up System**:
  - 🔴 Speed Boost: Increases ball speed
  - 🟢 Paddle Size: Temporarily increases paddle size
- **Scoring System**: First player to reach 5 points wins
- **Responsive Controls**: Smooth paddle movement and ball physics
- **Visual Effects**: Glowing elements and smooth animations

## Installation
-----------------------
1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd pong
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play
------------------------
### Controls
- **Left Paddle**: 
  - `W` key: Move Up
  - `S` key: Move Down
- **Right Paddle**: 
  - `↑` (Up Arrow): Move Up
  - `↓` (Down Arrow): Move Down
- **Reset Game**: 
  - `Space Bar`: Start new game after game over

### Game Rules
-----------------------
1. Each player controls a paddle on their side of the screen
2. The ball bounces between paddles
3. Miss the ball = opponent scores a point
4. First to 5 points wins
5. Power-ups appear randomly:
   - Red orb: Increases ball speed
   - Green orb: Makes your paddle larger for 5 seconds

### Power-up System
- Power-ups appear every 15 seconds
- Ball must hit the power-up to activate it
- Effects are temporary and apply to the receiving player
- Strategic timing can turn the tide of the game

## Technical Details
----------------------------
### Technologies Used
- **Backend**: 
  - Flask (Python web framework)
  - Flask-SocketIO (WebSocket support)
- **Frontend**: 
  - HTML5 Canvas
  - JavaScript
  - Socket.IO client

### File Structure
```
pong/
├── app.py              # Flask server and game logic
├── requirements.txt    # Python dependencies
├── static/
│   └── game.js        # Client-side game logic
└── templates/
    └── index.html     # Game interface
```

### Key Components
-------------------------
- **Server-Side**:
  - Game state management
  - WebSocket event handling
  - Player synchronization
- **Client-Side**:
  - Canvas rendering
  - Input handling
  - Power-up animations
  - Score tracking

## Troubleshooting

### Common Issues
---------------------------
1. **Game Not Loading**:
   - Ensure all requirements are installed
   - Check if Flask server is running
   - Clear browser cache

2. **Controls Not Responding**:
   - Refresh the page
   - Ensure browser window is focused
   - Check for console errors (F12)

3. **Multiplayer Issues**:
   - Verify both players are on the same network
   - Check server logs for connection issues
   - Ensure WebSocket connection is established



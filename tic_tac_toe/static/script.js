document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const statusDisplay = document.getElementById('status');
    const resetButton = document.getElementById('reset');

    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });

    resetButton.addEventListener('click', resetGame);

    function handleCellClick(e) {
        const cell = e.target;
        const row = cell.dataset.row;
        const col = cell.dataset.col;

        if (cell.textContent !== '') return;

        fetch('/make_move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ row: parseInt(row), col: parseInt(col) })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
                return;
            }
            updateBoard(data.board);
            if (data.status === 'winner') {
                statusDisplay.textContent = `Player ${data.player} wins!`;
                setTimeout(() => {
                    resetGame();
                }, 2000);
            } else if (data.status === 'tie') {
                statusDisplay.textContent = "It's a tie!";
                setTimeout(() => {
                    resetGame();
                }, 2000);
            } else {
                statusDisplay.textContent = `Player ${data.current_player}'s turn`;
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function updateBoard(board) {
        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                const cell = document.querySelector(`[data-row="${row}"][data-col="${col}"]`);
                const value = board[row][col];
                cell.textContent = value;
                if (value === 'X') {
                    cell.classList.add('x');
                    cell.classList.remove('o');
                } else if (value === 'O') {
                    cell.classList.add('o');
                    cell.classList.remove('x');
                } else {
                    cell.classList.remove('x', 'o');
                }
            }
        }
    }

    function resetGame() {
        fetch('/reset', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            updateBoard(data.board);
            statusDisplay.textContent = `Player ${data.current_player}'s turn`;
        })
        .catch(error => console.error('Error:', error));
    }
});

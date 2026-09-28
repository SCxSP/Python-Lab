import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Tic-Tac-Toe (Minimax)")
        self.board = [" "] * 9
        self.buttons = []
        for i in range(9):
            b = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                          command=lambda idx=i: self.player_move(idx))
            b.grid(row=i//3, column=i%3)
            self.buttons.append(b)

    def player_move(self, idx):
        if self.board[idx] == " ":
            self.board[idx] = "X"
            self.buttons[idx].config(text="X", fg="blue")
            if self.check_win("X"):
                messagebox.showinfo("Game Over", "You Win!")
                self.reset()
                return
            if " " not in self.board:
                messagebox.showinfo("Game Over", "It's a Tie!")
                self.reset()
                return
            self.ai_move()

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            self.board[best_move] = "O"
            self.buttons[best_move].config(text="O", fg="red")
            if self.check_win("O"):
                messagebox.showinfo("Game Over", "AI Wins!")
                self.reset()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a Tie!")
                self.reset()

    def minimax(self, depth, is_max):
        if self.check_win("O"): return 1
        if self.check_win("X"): return -1
        if " " not in self.board: return 0

        if is_max:
            best = -float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    best = max(best, self.minimax(depth + 1, False))
                    self.board[i] = " "
            return best
        else:
            best = float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    best = min(best, self.minimax(depth + 1, True))
                    self.board[i] = " "
            return best

    def check_win(self, p):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(self.board[a] == self.board[b] == self.board[c] == p for a, b, c in wins)

    def reset(self):
        self.board = [" "] * 9
        for b in self.buttons:
            b.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()

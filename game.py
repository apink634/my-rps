"""Rules for one Rock, Paper, Scissors round. See SPEC.md."""

MOVES = {"rock", "paper", "scissors"}
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def determine_winner(player: str, computer: str) -> str:
    """Return the player's outcome for two valid lowercase moves."""
    if player not in MOVES or computer not in MOVES:
        raise ValueError("Moves must be rock, paper, or scissors.")
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "win"
    return "lose"

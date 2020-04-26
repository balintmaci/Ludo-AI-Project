import ludopy
import numpy as np

def main():
    g = ludopy.Game()
    there_is_a_winner = False

    while not there_is_a_winner:
        (dice, move_pieces, player_pieces, enemy_pieces, player_is_a_winner, there_is_a_winner), player_i = g.get_observation()

        if len(move_pieces) > 0:
            piece_to_move = move_pieces[np.random.randint(0, len(move_pieces))]
        else:
            piece_to_move = -1

        _, _, _, _, _, there_is_a_winner = g.answer_observation(piece_to_move)

    print("Saving history to numpy file")
    g.save_hist(f"game_history.npy")
    print("Saving game video")
    g.save_hist_video(f"game_video.mp4")

if __name__ == "__main__":
    main()

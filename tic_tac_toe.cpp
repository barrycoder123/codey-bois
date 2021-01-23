#include <iostream>

using namespace std;

const string QUIT = "q";
const string PLAY = "p";
class Player{

	// constructor
	public:
		Player(string player_symbol){
			this->player_symbol = player_symbol;
		}
	
		void play(string player_symbol);
		string get_player();

	private:
		string player_symbol;
};

string Player::get_player(){
	return player_symbol;
}

string board[10] = {"0","1","2","3","4","5","6","7","8","9"};
void create_board();
void reset_board();
int victory_check();
bool tie_game();
int main(){
   	cout << "\n\n\tTic Tac Toe\n\n";
   	cout << "Player 1 (X)  -  Player 2 (O)" << endl << endl;
   	cout << endl;

	Player player_1("X");
	Player player_2("O");
	string player_move;
    int available = 9;
	bool game_over = false;
	bool player1_turn = true;
	while(!game_over){
		create_board();
		if(player1_turn){
			cout << "PLAYER 1: enter your move: ";
		}
		else{
			cout << "PLAYER 2: enter your move: ";
		}
		cin >> player_move; 
		if(player_move == QUIT){
			game_over = true;
            cout << "Thanks for playing this game, hope it wasn't too buggy.\n";
		}
		else if(player_move ==  PLAY){
			string my_symbol = player_1.get_player();
			if(player1_turn){
				player_1.play(my_symbol);
                available--;
			}else{
				player_2.play(player_2.get_player());
                available--;
			}
            int winner = victory_check();
            if(winner ==  1){
                create_board();
                cout << "CONGRATULATIONS Player 1, You won" << endl;
                cout << "Do you want to play again [y/n]" << endl;
                cin >> player_move;
                if(player_move == "y"){
                    game_over = false;
                    reset_board();
                    available = 9;
                }else{
                    game_over = true;
                }
            } else if(winner == 0){
                create_board();
                cout << "CONGRATULATIONS Player 2, You won" << endl;
                cout << "Do you want to play again [y/n]" << endl;
                cin >> player_move;
                if(player_move == "y"){
                    game_over = false;
                    reset_board();
                    available = 9;
                }else{
                    game_over = true;
                }
            }else if(available == 0){
                cout << "this game is a tie" << endl;
                cout << "Do you want to play again [y/n]" << endl;
                cin >> player_move;
                if(player_move == "y"){
                    game_over = false;
                    reset_board();
                    available = 9;
                }else{
                    game_over = true;
                }
            }
            player1_turn = !player1_turn;
		}
	}

}
void create_board(){
    
    cout << "     |     |     " << endl;
    cout << "  " << board[1] << "  |  " << board[2] << "  |  " << board[3] << endl;

    cout << "_____|_____|_____" << endl;
    cout << "     |     |     " << endl;

    cout << "  " << board[4] << "  |  " << board[5] << "  |  " << board[6] << endl;

    cout << "_____|_____|_____" << endl;
    cout << "     |     |     " << endl;

    cout << "  " << board[7] << "  |  " << board[8] << "  |  " << board[9] << endl;

    cout << "     |     |     " << endl << endl;
}

void reset_board(){
	for (int i = 0; i < 10; i++){
		board[i] = to_string(i);
	}
}

void Player::play(string player_symbol){
	int move_number;
	cin >> move_number;
	while(board[move_number] == "X" || board[move_number] == "O"){
		cout << "This position is already taken, try again: ";
		cin >> move_number;
	}
	board[move_number] = player_symbol;
}
bool tie_game(){
	for(int i = 0; i < 10; i++){
		if (board[i] != "X" && board[i] != "O"){
			return false;
		}
	}
	return true;
}

int victory_check(){
	// horizontal win
	if (board[1] == board[2] && board[2] == board[3]){
		if(board[1] == "X") return 1;
		else return 0;
	}
	if (board[4] == board[5] && board[5] == board[6]){
		if(board[4] == "X") return 1;
		else return 0;
	}
	if (board[7] == board[8] && board[8] == board[9]){
		if(board[8] == "X") return 1;
		else return 0;
	}
	// vertical
	
	if (board[1] == board[4] && board[4] == board[7]){
		if(board[7] == "X") return 1;
		else return 0;
	}
	if (board[2] == board[5] && board[5] == board[8]){
		if(board[5] == "X") return 1;
		else return 0;
	}
	if (board[3] == board[6] && board[6] == board[9]){
		if(board[6] == "X") return 1;
		else return 0;
	}
	// diagonal
	
	if (board[1] == board[5] && board[5] == board[9]){
		if(board[9] == "X") return 1;
		else return 0;
	}
	if (board[3] == board[5] && board[5] == board[7]){
		if(board[3] == "X") return 1;
		else return 0;
	}
	return -1;
}

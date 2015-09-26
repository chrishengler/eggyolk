%module gamerunner
%include std_vector.i

%{
#define SWIG_FILE_WITH_INIT
#include "gamerunner.h"
%}

class Gamerunner{
public:
  void initialise(CheckyrsAI &ai1,CheckyrsAI &ai2);
  bool continueGame();
  bool gameOver() const;
  bool isDraw() const;
  int getWinner() const;
  int getPiecesPlayer(const int player=1) const;
};

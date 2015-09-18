%module checkyrsai

%{
#define SWIG_FILE_WITH_INIT
#include "ai.h"
%}

class CheckyrsAI{
public:
  CheckyrsAI(const int player=1);
  CheckyrsAI breed(const CheckyrsAI&p2, float mutate=0.05);
  void Initialise(bool random=false);
  void setPlayer(const int player);
  int getPlayer();
};

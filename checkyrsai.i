%module checkyrsai
%include std_string.i

%{
#define SWIG_FILE_WITH_INIT
#include <string>
#include <boost/serialization/serialization.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <boost/archive/binary_iarchive.hpp>

#include "ai.h"

%}

class CheckyrsAI{
public:
  CheckyrsAI(const int player=1);
  CheckyrsAI breed(const CheckyrsAI&p2, float mutate=0.05);
  void Initialise(bool random=false);
  void setPlayer(const int player);
  int getPlayer();
  void save(const std::string &filename);
  void load(const std::string &filename);
};

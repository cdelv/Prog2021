#include <iostream>

const int steps = 5;
const int xdim =7;
const int ydim =5;

class GameOfLife{
private:
  const int Lx =xdim+steps*2;
  const int Ly =ydim+steps*2;
  int board[xdim+steps*2][ydim+steps*2] = {0};
  int new_board[xdim+steps*2][ydim+steps*2] = {0};

public:
  void Start(void);
  void Print_board(void);
  void Update(void);
  void Count_alive(void);
  int Sum_neighbours(int i, int j);
};

void GameOfLife::Start(void){
  int init_state[ydim][xdim] =
    {
      {0,1,1,1,0,0,1},
      {1,1,1,0,1,1,1},
      {0,0,0,0,0,0,0},
      {0,0,1,1,1,0,1},
      {0,0,0,1,1,0,0}
      };
  
  for(int i=0; i<ydim; i++)  //colocar el estado inicial en el centro del tablero
    for(int j=0; j<xdim; j++)
      {
	board[steps+i][steps+j]=init_state[i][j];
      }
  
  for(int i=0; i<Ly; i++) //copiar el tablero al nuevo tablero
    for(int j=0; j<Lx; j++)
	new_board[i][j]=board[i][j];
}
void GameOfLife::Print_board(void)
{
  for (int i = 0; i < Ly; ++i)
    {
      for (int j = 0; j < Lx; ++j)
	{
	  std::cout << board[i][j] << " ";
	}
      std::cout << std::endl;
    }
  std::cout << std::endl;
}
void GameOfLife::Update()
{
  int Sum = 0;
  for(int i=0; i<Lx; i++)
    for(int j=0; j<Ly; j++)
      {
	Sum = Sum_neighbours(i,j);
	if(board[i][j]==1){
	  if(Sum<2 || Sum>3)
	    new_board[i][j]=0;
	}
	else{
	  if(Sum==3)
	    new_board[i][j]=1;}
      }
  
  for(int i=0; i<Ly; i++) //copiar el nuevo tablero al tablero
    for(int j=0; j<Lx; j++)
      board[i][j]=new_board[i][j];
}
void GameOfLife::Count_alive(void)
{
  int Sum=0;
  for(int i=0; i<Ly; i++) //copiar el nuevo tablero al tablero
    for(int j=0; j<Lx; j++)
      Sum+=board[i][j];

  std::cout << Sum << " ";
}
int GameOfLife::Sum_neighbours(int i, int j)
{
  if(i==0 and j==0)
    return board[i+1][j]+board[i+1][j+1]+board[i][j+1]; //esquina superior izquierda
  else if (i==0 and j==(Lx-1))
    return board[i][j-1]+board[i+1][j-1]+board[i+1][j]; //esquina superior derecha
  else if (i==(Ly-1) and j==0)
    return board[i-1][j]+board[i-1][j+1]+board[i][j+1]; //esquina inferior izquierda
  else if(i==(Ly-1) and j==(Lx-1))
    return board[i-1][j]+board[i-1][j-1]+board[i][j-1]; //esquina inferior derecha
  else if(i==0)
    return board[i][j-1]+board[i][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]; //lado de arriba
  else if(j==0)
    return board[i-1][j]+board[i+1][j]+board[i-1][j+1]+board[i][j+1]+board[i+1][j+1]; //lado izquierdo 
  else if (i==(Ly-1))
    return board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]; // lado de abajo
  else if (j==(Lx-1))
    return board[i-1][j-1]+board[i][j-1]+board[i+1][j-1]+board[i-1][j]+board[i+1][j]; //lado derecho
  else
    return board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]; //centro
}

int main(void)
{
  GameOfLife Game;
  Game.Start();
  for(int ii=0; ii<steps; ii++)
    {
      Game.Update();
      Game.Count_alive();
    }
  std::cout << std::endl;
  Game.Print_board();

  return 0;
}

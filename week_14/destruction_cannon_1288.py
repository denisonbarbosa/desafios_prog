def calc_destruction(projectiles, qt_projectiles, cannon_capacity):
  S = [ [0] * (cannon_capacity+1) for _ in range(qt_projectiles+1) ]   
  
  for i in range(1, qt_projectiles+1):
    for j in range(0, cannon_capacity+1):
      if projectiles[i-1][1] > j:
        S[i][j] = S[i-1][j]
      
      else:
        S[i][j] = max(S[i-1][j], projectiles[i-1][0] + S[i-1][j-projectiles[i-1][1]])
                
  return S[qt_projectiles][cannon_capacity]
  
def destruction_cannon():
  
  test_cases = int(input())
  
  while test_cases > 0:
    
    qt_projectiles = int(input())
    
    projectiles = list()
    for i in range(qt_projectiles):
      projectiles.append(list(map(int, input().split())))
    
    cannon_capacity = int(input())
      
    castle_resistance = int(input())

    if calc_destruction(projectiles, qt_projectiles, cannon_capacity) >= castle_resistance:
      print("Missao completada com sucesso")
    else:
      print("Falha na missao")
    
    test_cases -= 1
  

if __name__ == "__main__":
  destruction_cannon()
// Autor: Denison Massulo Barbosa

#include <iostream>
#include <list>

// Estrutura de uma mudança no campo de batalha 
typedef struct change{
    int value;
    int x;
    int y;
} change_t;

int main()
{
    // Inicializando as váriaveis de leitura
    int n_brothers, n_rows, n_cols, n_battles;
    
    // Loop principal do código
    while (true)
    {
        std::cin >> n_brothers >> n_rows >> n_cols >> n_battles;

        // Se tudo for igual a 0, sai do loop
        if (n_brothers == 0 && n_rows == 0 && n_cols == 0 && n_battles == 0)
            break;
        
        int battlefield[n_rows+2][n_cols+2];
        
        // Lista para armazenar as mudanças que devem ser feitas a cada iteração
        // Criei essa lista para evitar alterar o campo conforme ocorressem os ataques
        // e para evitar ter que duplicar o campo
        std::list<change_t> changes;

        // Lendo o campo inicial e setando as primeiras e as ultimas linhas e colunas com -1
        for (int i = 0; i < n_rows+2; i++) 
        {
            for (int j = 0; j < n_cols+2; j++)
            {
                if ((i == 0) || (i == n_rows + 1))
                {
                    battlefield[i][0] = -1;
                    battlefield[i][n_cols+1] = -1;
                }
                else if ((j == 0) || (j == n_cols+1))
                {
                    battlefield[0][j] = -1;
                    battlefield[n_rows+1][j] = -1;
                }
                else
                    std::cin >> battlefield[i][j];
            }
        }

        // Loop para calcular as iterações
        while (n_battles > 0)
        {
            // Limpando a lista de mudanças a cada iteração
            changes.clear();
            
            // Percorrendo só as linhas e colunas não preenchidas com -1
            for (int i = 1; i < n_rows+1; i++)
            {
                for (int j = 1; j < n_cols+1; j++)
                {
                    // Caso seja o último irmão, compara com o primeiro
                    if (battlefield[i][j] == n_brothers-1)
                    {
                        if (battlefield[i][j+1] == 0)
                            changes.push_back({battlefield[i][j], i, j+1});
                        
                        if (battlefield[i][j-1] == 0)
                            changes.push_back({battlefield[i][j], i, j-1});

                        if (battlefield[i-1][j] == 0)
                            changes.push_back({battlefield[i][j], i-1, j});
                        
                        if (battlefield[i+1][j] == 0)
                            changes.push_back({battlefield[i][j], i+1, j});
                    }
                    else
                    {
                        // Se a diferença entre os irmãos é de 1, então guarda a mudança
                        if ((battlefield[i][j+1] != -1) && 
                        ((battlefield[i][j+1] - battlefield[i][j]) == 1))
                            changes.push_back({battlefield[i][j], i, j+1});

                        if ((battlefield[i][j-1] != -1) && 
                        ((battlefield[i][j-1] - battlefield[i][j]) == 1))
                            changes.push_back({battlefield[i][j], i, j-1});
                        
                        if ((battlefield[i-1][j] != -1) &&
                        ((battlefield[i-1][j] - battlefield[i][j]) == 1))
                            changes.push_back({battlefield[i][j], i-1, j});

                        if ((battlefield[i+1][j] != -1) &&
                        ((battlefield[i+1][j] - battlefield[i][j]) == 1))
                            changes.push_back({battlefield[i][j], i+1, j});
                    }
                }
            }
            
            // Percorre a lista de mudanças e aplica no campo
            for (auto change : changes)
            {
                battlefield[change.x][change.y] = change.value;
            }

            n_battles--;
        }

        // Imprime o campo final
        for (int i = 1; i < n_rows+1; i++)
        {
            for (int j = 1; j < n_cols+1; j++)
            {
                if (j == n_cols)
                    std::cout << battlefield[i][j] << std::endl;

                else 
                    std::cout << battlefield[i][j] << " ";
            }
        }
    }
}
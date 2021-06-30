#include <iostream>
#include <math.h>

typedef std::pair<int, int> coord;

double calc_distance(coord p1, coord p2)
{
    double distance = pow((p2.first - p1.first), 2) + pow((p2.second - p1.second), 2);
    return sqrt(distance);
}

bool calc_triangle(coord p1, coord p2, coord p3)
{
    bool answer = false;

    double d_p1_p2 = calc_distance(p1, p2);
    double d_p1_p3 = calc_distance(p1, p3);
    double d_p2_p3 = calc_distance(p2, p3);

    if ((d_p1_p2 == d_p1_p3) && (d_p2_p3 != d_p1_p2))
    {
        answer = true;
    }
    else if ((d_p1_p2 == d_p2_p3) && (d_p1_p3 != d_p1_p2))
    {
        answer = true;
    }
    else if ((d_p1_p3 == d_p2_p3) && (d_p1_p2 != d_p1_p3))
    {
        answer = true;
    }

    return answer;
}

int main()
{
    while (true)
    {
        int n_coords, x, y;
        coord aux;
        std::cin >> n_coords;

        if (n_coords == 0)
            break;

        coord coords[n_coords];

        for (int i = 0; i < n_coords; i++)
        {
            std::cin >> aux.first >> aux.second;
            coords[i] = aux;
        }

        int n_sets = 0;

        for (int i = 0; i < n_coords - 2; i++)
        {
            for (int j = i + 1; j < n_coords - 1; j++)
            {
                for (int k = j + 1; k < n_coords; k++)
                {
                    if (calc_triangle(coords[i], coords[j], coords[k]) == true)
                    {
                        n_sets++;
                    }
                }
            }
        }

        std::cout << n_sets << std::endl;
    }
}
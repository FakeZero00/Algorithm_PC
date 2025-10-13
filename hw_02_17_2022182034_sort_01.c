#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  const char *name;
  int x, y;
} City;

City cities[] = {
    {"Clean", 1336, 536}, {"Prosy", 977, 860},  {"Rabbi", 6, 758},    {"Addle", 222, 261},
    {"Smell", 1494, 836}, {"Quite", 905, 345},  {"Lives", 72, 714},   {"Cross", 23, 680},
    {"Synth", 1529, 785}, {"Tweak", 1046, 426}, {"Medic", 1485, 514}, {"Glade", 660, 476},
    {"Breve", 1586, 448}, {"Hotel", 1269, 576}, {"Toing", 398, 561},  {"Scorn", 617, 373},
    {"Tweet", 1253, 403}, {"Zilch", 1289, 29},  {"React", 296, 659},  {"Fiche", 787, 278},
};

void City_print(City *c)
{
  printf("%s(%d,%d)", c->name, c->x, c->y);
}
void City_printAll(City *p, int count)
{
  for (int i = 0; i < count; i++, p++) {
    City_print(p);
    putchar(' ');
  }
  putchar('\n');
}

int City_comparator_name_asc(const void *a, const void *b)
{
    City* p1 = (City*)a;
    City* p2 = (City*)b;

    return strcmp(p1->name, p2->name);
}

int City_comparator_x_asc(const void* a, const void* b)
{
    City* p1 = (City*)a;
    City* p2 = (City*)b;

    return p1->x - p2->x;
}

int City_comparator_y_desc(const void* a, const void* b)
{
    City* p1 = (City*)a;
    City* p2 = (City*)b;

    return p2->y - p1->y;
}

int main(void) 
{
  const int Width = sizeof(cities[0]);
  const int Count = sizeof(cities) / sizeof(cities[0]);

  City_printAll(cities, Count);
  printf("\n");

  qsort(cities, Count, Width, City_comparator_name_asc);
  City_printAll(cities, Count);
  printf("\n");

  qsort(cities, Count, Width, City_comparator_x_asc);
  City_printAll(cities, Count);
  printf("\n");

  qsort(cities, Count, Width, City_comparator_y_desc);
  City_printAll(cities, Count);
  printf("\n");

  system("pause");
  return 0;
}
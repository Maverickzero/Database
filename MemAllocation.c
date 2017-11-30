#include <stdio.h>
#include <stdlib.h>

int main()
{
  int *numeros, quantidade; // A gente ainda n sabe quandos numeros vao ter, entao em vez de comecar com um vetor, a gente comeca com um pointer

  printf("Quantos numeros vc quer preencher? ");
  scanf("%d", &quantidade); // Preenche a quantidade de numeros que o vetor deve ter

  numeros = (int*)malloc(quantidade*sizeof(int));

  for(int i = 0; i < quantidade; i++)
  {
    printf("Entre o valor do numero %d: ", i+1);
    scanf("%d",&numeros[i]);
  }
  for(int i = 0; i < quantidade; i++)
  {
    printf("O valor do numero %d é %d.\n", i+1, numeros[i]);
  }

  free(numeros);

  return 1;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
  int *numeros, quantidade, quant_calc; // A gente ainda n sabe quandos numeros vao ter, entao em vez de comecar com um vetor, a gente comeca com um pointer

  printf("Quantos numeros vc quer preencher? ");
  scanf("%d", &quantidade); // Preenche a quantidade de numeros que o vetor deve ter

  numeros = (int*)malloc(quantidade*sizeof(int));
  quant_calc = sizeof(numeros)/sizeof(int);
  printf("Pointer aponta gora para um bloco de memoria de %ld bytes. "
         "Com um vetor de %d dimensoes.\n", 
         sizeof(numeros), quant_calc);

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

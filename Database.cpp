#include <stdio.h>
int main ()
{
    int codigo, conf_cont=0;
    float matriz[5][2], deposit, num_cont, saque, saldo_geral=0;
    for (int i=0;i<5;i++)
    //Teste
    {
        for (int j=0;j<=0;j++)
        {
            printf("Informe o numero da conta %d: ", i);
            scanf ("%f", &matriz[i][j]);
        }
        for (int j=1;j<=1;j++)
        {
            printf ("Informe o saldo da conta %d: ", i);
            scanf ("%f", &matriz[i][j]);
        }
        printf ("\n");
    }
    do
    {
            printf ("Insira o codigo das seguintes operacoes:\n\t\
	            1. Efetuar um depósito em uma conta\n\t\
		    2. Efetuar um saque de uma conta\n\t\
		    3. Consultar o saldo de uma conta\n\t\
		    4. Consultar o saldo geral\n\t\
		    5. Finalizar o programa:\n\n\t "); 
		    // Antes da mudanca os dois pontos eram depoist do \t
            scanf ("%d", &codigo);
            switch (codigo){
            case 1:
                printf("Digite o numero da conta: ");
                scanf("%f",&num_cont);
                printf("Digite o valor do deposito: ");
                scanf("%f",&deposit);
                printf("\n");
                for(int i=0; i<=4; i++)
                {
                    if (num_cont==matriz[i][0])
                    {
                        matriz[i][1] = matriz[i][1] + deposit;
                        printf("A conta tem agora %f\n\n",matriz[i][1]);
                        conf_cont = 1;
                    }

                }
                    if(conf_cont==0)
                    {
                    printf("\nConta inexistente\n\n");

                    }
                break;
                case 2:
                printf("Digite o numero da conta: ");
                scanf("%f",&num_cont);
                printf("Digite o valor do saque: ");
                scanf("%f",&saque);
                printf("\n");
                for(int i=0; i<=4; i++)
                {
                    if (num_cont==matriz[i][0])
                    {
                        conf_cont = 1;
                        if(saque>matriz[i][1])
                        {
                        printf("\nSaldo insuficiente\n\n");
                        break;
                        }
                        matriz[i][1] = matriz[i][1] - saque;
                        printf("A conta tem agora %f\n\n",matriz[i][1]) ;
                    }
                }
                if(conf_cont==0)
                    {
                    printf("\nConta inexistente\n\n");

                    }
                break;
                case 3:
                printf("Digite o numero da conta: ");
                scanf("%f",&num_cont);
                for(int i=0; i<=4; i++)
                {
                    if (num_cont==matriz[i][0])
                    {
                        matriz[i][1] = matriz[i][1];
                        printf("\nA conta tem: %f\n\n",matriz[i][1]) ;
                        conf_cont = 1;
                    }
               }
               if(conf_cont==0)
                    {
                    printf("\nConta inexistente\n\n");

                    }
               break;

               case 4:

               for(int i=0; i<=4; i++)
                {
                 saldo_geral = saldo_geral + matriz[i][1];
                }
                 printf("\nO saldo geral e: %f\n\n",saldo_geral);
                 break;
            }
            saldo_geral=0;
            conf_cont = 0;
    } while(codigo != 5);
}

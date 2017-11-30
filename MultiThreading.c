#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define NTHREADS 2

sem_t sem;
char string[24];

void *wait(void *x)
{
  sem_wait(&sem); // Esperar até o usuario der uma string para mostrar para a gente
  printf("Voce digitou: %s\n", string);
  return NULL;
}

void *input(void *x)
{
  printf("Digite algo para o outro thread fazer printf: "); 
  scanf("%[^\n]", string);
  sem_post(&sem); // Mandar sinal dizendo que o outro thread pode continuar
  return NULL;
}

int main(int argc, char *argv[])
{
  pthread_t threads[NTHREADS];
  int thread_args[NTHREADS];
  int rc, i;
  sem_init(&sem, 0, 0);

  /* spawn the threads */
  thread_args[0] = 1;
  thread_args[1] = 2;
  rc = pthread_create(&threads[0], NULL, wait, (void *) &thread_args[1]);
  rc = pthread_create(&threads[1], NULL, input, (void *) &thread_args[2]);

  /* wait for threads to finish */
  for (i=0; i<NTHREADS; ++i) {
    rc = pthread_join(threads[i], NULL);
  }

  return 1;
}

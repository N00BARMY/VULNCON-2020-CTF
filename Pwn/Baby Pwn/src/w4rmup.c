#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
  setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    alarm(20);  
  char overflowthis[16];
  gets(overflowthis);
  printf("%d\n");

  
}
int overflowed(){
  system("/bin/sh");
}

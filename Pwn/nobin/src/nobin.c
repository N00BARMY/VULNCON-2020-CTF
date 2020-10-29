#include <stdio.h>
#include <stdlib.h>

int check;

int main() {
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
  setvbuf(stderr,0,2,0);
  alarm(20);
  char buf[256];
  fgets(buf, sizeof(buf), stdin);
  printf(buf, "\n");
  exit(0);
}

int shell() {
  if(check == 0x1337) {
    system("/bin/sh");
  }
  printf("Not that easy...\n");
}

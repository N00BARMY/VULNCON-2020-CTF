#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
  setvbuf(stderr,0,2,0);
  alarm(20);
  char buf[64];
  for(int i = 1; i <= 2; i++) {
    memset(buf, 0, 64);
    read(0, buf, 640);
    printf("%s\n", buf);
  }
  printf("TryHarder\n");
  return 0;
}

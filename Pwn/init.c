#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init() {
  alarm(0x20);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
}

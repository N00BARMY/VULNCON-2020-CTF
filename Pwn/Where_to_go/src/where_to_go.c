#include <stdio.h>

int main() {
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
  setvbuf(stderr,0,2,0);
  alarm(20);
  write(1, "Hello!\n", 7);
  getinput();
}

int getinput() {
  char buf[32];
  read(0, buf, 320);
}

int vuln() {
  int *ptr = &main;
  int *leak = &ptr;
  write(1, leak, 6);
  main();
}

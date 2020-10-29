#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
  setvbuf(stderr,0,2,0);
  alarm(20);
  char name[128];
  system("echo -n 'Enter your name: '");
  gets(name);
  if(strcmp(name, "w3lc0m3")) {
    exit(0);
  }
}

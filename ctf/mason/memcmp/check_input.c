// A conversion to c of check_input from ghidra
#include <stdio.h>

unsigned long check_input(void)
{
  int increment;
  unsigned int val;
  char err [25];
  int *err_loc;

  generate_error_1();
  err_loc = __errno_location();

  int i;
  for (i = 0; i < 25; i = i + 1){
    err[i] = *err_loc;
  }

  unsigned read_string;
  read_string = 0;
  printf("Enter a value: ");

  fgets((char *)&read_string,0x32,stdin);

  val = 0x1a;
  increment = 0;
  while (increment < 0x19) {
    if (*(char *)((long)&read_string + (long)increment) == err[increment]) { // ALL VALUES OF ERR ARE THE SAME
      val = val - 1;
    }
    increment = increment + 1;
  }
  return (unsigned long)val;
}
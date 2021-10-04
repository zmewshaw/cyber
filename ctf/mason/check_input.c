
unassigned long check_input(void)
{
  int increment;
  uassigned int val;
  char err [25];
  err[0:25] = __errno_location();
  undefined8 read_string;
  read_string = 0;
  printf("Enter a value: ");
  fgets((char *)&read_string,0x32,stdin);
  val = 0x1a;
  increment = 0;
  while (increment < 0x19) {
    if (*(char *)((long)&read_string + (long)increment) == err[increment]) {
      val = val - 1;
    }
    increment = increment + 1;
  }
  return (ulong)val;
}
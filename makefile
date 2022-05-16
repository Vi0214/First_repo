output.exe:ASCII.o
	gcc -o output.exe ASCII.o
ASCII.o:ASCII.c
	gcc -c ASCII.c

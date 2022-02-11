all: dynamic_block static_block
clean:
	   rm dynamic_block static_block block.o lib.a lib.so program.o 
static_block: program.o lib.a
		cc program.o lib.a -o static_block
dynamic_block: program.o lib.so
	  cc program.o lib.so -o dynamic_block -Wl,-rpath .
block.o: block.c
		cc -fPIC block.c -o block.o
block.o: block.c
	  cc -c block.c -o block.o
lib.a: block.o
		ar qc lib.a block.o
lib.so: block.o
		cc -shared -o lib.so block.o
program.o: program.c
		cc -c ../program.c -o program.o
program.c: ../headers/block.h

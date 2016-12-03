#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "util.h"

#define MAX_CSV_SIZE 1024

void fatal(char*);
void *ec_malloc(unsigned int);
char *getField(char*, int);

void usage (char *program) {
	printf("%s: <file with CSV sudoku file>", program);
	exit(1);
}

int main (int argc, char *argv[]) {
	if (argc < 2)
		usage(argv[0]);
}

char *getField (char *line, int num) {
	const char *tok;
	for (tok = strtok(line, ","); tok && *tok; tok = strtok(NULL, ",\n")) {
		if (!--num)
			return tok;
	}
	return NULL;
}
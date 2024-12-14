#include <stdio.h>

char INPUT[8] = "1_input";

int main() {
	FILE *input = fopen(INPUT, "r");
	char text[12];
	fscanf(input, text);
	fclose(input);	
	printf("%s", text);
	return 0;
}

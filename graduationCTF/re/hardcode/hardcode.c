#include <stdio.h>

int main() {

	char password[64];
	char flag[64];
	FILE *fptr;
	printf("Enter the password to retrieve the flag: ");
	gets(password);
	if(strcmp(password, "GottaReverseMe!") == 0){
		printf("You found the flag!\n");
		fptr = fopen("flag.txt", "rb");
		if(fptr == NULL){
			printf("Flag file missing! Try on the remote server.\n");
			exit(1);
		}
		else {
			fscanf(fptr, "%s", &flag);
			printf("%s\n", flag);
		}
		fclose(fptr);
	}
	else
		printf("Nope. Thats not it.\n");

	return 0;
}

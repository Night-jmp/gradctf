#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void flag() {
	FILE *fptr;
	char flag[64];

	printf("You found the flag!\n");
	fptr = fopen("flag.txt", "rb");
        if(fptr == NULL){
        	printf("Flag file missing! Try on the remote server.\n");
		exit(1);
        }
        else {
                fscanf(fptr, "%s", flag);
                printf("%s\n", flag);
	}
        fclose(fptr);
}

void getSpell() {

	char spell[128];
	
	printf("You shall not pass!\n");
	printf("But if you get the spell right, you may: ");
	scanf("%s",spell);

	if(strcmp(spell, "Avada_Kedavra") == 0)
		printf("Cool I guess. You may pass. Live long a prosper.\n");
	else
		printf("I find your lack of faith disturbing.\n");
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0); 
	getSpell();
	return 0;
}

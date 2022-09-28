#include <stdio.h>
#include <string.h>
#include <stdlib.h>

__attribute__((constructor)) void ignore_me() {
        setbuf(stdin, NULL);
        setbuf(stdout, NULL);
        setbuf(stderr, NULL);
}


void flag() {
	
        FILE *fptr;
        char flag[64];
        unsigned int selection = 0;
        printf("Make a selection:\n");
        printf("Authenticate with password:             1)\n");
        printf("Authenticate with retinal scan:         2)\n");
        printf("Bypass authentication:                  3)\n"); 
	scanf("%d", &selection);

	if((short)abs(selection) >= 0){
		if(selection == 1){

			printf("Enter the password: ");
			char pass[32];
                        scanf("%s", pass);
                        if(strcmp(pass, "AdAstraPerAspera") == 0)
                                printf("Authenticated! But no flag for you!\n");
                        else
				printf("Acccess Denied!\n");
                }
                else if(selection == 2)
                        printf("Error! No retinal scanner found!\n");
                else if(selection == 3)
                        printf("Authorization required!\n");
        }
        else {
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
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0); 
	printf("Solar Array Deployer 2.0\n");
	printf("WARNING! Attack detected. Defaulting to authentication mode.\n");
	flag();
	return 0;
}

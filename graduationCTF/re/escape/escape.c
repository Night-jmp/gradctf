#include <stdio.h>

void print_flag(){
        FILE *fp = fopen("flag.txt", "r");
        char c;
	printf("Connection established.\nEscape Shuttle Deployed\nNew message from shuttle:\n");
        if(!fp){
                printf("Could not print flag.\n");
		return;
        }
        c = fgetc(fp);
        while ( c != EOF ){
                printf("%c", c);
                c = fgetc(fp);
        }
        fclose(fp);	
}

int check_password(char *code0, char *code1, char *code2){
	if(code0[0] != 'y') return 0;
	else if(code0[3] != 'g') return 0;
	else if(code0[6] != 'i') return 0;
	else if(code1[1] != 'o') return 0;
	else if(code1[4] != 'o') return 0;
	else if(code1[7] != 't') return 0;
	else if(code2[2] != 'u') return 0;
	else if(code2[5] != 't') return 0;
	else if(code2[8] != '!') return 0;
	return 1;
}

void main(void){
	setvbuf(stdout, NULL, _IONBF, 0); 	

	char codes[3][9];
	printf("---- Emergency Shuttle System ----\nEnter three control codes:\n");
	scanf("%9s", codes[0]);
	scanf("%9s", codes[1]);
	scanf("%9s", codes[2]);
	
	if(check_password(codes[0], codes[1], codes[2])){
		print_flag();
	} else {
		printf("Incorrect\n");
	}
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//This binary is a reverse engineering crackme style hash break.
//First, create a function that asks for the airlock password
//Next, hash the passcode and check it against a static hash
//If the password is valid, grant entry
#define PHRASE_LENG 32


char* hash(char* pt){
	char* ct;
	ct = malloc(32);

	for(int i = 0; i < strlen(pt) - 1; i++){
		ct[i] = (pt[i] ^ 'w') + 40;
	}
	return ct;
}

int main() {
	
	char passphrase[PHRASE_LENG];
	char cipher[PHRASE_LENG];
	char hashed[PHRASE_LENG];
	printf("-----Airlock manual override-----\n");
	printf("\n");
	printf("Authentication phrase: ");
	fgets(passphrase, PHRASE_LENG, stdin);
	
	strncpy(hashed, hash(passphrase), strlen(passphrase));
	if(strcmp(hashed, "9F+,:<4<-k<DnA8P+GlPGk,Gl,P9*AP2") == 0){
		fprintf(stdout, "Airlock has successfully been overridden.\n");
		printf("Nice!");
	}
	else{
		fprintf(stdout, "Authentication failure! Aborting manual override.\n");
		fprintf(stdout, "Error code: 31084\nWARNING!!\n");
		fprintf(stdout, "Airlock is currently scheduled to open at 0200UTC\n");
		fprintf(stdout, "Make sure all crewmembers have egressed!\n");
	}
	return 0;
}

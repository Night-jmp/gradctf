#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void ignore_me() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void print_flag(){

	FILE* fd;
	char ch;
	char flag[100];
	fd = fopen("flag.txt", "r");
	
	do
	{
		ch = fgetc(fd);
		printf("%c", ch);
	} while (ch != EOF);
	printf("\n");
}

void vuln()
{
	char name[10];
	printf("Username: ");

	char mode[10];	
	strcpy(mode, "noob");

	gets(&name);
	if(strcmp(mode, "hax0r") == 0)
	{
		printf("So leet\n");
		print_flag();
	}

}

int main(){
	vuln();	
	return 0;
}

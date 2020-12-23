#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<stdlib.h>
#include<stdio.h>

int main()
{
	int s,r,recb,sntb,x,ns,a=0;
	printf("INPUT port number: ");
	scanf("%d", &x);
	socklen_t len;
	struct sockaddr_in server,client;
	char buff[50];

	s=socket(AF_INET,SOCK_STREAM,0);
	if(s==-1)
	{
		printf("\nSocket creation error.");
		exit(0);
	}
	printf("\nSocket created.");

	server.sin_family=AF_INET;
	server.sin_port=htons(x);
	server.sin_addr.s_addr=htonl(INADDR_ANY);

	r=bind(s,(struct sockaddr*)&server,sizeof(server));
	if(r==-1)
	{
		printf("\nBinding error.");
		exit(0);
	}
	printf("\nSocket binded.");

	r=listen(s,1);
	if(r==-1)
	{
		close(s);
		exit(0);
	}
	printf("\nSocket listening.");

	len=sizeof(client);

	ns=accept(s,(struct sockaddr*)&client, &len);
	if(ns==-1)
	{
		close(s);
		exit(0);
	}
	printf("\nSocket accepting.\n");
	char arr[50];
    recb=recv(ns,arr,sizeof(arr),0);
	if(recb==-1)
	{
		printf("\nMessage Recieving Failed");
		close(s);
		close(ns);
		exit(0);
	}
	puts(arr);
	//printf("\n");
    //printf("%i ", htonl(client.sin_addr.s_addr));
    //printf("\n %i", htons(client.sin_port));
   // printf("\n %i", htonl("127.0.0.1"));
    printf("\n");
    char IP[50];
    recb=recv(ns,IP,sizeof(IP),0);
    strcat(IP,":");
    strcat(IP,"3000");
    puts(IP);
FILE * fTemp;
    char fil[50];
	if( access( "temp.txt", F_OK ) != -1 ) {
    // file exists
            	fTemp = fopen("temp.txt", "w");
            	fputs(IP, fTemp);
	} else {
    // file doesn't exist
		strcpy(buff,"File does not exist!");
	}

    char changedBuff[50];
    int i;
    for(i = 0; i<strlen(IP);i++)
	{
	if(IP[i]=='.'){
        strcat(changedBuff,"dot");
	}
	else if(IP[i]==':'){
            strcat(changedBuff,"colon");

	}
	else{
        char x[2];
        x[0] =IP[i];
        x[i] ='\0';
        //printf("%s",x);
        printf("\n");
        strcat(changedBuff,x);
	}
	}
	puts(changedBuff);
/*
	sntb=send(ns,changedBuff,sizeof(changedBuff),0);
	{
		close(s);
		close(ns);
		printf("\nMessage Sending Failed");
		exit(0);
	}
	*/
	close(ns);
	close(s);
}

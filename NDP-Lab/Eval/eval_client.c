#include<string.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<fcntl.h>
#include<sys/stat.h>
int main()
{
	int s,r,recb,sntb,x,i,j;
	printf("INPUT port number: ");
	scanf("%d", &x);
	struct sockaddr_in server;
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
	server.sin_addr.s_addr=inet_addr("127.0.0.1");

	r=connect(s,(struct sockaddr*)&server,sizeof(server));
	if(r==-1)
	{
		printf("\nConnection error.");
		exit(0);
	}
	printf("\nSocket connected.");

	int ch=1;
	int a[50];
	char arr[50],IP[50];
	int n;
    strcpy(arr,"Hello from client");
	sntb=send(s,arr,sizeof(arr),0);

	if(sntb==-1)
	{
		close(s);
		printf("\nMessage Sending Failed");
		exit(0);
	}

    strcpy(IP,"127.0.0.1");

    sntb=send(s,IP,sizeof(IP),0);
	if(sntb==-1)
	{
		close(s);
		printf("\nMessage Sending Failed");
		exit(0);
	}


    char buff2[50];
    recb=recv(s,buff2,sizeof(buff2),0);

	if(recb==-1)
	{
		close(s);
		printf("\nMessage Recieving Failed");
		exit(0);
	}
	printf("\n");
	puts(buff2);
	close(s);

}

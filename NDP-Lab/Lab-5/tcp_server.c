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
	char buff[50],buff2[50];

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

	r=listen(s,2);
	if(r==-1)
	{
		close(s);
		exit(0);
	}
	printf("\nSocket listening.");
    int count =0;
    while(1){

	len=sizeof(client);
	ns=accept(s,(struct sockaddr*)&client, &len);
    if(ns==-1)
	{
		close(s);
		exit(0);
	}
	int childpid,n;
	printf("\nSocket accepting.\n");
	if((childpid == fork()) == 0){
		printf("\nChild process to deal with multiple clients. \n");
		while((n = recv(ns,buff,sizeof(buff),0))>0){
		count++;

    if(count>2){
    char buffer[30];
        strcpy(buffer,"terminate");
        sntb=send(ns,buffer,sizeof(buffer),0);
        close(ns);
        close(s);
    }

            FILE *fTemp;
        char fil[50];
	if( access( "temp.txt", F_OK ) != -1 ) {
    // file exists
    puts(buff);
            	fTemp = fopen("temp.txt", "a");
            	fputs(buff, fTemp);
            	fclose(fTemp);
	} else {
    // file doesn't exist
		strcpy(buff,"File does not exist!");
	}
		}
    //puts(buff);
	}

}

	close(ns);
	close(s);
}

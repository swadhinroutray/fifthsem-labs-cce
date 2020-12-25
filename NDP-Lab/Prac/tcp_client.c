#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#define MAXSIZE 90

int main () {

    struct sockaddr_in server, client;
    int recvbytes, sendbytes;
    char buff[50];

    int s = socket(AF_INET,SOCK_STREAM,0);
    if(s==-1){
        printf("Socket Creation error");
        exit(0);
    }
    server.sin_port = htons(1337);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("127.0.0.1"); 
    
    int recvConn = connect(s,(struct sockaddr *)&server, sizeof(server));
    if(recvConn==-1){
        printf("\nError in Connecting");
        close(s);
    }
    //  recvbytes = recv(s,buff,sizeof(buff),0);
    // if(recvbytes==-1){
    //     printf("\nError in Recieving");
    //     close(s);
    // }
    // puts(buff);
    // printf("\n Enter Something: ");
    
    char sendServer[50],sendServer1[50];
    // memset()
    // memset(sendServer1,"",sizeof(char)*strlen(sendServer1));
    // memset(sendServer,"",sizeof(char)*strlen(sendServer));
        gets(sendServer);
    strcpy(sendServer1,"1");    
    strcat(sendServer1,sendServer);
    strcat(sendServer1,"\0");
    int sentBytes = send(s,sendServer1,sizeof(sendServer1),0);
    if(sentBytes==-1){
        printf("\nError in Sending");
        close(s);
    }
    close(s);

}
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#define MAXSIZE 90

char* reverseStr(char str[MAXSIZE])
{
    int i;
    int n = strlen(str);
    // Swap character starting from two
    // corners
    for ( i = 0; i < n / 2; i++){
        char temp = str[i];
        str[i] = str[n-i-1];
        str[n-i-1] = temp;
    }
        return str;
    }


int checkPalindrome(char *str){
    int l = 0;
    int h = strlen(str) - 1;
      while (h > l)
    {
        if (str[l++] != str[h--])
        {
        return 0;
        }
    }
        return 1;
    }
int main()
{
	int sockfd,newsockfd,retval,i;
	socklen_t actuallen;
	int recedbytes,sentbytes;
	struct sockaddr_in serveraddr,clientaddr;

	char buff[MAXSIZE];
	int a=0;
	sockfd=socket(AF_INET,SOCK_DGRAM,0);

	if(sockfd==-1)
	{
		printf("\nSocket creation error");
	}
	clientaddr.sin_family=AF_INET;
	clientaddr.sin_port=htons(3389);
	clientaddr.sin_addr.s_addr=htons(INADDR_ANY);


	serveraddr.sin_family=AF_INET;
	serveraddr.sin_port=htons(3388);
	serveraddr.sin_addr.s_addr=htons(INADDR_ANY);

	retval=bind(sockfd,(struct sockaddr*)&serveraddr,sizeof(serveraddr));
	if(retval==1)
	{
		printf("Binding error");
		close(sockfd);
	}
    int flag =1;
	for (i = 0; ; i+=1)
	{


		actuallen=sizeof(clientaddr);
		recedbytes=recvfrom(sockfd,buff,sizeof(buff),0,(struct sockaddr*)&clientaddr,&actuallen);

		if(recedbytes==-1)
		{
			printf("Reciving error\n");
			close(sockfd);
		}

		puts(buff);
        char *p;
        p = reverseStr(buff);
        printf("\n");
        puts(p);
        if(checkPalindrome(p)){
            char buff2[MAXSIZE];
            buff2[0] = strlen(buff);
            int j;
            int cnt =0;
            for(j =0; j<buff2[0];j++){
                    if(buff[j]=='a'||buff[j]=='e'|| buff[j]=='i'|| buff[j]=='o' || buff[j]=='u')
                    cnt ++;
                }
                printf("%d",cnt);
                char num_str[20];
                sprintf(num_str, "%d", cnt);
                strcat(buff2," ");
                strcat(buff2, num_str);
                printf("%s",buff2);
            sentbytes=sendto(sockfd,buff2,sizeof(buff2),0,(struct sockaddr*)&clientaddr,sizeof(clientaddr));
            flag =0;
            continue;

            }
		printf("\n");

		if (buff[0] == 'h' && buff[1] == 'a' && buff[2] == 'l' && buff[3] == 't')
		{
			break;
		}

        if(flag ==1){
		char x[MAXSIZE] = "Please try again";
		sentbytes=sendto(sockfd,x,sizeof(x),0,(struct sockaddr*)&clientaddr,sizeof(clientaddr));
		if(sentbytes==-1)
		{
			printf("sending error");
			close(sockfd);
		}

		if (buff[0] == 'h' && buff[1] == 'a' && buff[2] == 'l' && buff[3] == 't')
		{
			break;
		}
        }
	}



	close(sockfd);
	close(newsockfd);
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#define MAXSIZE 90

// char reverseLines(char lines[50]){
//     puts(lines);
//     return lines;
// }
int main()
{

    struct sockaddr_in server, client;
    int recvbytes, sendbytes;
    char buff[50];
    socklen_t actualLen;
    int s = socket(AF_INET, SOCK_STREAM, 0);
    if (s == -1)
    {
        printf("\nSocket Creation error");
        exit(0);
    }
    server.sin_port = htons(1337);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = htons(INADDR_ANY);
    int pid_C;
    int recval = bind(s, (struct sockaddr *)&server, sizeof(server));
    if (recval == -1)
    {
        printf("\nError in binding");
        close(s);
    }
    recval = listen(s, 1);
    if (recval == -1)
    {
        printf("\nError in Listening");
        close(s);
    }
    int ns;
    while (1)
    {
        actualLen = sizeof(client);
        ns = accept(s, (struct sockaddr *)&client, &actualLen);
        if (ns == -1)
        {
            printf("\nError in accepting");
            close(s);
        }

        if ((pid_C == fork()) == 0)
        {
            char recvBuff[50];
            while ((recvbytes = recv(ns, recvBuff, sizeof(recvBuff), 0)) > 0)
            {

                // printf("\nMessage from Client \n");
                // puts(recvBuff);
                if (recvBuff[0] == '1')
                {
                    //client1 calculations
                    char newBuff[50];
                    memset(newBuff, "", sizeof(char) * strlen(newBuff));
                    // strcpy(newBuff,"");
                    // newBuff = reverseLines(recvBuff);
                    strcpy(newBuff, recvBuff);

                    // strcat(newBuff,"\0");
                    puts(newBuff);
                    // printf("%s ",newBuff);
                    FILE *ftemp;
                    char F[512];
                    if ( access("temp.txt", F_OK) == -1)
                    {
                        
                        printf("\nLife ke laudasdasdde");
                        close(s);
                        exit(0);
                    }
                    ftemp = fopen("temp.txt", "r");
                        while (fgets(F, 512, ftemp) != NULL)
                        {
                            puts(F);
                            
                        }
                        fclose(ftemp);
                }
                else if (recvBuff[0] == '2')
                {
                    //client2 calculation
                    char digits[50];
                    printf("Input Alphabets: ");
                    gets(digits);
                    sendbytes = send(ns, digits, sizeof(digits), 0);
                    if (sendbytes == -1)
                    {
                        printf("Error Sending");
                    }
                }
            }
        }
    }
    close(s);
    close(ns);
}
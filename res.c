#include <stdio.h> 
#include <stdlib.h> 

struct response
{
    char * header_code;
    char * header_type;
    char * data;
};

struct reponse * procResponse(char * path) {
    struct response * res = malloc(sizeof(struct response));
    res-> header_type = "Content-Type: text/html \r\n";
    FILE* file;
    file = fopen(path, "r");
    if (file == NULL) 
        res-> header_code = "404 Not Found";
        return res;
   
    while (fgetc(file) != EOF) {
        if (feof(file))
            res-> header_code = "500 Internal Server Error";
            break;
        res-> data = fgetc(file);
        res-> data ++;
    }
    res-> data = "\0";
    res -> header_code = "200 OK";
    return res;
    
}
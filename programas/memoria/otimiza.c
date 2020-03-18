#include<stdio.h>
#include<stdlib.h>
#include<string.h>


#define OUT
#define DEBUG
#define MY_INPUT


FILE *_my_input;

#ifdef MY_INPUT
#define INPUT _my_input
#else
#define INPUT stdin
#endif


#ifdef OUT
#define PRINT(x, ...)\
    printf(x,##__VA_ARGS__);
#else
#define PRINT(...)
#endif
#ifdef DEBUG
#define LOG(x, ...)\
    printf("\nlog--->");\
    printf(x,##__VA_ARGS__);\
    printf("\n");
#else
#define LOG(...)
#endif

typedef struct _arq {
    char name[50];
    char existo;
    unsigned int size;
    int index;
    struct _arq *next;
} *arq, Arq;
typedef struct {
    arq files;
    int size_max;
} Disc, *disc;

unsigned int inputSize() {
    char str[30];
    fgets(str, 30, INPUT);

    return atoi(str);
}

int len(char *str) {
    int i;
    for (i = 0; str[i]; i++);
    return i;
}

void inputStr(char *buff, int size, FILE *inp) {
    // fflush(inp);
    fgets(buff, size, inp);
    int length = len(buff);
    if (buff[length - 1] == '\n') {
        buff[length - 1] = 0;
    }
    //fflush(inp);
}

void addFile(disc d) {
    Arq tmp = {0};
    arq last = NULL;
    arq atual = d->files;

    PRINT("Nome do arquivo: ");
    inputStr(tmp.name, 50, INPUT);

    PRINT("Tamanho do arquivo:");
    tmp.size = inputSize();

    tmp.existo = 1;
    while (atual) {
        LOG("Achando atual\n")
        last = atual;
        atual = atual->next;
    }
    if (!last) {// d->files é nulo
        LOG("Disco esta nulo\n")
        tmp.index = 0;
        d->files = calloc(1, sizeof(Arq));
        *d->files = tmp;

    } else {
        LOG("Disco nao esta nulo\n")
        tmp.index = last->index + 1;
        last->next = calloc(1, sizeof(Arq));
        *last->next = tmp;
    }
}

void showArq(arq aq) {
    if (!aq)
        return;
    PRINT("    Nome :%s\n", aq->name)
    PRINT("    Tamanho = %d\n", aq->size)
    PRINT("    index = %d\n\n", aq->index)
}

void show(disc c) {
    unsigned int size = 0;
    arq tmp = c->files;

    while (tmp) {
        if (tmp->existo)
            size += tmp->size;
        tmp = tmp->next;
    }
    PRINT("Tamanho total = %d \n", c->size_max)
    PRINT("disponivel %d\n", (c->size_max - size) / 8 * 8)
    PRINT("utilizado %d\n", size)
    PRINT("Arquivos :\n")
    tmp = c->files;
    while (tmp) {
        if (tmp->existo) {
            showArq(tmp);
        }
        tmp = tmp->next;
    }

}

void liberar(arq c) {
    if (c) {
        liberar(c->next);
        LOG("liberando arq")
        showArq(c);
        free(c);
    }

}

void delete(char *name, disc c) {
    arq tmp = c->files;
    for (; tmp && tmp->existo && !strcmp(tmp->name, name); tmp = tmp->next);
    if (tmp)
        tmp->existo = 0;

}
// a b c d
// 
void voltaP(arq f){
    arq last =f;
    arq at = f->next;
    while (at){
        
    }
}
void otimiza(disc c) {
    arq  at = c->files;
    while(at){
        if(!at->existo){
            voltaP(at);
        }
    }
}

int main() {
#ifdef MY_INPUT
    _my_input = fopen("../input.txt", "r");
#endif

    Disc c = {0};
    char comand[100] = {0};
    PRINT("insira o tamanho do disco: ")
    c.size_max = inputSize();
    disc pc = &c;
    inputStr(comand, 100, INPUT);
    if (!strcmp(comand, "adiciona")) {
        addFile(pc);
    } else if (!strcmp(comand, "remove")) {
        inputStr(comand, 50, INPUT);
        delete(comand, pc);
    } else if (!strcmp(comand, "otimiza")) {
        otimiza(&pc->files);
    } else {
        PRINT("ERROR: comannd not found\n")
    }
    liberar(pc->files);
    c = (Disc) {0};

#ifdef MY_INPUT
    fclose(_my_input);
#endif
}

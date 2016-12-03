// Error logging
void fatal (char *message) {
    char msg[100];

    strcpy(msg, "[!] Error ");
    strncat(msg, message, 100);
    perror(msg);
    exit(-1);
}

// Error-checked malloc
void *ec_malloc (unsigned int size) {
    void *ptr;
    ptr = malloc(size);
    if (ptr == NULL)
        fatal("in ec_malloc() on memory allocation");
    return ptr;
}
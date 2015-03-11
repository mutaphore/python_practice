#include <stdio.h>
#include <string.h>

int strStr(char *haystack, char *needle) {
	char *p, *q;
	int i;

	for (i = 0; i <= strlen(haystack) - strlen(needle); i++) {
		p = haystack + i;
		q = needle;
		while (*q && *p == *q)
			q++;
		if (*q == 0)
			return i;
	}
	return -1;
}

int main() {
	char *haystack = "hello world";
	char *needle = "world";

	printf("Index of %s in %s is %d", needle, haystack, strStr(haystack, needle));
}
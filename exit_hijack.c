#include "stdio.h"

extern void *_rtld_global;

/* this is the offset we want to auto find */
int rtld_offset = -520;

void win()
{
	puts("OK");
}

void vul()
{
	size_t *target = (size_t *)(_rtld_global + rtld_offset);
	*(target) = &win;
	exit(0);
}

int main()
{
	vul();
}

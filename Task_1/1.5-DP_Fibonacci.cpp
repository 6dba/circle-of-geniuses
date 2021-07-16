#include <iostream>

int fib(int n) {
	
	const int MAXN = 1000;
	
	// Ïî óìîë÷àíèþ ìàññèâ èíèöèàëèçèðóåòñÿ íóëÿìè
	static int c[MAXN];

	if (n <= 0) return 0;

	if (n == 1) return 1;
	
	// Åñëè åñòü çíà÷åíèå ïî èíäåêñó -> âîçâðàùàåì
	if (c[n] > 0) return c[n];
	
	// Åñëè íåò - âû÷èñëÿåì
	return c[n] = fib(n-1) + fib(n-2);
}

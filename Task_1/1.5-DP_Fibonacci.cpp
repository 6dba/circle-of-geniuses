#include <iostream>

int fib(int n) {
	const int MAXN = 1000;
	
	// массив для осуществления принципа мемоизации
	static int c[MAXN];

	if (n <= 0) return 0;

	if (n == 1) return 1;
	
	// если элемент по индексу n присутсвует в массиве -> возвращаем
	if (c[n] > 0) return c[n];
	
	// иначе - рекурсивно вычисляем
	return c[n] = fib(n-1) + fib(n-2);
}

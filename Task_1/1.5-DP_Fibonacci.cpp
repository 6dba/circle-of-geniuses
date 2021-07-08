#include <iostream>

int fib(int n) {
	
	const int MAXN = 1000;
	
	// По умолчанию массив инициализируется нулями
	static int c[MAXN];

	if (n == 0) return 0;

	if (n == 1) return 1;
	
	// Если есть значение по индексу -> возвращаем
	if (c[n] > 0) return c[n];
	
	// Если нет - вычисляем
	return c[n] = fib(n-1) + fib(n-2);
}

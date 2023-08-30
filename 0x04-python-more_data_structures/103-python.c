#include <Python.h>

/**
 * print_python_bytes - Printing by information
 * @p: Python Obj
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, d, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (d = 0; d < limit; d++)
		if (string[d] >= 0)
			printf(" %02x", string[d]);
		else
			printf(" %02x", 256 + string[d]);

	printf("\n");
}

/**
 * print_python_list - Pr list information
 * @p: Python O
 * Return: return ob
 */
void print_python_list(PyObject *p)
{
	long int sizee, h;
	PyListObject *list;
	PyObject *obj;

	sizee = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sizee);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (h = 0; h < sizee; h++)
	{
		obj = ((PyListObject *)p)->ob_item[h];
		printf("Element %ld: %s\n", h, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - outputs bytes information
 *
 * @p: This is a Python object
 * Return: it doesnt return
 */
void print_python_bytes(PyObject *p)
{
	long int len, count, limit;
    char *string;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", string);

	if (len >= 10)
		limit = 10;
	else
		limit = len + 1;

	printf("  first %ld bytes:", limit);

	for (count = 0; count < limit; count++)
		if (string[count] >= 0)
			printf(" %02x", string[count]);
		else
			printf(" %02x", 256 + string[count]);

	printf("\n");
}

/**
 * print_python_list - Prints python list information
 *
 * @p: This is a Python project
 * 
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	
	PyListObject *list;
	PyObject *object;
    long int len, counter;
    list = (PyListObject *)p;
	len = ((PyVarObject *)(p))->ob_size;
	

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (counter = 0; counter < len; counter++)
	{
		object = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", counter, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}

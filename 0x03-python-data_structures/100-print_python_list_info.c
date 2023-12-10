#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: Pointer to a Python object (assumed to be a list)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	/* Print basic info about the Python list */
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/* Print each element of the list */
	size = Py_SIZE(p);
	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

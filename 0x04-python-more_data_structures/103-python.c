#include <Python.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes_data;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    if (size > 10)
        size = 10;

    bytes_data = ((PyBytesObject *)p)->ob_sval;
    printf("  first %ld bytes:", size);
    for (i = 0; i < size; ++i) {
        printf(" %02x", (unsigned char)bytes_data[i]);
    }
    printf("\n");
}

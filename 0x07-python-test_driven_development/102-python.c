#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Invalid String Object\n");
        return;
    }

    // Extracting information about the Unicode object
    Py_ssize_t length;
    const char *str = PyUnicode_AsUTF8AndSize(p, &length);

    // Checking if PyUnicode_AsUTF8AndSize was successful
    if (str == NULL) {
        fprintf(stderr, "Error decoding Unicode string\n");
        return;
    }

    // Printing information about the Unicode object
    printf("String data: %s\n", str);
    printf("Length of the Unicode object: %zd\n", length);
}

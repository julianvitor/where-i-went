#include <Python.h>

double convert_to_decimal(PyObject *coord_values) {
    double degrees = PyFloat_AsDouble(PyTuple_GetItem(coord_values, 0));
    double minutes = PyFloat_AsDouble(PyTuple_GetItem(coord_values, 1));
    double seconds = PyFloat_AsDouble(PyTuple_GetItem(coord_values, 2));

    return degrees + (minutes / 60.0) + (seconds / 3600.0);
}

static PyObject *convert_coordinates(PyObject *self, PyObject *args) {
    PyObject *coord_values;

    if (!PyArg_ParseTuple(args, "O", &coord_values)) {
        return NULL;
    }

    if (!PyTuple_Check(coord_values) || PyTuple_Size(coord_values) != 3) {
        PyErr_SetString(PyExc_TypeError, "Input should be a tuple of three floats.");
        return NULL;
    }

    double result = convert_to_decimal(coord_values);

    return PyFloat_FromDouble(result);
}

static PyMethodDef methods[] = {
    {"convert_coordinates", convert_coordinates, METH_VARARGS, "Convert coordinates from degrees, minutes, and seconds to decimal."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "coord_converter",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_coord_converter(void) {
    return PyModule_Create(&module);
}

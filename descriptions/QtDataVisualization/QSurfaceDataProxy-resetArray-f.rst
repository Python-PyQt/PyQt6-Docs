.. sip:method-description::
    :status: todo
    :pysig: a40303d7a11240fe7ee7c7f5af0e5c0b
    :realsig: (QSurfaceDataArray*)
    :digest: 1dc830ac74b2a2c6f2b9fc0188304624

Takes ownership of the array *newArray*. Clears the existing array if the new array differs from it. If the arrays are the same, this function just triggers the :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy.arrayReset` signal.

Passing a null array deletes the old array and creates a new empty array. All rows in *newArray* must be of same length.

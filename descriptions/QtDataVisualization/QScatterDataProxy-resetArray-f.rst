.. sip:method-description::
    :status: todo
    :pysig: cfa5d52324c0869a9cca2119d71ad8d2
    :realsig: (QScatterDataArray*)
    :digest: c7a848cecb7f0a493d3475ce87d6444c

Takes ownership of the array *newArray*. Clears the existing array if the new array differs from it. If the arrays are the same, this function just triggers the :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.arrayReset` signal.

Passing a null array deletes the old array and creates a new empty array.

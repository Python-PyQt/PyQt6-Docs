.. sip:method-description::
    :status: todo
    :pysig: e57ef7e9ef1cbe7cf2a459a399a15b21
    :realsig: (QBarDataArray*)
    :digest: 129e15a68e3574f8a0ef15108bda2f7a

Takes ownership of the array *newArray*. Clears the existing array if the new array differs from it. If the arrays are the same, this function just triggers the :sip:ref:`~PyQt6.QtDataVisualization.QBarDataProxy.arrayReset` signal.

Passing a null array deletes the old array and creates a new empty array. Row and column labels are not affected.

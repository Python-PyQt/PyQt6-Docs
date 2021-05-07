.. sip:method-description::
    :status: todo
    :pysig: 1282c64dd6e0f3883b088cd0156d152a
    :realsig: (QBarDataArray*,const QStringList&,const QStringList&)
    :digest: 4567c382aa977ed515df2509410765fe

Takes ownership of the array *newArray*. Clears the existing array if the new array differs from it. If the arrays are the same, this function just triggers the :sip:ref:`~PyQt6.QtDataVisualization.QBarDataProxy.arrayReset` signal.

Passing a null array deletes the old array and creates a new empty array.

The *rowLabels* and *columnLabels* lists specify the new labels for rows and columns.

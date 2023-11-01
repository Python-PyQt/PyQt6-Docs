.. sip:method-description::
    :status: todo
    :pysig: 6fb60876b5136c816ecc1a895d3012c0
    :realsig: (const QString&, const QString&)
    :digest: 885def191b5924d992e384b246634401

Inserts the environment variable of name *name* and contents *value* into this :sip:ref:`~PyQt6.QtCore.QProcessEnvironment` object. If that variable already existed, it is replaced by the new value.

On most systems, inserting a variable with no contents will have the same effect for applications as if the variable had not been set at all. However, to guarantee that there are no incompatibilities, to remove a variable, please use the :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.remove` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.contains`, :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.remove`, :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.value`.

.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: () const
    :digest: bea895237420663e6063c455a0ba1b4d

Returns a pointer to a :sip:ref:`~PyQt6.QtCore.QIODevice` that gives access to the request body. The request body can contain data for example when the request is a POST request. If the request body is empty the :sip:ref:`~PyQt6.QtCore.QIODevice` reflects this and does not return any data when performing read operations on it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice`.

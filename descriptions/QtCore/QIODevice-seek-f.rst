.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (qint64)
    :digest: 600128ecd94afb64f33c7a2dbf572236

For random-access devices, this function sets the current position to *pos*, returning true on success, or false if an error occurred. For sequential devices, the default behavior is to produce a warning and return false.

When subclassing :sip:ref:`~PyQt6.QtCore.QIODevice`, you must call  at the start of your function to ensure integrity with :sip:ref:`~PyQt6.QtCore.QIODevice`'s built-in buffer.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.pos`, :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential`.

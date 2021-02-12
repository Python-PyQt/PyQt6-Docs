.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 0a4cf9b914fed163fe0a1a20b0d93f41

Sets the current field width to *width*. If *width* is 0 (the default), the field width is equal to the length of the generated text.

**Note:** The field width applies to every element appended to this stream after this function has been called (e.g., it also pads endl). This behavior is different from similar classes in the STL, where the field width only applies to the next element.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.fieldWidth`, :sip:ref:`~PyQt6.QtCore.QTextStream.setPadChar`.

.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 578cbbc933f7cbd1249b66ae45913295

Seeks to the start of input for random-access devices. Returns true on success; otherwise returns ``false`` (for example, if the device is not open).

Note that when using a :sip:ref:`~PyQt6.QtCore.QTextStream` on a :sip:ref:`~PyQt6.QtCore.QFile`, calling  on the :sip:ref:`~PyQt6.QtCore.QFile` will not have the expected result because :sip:ref:`~PyQt6.QtCore.QTextStream` buffers the file. Use the :sip:ref:`~PyQt6.QtCore.QTextStream.seek` function instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.seek`.

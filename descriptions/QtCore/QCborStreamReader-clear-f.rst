.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 20a1159dbc2558fb70d987558f6e33fa

Clears the decoder state and resets the input source data to an empty byte array. After this function is called, :sip:ref:`~PyQt6.QtCore.QCborStreamReader` will be indicating an error parsing.

Call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.addData` to add more data to be parsed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.reset`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.setDevice`.

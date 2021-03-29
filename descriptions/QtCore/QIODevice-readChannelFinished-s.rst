.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7fd5e3469e6fa5860daa2da400ea496e

This signal is emitted when the input (reading) stream is closed in this device. It is emitted as soon as the closing is detected, which means that there might still be data available for reading with :sip:ref:`~PyQt6.QtCore.QIODevice.read`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.atEnd`, :sip:ref:`~PyQt6.QtCore.QIODevice.read`.

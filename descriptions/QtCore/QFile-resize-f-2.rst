.. sip:method-description::
    :status: todo
    :pysig: fc72e78f0301238e410e562a38d54f4a
    :realsig: (const QString&, qint64)
    :digest: 5e97cd57912c7928ecb4e7b5bd3e6796

Sets *fileName* to size (in bytes) *sz*. Returns ``true`` if the resize succeeds; false otherwise. If *sz* is larger than *fileName* currently is the new bytes will be set to 0, if *sz* is smaller the file is simply truncated.

**Warning:** This function can fail if the file doesn't exist.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.resize`.

.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 9236e4ee77bfc3b648a3d87f250f36de

If an error has occurred, returns its associated error message.

The error message is either set internally by :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` or provided by the user via :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.raiseError`. If no error has occured, this function returns a null string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.error`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.raiseError`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.hasError`.

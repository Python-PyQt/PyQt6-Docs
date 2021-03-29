.. sip:method-description::
    :status: todo
    :pysig: 0f9b0ea7a3407ca50e1df7b110b9ad1f
    :realsig: (const QString&)
    :digest: 299a4b4099b8cb6100715333958662d5

Adds *prefix* to the current group and starts reading from an array. Returns the size of the array.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 160-176

Use :sip:ref:`~PyQt6.QtCore.QSettings.beginWriteArray` to write the array in the first place.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.beginWriteArray`, :sip:ref:`~PyQt6.QtCore.QSettings.endArray`, :sip:ref:`~PyQt6.QtCore.QSettings.setArrayIndex`.

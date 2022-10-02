.. sip:method-description::
    :status: todo
    :pysig: ca078571a8a1f740866f3c4c87696798
    :realsig: (QAnyStringView)
    :digest: d74c138e859d3a34fda6875c967afe12

Adds *prefix* to the current group and starts reading from an array. Returns the size of the array.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 160-176

Use :sip:ref:`~PyQt6.QtCore.QSettings.beginWriteArray` to write the array in the first place.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.beginWriteArray`, :sip:ref:`~PyQt6.QtCore.QSettings.endArray`, :sip:ref:`~PyQt6.QtCore.QSettings.setArrayIndex`.

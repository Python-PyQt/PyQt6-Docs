.. sip:method-description::
    :status: todo
    :pysig: 0f6fb60ef827df111b0651fef08e83ee
    :realsig: (QAnyStringView, const QVariant&)
    :digest: 2338264107fbc9f157f4e37bea2d7686

Sets the value of setting *key* to *value*. If the *key* already exists, the previous value is overwritten.

Key lookup will either be sensitive or insensitive to case depending on file format and operating system. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 257-262

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.remove`, :sip:ref:`~PyQt6.QtCore.QSettings.contains`.

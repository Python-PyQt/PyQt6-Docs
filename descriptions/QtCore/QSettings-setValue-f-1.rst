.. sip:method-description::
    :status: todo
    :pysig: 637da7c3308a0bafa39dc8eb7fc6fe1e
    :realsig: (QAnyStringView,const QVariant&)
    :digest: c98389d657f46c52965eb4fd9ac3721d

Sets the value of setting *key* to *value*. If the *key* already exists, the previous value is overwritten.

Note that the Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 257-262

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.remove`, :sip:ref:`~PyQt6.QtCore.QSettings.contains`.

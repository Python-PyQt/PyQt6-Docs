.. sip:method-description::
    :status: todo
    :pysig: 9064598f6881fe97156ec2e9c47c55cf
    :realsig: (const QString&,const QVariant&)
    :digest: a367d21d19737cab9301a1407a6170d8

Sets the value of setting *key* to *value*. If the *key* already exists, the previous value is overwritten.

Note that the Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 257-262

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.remove`, :sip:ref:`~PyQt6.QtCore.QSettings.contains`.

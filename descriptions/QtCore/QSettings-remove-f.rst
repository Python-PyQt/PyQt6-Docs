.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 44b7fc8c1dce01aaebf13ce29996a55d

Removes the setting *key* and any sub-settings of *key*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 267-275

Be aware that if one of the fallback locations contains a setting with the same key, that setting will be visible after calling .

If *key* is an empty string, all keys in the current :sip:ref:`~PyQt6.QtCore.QSettings.group` are removed. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 280-291

Note that the Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.setValue`, :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.contains`.

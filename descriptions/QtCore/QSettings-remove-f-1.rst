.. sip:method-description::
    :status: todo
    :pysig: 81445f071599e8ca359c5cd31fa289a9
    :realsig: (QAnyStringView)
    :digest: a98de2529c952db2661706823db04310

Removes the setting *key* and any sub-settings of *key*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 267-275

Be aware that if one of the fallback locations contains a setting with the same key, that setting will be visible after calling remove().

If *key* is an empty string, all keys in the current :sip:ref:`~PyQt6.QtCore.QSettings.group` are removed. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 280-291

Note that the Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.setValue`, :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.contains`.

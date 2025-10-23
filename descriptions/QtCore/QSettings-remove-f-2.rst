.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: e0857c8e719d8b56d6cef035f89265ee

Removes the setting *key* and any sub-settings of *key*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 267-275

Be aware that if one of the fallback locations contains a setting with the same key, that setting will be visible after calling remove().

If *key* is an empty string, all keys in the current :sip:ref:`~PyQt6.QtCore.QSettings.group` are removed. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 280-291

Key lookup will either be sensitive or insensitive to case depending on file format and operating system. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.setValue`, :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.contains`.

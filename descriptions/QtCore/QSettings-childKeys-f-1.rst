.. sip:method-description::
    :status: todo
    :pysig: 3c9a938a1e983dbe538fd869f2db5e67
    :realsig: () const
    :digest: f05773b4789e832bc9650bad35b57687

Returns a list of all top-level keys that can be read using the :sip:ref:`~PyQt6.QtCore.QSettings` object.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 219-226

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, the top-level keys in that group are returned, without the group prefix:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 231-233

You can navigate through the entire setting hierarchy using childKeys() and :sip:ref:`~PyQt6.QtCore.QSettings.childGroups` recursively.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.childGroups`, :sip:ref:`~PyQt6.QtCore.QSettings.allKeys`.

.. sip:method-description::
    :status: todo
    :pysig: 3c9a938a1e983dbe538fd869f2db5e67
    :realsig: () const
    :digest: bb7031e37b15d31b2e02f3cc4dca472b

Returns a list of all key top-level groups that contain keys that can be read using the :sip:ref:`~PyQt6.QtCore.QSettings` object.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 238-245

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, the first-level keys in that group are returned, without the group prefix.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 250-252

You can navigate through the entire setting hierarchy using :sip:ref:`~PyQt6.QtCore.QSettings.childKeys` and childGroups() recursively.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.childKeys`, :sip:ref:`~PyQt6.QtCore.QSettings.allKeys`.

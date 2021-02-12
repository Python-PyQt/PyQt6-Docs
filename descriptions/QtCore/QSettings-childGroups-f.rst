.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: bb7031e37b15d31b2e02f3cc4dca472b

Returns a list of all key top-level groups that contain keys that can be read using the :sip:ref:`~PyQt6.QtCore.QSettings` object.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 238-245

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, the first-level keys in that group are returned, without the group prefix.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 250-252

You can navigate through the entire setting hierarchy using :sip:ref:`~PyQt6.QtCore.QSettings.childKeys` and  recursively.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.childKeys`, :sip:ref:`~PyQt6.QtCore.QSettings.allKeys`.

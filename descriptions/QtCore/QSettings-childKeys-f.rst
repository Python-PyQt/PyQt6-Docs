.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 8df59fe0ee13f82c0dce899e33d2bcf4

Returns a list of all top-level keys that can be read using the :sip:ref:`~PyQt6.QtCore.QSettings` object.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 219-226

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, the top-level keys in that group are returned, without the group prefix:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 231-233

You can navigate through the entire setting hierarchy using  and :sip:ref:`~PyQt6.QtCore.QSettings.childGroups` recursively.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.childGroups`, :sip:ref:`~PyQt6.QtCore.QSettings.allKeys`.

.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 7e654eaa3443db3034f963babbb365ff

Returns a list of all keys, including subkeys, that can be read using the :sip:ref:`~PyQt6.QtCore.QSettings` object.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 200-207

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, only the keys in the group are returned, without the group prefix:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 212-214

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.childGroups`, :sip:ref:`~PyQt6.QtCore.QSettings.childKeys`.

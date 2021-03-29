.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: dfe1eeb89b8c753c51855167cd09c305

Appends *prefix* to the current group.

The current group is automatically prepended to all keys specified to :sip:ref:`~PyQt6.QtCore.QSettings`. In addition, query functions such as :sip:ref:`~PyQt6.QtCore.QSettings.childGroups`, :sip:ref:`~PyQt6.QtCore.QSettings.childKeys`, and :sip:ref:`~PyQt6.QtCore.QSettings.allKeys` are based on the group. By default, no group is set.

Groups are useful to avoid typing in the same setting paths over and over. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 133-140

This will set the value of three settings:

* ``mainwindow/size``

* ``mainwindow/fullScreen``

* ``outputpanel/visible``

Call :sip:ref:`~PyQt6.QtCore.QSettings.endGroup` to reset the current group to what it was before the corresponding  call. Groups can be nested.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.endGroup`, :sip:ref:`~PyQt6.QtCore.QSettings.group`.

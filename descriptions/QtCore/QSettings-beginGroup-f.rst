.. sip:method-description::
    :status: todo
    :pysig: 48964e5682cadc964cb6cdcfffc910dc
    :realsig: (QAnyStringView)
    :digest: 9ef2d9847c91604e43ad8b0244e1bda1

Appends *prefix* to the current group.

The current group is automatically prepended to all keys specified to :sip:ref:`~PyQt6.QtCore.QSettings`. In addition, query functions such as :sip:ref:`~PyQt6.QtCore.QSettings.childGroups`, :sip:ref:`~PyQt6.QtCore.QSettings.childKeys`, and :sip:ref:`~PyQt6.QtCore.QSettings.allKeys` are based on the group. By default, no group is set.

Groups are useful to avoid typing in the same setting paths over and over. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 133-140

This will set the value of three settings:

* ``mainwindow/size``

* ``mainwindow/active``

* ``outputpanel/visible``

Call :sip:ref:`~PyQt6.QtCore.QSettings.endGroup` to reset the current group to what it was before the corresponding beginGroup() call. Groups can be nested.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.endGroup`, :sip:ref:`~PyQt6.QtCore.QSettings.group`.

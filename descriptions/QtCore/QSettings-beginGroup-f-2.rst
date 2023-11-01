.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: aacf9677ad1d6402aec2dcd7da76a454

Appends *prefix* to the current group.

The current group is automatically prepended to all keys specified to :sip:ref:`~PyQt6.QtCore.QSettings`. In addition, query functions such as :sip:ref:`~PyQt6.QtCore.QSettings.childGroups`, :sip:ref:`~PyQt6.QtCore.QSettings.childKeys`, and :sip:ref:`~PyQt6.QtCore.QSettings.allKeys` are based on the group. By default, no group is set.

Groups are useful to avoid typing in the same setting paths over and over. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 133-140

This will set the value of three settings:

* ``mainwindow/size``

* ``mainwindow/fullScreen``

* ``outputpanel/visible``

Call :sip:ref:`~PyQt6.QtCore.QSettings.endGroup` to reset the current group to what it was before the corresponding beginGroup() call. Groups can be nested.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.endGroup`, :sip:ref:`~PyQt6.QtCore.QSettings.group`.

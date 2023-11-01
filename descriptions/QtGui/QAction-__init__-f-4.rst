.. sip:method-description::
    :status: todo
    :pysig: c6a4ac097adbb6f90550770a8c55db1d
    :realsig: (const QIcon&, const QString&, QObject*)
    :digest: 9370f99d17f8357c11df5779ae0c61d5

Constructs an action with an *icon* and some *text* and *parent*. If *parent* is an action group the action will be automatically inserted into the group.

A stripped version of *text* (for example, "&Menu Option..." becomes "Menu Option") will be used for tooltips and icon text unless you specify a different text using :sip:ref:`~PyQt6.QtGui.QAction.setToolTip` or :sip:ref:`~PyQt6.QtGui.QAction.setIconText`, respectively.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.text`, :sip:ref:`~PyQt6.QtGui.QAction.icon`.

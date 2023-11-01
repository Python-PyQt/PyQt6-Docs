.. sip:method-description::
    :status: todo
    :pysig: 7d74642492c1254c6ab51fbfe503f7bc
    :realsig: (const QString&, QObject*)
    :digest: e675eac124f823df0f5c1680b26238f2

Constructs an action with some *text* and *parent*. If *parent* is an action group the action will be automatically inserted into the group.

A stripped version of *text* (for example, "&Menu Option..." becomes "Menu Option") will be used for tooltips and icon text unless you specify a different text using :sip:ref:`~PyQt6.QtGui.QAction.setToolTip` or :sip:ref:`~PyQt6.QtGui.QAction.setIconText`, respectively.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.text`.

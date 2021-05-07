.. sip:method-description::
    :status: todo
    :pysig: 95391368283d83f1e44e97bef46a0a2c
    :realsig: (int,QAction*,QAction*)
    :digest: cff2b13e2aac519889f6f2626b5a2b8c

Constructs an action event. The *type* can be :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionChanged`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionRemoved`.

*action* is the action that is changed, added, or removed. If *type* is ActionAdded, the action is to be inserted before the action *before*. If *before* is ``nullptr``, the action is appended.

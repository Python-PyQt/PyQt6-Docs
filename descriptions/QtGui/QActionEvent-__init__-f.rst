.. sip:method-description::
    :status: todo
    :pysig: 95391368283d83f1e44e97bef46a0a2c
    :realsig: (int,QAction*,QAction*)
    :digest: fb5e91c49b0a38f8f32c896736c7c6f8

Constructs an action event. The *type* can be :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionChanged`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionRemoved`.

*action* is the action that is changed, added, or removed. If *type* is :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded`, the action is to be inserted before the action *before*. If *before* is ``nullptr``, the action is appended.

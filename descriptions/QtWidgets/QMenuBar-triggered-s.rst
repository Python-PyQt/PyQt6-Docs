.. sip:signal-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: (QAction*)
    :digest: f73031c0f5a37ba9ae3b8da53601d26d

This signal is emitted when an action in a menu belonging to this menubar is triggered as a result of a mouse click; *action* is the action that caused the signal to be emitted.

**Note:** :sip:ref:`~PyQt6.QtWidgets.QMenuBar` has to have ownership of the :sip:ref:`~PyQt6.QtWidgets.QMenu` in order this signal to work.

Normally, you connect each menu action to a single slot using :sip:ref:`~PyQt6.QtGui.QAction.triggered`, but sometimes you will want to connect several items to a single slot (most often if the user selects from an array). This signal is useful in such cases.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenuBar.hovered`, :sip:ref:`~PyQt6.QtGui.QAction.triggered`.

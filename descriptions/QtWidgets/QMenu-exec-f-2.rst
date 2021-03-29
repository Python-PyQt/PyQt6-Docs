.. sip:method-description::
    :status: todo
    :pysig: 497f25a929e0c3c62e31f1c3b1d61a98
    :realsig: (const QList<QAction*>&,const QPoint&,QAction*,QWidget*)
    :digest: 2783bfeed4ac1a4d91e47ba63884fcd2

This is an overloaded function.

Executes a menu synchronously.

The menu's actions are specified by the list of *actions*. The menu will pop up so that the specified action, *at*, appears at global position *pos*. If *at* is not specified then the menu appears at position *pos*. *parent* is the menu's parent widget; specifying the parent will provide context when *pos* alone is not enough to decide where the menu should go (e.g., with multiple desktops or when the parent is embedded in :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`).

The function returns the triggered :sip:ref:`~PyQt6.QtGui.QAction` in either the popup menu or one of its submenus, or ``nullptr`` if no item was triggered (normally because the user pressed Esc).

This is equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 84-88

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenu.popup`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`.

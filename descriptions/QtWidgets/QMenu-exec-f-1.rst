.. sip:method-description::
    :status: todo
    :pysig: 9ad61883e1e1619cb72e5927d0814e17
    :realsig: (const QPoint&,QAction*)
    :digest: 0caccce05f3d1f3a81305f5787ce75f6

This is an overloaded function.

Executes this menu synchronously.

Pops up the menu so that the action *action* will be at the specified *global* position *p*. To translate a widget's local coordinates into global coordinates, use :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`.

This returns the triggered :sip:ref:`~PyQt6.QtGui.QAction` in either the popup menu or one of its submenus, or ``nullptr`` if no item was triggered (normally because the user pressed Esc).

Note that all signals are emitted as usual. If you connect a :sip:ref:`~PyQt6.QtGui.QAction` to a slot and call the menu's :sip:ref:`~PyQt6.QtWidgets.QMenu.exec`, you get the result both via the signal-slot connection and in the return value of :sip:ref:`~PyQt6.QtWidgets.QMenu.exec`.

Common usage is to position the menu at the current mouse position:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 69-69

or aligned to a widget:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 74-74

or in reaction to a :sip:ref:`~PyQt6.QtGui.QMouseEvent` \*e:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 79-79

When positioning a menu with :sip:ref:`~PyQt6.QtWidgets.QMenu.exec` or :sip:ref:`~PyQt6.QtWidgets.QMenu.popup`, bear in mind that you cannot rely on the menu's current size(). For performance reasons, the menu adapts its size only when necessary. So in many cases, the size before and after the show is different. Instead, use :sip:ref:`~PyQt6.QtWidgets.QMenu.sizeHint` which calculates the proper size depending on the menu's current contents.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenu.popup`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`.

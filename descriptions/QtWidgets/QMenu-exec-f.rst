.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: ()
    :digest: 0bf1d86822255f3b79efb108f381a01a

Executes this menu synchronously.

This is equivalent to ``exec(pos())``.

This returns the triggered :sip:ref:`~PyQt6.QtGui.QAction` in either the popup menu or one of its submenus, or ``nullptr`` if no item was triggered (normally because the user pressed Esc).

In most situations you'll want to specify the position yourself, for example, the current mouse position:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 54-54

or aligned to a widget:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 59-59

or in reaction to a :sip:ref:`~PyQt6.QtGui.QMouseEvent` \*e:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenu.py
    :lines: 64-64

.. sip:method-description::
    :status: todo
    :pysig: 39a06d8ea935289a215dbc96b8ebf29b
    :realsig: (QWidget*,QWidget*)
    :digest: 5c6d34e6f962985b54e1e7c78aafb4a2

Puts the *second* widget after the *first* widget in the focus order.

It effectively removes the *second* widget from its focus chain and inserts it after the *first* widget.

Note that since the tab order of the *second* widget is changed, you should order a chain like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 107-109

*not* like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 114-117

If *first* or *second* has a focus proxy,  correctly substitutes the proxy.

**Note:** Since Qt 5.10: A widget that has a child as focus proxy is understood as a compound widget. When setting a tab order between one or two compound widgets, the local tab order inside each will be preserved. This means that if both widgets are compound widgets, the resulting tab order will be from the last child inside *first*, to the first child inside *second*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusProxy`, `Keyboard Focus in Widgets <https://doc.qt.io/qt-6/focus.html>`_.

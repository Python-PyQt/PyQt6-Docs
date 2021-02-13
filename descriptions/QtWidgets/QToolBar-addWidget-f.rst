.. sip:method-description::
    :status: todo
    :pysig: 4e2774b95ed3986e7088297d5c9c1866
    :realsig: (QWidget*)
    :digest: a09786ad84c7fe9a64d5f382f8f0f31f

Adds the given *widget* to the toolbar as the toolbar's last item.

The toolbar takes ownership of *widget*.

If you add a :sip:ref:`~PyQt6.QtWidgets.QToolButton` with this method, the toolbar's :sip:ref:`~PyQt6.QtCore.Qt.ToolButtonStyle` will not be respected.

**Note:** You should use :sip:ref:`~PyQt6.QtGui.QAction.setVisible` to change the visibility of the widget. Using :sip:ref:`~PyQt6.QtWidgets.QWidget.setVisible`, :sip:ref:`~PyQt6.QtWidgets.QWidget.show` and :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` does not work.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QToolBar.insertWidget`.

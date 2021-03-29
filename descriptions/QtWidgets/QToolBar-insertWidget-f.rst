.. sip:method-description::
    :status: todo
    :pysig: db54ea53742df181e10d2acae6c6533c
    :realsig: (QAction*,QWidget*)
    :digest: 7351836e3c3f66c13d727873011d65ba

Inserts the given *widget* in front of the toolbar item associated with the *before* action.

Note: You should use :sip:ref:`~PyQt6.QtGui.QAction.setVisible` to change the visibility of the widget. Using :sip:ref:`~PyQt6.QtWidgets.QWidget.setVisible`, :sip:ref:`~PyQt6.QtWidgets.QWidget.show` and :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` does not work.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QToolBar.addWidget`.

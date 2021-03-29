.. sip:method-description::
    :status: todo
    :pysig: 5a6e30521ff6150b2e0a693194e10d98
    :realsig: ()
    :digest: fce001476584f2c9ba30598f110f26e1

Returns the active modal widget.

A modal widget is a special top-level widget which is a subclass of :sip:ref:`~PyQt6.QtWidgets.QDialog` that specifies the modal parameter of the constructor as true. A modal widget must be closed before the user can continue with other parts of the program.

Modal widgets are organized in a stack. This function returns the active modal widget at the top of the stack.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.activePopupWidget`, :sip:ref:`~PyQt6.QtWidgets.QApplication.topLevelWidgets`.

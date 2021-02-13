.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: () const
    :digest: 3ea715cc930c2762b6211c56d019ad35

Returns a checkable action that can be added to menus and toolbars so that the user can show or close this dock widget.

The action's text is set to the dock widget's window title.

**Note:** The action can not be used to programmatically show or hide the dock widget. Use the visible property for that.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.text`, :sip:ref:`~PyQt6.QtWidgets.QWidget.windowTitle`.

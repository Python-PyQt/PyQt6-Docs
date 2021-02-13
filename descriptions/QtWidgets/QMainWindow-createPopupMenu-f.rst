.. sip:method-description::
    :status: todo
    :pysig: 0bee5ee99a425921db962be70be70688
    :realsig: ()
    :digest: 44013a68b5ad0286ff9a030258cab99c

Returns a popup menu containing checkable entries for the toolbars and dock widgets present in the main window. If there are no toolbars and dock widgets present, this function returns ``nullptr``.

By default, this function is called by the main window when the user activates a context menu, typically by right-clicking on a toolbar or a dock widget.

If you want to create a custom popup menu, reimplement this function and return a newly-created popup menu. Ownership of the popup menu is transferred to the caller.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow.addDockWidget`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.addToolBar`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.menuBar`.

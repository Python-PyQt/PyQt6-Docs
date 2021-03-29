.. sip:method-description::
    :status: todo
    :pysig: 3c0614831027040a14f9864303b7c627
    :realsig: () const
    :digest: 89d2673885ed8b8d11cea8c371fff9d9

Returns the menu bar for the main window. This function creates and returns an empty menu bar if the menu bar does not exist.

If you want all windows in a Mac application to share one menu bar, don't use this function to create it, because the menu bar created here will have this :sip:ref:`~PyQt6.QtWidgets.QMainWindow` as its parent. Instead, you must create a menu bar that does not have a parent, which you can then share among all the Mac windows. Create a parent-less menu bar this way:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenubar.py
    :lines: 59-59

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow.setMenuBar`.

.. sip:method-description::
    :status: todo
    :pysig: 88fd00acd51d10e4f7ab23b3f203a059
    :realsig: ()
    :digest: 1b7778f4d6a97c8242f22a9828ff6bf4

Returns a list of all the widgets in the application.

The list is empty (QList::isEmpty()) if there are no widgets.

**Note:** Some of the widgets may be hidden.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qapplication.py
    :lines: 116-121

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.topLevelWidgets`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`.

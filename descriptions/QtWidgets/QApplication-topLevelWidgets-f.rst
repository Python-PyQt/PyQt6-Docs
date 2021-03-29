.. sip:method-description::
    :status: todo
    :pysig: 32a6718bb2f66c1b3ba54b8ded7c2d7b
    :realsig: ()
    :digest: 4b16723770979f9c78b0174a2c03234a

Returns a list of the top-level widgets (windows) in the application.

**Note:** Some of the top-level widgets may be hidden, for example a tooltip if no tooltip is currently shown.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qapplication.py
    :lines: 104-111

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.allWidgets`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isWindow`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isHidden`.

.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: () const
    :digest: ae857dba1d52841f0f07dcefa40cac3b

Returns the window for this widget, i.e. the next ancestor widget that has (or could have) a window-system frame.

If the widget is a window, the widget itself is returned.

Typical usage is changing the window title:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 70-70

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.isWindow`.

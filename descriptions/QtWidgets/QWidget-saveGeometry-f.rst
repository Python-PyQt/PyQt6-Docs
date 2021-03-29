.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: c3750ad5f8eb313b631b91fff63e2e78

Saves the current geometry and state for top-level widgets.

To save the geometry when the window closes, you can implement a close event like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 122-127

See the `Window Geometry <https://doc.qt.io/qt-6/application-windows.html#window-geometry>`_ documentation for an overview of geometry issues with windows.

Use :sip:ref:`~PyQt6.QtWidgets.QMainWindow.saveState` to save the geometry and the state of toolbars and dock widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.restoreGeometry`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.saveState`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.restoreState`.

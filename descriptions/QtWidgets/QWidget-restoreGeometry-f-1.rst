.. sip:method-description::
    :status: todo
    :pysig: 818ceb9f7882cf71214966cf00526abf
    :realsig: (const QByteArray&)
    :digest: fa9b26a8cfe1821009e93116bf2d6702

Restores the geometry and state of top-level widgets stored in the byte array *geometry*. Returns ``true`` on success; otherwise returns ``false``.

If the restored geometry is off-screen, it will be modified to be inside the available screen geometry.

To restore geometry saved using :sip:ref:`~PyQt6.QtCore.QSettings`, you can use code like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 132-133

See the `Window Geometry <https://doc.qt.io/qt-6/application-windows.html#window-geometry>`_ documentation for an overview of geometry issues with windows.

Use :sip:ref:`~PyQt6.QtWidgets.QMainWindow.restoreState` to restore the geometry and the state of toolbars and dock widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.saveGeometry`, :sip:ref:`~PyQt6.QtCore.QSettings`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.saveState`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.restoreState`.

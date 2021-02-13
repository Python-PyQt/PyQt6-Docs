.. sip:method-description::
    :status: todo
    :pysig: 07981c8c8275ca742c47328f8dcaadf2
    :realsig: (QStatusBar*)
    :digest: c0099396f55b0022d25a4a7182f6b719

Sets the status bar for the main window to *statusbar*.

Setting the status bar to ``nullptr`` will remove it from the main window. Note that :sip:ref:`~PyQt6.QtWidgets.QMainWindow` takes ownership of the *statusbar* pointer and deletes it at the appropriate time.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow.statusBar`.

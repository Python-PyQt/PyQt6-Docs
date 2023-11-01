.. sip:method-description::
    :status: todo
    :pysig: 875ce01f472dcfe750752bc5ac3d0792
    :realsig: (QWidget*, const QString&)
    :digest: 3e7fc7c1e9f457fd3aecf8ecafb4f9c5

Displays a simple message box about Qt, with the given *title* and centered over *parent* (if *parent* is not ``nullptr``). The message includes the version number of Qt being used by the application.

This is useful for inclusion in the Help menu of an application, as shown in the `Menus <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_ example.

:sip:ref:`~PyQt6.QtWidgets.QApplication` provides this functionality as a slot.

On macOS, the about box is popped up as a modeless window; on other platforms, it is currently application modal.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.aboutQt`.

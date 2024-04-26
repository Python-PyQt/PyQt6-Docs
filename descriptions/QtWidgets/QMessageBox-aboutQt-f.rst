.. sip:method-description::
    :status: todo
    :pysig: 0e4713436bad6ebc799645cb2244ce91
    :realsig: (QWidget*,const QString&)
    :digest: 6e160baadca03bcee961684af7a35c78

Displays a simple message box about Qt, with the given *title* and centered over *parent* (if *parent* is not ``nullptr``). The message includes the version number of Qt being used by the application.

This is useful for inclusion in the Help menu of an application, as shown in the `Menus <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_ example.

:sip:ref:`~PyQt6.QtWidgets.QApplication` provides this functionality as a slot.

On macOS, the aboutQt box is popped up as a modeless window; on other platforms, it is currently application modal.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.aboutQt`.

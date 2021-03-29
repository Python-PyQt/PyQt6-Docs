.. sip:method-description::
    :status: todo
    :pysig: 40a6e8cad65568415186158f5079fab6
    :realsig: (int) const
    :digest: 65c605d4e4729619ab0769becca7b307

Saves the current state of this mainwindow's toolbars and dockwidgets. This includes the corner settings which can be set with :sip:ref:`~PyQt6.QtWidgets.QMainWindow.setCorner`. The *version* number is stored as part of the data.

The :sip:ref:`~PyQt6.QtCore.QObject.objectName` property is used to identify each :sip:ref:`~PyQt6.QtWidgets.QToolBar` and :sip:ref:`~PyQt6.QtWidgets.QDockWidget`. You should make sure that this property is unique for each :sip:ref:`~PyQt6.QtWidgets.QToolBar` and :sip:ref:`~PyQt6.QtWidgets.QDockWidget` you add to the :sip:ref:`~PyQt6.QtWidgets.QMainWindow`

To restore the saved state, pass the return value and *version* number to :sip:ref:`~PyQt6.QtWidgets.QMainWindow.restoreState`.

To save the geometry when the window closes, you can implement a close event like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmainwindow.py
    :lines: 54-60

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow.restoreState`, :sip:ref:`~PyQt6.QtWidgets.QWidget.saveGeometry`, :sip:ref:`~PyQt6.QtWidgets.QWidget.restoreGeometry`.

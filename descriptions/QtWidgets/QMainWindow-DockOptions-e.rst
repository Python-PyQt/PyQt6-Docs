.. sip:enum-description::
    :status: todo
    :realname: QMainWindow::DockOption
    :digest: 9176a94601af33a34ac3ae605d785b72

This enum contains flags that specify the docking behavior of :sip:ref:`~PyQt6.QtWidgets.QMainWindow`.

These options only control how dock widgets may be dropped in a :sip:ref:`~PyQt6.QtWidgets.QMainWindow`. They do not re-arrange the dock widgets to conform with the specified options. For this reason they should be set before any dock widgets are added to the main window. Exceptions to this are the  and  options, which may be set at any time.

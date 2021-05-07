.. sip:enum-member-description::
    :status: todo
    :value: 0x00000002 | Window
    :digest: 43a121b793533355550abd780be505fd

Indicates that the widget is a window that should be decorated as a dialog (i.e., typically no maximize or minimize buttons in the title bar). This is the default type for :sip:ref:`~PyQt6.QtWidgets.QDialog`. If you want to use it as a modal dialog, it should be launched from another window, or have a parent and used with the :sip:ref:`~PyQt6.QtWidgets.QWidget.windowModality` property. If you make it modal, the dialog will prevent other top-level windows in the application from getting any input. We refer to a top-level window that has a parent as a *secondary* window.

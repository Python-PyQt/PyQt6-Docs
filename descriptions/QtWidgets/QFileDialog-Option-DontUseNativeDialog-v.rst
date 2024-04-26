.. sip:enum-member-description::
    :status: todo
    :value: 0x00000008
    :digest: ad90a8856fa7623b34b81d17ae044854

Don't use a platform-native file dialog, but the widget-based one provided by Qt. By default, a native file dialog is shown unless you use a subclass of :sip:ref:`~PyQt6.QtWidgets.QFileDialog` that contains the Q_OBJECT macro, the global :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DontUseNativeDialogs` application attribute is set, or the platform does not have a native dialog of the type that you require. For the option to be effective, you must set it before changing other properties of the dialog, or showing the dialog.

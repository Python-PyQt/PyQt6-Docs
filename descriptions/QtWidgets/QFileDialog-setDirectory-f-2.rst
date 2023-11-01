.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 26af149dec9c4e5f0cffcbc1d6a72540

Sets the file dialog's current *directory*.

**Note:** On iOS, if you set *directory* to :sip:ref:`~PyQt6.QtCore.QStandardPaths.standardLocations`, a native image picker dialog will be used for accessing the user's photo album. The filename returned can be loaded using :sip:ref:`~PyQt6.QtCore.QFile` and related APIs. For this to be enabled, the Info.plist assigned to QMAKE_INFO_PLIST in the project file must contain the key ``NSPhotoLibraryUsageDescription``. See Info.plist documentation from Apple for more information regarding this key. This feature was added in Qt 5.5.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.directory`.

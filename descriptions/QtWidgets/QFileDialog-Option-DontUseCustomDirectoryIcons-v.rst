.. sip:enum-member-description::
    :status: todo
    :value: 0x00000040
    :digest: 115c41958b5bdb78d9b954809fdf5407

Always use the default directory icon. Some platforms allow the user to set a different icon, but custom icon lookup might cause significant performance issues over network or removable drives. Setting this will enable the :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider.Option.DontUseCustomDirectoryIcons` option in :sip:ref:`~PyQt6.QtWidgets.QFileDialog.iconProvider`. This enum value was added in Qt 5.2.

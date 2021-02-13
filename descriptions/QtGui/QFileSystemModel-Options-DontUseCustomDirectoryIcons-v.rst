.. sip:enum-member-description::
    :status: todo
    :value: 0x00000004
    :realname: QFileSystemModel::Option::DontUseCustomDirectoryIcons
    :digest: 80973452f68270a2e07a408d0c5bb5c7

Always use the default directory icon. Some platforms allow the user to set a different icon. Custom icon lookup causes a big performance impact over network or removable drives. This sets the :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider.Options.DontUseCustomDirectoryIcons` option in the icon provider accordingly.

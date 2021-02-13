.. sip:enum-member-description::
    :status: todo
    :value: 0x00000040
    :realname: QFileDialog::Option::DontUseCustomDirectoryIcons
    :digest: 4ab77540fc06db4dcbdba6caf535cb81

Always use the default directory icon. Some platforms allow the user to set a different icon. Custom icon lookup cause a big performance impact over network or removable drives. Setting this will enable the :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider.Options.DontUseCustomDirectoryIcons` option in the icon provider. This enum value was added in Qt 5.2.

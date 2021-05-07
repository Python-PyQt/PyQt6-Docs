.. sip:enum-member-description::
    :status: todo
    :value: 0x00000004
    :realname: QFileSystemModel::Option::DontUseCustomDirectoryIcons
    :digest: 6ab47a8901fcd4512bf88433ab8170f2

Always use the default directory icon. Some platforms allow the user to set a different icon. Custom icon lookup causes a big performance impact over network or removable drives. This sets the QFileIconProvider::DontUseCustomDirectoryIcons option in the icon provider accordingly.

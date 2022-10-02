.. sip:enum-member-description::
    :status: todo
    :value: 17
    :digest: 4a1670630f6ad806747e52883acc2f99

Returns a directory location where persistent application data can be stored. This is an application-specific directory. To obtain a path to store data to be shared with other applications, use QStandardPaths::GenericDataLocation. The returned path is never empty. On the Windows operating system, this returns the roaming path. This enum value was added in Qt 5.4.

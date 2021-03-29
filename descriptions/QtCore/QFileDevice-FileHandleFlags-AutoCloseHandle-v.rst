.. sip:enum-member-description::
    :status: todo
    :value: 0x0001
    :realname: QFileDevice::FileHandleFlag::AutoCloseHandle
    :digest: 6989d3a96eccf44ba6ff3504364ef9fd

The file handle passed into open() should be closed by :sip:ref:`~PyQt6.QtCore.QFileDevice.close`, the default behavior is that close just flushes the file and the application is responsible for closing the file handle. When opening a file by name, this flag is ignored as Qt always owns the file handle and must close it.

.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: a97664768f9e62228232b1b5dbe3a01d

Returns the human-readable name of this network interface on Windows, such as "Local Area Connection", if the name could be determined. If it couldn't, this function returns the same as :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.name`. The human-readable name is a name that the user can modify in the Windows Control Panel, so it may change during the execution of the program.

On Unix, this function currently always returns the same as :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.name`, since Unix systems don't store a configuration for human-readable names.

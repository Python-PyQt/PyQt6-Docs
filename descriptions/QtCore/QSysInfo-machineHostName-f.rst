.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 4723570b1c0a123f1ae280f918d4e4fb

Returns this machine's host name, if one is configured. Note that hostnames are not guaranteed to be globally unique, especially if they were configured automatically.

This function does not guarantee the returned host name is a Fully Qualified Domain Name (FQDN). For that, use QHostInfo to resolve the returned name to an FQDN.

This function returns the same as QHostInfo::localHostName().

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.machineUniqueId`, :sip:ref:`~PyQt6.QtNetwork.QHostInfo.localDomainName`.

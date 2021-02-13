.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 86a5fdd10b053270aaf44fa36e6e5659

Returns this machine's host name, if one is configured. Note that hostnames are not guaranteed to be globally unique, especially if they were configured automatically.

This function does not guarantee the returned host name is a Fully Qualified Domain Name (FQDN). For that, use :sip:ref:`~PyQt6.QtNetwork.QHostInfo` to resolve the returned name to an FQDN.

This function returns the same as :sip:ref:`~PyQt6.QtNetwork.QHostInfo.localHostName`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostInfo.localDomainName`, :sip:ref:`~PyQt6.QtCore.QSysInfo.machineUniqueId`.

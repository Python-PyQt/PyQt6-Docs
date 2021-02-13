.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: d24b1f830a530f0c3a331c1f852c1593

Returns this machine's host name, if one is configured. Note that hostnames are not guaranteed to be globally unique, especially if they were configured automatically.

This function does not guarantee the returned host name is a Fully Qualified Domain Name (FQDN). For that, use :sip:ref:`~PyQt6.QtNetwork.QHostInfo.fromName` to resolve the returned name to an FQDN.

This function returns the same as :sip:ref:`~PyQt6.QtCore.QSysInfo.machineHostName`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostInfo.hostName`, :sip:ref:`~PyQt6.QtNetwork.QHostInfo.localDomainName`.

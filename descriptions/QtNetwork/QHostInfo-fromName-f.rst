.. sip:method-description::
    :status: todo
    :pysig: 07677f4ba4bc04ee096adb6018ddd409
    :realsig: (const QString&)
    :digest: f112b9e32dde2a17686aae9ee0444442

Looks up the IP address(es) for the given host *name*. The function blocks during the lookup which means that execution of the program is suspended until the results of the lookup are ready. Returns the result of the lookup in a :sip:ref:`~PyQt6.QtNetwork.QHostInfo` object.

If you pass a literal IP address to *name* instead of a host name, :sip:ref:`~PyQt6.QtNetwork.QHostInfo` will search for the domain name for the IP (i.e., :sip:ref:`~PyQt6.QtNetwork.QHostInfo` will perform a *reverse* lookup). On success, the returned :sip:ref:`~PyQt6.QtNetwork.QHostInfo` will contain both the resolved domain name and IP addresses for the host name.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostInfo.lookupHost`.

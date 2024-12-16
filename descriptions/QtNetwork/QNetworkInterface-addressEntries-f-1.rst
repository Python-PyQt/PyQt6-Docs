.. sip:method-description::
    :status: todo
    :pysig: e9085ac01c6a3004a28c523bdba3daaf
    :realsig: () const
    :digest: d9986d41c1cb860c3757ac2022c9d84a

Returns the list of IP addresses that this interface possesses along with their associated netmasks and broadcast addresses.

If the netmask or broadcast address or other information is not necessary, you can call the :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.allAddresses` function to obtain just the IP addresses of the active interfaces.

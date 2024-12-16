.. sip:method-description::
    :status: todo
    :pysig: c303781efb132441000cada9251d543f
    :realsig: ()
    :digest: 8fe56579e38632ee51c04d433f9264fc

This convenience function returns all IP addresses found on the host machine. It is equivalent to calling :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.addressEntries` on all the objects returned by :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.allInterfaces` that are in the :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.InterfaceFlag.IsUp` state to obtain lists of :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry` objects then calling :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.ip` on each of these.

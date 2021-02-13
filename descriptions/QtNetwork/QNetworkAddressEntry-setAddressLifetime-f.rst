.. sip:method-description::
    :status: todo
    :pysig: 5f81a4737b90826f6b056f9f89c1189e
    :realsig: (QDeadlineTimer,QDeadlineTimer)
    :digest: 3bbc81d8d15efbf2fd3e087c1169c029

Sets both the preferred and valid lifetimes for this address to the *preferred* and *validity* deadlines, respectively. After this call, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown` will return ``true``, even if both parameters are :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.ForeverConstant.Forever`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.preferredLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.validityLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.clearAddressLifetime`.

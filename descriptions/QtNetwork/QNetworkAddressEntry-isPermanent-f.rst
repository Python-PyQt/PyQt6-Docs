.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 93be2df6c7e5d05c02cea40b94748b95

Returns ``true`` if this address is permanent on this interface, ``false`` if it's temporary. A permenant address is one which has no expiration time and is often static (manually configured).

If this information could not be determined, this function returns ``true``.

**Note:** Depending on the operating system and the networking configuration tool, it is possible for a temporary address to be interpreted as permanent, if the tool did not inform the details correctly to the operating system.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.validityLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isTemporary`.

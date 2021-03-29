.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 154456372ad3f28fa6f048a77a24d3e3

Returns the flag that indicates if this message should see a reply or not. This is only meaningful for :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.MethodCallMessage`: any other kind of message cannot have replies and this function will always return false for them.

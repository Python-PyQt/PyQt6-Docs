.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: c51cb3f025e0d1e1003fbeac1514d27d

Returns the binary data field for this record. The interpretation of this binary data depends on the three numeric fields provided by certificateUsage(), :sip:ref:`~PyQt6.QtNetwork.QDnsTlsAssociationRecord.selector`, and :sip:ref:`~PyQt6.QtNetwork.QDnsTlsAssociationRecord.matchType`.

Do note this is a binary field, even for the checksums, similar to what QCyrptographicHash::result() returns.

.. sip:method-description::
    :status: todo
    :pysig: bd954e66a71c8971f75a765e7be7b4f7
    :realsig: (const QByteArray&)
    :digest: 510267b15ffb30b8a86f68aa90496de2

Creates a :sip:ref:`~PyQt6.QtCore.QUuid` object from the binary representation of the UUID, as specified by RFC 4122 section 4.1.2. See :sip:ref:`~PyQt6.QtCore.QUuid.toRfc4122` for a further explanation of the order of *bytes* required.

The byte array accepted is NOT a human readable format.

If the conversion fails, a null UUID is created.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.toRfc4122`, :sip:ref:`~PyQt6.QtCore.QUuid`.

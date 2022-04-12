.. sip:method-description::
    :status: todo
    :pysig: afb5b12271fe20cdeb2f02fa0acd3e09
    :realsig: (QByteArrayView)
    :digest: bf0204f7d47a6359df87d7f32f3ee3b3

Creates a :sip:ref:`~PyQt6.QtCore.QUuid` object from the binary representation of the UUID, as specified by RFC 4122 section 4.1.2. See :sip:ref:`~PyQt6.QtCore.QUuid.toRfc4122` for a further explanation of the order of *bytes* required.

The byte array accepted is NOT a human readable format.

If the conversion fails, a null UUID is created.

**Note:** In Qt versions prior to 6.3, this function took :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.toRfc4122`, :sip:ref:`~PyQt6.QtCore.QUuid`.

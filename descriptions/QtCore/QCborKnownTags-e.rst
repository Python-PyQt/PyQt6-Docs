.. sip:enum-description::
    :status: todo
    :digest: 0594a4eaa7e7a4ff4512b8e34cd3b9bb

This enum contains a list of CBOR tags, known at the time of the Qt implementation. This list is not meant to be complete and contains only tags that are either backed by an RFC or specifically used by the Qt implementation.

The authoritative list is maintained by IANA in the `CBOR tag registry <https://www.iana.org/assignments/cbor-tags/cbor-tags.xhtml>`_.

The following tags are interpreted by QCborValue during decoding and will produce objects with extended Qt types, and it will use those tags when encoding the same extended types.

Additionally, if a QCborValue containing a :sip:ref:`~PyQt6.QtCore.QByteArray` is tagged using one of ``ExpectedBase64url``, ``ExpectedBase64`` or ``ExpectedBase16``, QCborValue will use the expected encoding when converting to JSON (see QCborValue::toJsonValue).

.. seealso:: QCborTag, QCborStreamWriter::append(QCborTag), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isTag`, QCborStreamReader::toTag(), QCborValue::isTag(), QCborValue::tag().

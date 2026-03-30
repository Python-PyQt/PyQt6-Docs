.. sip:method-description::
    :status: todo
    :pysig: db986ab1b4262b1cd93d14bdfb661239
    :realsig: (QUuid, QByteArrayView)
    :digest: 073a168e4021a4158fe084477377e48f

This function returns a new UUID with variant :sip:ref:`~PyQt6.QtCore.QUuid.Variant.DCE` and version :sip:ref:`~PyQt6.QtCore.QUuid.Version.Sha1`. *ns* is the namespace and *baseData* is the basic data as described by RFC 4122.

**Note:** In Qt versions prior to 6.8, this function took :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.variant`, :sip:ref:`~PyQt6.QtCore.QUuid.version`, :sip:ref:`~PyQt6.QtCore.QUuid.createUuidV3`.

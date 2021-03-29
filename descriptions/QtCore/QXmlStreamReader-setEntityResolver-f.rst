.. sip:method-description::
    :status: todo
    :pysig: 4afba593d185fb0ba98f8e66abde6aa6
    :realsig: (QXmlStreamEntityResolver*)
    :digest: 1923915bbb98037b9d293daffd799af5

Makes *resolver* the new :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.entityResolver`.

The stream reader does *not* take ownership of the resolver. It's the callers responsibility to ensure that the resolver is valid during the entire life-time of the stream reader object, or until another resolver or ``nullptr`` is set.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.entityResolver`.

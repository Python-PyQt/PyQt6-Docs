.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: e41ea826577be8b8abb8409696aeb9e8

Sets the boundary to *boundary*.

Usually, you do not need to generate a boundary yourself; upon construction the boundary is initiated with the string "boundary_.oOo._" followed by random characters, and provides enough uniqueness to make sure it does not occur inside the parts itself.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart.boundary`.

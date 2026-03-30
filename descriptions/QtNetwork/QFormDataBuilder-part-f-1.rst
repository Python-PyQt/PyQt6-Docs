.. sip:method-description::
    :status: todo
    :pysig: fb74d7d8afca8f1ab234a00321b5d440
    :realsig: (QAnyStringView)
    :digest: f6fb28a1827693f9e2c27ae97f57a5b3

Returns a newly-constructed :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder` object using *name* as the form-data's ``name`` parameter. The object is valid for as long as the associated :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder` has not been destroyed.

Limiting *name* characters to US-ASCII is `strongly recommended <https://datatracker.ietf.org/doc/html/rfc7578#section-5.1.1>`_ for interoperability reasons.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder`, :sip:ref:`~PyQt6.QtNetwork.QHttpPart`.

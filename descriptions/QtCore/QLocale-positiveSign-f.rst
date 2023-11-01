.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 321d649f4185c42bea0a28736c36d147

Returns the positive sign indicator of this locale.

This is a token presumed to be used as a prefix to a number to indicate that it is positive. It is (since Qt 6.0) returned as a string because, in some locales, it is not a single character - for example, because it includes a text-direction-control character.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.negativeSign`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.

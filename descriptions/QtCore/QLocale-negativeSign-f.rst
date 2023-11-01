.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 29b242cebcd33614c7d35c71414ee624

Returns the negative sign indicator of this locale.

This is a token presumed to be used as a prefix to a number to indicate that it is negative. It is (since Qt 6.0) returned as a string because, in some locales, it is not a single character - for example, because it includes a text-direction-control character.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.positiveSign`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.

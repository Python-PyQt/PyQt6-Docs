.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 72cd6cfe9e6e9cb79899afca42377658

Returns the percent marker of this locale.

This is a token presumed to be appended to a number to indicate a percentage. It is (since Qt 6.0) returned as a string because, in some locales, it is not a single character - for example, because it includes a text-direction-control character.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toString`.

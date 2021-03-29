.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 25a2be009fd31953e6b788f5272b5478

Returns an ordered list of locale names for translation purposes in preference order (like "en-Latn-US", "en-US", "en").

The return value represents locale names that the user expects to see the UI translation in.

Most like you do not need to use this function directly, but just pass the :sip:ref:`~PyQt6.QtCore.QLocale` object to the :sip:ref:`~PyQt6.QtCore.QTranslator.load` function.

The first item in the list is the most preferred one.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.

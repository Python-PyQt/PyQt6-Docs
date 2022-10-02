.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: f550ee57c32528a3e42c025392af10f7

Returns an ordered list of locale names for translation purposes in preference order (like "en-Latn-US", "en-US", "en").

The return value represents locale names that the user expects to see the UI translation in.

Most likely you do not need to use this function directly, but just pass the :sip:ref:`~PyQt6.QtCore.QLocale` object to the :sip:ref:`~PyQt6.QtCore.QTranslator.load` function.

Earlier items in the list are to be preferred over later ones.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.

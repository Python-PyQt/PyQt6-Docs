.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 235c1be21611fe3875388eee4d1181ad

List of locale names for use in selecting translations

Each entry in the returned list is the dash-joined name of a locale, suitable to the user's preferences for what to translate the UI into. For example, if the user has configured their system to use English as used in the USA, the list would be "en-Latn-US", "en-US", "en". The order of entries is the order in which to check for translations; earlier items in the list are to be preferred over later ones.

Most likely you do not need to use this function directly, but just pass the :sip:ref:`~PyQt6.QtCore.QLocale` object to the :sip:ref:`~PyQt6.QtCore.QTranslator.load` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.

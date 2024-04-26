.. sip:method-description::
    :status: todo
    :pysig: 56ad4ef883cc4ce8024ea8b23467505d
    :realsig: (QLocale::TagSeparator) const
    :digest: 57bf76f95dccc04133f7838296ea9783

List of locale names for use in selecting translations

Each entry in the returned list is the name of a locale suitable to the user's preferences for what to translate the UI into. Where a name in the list is composed of several tags, they are joined as indicated by *separator*. Prior to Qt 6.7 a dash was used as separator.

For example, using the default separator :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Dash`, if the user has configured their system to use English as used in the USA, the list would be "en-Latn-US", "en-US", "en". The order of entries is the order in which to check for translations; earlier items in the list are to be preferred over later ones. If your translation files use underscores, rather than dashes, to separate locale tags, pass :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Underscore` as *separator*.

Most likely you do not need to use this function directly, but just pass the :sip:ref:`~PyQt6.QtCore.QLocale` object to the :sip:ref:`~PyQt6.QtCore.QTranslator.load` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.

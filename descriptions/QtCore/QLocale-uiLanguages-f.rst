.. sip:method-description::
    :status: todo
    :pysig: ec3c9a3752adf978bc5211bc4af5be71
    :realsig: (QLocale::TagSeparator) const
    :digest: 2ece52f2d6d12934e435e70bc563914d

List of locale names for use in selecting translations

Each entry in the returned list is the name of a locale suitable to the user's preferences for what to translate the UI into. Where a name in the list is composed of several tags, they are joined as indicated by *separator*. Prior to Qt 6.7 a dash was used as separator.

For example, using the default separator :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Dash`, if the user has configured their system to use English as used in the USA, the list would be "en-Latn-US", "en-US", "en". The order of entries is the order in which to check for translations; earlier items in the list are to be preferred over later ones. If your translation files use underscores, rather than dashes, to separate locale tags, pass :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Underscore` as *separator*.

The returned list may contain entries for more than one language. In particular, this happens for :sip:ref:`~PyQt6.QtCore.QLocale.system` when the user has configured the system to accept several languages for user-interface translations. In such a case, the order of entries for distinct languages is significant. For example, where a user has configured a primarily German system to also accept English and Chinese, in that order of preference, the returned list shall contain some entries for German, then some for English, and finally some for Chinese.

Most likely you do not need to use this function directly, but just pass the :sip:ref:`~PyQt6.QtCore.QLocale` object to the :sip:ref:`~PyQt6.QtCore.QTranslator.load` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.

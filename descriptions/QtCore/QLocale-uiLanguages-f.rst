.. sip:method-description::
    :status: todo
    :pysig: ec3c9a3752adf978bc5211bc4af5be71
    :realsig: (QLocale::TagSeparator) const
    :digest: 93f3e25452c50769728e173bcdb2f4e7

List of locale names for use in selecting translations

Each entry in the returned list is the name of a locale suitable to the user's preferences for what to translate the UI into. Where a name in the list is composed of several tags, they are joined as indicated by *separator*. Prior to Qt 6.7 a dash was used as separator.

For example, using the default separator :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Dash`, if the user has configured their system to use English as used in the USA, the list would be "en-Latn-US", "en-US", "en". The order of entries is the order in which to check for translations; earlier items in the list are to be preferred over later ones. If your translation files use underscores, rather than dashes, to separate locale tags, pass :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Underscore` as *separator*.

Returns a list of locale names. This may include multiple languages, especially for the system locale when multiple UI translation languages are configured. The order of entries is significant. For example, for the system locale, it reflects user preferences.

Prior to Qt 6.9, the list only contained explicitly configured locales and their equivalents. This led some callers to add truncations (such as from 'en-Latn-DE' to 'en') as fallbacks. This could sometimes result in inappropriate choices, especially if these were tried before later entries that would be more appropriate fallbacks.

Starting from Qt 6.9, reasonable truncations are included in the returned list *after* the explicitly specified locales. This change allows for more accurate fallback options without callers needing to do any truncation.

Users can explicitly include preferred fallback locales (such as en-US) in their system configuration to control the order of preference. You are advised to rely on the order of entries in uiLanguages() rather than using custom fallback methods.

Most likely you do not need to use this function directly, but just pass the :sip:ref:`~PyQt6.QtCore.QLocale` object to the :sip:ref:`~PyQt6.QtCore.QTranslator.load` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.

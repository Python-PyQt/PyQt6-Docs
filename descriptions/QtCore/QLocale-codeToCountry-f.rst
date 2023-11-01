.. sip:method-description::
    :status: todo
    :pysig: 34fe242c1692bbfd98eec30b8774fe82
    :realsig: (QStringView)
    :digest: 6c6b040b755ead59b1cd83324d16d782

Returns the QLocale::Territory enum corresponding to the two-letter or three-digit *countryCode*, as defined in the ISO 3166 standard.

If the code is invalid or not known :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` is returned.

Use :sip:ref:`~PyQt6.QtCore.QLocale.codeToTerritory`\ (QStringView) instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.territoryToCode`, :sip:ref:`~PyQt6.QtCore.QLocale.codeToLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.codeToScript`.

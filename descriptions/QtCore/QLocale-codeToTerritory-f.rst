.. sip:method-description::
    :status: todo
    :pysig: 34fe242c1692bbfd98eec30b8774fe82
    :realsig: (QStringView)
    :digest: 968d75cb9af44717ee86d5959d3660d5

Returns the QLocale::Territory enum corresponding to the two-letter or three-digit *territoryCode*, as defined in the ISO 3166 standard.

If the code is invalid or not known :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.territoryToCode`, :sip:ref:`~PyQt6.QtCore.QLocale.codeToLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.codeToScript`.

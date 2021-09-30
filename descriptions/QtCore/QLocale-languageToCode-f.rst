.. sip:method-description::
    :status: todo
    :pysig: 73006f7782b6a3bfad28bb041a77127a
    :realsig: (QLocale::Language)
    :digest: e8615d9e02bc7f302ff7e690f44e1998

Returns the two- or three-letter language code for *language*, as defined in the ISO 639 standards.

**Note:** For ``QLocale::C`` the function returns ``"C"``. For ``QLocale::AnyLanguage`` an empty string is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.codeToLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.name`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`, :sip:ref:`~PyQt6.QtCore.QLocale.territoryToCode`, :sip:ref:`~PyQt6.QtCore.QLocale.scriptToCode`.

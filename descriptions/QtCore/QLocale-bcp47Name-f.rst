.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 5190ddb46ec791021787be3db4e5de5f

Returns the dash-separated language, script and country (and possibly other BCP47 fields) of this locale as a string.

Unlike the :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages` the returned value of the  represents the locale name of the :sip:ref:`~PyQt6.QtCore.QLocale` data but not the language the user-interface should be in.

This function tries to conform the locale name to BCP47.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.country`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`.

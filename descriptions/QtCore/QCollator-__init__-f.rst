.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 326e24a092968fce6eb2399e1cbe3653

Constructs a :sip:ref:`~PyQt6.QtCore.QCollator` using the default locale's collation locale.

The system locale, when used as default locale, may have a collation locale other than itself (e.g. on Unix, if LC_COLLATE is set differently to LANG in the environment). All other locales are their own collation locales.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCollator.setLocale`, :sip:ref:`~PyQt6.QtCore.QLocale.collation`, :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`.

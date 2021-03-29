.. sip:method-description::
    :status: todo
    :pysig: 36f9da782e7efe22aed73d2c2bc20799
    :realsig: (QTranslator*)
    :digest: 9d6c7d7ca5d1bc94203692c05df9b140

Removes the translation file *translationFile* from the list of translation files used by this application. (It does not delete the translation file from the file system.)

The function returns ``true`` on success and false on failure.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.installTranslator`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.translate`, :sip:ref:`~PyQt6.QtCore.QObject.tr`.

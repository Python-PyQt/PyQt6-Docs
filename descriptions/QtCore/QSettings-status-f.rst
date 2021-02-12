.. sip:method-description::
    :status: todo
    :pysig: 31c8f6191c53aa6c4d91053c337c12ae
    :realsig: () const
    :digest: 81eb494c1f6f63af1cae5dd78bdc82f8

Returns a status code indicating the first error that was met by :sip:ref:`~PyQt6.QtCore.QSettings`, or :sip:ref:`~PyQt6.QtCore.QSettings.Status.NoError` if no error occurred.

Be aware that :sip:ref:`~PyQt6.QtCore.QSettings` delays performing some operations. For this reason, you might want to call :sip:ref:`~PyQt6.QtCore.QSettings.sync` to ensure that the data stored in :sip:ref:`~PyQt6.QtCore.QSettings` is written to disk before calling .

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.sync`.

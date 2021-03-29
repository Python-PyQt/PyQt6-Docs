.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: (bool)
    :digest: c5eec200cd1db354b0e562ca1a2559a3

Allows the application to run setuid on UNIX platforms if *allow* is true.

If *allow* is false (the default) and Qt detects the application is running with an effective user id different than the real user id, the application will be aborted when a :sip:ref:`~PyQt6.QtCore.QCoreApplication` instance is created.

Qt is not an appropriate solution for setuid programs due to its large attack surface. However some applications may be required to run in this manner for historical reasons. This flag will prevent Qt from aborting the application when this is detected, and must be set before a :sip:ref:`~PyQt6.QtCore.QCoreApplication` instance is created.

**Note:** It is strongly recommended not to enable this option since it introduces security risks.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.isSetuidAllowed`.

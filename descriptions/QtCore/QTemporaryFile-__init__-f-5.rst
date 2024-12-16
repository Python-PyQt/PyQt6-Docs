.. sip:method-description::
    :status: todo
    :pysig: 7a792ec7fc75acdd989096b04406cda5
    :realsig: (const QString&, QObject*)
    :digest: 6c98935b9ce630e1c30da590ee24eba5

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` with the specified *parent*, and *templateName* as the file name template.

Upon opening the temporary file, *templateName* will be used to create a unique filename.

If the file name (the part after the last directory path separator in *templateName*) doesn't contain ``"XXXXXX"``, it will be added automatically.

``"XXXXXX"`` will be replaced with the dynamic part of the file name, which is calculated to be unique.

If *templateName* is a relative path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *templateName* if you want use the system's temporary directory. It is important to specify the correct directory if the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename` function will be called, as :sip:ref:`~PyQt6.QtCore.QTemporaryFile` can only rename files within the same volume / filesystem as the temporary file itself was created on.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.

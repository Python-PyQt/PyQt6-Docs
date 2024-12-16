.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 7653a77fb1071b620c14cefec136989a

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` with *templateName* as the file name template.

Upon opening the temporary file, *templateName* will be used to create a unique filename.

If the file name (the part after the last directory path separator in *templateName*) doesn't contain ``"XXXXXX"``, it will be added automatically.

``"XXXXXX"`` will be replaced with the dynamic part of the file name, which is calculated to be unique.

If *templateName* is a relative path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *templateName* if you want use the system's temporary directory.

It is important to specify the correct directory if the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename` function will be called, as :sip:ref:`~PyQt6.QtCore.QTemporaryFile` can only rename files within the same volume / filesystem as the temporary file itself was created on.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.

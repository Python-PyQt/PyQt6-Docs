.. sip:method-description::
    :status: todo
    :pysig: 7a792ec7fc75acdd989096b04406cda5
    :realsig: (const QString&, QObject*)
    :digest: d7fd5fe1f8a9522e4922c8e815bc0d39

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` with a template filename of *templateName* and the specified *parent*. Upon opening the temporary file this will be used to create a unique filename.

If the *templateName* does not contain XXXXXX it will automatically be appended and used as the dynamic portion of the filename.

If *templateName* is a relative path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *templateName* if you want use the system's temporary directory. It is important to specify the correct directory if the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename` function will be called, as :sip:ref:`~PyQt6.QtCore.QTemporaryFile` can only rename files within the same volume / filesystem as the temporary file itself was created on.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.

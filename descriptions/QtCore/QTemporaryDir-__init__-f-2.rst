.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 5db4a76d3f9763d318ab6a67021b2326

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryDir` with a template of *templatePath*.

If *templatePath* is a relative path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *templatePath* if you want use the system's temporary directory.

If the *templatePath* ends with XXXXXX it will be used as the dynamic portion of the directory name, otherwise it will be appended. Unlike :sip:ref:`~PyQt6.QtCore.QTemporaryFile`, XXXXXX in the middle of the template string is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.

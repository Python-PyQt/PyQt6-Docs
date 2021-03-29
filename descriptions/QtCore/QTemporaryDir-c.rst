.. sip:class-description::
    :status: todo
    :brief: Creates a unique directory for temporary use
    :digest: 153d9564418dc109839533e24335b112

The :sip:ref:`~PyQt6.QtCore.QTemporaryDir` class creates a unique directory for temporary use.

:sip:ref:`~PyQt6.QtCore.QTemporaryDir` is used to create unique temporary directories safely. The directory itself is created by the constructor. The name of the temporary directory is guaranteed to be unique (i.e., you are guaranteed to not overwrite an existing directory), and the directory will subsequently be removed upon destruction of the :sip:ref:`~PyQt6.QtCore.QTemporaryDir` object. The directory name is either auto-generated, or created based on a template, which is passed to :sip:ref:`~PyQt6.QtCore.QTemporaryDir`'s constructor.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtemporarydir.py
    :lines: 55-63

It is very important to test that the temporary directory could be created, using :sip:ref:`~PyQt6.QtCore.QTemporaryDir.isValid`. Do not use :sip:ref:`~PyQt6.QtCore.QDir.exists`, since a default-constructed :sip:ref:`~PyQt6.QtCore.QDir` represents the current directory, which exists.

The path to the temporary directory can be found by calling :sip:ref:`~PyQt6.QtCore.QTemporaryDir.path`.

A temporary directory will have some static part of the name and some part that is calculated to be unique. The default path will be determined from :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` (otherwise ``qt_temp``) and will be placed into the temporary path as returned by :sip:ref:`~PyQt6.QtCore.QDir.tempPath`. If you specify your own path, a relative path will not be placed in the temporary directory by default, but be relative to the current working directory. In all cases, a random string will be appended to the path in order to make it unique.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.tempPath`, :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile`.

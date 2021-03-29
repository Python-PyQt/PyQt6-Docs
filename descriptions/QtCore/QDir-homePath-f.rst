.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 6910b2dc14ce14a86ca848ac3df6b17d

Returns the absolute path of the user's home directory.

Under Windows this function will return the directory of the current user's profile. Typically, this is:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 159-159

Use the :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators` function to convert the separators to the ones that are appropriate for the underlying operating system.

If the directory of the current user's profile does not exist or cannot be retrieved, the following alternatives will be checked (in the given order) until an existing and available path is found:

#. The path specified by the ``USERPROFILE`` environment variable.

#. The path formed by concatenating the ``HOMEDRIVE`` and ``HOMEPATH`` environment variables.

#. The path specified by the ``HOME`` environment variable.

#. The path returned by the :sip:ref:`~PyQt6.QtCore.QDir.rootPath` function (which uses the ``SystemDrive`` environment variable)

#. The ``C:/`` directory.

Under non-Windows operating systems the ``HOME`` environment variable is used if it exists, otherwise the path returned by the :sip:ref:`~PyQt6.QtCore.QDir.rootPath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.home`, :sip:ref:`~PyQt6.QtCore.QDir.currentPath`, :sip:ref:`~PyQt6.QtCore.QDir.rootPath`, :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.

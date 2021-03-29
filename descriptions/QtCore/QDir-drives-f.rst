.. sip:method-description::
    :status: todo
    :pysig: 0878348e7932f1af774296939cf52b70
    :realsig: ()
    :digest: 2498495f0dac4dc78bdba726cd192ab7

Returns a list of the root directories on this system.

On Windows this returns a list of :sip:ref:`~PyQt6.QtCore.QFileInfo` objects containing "C:/", "D:/", etc. On other operating systems, it returns a list containing just one root directory (i.e. "/").

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.root`, :sip:ref:`~PyQt6.QtCore.QDir.rootPath`.

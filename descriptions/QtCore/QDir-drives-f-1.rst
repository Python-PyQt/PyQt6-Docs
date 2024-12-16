.. sip:method-description::
    :status: todo
    :pysig: f6c7acd9eb85295547c7f02ff98b1213
    :realsig: ()
    :digest: 2498495f0dac4dc78bdba726cd192ab7

Returns a list of the root directories on this system.

On Windows this returns a list of :sip:ref:`~PyQt6.QtCore.QFileInfo` objects containing "C:/", "D:/", etc. This does not return drives with ejectable media that are empty. On other operating systems, it returns a list containing just one root directory (i.e. "/").

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.root`, :sip:ref:`~PyQt6.QtCore.QDir.rootPath`.

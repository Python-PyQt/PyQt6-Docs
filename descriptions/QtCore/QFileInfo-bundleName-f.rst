.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 854a458a436d04ea470a7f59cbb7ace1

Returns the name of the bundle.

On macOS and iOS this returns the proper localized name for a bundle if the path :sip:ref:`~PyQt6.QtCore.QFileInfo.isBundle`. On all other platforms an empty QString is returned.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 116-117

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isBundle`, :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix`.

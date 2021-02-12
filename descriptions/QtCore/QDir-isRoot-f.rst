.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 25d3a7ae6db76a3a462a4d268572b0ea

Returns ``true`` if the directory is the root directory; otherwise returns ``false``.

**Note:** If the directory is a symbolic link to the root directory this function returns ``false``. If you want to test for this use :sip:ref:`~PyQt6.QtCore.QDir.canonicalPath`, e.g.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 132-135

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.root`, :sip:ref:`~PyQt6.QtCore.QDir.rootPath`.

.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 065866dbcee797dd2a50783ccfbd8117

Returns ``true`` if this URL is pointing to a local file path. A URL is a local file path if the scheme is "file".

Note that this function considers URLs with hostnames to be local file paths, even if the eventual file path cannot be opened with :sip:ref:`~PyQt6.QtCore.QFile.open`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile`, :sip:ref:`~PyQt6.QtCore.QUrl.toLocalFile`.

.. sip:method-description::
    :status: todo
    :pysig: 5ae4df144bb6014c3175a8eeb873f7f7
    :realsig: (const QString&)
    :digest: dd38ad490b2fddb71e1ce60d7c0c5ebe

Returns *path* with directory separators normalized (that is, platform-native separators converted to "/") and redundant ones removed, and "."s and ".."s resolved (as far as possible).

Symbolic links are kept. This function does not return the canonical path, but rather the simplest version of the input. For example, "./local" becomes "local", "local/../bin" becomes "bin" and "/local/usr/../bin" becomes "/local/bin".

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.canonicalPath`.

.. sip:method-description::
    :status: todo
    :pysig: af76945fd0d9041f46237f50227c25fb
    :realsig: (const QString&)
    :digest: 26c67f320f694ef89cbd41dbe5e6313e

Returns ``true`` if the file system entry *path* exists; otherwise returns ``false``.

**Note:** If *path* is a symlink that points to a non-existing target, this method returns ``false``.

**Note:** Using this function is faster than using ``QFileInfo(path).exists()`` for file system access.

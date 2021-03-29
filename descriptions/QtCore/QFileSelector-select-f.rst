.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&) const
    :digest: b286349fcafe6ad4fd120db9020db8db

This function returns the selected version of the path, based on the conditions at runtime. If no selectable files are present, returns the original *filePath*.

If the original file does not exist, the original *filePath* is returned. This means that you must have a base file to fall back on, you cannot have only files in selectable sub-directories.

See the class overview for the selection algorithm.

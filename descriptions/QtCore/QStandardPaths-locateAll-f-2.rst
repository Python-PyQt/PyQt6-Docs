.. sip:method-description::
    :status: todo
    :pysig: 4fa8b7c7fdde8c6814e1551706e18292
    :realsig: (QStandardPaths::StandardLocation, const QString&, QStandardPaths::LocateOptions)
    :digest: 2785fabc2bb2c1932e5613d2272adcce

Finds all files or directories by the name, *fileName*, in the standard locations for *type*.

The *options* flag lets you specify whether to look for files or directories. By default, this flag is set to ``LocateFile``.

Returns the list of all the files that were found.

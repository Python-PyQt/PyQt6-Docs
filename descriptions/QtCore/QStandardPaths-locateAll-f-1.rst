.. sip:method-description::
    :status: todo
    :pysig: 70be25a34c464e2c915f64879ae13878
    :realsig: (QStandardPaths::StandardLocation, const QString&, QStandardPaths::LocateOptions)
    :digest: 2785fabc2bb2c1932e5613d2272adcce

Finds all files or directories by the name, *fileName*, in the standard locations for *type*.

The *options* flag lets you specify whether to look for files or directories. By default, this flag is set to ``LocateFile``.

Returns the list of all the files that were found.

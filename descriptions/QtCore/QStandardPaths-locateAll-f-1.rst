.. sip:method-description::
    :status: todo
    :pysig: 89816a55353f704b7b69416be45342ea
    :realsig: (QStandardPaths::StandardLocation,const QString&,QStandardPaths::LocateOptions)
    :digest: 2785fabc2bb2c1932e5613d2272adcce

Finds all files or directories by the name, *fileName*, in the standard locations for *type*.

The *options* flag lets you specify whether to look for files or directories. By default, this flag is set to ``LocateFile``.

Returns the list of all the files that were found.

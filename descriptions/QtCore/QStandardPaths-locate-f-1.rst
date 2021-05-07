.. sip:method-description::
    :status: todo
    :pysig: a6af309a222379b52d79c2c93afeeef1
    :realsig: (QStandardPaths::StandardLocation,const QString&,QStandardPaths::LocateOptions)
    :digest: b26ecba29f363a7a044ed0a74e806cbf

Finds a file or directory called *fileName* in the standard locations for *type*.

The *options* flag lets you specify whether to look for files or directories. By default, this flag is set to ``LocateFile``.

Returns the absolute path to the first file or directory found, otherwise returns an empty string.

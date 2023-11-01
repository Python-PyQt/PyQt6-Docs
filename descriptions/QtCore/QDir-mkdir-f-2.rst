.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: ade439596a47efb8921ba9e16ec7160f

This is an overloaded function.

Creates a sub-directory called *dirName* with default permissions.

On POSIX systems the default is to grant all permissions allowed by ``umask``. On Windows, the new directory inherits its permissions from its parent directory.

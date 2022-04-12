.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: ade439596a47efb8921ba9e16ec7160f

This is an overloaded function.

Creates a sub-directory called *dirName* with default permissions.

On POSIX systems the default is to grant all permissions allowed by ``umask``. On Windows, the new directory inherits its permissions from its parent directory.

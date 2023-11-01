.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: f61f9cfef814005ea3a2ab352e383c81

Constructs a new file object to represent the file with the given *name*.

**Note:** In versions up to and including Qt 6.8, this constructor is implicit, for backward compatibility. Starting from Qt 6.9 this constructor is unconditionally ``explicit``. Users can force this constructor to be ``explicit`` even in earlier versions of Qt by defining the ``QT_EXPLICIT_QFILE_CONSTRUCTION_FROM_PATH`` macro before including any Qt header.

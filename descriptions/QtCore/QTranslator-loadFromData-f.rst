.. sip:method-description::
    :status: todo
    :pysig: 4f368d9839817c1d5e7c5419bd564d38
    :realname: QTranslator::load
    :realsig: (const uchar*, int, const QString&)
    :digest: d5e75e209dcbbb2a015da85bbd13d27f

Loads the QM file data *data* of length *len* into the translator.

The data is not copied. The caller must be able to guarantee that *data* will not be deleted or modified.

*directory* is only used to specify the base directory when loading the dependencies of a QM file. If the file does not have dependencies, this argument is ignored.

.. sip:method-description::
    :status: todo
    :pysig: 9b562737461578d8cc91b1e52d7fdebd
    :realname: QTranslator::load
    :realsig: (const uchar*, int, const QString&)
    :digest: d0aff0770cbad0cf04fdb88c2ecdf0ba

This function overloads :sip:ref:`~PyQt6.QtCore.QTranslator.load`.

Loads the QM file data *data* of length *len* into the translator.

The data is not copied. The caller must be able to guarantee that *data* will not be deleted or modified.

*directory* is only used to specify the base directory when loading the dependencies of a QM file. If the file does not have dependencies, this argument is ignored.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8577eaf0f5a6a1ac33462892ccfe4738

Constructs a :sip:ref:`~PyQt6.QtCore.QMimeDatabase` object.

It is perfectly OK to create an instance of :sip:ref:`~PyQt6.QtCore.QMimeDatabase` every time you need to perform a lookup. The parsing of mimetypes is done on demand (when shared-mime-info is installed) or when the very first instance is constructed (when parsing XML files directly).

.. sip:enum-description::
    :status: todo
    :realname: QByteArray::Base64Option
    :digest: 629dc3b17cc59cb67859f48e952fe718

This enum contains the options available for encoding and decoding Base64. Base64 is defined by RFC 4648, with the following options:

:sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64Encoding` and :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64` ignore the  and  options. If the  option is specified, they will not flag errors in case trailing equal signs are missing or if there are too many of them. If instead the  is specified, then the input must either have no padding or have the correct amount of equal signs.

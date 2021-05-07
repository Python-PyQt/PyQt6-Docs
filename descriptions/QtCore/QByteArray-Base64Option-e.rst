.. sip:enum-description::
    :status: todo
    :digest: 7caffe9d50b1665f4db910f56512b030

This enum contains the options available for encoding and decoding Base64. Base64 is defined by `RFC 4648 <https://doc.qt.io/qt-6/http://www.ietf.org/rfc/rfc4648.txt>`_, with the following options:

:sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64Encoding` and :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64` ignore the  and  options. If the  option is specified, they will not flag errors in case trailing equal signs are missing or if there are too many of them. If instead the  is specified, then the input must either have no padding or have the correct amount of equal signs.

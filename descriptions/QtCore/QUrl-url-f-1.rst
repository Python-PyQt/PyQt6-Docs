.. sip:method-description::
    :status: todo
    :pysig: 7ae44f1bbde23e9558980e5884c5eed9
    :realsig: (QUrl::FormattingOptions) const
    :digest: 69e3f6fe44adad309288c0e80c49de60

Returns a string representation of the URL. The output can be customized by passing flags with *options*. The option :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` is not permitted in this function since it would generate ambiguous data.

The resulting QString can be passed back to a :sip:ref:`~PyQt6.QtCore.QUrl` later on.

Synonym for :sip:ref:`~PyQt6.QtCore.QUrl.toString`\ (options).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`, FormattingOptions, :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.toString`.

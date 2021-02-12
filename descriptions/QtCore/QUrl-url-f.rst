.. sip:method-description::
    :status: todo
    :pysig: 19a424c55930c467a30dee31e5d257ea
    :realsig: (QUrl::FormattingOptions) const
    :digest: 69e3f6fe44adad309288c0e80c49de60

Returns a string representation of the URL. The output can be customized by passing flags with *options*. The option :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` is not permitted in this function since it would generate ambiguous data.

The resulting QString can be passed back to a :sip:ref:`~PyQt6.QtCore.QUrl` later on.

Synonym for :sip:ref:`~PyQt6.QtCore.QUrl.toString`\ (options).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`, FormattingOptions, :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.toString`.

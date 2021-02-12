.. sip:method-description::
    :status: todo
    :pysig: 19a424c55930c467a30dee31e5d257ea
    :realsig: (QUrl::FormattingOptions) const
    :digest: 5bbb3556e5905b72c336f5d720ab5fa9

Returns a string representation of the URL. The output can be customized by passing flags with *options*. The option :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` is not permitted in this function since it would generate ambiguous data.

The default formatting option is PrettyDecoded.

.. seealso:: FormattingOptions, :sip:ref:`~PyQt6.QtCore.QUrl.url`, :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`.

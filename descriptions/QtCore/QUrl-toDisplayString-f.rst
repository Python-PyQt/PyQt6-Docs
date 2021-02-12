.. sip:method-description::
    :status: todo
    :pysig: 19a424c55930c467a30dee31e5d257ea
    :realsig: (QUrl::FormattingOptions) const
    :digest: c64f3e7e5dfb8418a9fbfbdb9d7ba5de

Returns a human-displayable string representation of the URL. The output can be customized by passing flags with *options*. The option :sip:ref:`~PyQt6.QtCore.QUrl.FormattingOptions.RemovePassword` is always enabled, since passwords should never be shown back to users.

With the default options, the resulting QString can be passed back to a :sip:ref:`~PyQt6.QtCore.QUrl` later on, but any password that was present initially will be lost.

.. seealso:: FormattingOptions, :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.toString`.

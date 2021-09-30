.. sip:method-description::
    :status: todo
    :pysig: d01569e705624c96f60d83befc47f176
    :realsig: (const QNearFieldTarget::RequestId&,int)
    :digest: 3577efef7c73cd91f9dac6b40dff5b6d

Waits up to *msecs* milliseconds for the request *id* to complete. Returns ``true`` if the request completes successfully and the requestCompeted() signal is emitted; otherwise returns ``false``.

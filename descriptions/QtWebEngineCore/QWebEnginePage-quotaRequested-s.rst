.. sip:signal-description::
    :status: todo
    :pysig: 49b64e54ace4f4d65c3597c91bda7b3d
    :realsig: (QWebEngineQuotaRequest)
    :digest: f8736d3585daa4cde34116a12b113c58

This signal is emitted when the web page requests larger persistent storage than the application's current allocation in File System API. The default quota is 0 bytes.

The request object *quotaRequest* can be used to accept or reject the request.

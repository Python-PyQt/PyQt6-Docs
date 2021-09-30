.. sip:method-description::
    :status: todo
    :pysig: a0a8d6c42a6cfd32085dec64a6c5e9ae
    :realsig: (const QNetworkRequest&)
    :digest: e62975cf1bd533b372993e86c8a55783

Opens a WebSocket connection using the given *request*.

The *request* url will be used to open the WebSocket connection. Headers present in the request will be sent to the server in the upgrade request, together with the ones needed for the websocket handshake.

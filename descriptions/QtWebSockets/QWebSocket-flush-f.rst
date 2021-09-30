.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 8366258057cedbfff58b05926c8a1555

This function writes as much as possible from the internal write buffer to the underlying network socket, without blocking. If any data was written, this function returns true; otherwise false is returned. Call this function if you need :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` to start sending buffered data immediately. The number of bytes successfully written depends on the operating system. In most cases, you do not need to call this function, because :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` will start sending data automatically once control goes back to the event loop.

.. sip:method-description::
    :status: todo
    :pysig: 43c26245edbe714e78d9955a1dcc4223
    :realsig: (const QByteArray&, QIODevice*)
    :digest: e83745ff6ce95e15172cfa706d7e141b

Replies to the request with *device* and the content type *contentType*. Content type is similar to the HTTP Content-Type header, and can either be a MIME type, or a MIME type and charset encoding combined like this: "text/html; charset=utf-8".

The user has to be aware that *device* will be used on another thread until the job is deleted. In case simultaneous access from the main thread is desired, the user is reponsible for making access to *device* thread-safe for example by using :sip:ref:`~PyQt6.QtCore.QMutex`. Note that the *device* object is not owned by the web engine. Therefore, the signal :sip:ref:`~PyQt6.QtCore.QObject.destroyed` of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob` must be monitored.

The device should remain available at least as long as the job exists. When calling this method with a newly constructed device, one solution is to make the device as a child of the job or delete itself when job is deleted, like this:

::

    connect(job, &QObject::destroyed, device, &QObject::deleteLater);

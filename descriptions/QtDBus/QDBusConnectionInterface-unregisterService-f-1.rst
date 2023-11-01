.. sip:method-description::
    :status: todo
    :pysig: 76c3e4438585fd77ca965677159dcbb9
    :realsig: (const QString&)
    :digest: d3c270905799ac80f98321810b161981

Releases the claim on the bus service name *serviceName*, that had been previously registered with :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.registerService`. If this application had ownership of the name, it will be released for other applications to claim. If it only had the name queued, it gives up its position in the queue.

.. sip:signal-description::
    :status: todo
    :pysig: cd7c8f0d56c5dcad36dbab44b782da4c
    :realsig: (const QString&, int, void*)
    :digest: e2e3395dc9223162d03f04c3991d974d

This generic signal gets emitted when the COM object issues the event *name*. *argc* is the number of parameters provided by the event (DISPPARAMS.cArgs), and *argv* is the pointer to the parameter values (DISPPARAMS.rgvarg). Note that the order of parameter values is turned around, ie. the last element of the array is the first parameter in the function.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 198-210

Use this signal if the event has parameters of unsupported data types. Otherwise, connect directly to the signal *name*.

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBaseObject.signal`.

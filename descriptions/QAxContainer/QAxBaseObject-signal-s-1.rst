.. sip:signal-description::
    :status: todo
    :pysig: f704bcbcf4f8390219d3e0aefd8ae085
    :realsig: (const QString&,int,void*)
    :digest: 2504b5ddbd11fe41c87b4e7efaccc855

This generic signal gets emitted when the COM object issues the event *name*. *argc* is the number of parameters provided by the event (DISPPARAMS.cArgs), and *argv* is the pointer to the parameter values (DISPPARAMS.rgvarg). Note that the order of parameter values is turned around, ie. the last element of the array is the first parameter in the function.

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBaseWidget.signal`.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 307abe95b48f361d256eeaeac1431dcc

Trims the engine's internal component cache.

This function causes the property metadata of any loaded components which are not currently in use to be destroyed.

A component is considered to be in use if there are any extant instances of the component itself, any instances of other components that use the component, or any objects instantiated by any of those components.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.clearComponentCache`.

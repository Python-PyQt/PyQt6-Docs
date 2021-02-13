.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: () const
    :digest: 36fe2f01c21bddd665883ebae6d33694

Return the base URL for this engine. The base URL is only used to resolve components when a relative URL is passed to the :sip:ref:`~PyQt6.QtQml.QQmlComponent` constructor.

If a base URL has not been explicitly set, this method returns the application's current working directory.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.setBaseUrl`.

.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0f72b08612d2a9fcb9f0185ee7950e2a

Clears the engine's internal component cache.

This function causes the property metadata of all components previously loaded by the engine to be destroyed. All previously loaded components and the property bindings for all extant objects created from those components will cease to function.

This function returns the engine to a state where it does not contain any loaded component data. This may be useful in order to reload a smaller subset of the previous component set, or to load a new version of a previously loaded component.

Once the component cache has been cleared, components must be loaded before any new objects can be created.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.trimComponentCache`.

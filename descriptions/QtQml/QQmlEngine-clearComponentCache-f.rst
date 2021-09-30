.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a58675f3c43dfbc6a8220d8e8a2a948a

Clears the engine's internal component cache.

This function causes the property metadata of all components previously loaded by the engine to be destroyed. All previously loaded components and the property bindings for all extant objects created from those components will cease to function.

This function returns the engine to a state where it does not contain any loaded component data. This may be useful in order to reload a smaller subset of the previous component set, or to load a new version of a previously loaded component.

Once the component cache has been cleared, components must be loaded before any new objects can be created.

**Note:** Any existing objects created from QML components retain their types, even if you clear the component cache. This includes singleton objects. If you create more objects from the same QML code after clearing the cache, the new objects will be of different types than the old ones. Assigning such a new object to a property of its declared type belonging to an object created before clearing the cache won't work.

As a general rule of thumb, make sure that no objects created from QML components are alive when you clear the component cache.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.trimComponentCache`.

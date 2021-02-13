.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,int)
    :digest: e43e299b08f0abee334819a237c6e1cc

This function protects a module from having types registered into it. This can be used to prevent other plugins from injecting types into your module. It can also be a performance improvement, as it allows the engine to skip checking for the possibility of new types or plugins when this import is reached.

The performance benefit is primarily seen when registering application specific types from within the application instead of through a plugin. Using  allows the engine to skip checking for a plugin when that uri is imported, which can be noticeable with slow file systems.

After this function is called, any attempt to register C++ types into this uri, major version combination will lead to a runtime error. Call this after you have registered all of your types with the engine.

Returns true if the module with *uri* as a `module identifier <https://doc.qt.io/qt-6/qtqml-modules-identifiedmodules.html>`_ and *majVersion* as a major version number was found and locked, otherwise returns false. The module must contain exported types in order to be found.

.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,int)
    :digest: e1c7e3e147ed8cc3ba3db96062c584de

This function protects a module from further modification. This can be used to prevent other plugins from injecting types into your module. It can also be a performance improvement, as it allows the engine to skip checking for the possibility of new types or plugins when this import is reached.

Once  has been called, a QML engine will not search for a new ``qmldir`` file to load the module anymore. It will re-use any ``qmldir`` files it has loaded before, though. Therefore, types present at this point continue to work. Mind that different QML engines may load different modules. The module protection, however, is global and affects all engines. The overhead of locating ``qmldir`` files and loading plugins may be noticeable with slow file systems. Therefore, protecting a module once you are sure you won't need to load it anymore can be a good optimization. Mind also that the module lock not only affects plugins but also any other qmldir directives, like ``import`` or ``prefer``, as well as any composite types or scripts declared in a ``qmldir`` file.

In addition, after this function is called, any attempt to register C++ types into this uri, major version combination will lead to a runtime error.

Returns true if the module with *uri* as a `module identifier <https://doc.qt.io/qt-6/qtqml-modules-identifiedmodules.html>`_ and *majVersion* as a major version number was found and locked, otherwise returns false. The module must contain exported types in order to be found.

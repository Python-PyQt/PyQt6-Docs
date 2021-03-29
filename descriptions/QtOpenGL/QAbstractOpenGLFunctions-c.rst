.. sip:class-description::
    :status: todo
    :brief: The base class of a family of classes that expose all functions for each OpenGL version and profile
    :digest: c4f351509d30bae7e675ab2e090e10f8

The :sip:ref:`~PyQt6.QtOpenGL.QAbstractOpenGLFunctions` class is the base class of a family of classes that expose all functions for each OpenGL version and profile.

OpenGL implementations on different platforms are able to link to a variable number of OpenGL functions depending upon the OpenGL ABI on that platform. For example, on Microsoft Windows only functions up to those in OpenGL 1.1 can be linked to at build time. All other functions must be resolved at runtime. The traditional solution to this has been to use either :sip:ref:`~PyQt6.QtGui.QOpenGLContext.getProcAddress` or QOpenGLFunctions. The former is tedious and error prone and means dealing directly with function pointers. The latter only exposes those functions common to OpenGL ES 2 and desktop OpenGL. There is however much new OpenGL functionality that is useful when writing real world OpenGL applications.

Qt now provides a family of classes which all inherit from :sip:ref:`~PyQt6.QtOpenGL.QAbstractOpenGLFunctions` which expose every core OpenGL function by way of a corresponding member function. There is a class for every valid combination of OpenGL version and profile. Each class follows the naming convention:

::

    QOpenGLFunctions_<MAJOR VERSION>_<MINOR VERSION>[_PROFILE]

For OpenGL versions 1.0 through to 3.0 there are no profiles, leading to the classes:

* QOpenGLFunctions_1_0

* QOpenGLFunctions_1_1

* QOpenGLFunctions_1_2

* QOpenGLFunctions_1_3

* QOpenGLFunctions_1_4

* QOpenGLFunctions_1_5

* :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFunctions_2_0`

* :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFunctions_2_1`

* QOpenGLFunctions_3_0

where each class inherits from :sip:ref:`~PyQt6.QtOpenGL.QAbstractOpenGLFunctions`.

OpenGL version 3.1 removed many deprecated functions leading to a much simpler and generic API.

With OpenGL 3.2 the concept of profiles was introduced. Two profiles are currently defined for OpenGL: Core and Compatibility.

The Core profile does not include any of the functions that were removed in OpenGL 3.1. The Compatibility profile contains all functions in the Core profile of the same version plus all of the functions that were removed in OpenGL 3.1. In this way the Compatibility profile classes allow use of newer OpenGL functionality but also allows you to keep using your legacy OpenGL code. For new OpenGL code the Core profile should be preferred.

Please note that some vendors, notably Apple, do not implement the Compatibility profile. Therefore if you wish to target new OpenGL features on macOS then you should ensure that you request a Core profile context via :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setProfile`.

Qt provides classes for all version and Core and Compatibility profile combinations. The classes for OpenGL versions 3.1 through to 4.3 are:

* QOpenGLFunctions_3_1

* QOpenGLFunctions_3_2_Core

* QOpenGLFunctions_3_2_Compatibility

* QOpenGLFunctions_3_3_Core

* QOpenGLFunctions_3_3_Compatibility

* QOpenGLFunctions_4_0_Core

* QOpenGLFunctions_4_0_Compatibility

* :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFunctions_4_1_Core`

* QOpenGLFunctions_4_1_Compatibility

* QOpenGLFunctions_4_2_Core

* QOpenGLFunctions_4_2_Compatibility

* QOpenGLFunctions_4_3_Core

* QOpenGLFunctions_4_3_Compatibility

where each class inherits from :sip:ref:`~PyQt6.QtOpenGL.QAbstractOpenGLFunctions`.

A pointer to an object of the class corresponding to the version and profile of OpenGL in use can be obtained from :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVersionFunctionsFactory.get`. If obtained in this way, note that the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ retains ownership of the object. This is so that the instance can be cached and shared.

Before calling any of the exposed OpenGL functions you must ensure that the object has resolved the function pointers to the OpenGL functions. This only needs to be done once per instance with . Once initialized, the object can be used to call any OpenGL function for the corresponding version and profile. Note that  can fail in some circumstances so check the return value. Situations in which initialization can fail are if you have a functions object for a version or profile that contains functions that are not part of the context being used to resolve the function pointers.

If you exclusively use function objects then you will get compile time errors if you attempt to use a function not included in that version and profile. This is obviously a lot easier to debug than undefined behavior at run time.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVersionFunctionsFactory.get`.

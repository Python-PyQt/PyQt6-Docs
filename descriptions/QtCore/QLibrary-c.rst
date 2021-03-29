.. sip:class-description::
    :status: todo
    :brief: Loads shared libraries at runtime
    :digest: 4b9c5d379f6d3137457725cfe7261be7

The :sip:ref:`~PyQt6.QtCore.QLibrary` class loads shared libraries at runtime.

An instance of a :sip:ref:`~PyQt6.QtCore.QLibrary` object operates on a single shared object file (which we call a "library", but is also known as a "DLL"). A :sip:ref:`~PyQt6.QtCore.QLibrary` provides access to the functionality in the library in a platform independent way. You can either pass a file name in the constructor, or set it explicitly with :sip:ref:`~PyQt6.QtCore.QLibrary.setFileName`. When loading the library, :sip:ref:`~PyQt6.QtCore.QLibrary` searches in all the system-specific library locations (e.g. ``LD_LIBRARY_PATH`` on Unix), unless the file name has an absolute path.

If the file name is an absolute path then an attempt is made to load this path first. If the file cannot be found, :sip:ref:`~PyQt6.QtCore.QLibrary` tries the name with different platform-specific file prefixes, like "lib" on Unix and Mac, and suffixes, like ".so" on Unix, ".dylib" on the Mac, or ".dll" on Windows.

If the file path is not absolute then :sip:ref:`~PyQt6.QtCore.QLibrary` modifies the search order to try the system-specific prefixes and suffixes first, followed by the file path specified.

This makes it possible to specify shared libraries that are only identified by their basename (i.e. without their suffix), so the same code will work on different operating systems yet still minimise the number of attempts to find the library.

The most important functions are :sip:ref:`~PyQt6.QtCore.QLibrary.load` to dynamically load the library file, :sip:ref:`~PyQt6.QtCore.QLibrary.isLoaded` to check whether loading was successful, and :sip:ref:`~PyQt6.QtCore.QLibrary.resolve` to resolve a symbol in the library. The :sip:ref:`~PyQt6.QtCore.QLibrary.resolve` function implicitly tries to load the library if it has not been loaded yet. Multiple instances of :sip:ref:`~PyQt6.QtCore.QLibrary` can be used to access the same physical library. Once loaded, libraries remain in memory until the application terminates. You can attempt to unload a library using :sip:ref:`~PyQt6.QtCore.QLibrary.unload`, but if other instances of :sip:ref:`~PyQt6.QtCore.QLibrary` are using the same library, the call will fail, and unloading will only happen when every instance has called :sip:ref:`~PyQt6.QtCore.QLibrary.unload`.

A typical use of :sip:ref:`~PyQt6.QtCore.QLibrary` is to resolve an exported symbol in a library, and to call the C function that this symbol represents. This is called "explicit linking" in contrast to "implicit linking", which is done by the link step in the build process when linking an executable against a library.

The following code snippet loads a library, resolves the symbol "mysymbol", and calls the function if everything succeeded. If something goes wrong, e.g. the library file does not exist or the symbol is not defined, the function pointer will be ``nullptr`` and won't be called.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_plugin_qlibrary.py
    :lines: 54-58

The symbol must be exported as a C function from the library for :sip:ref:`~PyQt6.QtCore.QLibrary.resolve` to work. This means that the function must be wrapped in an ``extern "C"`` block if the library is compiled with a C++ compiler. On Windows, this also requires the use of a ``dllexport`` macro; see :sip:ref:`~PyQt6.QtCore.QLibrary.resolve` for the details of how this is done. For convenience, there is a static :sip:ref:`~PyQt6.QtCore.QLibrary.resolve` function which you can use if you just want to call a function in a library without explicitly loading the library first:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_plugin_qlibrary.py
    :lines: 63-67

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPluginLoader`.

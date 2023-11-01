.. sip:method-description::
    :status: todo
    :pysig: dd431a34e6382be8567cf5b44f2db6a6
    :realsig: (const QString&)
    :digest: 5b71e90a7a9805110c0a44023eac3790

Returns ``true`` if *fileName* has a valid suffix for a loadable library; otherwise returns ``false``.

+---------------+----------------------------------+
| Platform      | Valid suffixes                   |
+===============+==================================+
| Windows       | ``.dll``, ``.DLL``               |
+---------------+----------------------------------+
| Unix/Linux    | ``.so``                          |
+---------------+----------------------------------+
| AIX           | ``.a``                           |
+---------------+----------------------------------+
| HP-UX         | ``.sl``, ``.so`` (HP-UXi)        |
+---------------+----------------------------------+
| macOS and iOS | ``.dylib``, ``.bundle``, ``.so`` |
+---------------+----------------------------------+

Trailing versioning numbers on Unix are ignored.

.. sip:enum-description::
    :status: todo
    :digest: fabe65ade8061c30842bd94fdf965a0b

This enum describes the different levels of hinting that can be applied to glyphs to improve legibility on displays where it might be warranted by the density of pixels.

Please note that this enum only describes a preference, as the full range of hinting levels are not supported on all of Qt's supported platforms. The following table details the effect of a given hinting preference on a selected set of target platforms.

+-------------------------------------------------------------------------------+--------------------------+------------------+--------------------------+--------------+
+===============================================================================+==========================+==================+==========================+==============+
| Windows Vista (w/o Platform Update) and earlier                               | Full hinting             | Full hinting     | Full hinting             | Full hinting |
+-------------------------------------------------------------------------------+--------------------------+------------------+--------------------------+--------------+
| Windows 7 and Windows Vista (w/Platform Update) and DirectWrite enabled in Qt | Full hinting             | Vertical hinting | Vertical hinting         | Full hinting |
+-------------------------------------------------------------------------------+--------------------------+------------------+--------------------------+--------------+
| FreeType                                                                      | Operating System setting | No hinting       | Vertical hinting (light) | Full hinting |
+-------------------------------------------------------------------------------+--------------------------+------------------+--------------------------+--------------+
| Cocoa on macOS                                                                | No hinting               | No hinting       | No hinting               | No hinting   |
+-------------------------------------------------------------------------------+--------------------------+------------------+--------------------------+--------------+

**Note:** Please be aware that altering the hinting preference on Windows is available through the DirectWrite font engine. This is available on Windows Vista after installing the platform update, and on Windows 7. In order to use this extension, configure Qt using -directwrite. The target application will then depend on the availability of DirectWrite on the target system.

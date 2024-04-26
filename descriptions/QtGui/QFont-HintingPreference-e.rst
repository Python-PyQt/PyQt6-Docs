.. sip:enum-description::
    :status: todo
    :digest: ab898495acc0a1a40a9cb3478546aa2a

This enum describes the different levels of hinting that can be applied to glyphs to improve legibility on displays where it might be warranted by the density of pixels.

Please note that this enum only describes a preference, as the full range of hinting levels are not supported on all of Qt's supported platforms. The following table details the effect of a given hinting preference on a selected set of target platforms.

+---------------------------------------+--------------------------+------------------+--------------------------+-------------------+
|                                       | PreferDefaultHinting     | PreferNoHinting  | PreferVerticalHinting    | PreferFullHinting |
+=======================================+==========================+==================+==========================+===================+
| Windows and DirectWrite enabled in Qt | Full hinting             | Vertical hinting | Vertical hinting         | Full hinting      |
+---------------------------------------+--------------------------+------------------+--------------------------+-------------------+
| FreeType                              | Operating System setting | No hinting       | Vertical hinting (light) | Full hinting      |
+---------------------------------------+--------------------------+------------------+--------------------------+-------------------+
| Cocoa on macOS                        | No hinting               | No hinting       | No hinting               | No hinting        |
+---------------------------------------+--------------------------+------------------+--------------------------+-------------------+

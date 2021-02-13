.. sip:enum-member-description::
    :status: todo
    :value: 0x1000
    :digest: 0205c651ea22a36c6f3a24de7a09b6e8

Sometimes, a font will apply complex rules to a set of characters in order to display them correctly. In some writing systems, such as Brahmic scripts, this is required in order for the text to be legible, but in e.g. Latin script, it is merely a cosmetic feature. The  flag will disable all such features when they are not required, which will improve performance in most cases (since Qt 5.10).

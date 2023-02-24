terminalApps = [
    "/usr/bin/konsole -e",
    "/usr/bin/tilix -x"
    "/usr/bin/alacritty -e",
    "/usr/bin/kitty -e"
    "/usr/bin/kgx --",
    "/usr/bin/gnome-terminal --",
    "/usr/bin/xfce4-terminal -x",
    "/usr/bin/lxterminal -e",
    "/usr/bin/mate-terminal --",
    "/usr/bin/qterminal -e"
    "/usr/bin/xterm -e"
]

itemsTitles = [
    "Audio Players",
    "Browsers",
    "Communications",
    "Development Tools",
    "Email",
    "Image Processing and Editing",
    "Image Viewers and Managers",
    "Math",
    "Miscellaneous System Tools",
    "Office",
    "PDF Viewers",
    "Personal Finance",
    "Personal Security",
    "Text Editors",
    "Torrent Clients",
    "Video Players"
]

itemsTitles_Icons = [
    "audio-headphones",
    "internet-amarok",
    "audio-input-microphone",
    "code-context",
    "mail-unread",
    "edit-image",
    "folder-picture",
    "math0",
    "tools",
    "document-multiple",
    "documentation",
    "format-currency",
    "lock",
    "text-field",
    "download",
    "videoclip-amarok"
]

itemsContents = [
    ["Audacious", "Elisa", "Lollypop", "Rhythymbox", "Strawberry"],
    ["Chromium", "Falkon", "Firefox", "Konqueror", "Tor Browser Launcher", "Vivaldi"],
    ["Hexchat", "Konversation", "Pidgin", "Polari", "Telegram Desktop", "Telepathy KDE"],
    ["Visual Studio Code", "Geany", "GNOME Builder", "IntelliJ IDEA Community", "KDevelop", "NetBeans", "PyCharm Community", "QT Creator"],
    ["Evolution", "Geary", "KMail", "Kube", "Sylpheed", "Thunderbird"],
    ["darktable", "GIMP", "Inkscape", "KolourPaint", "Krita", "Photoflare", "Pinta", "RawTherapee"],
    ["digiKam", "Eye of GNOME", "Geeqie", "GNOME Photos", "gThumb", "Gwenview", "Rapid Photo Downloader", "Ristretto", "Shotwell"],
    ["Geogebra", "GNOME Calculator", "Kalgebra", "KCalc", "Octave", "Sagemath"],
    ["Baobab", "Catfish", "Filelight", "Flatpak", "GNOME Boxes", "GParted", "KRename", "KDE Partition Manager"],
    ["Calligra", "Gnumeric", "LibreOffice (fresh)", "LibreOffice (still)"],
    ["Atril", "Evince", "Okular", "Xreader"],
    ["GnuCash", "HomeBank", "KMyMoney", "Skrooge"],
    ["Bitwarden", "Firewalld", "Gufw", "KeePassXC", "KWalletManager", "Seahorse"],
    ["FeatherPad", "Gedit", "Kate", "Leafpad", "Mousepad", "Pluma", "xed"],
    ["Deluge (GTK)", "KTorrent", "qBittorrent", "Transmission (GTK)", "Transmission (Qt)"],
    ["Baka Mplayer", "Celluloid", "Haruna", "Kaffeine", "SMPlayer", "Totem", "VLC"]
]

itemsContents_PackageNames = [
    ["audacious", "elisa", "lollypop", "rhythymbox", "strawberry"],
    ["chromium", "falkon", "firefox", "konqueror", "torbrowser-launcher", "vivaldi"],
    ["hexchat", "konversation", "pidgin", "polari", "telegram-desktop", "telepathy-kde-meta"],
    ["code", "geany", "gnome-builder", "intellij-idea-community-edition", "kdevelop", "netbeans", "pycharm-community-edition", "qtcreator"],
    ["evolution", "geary", "kmail", "kube", "sylpheed", "thunderbird"],
    ["darktable", "gimp", "inkscape", "kolourpaint", "krita", "photoflare", "pinta", "rawtherapee"],
    ["digikam", "eog", "geeqie", "gnome-photos", "gthumb", "gwenview", "rapid-photo-downloader", "ristretto", "shotwell"],
    ["geogebra", "gnome-calculator", "kalgebra", "kcalc", "octave", "sagemath"],
    ["baobab", "catfish", "filelight", "flatpak", "gnome-boxes", "gparted", "krename", "partitionmanager"],
    ["calligra", "gnumeric", "libreoffice-fresh", "libreoffice-still"],
    ["atril", "evince", "okular", "xreader"],
    ["gnucash", "homebank", "kmymoney", "skrooge"],
    ["bitwarden", "firewalld", "gufw", "keepassxc", "kwalletmanager", "seahorse"],
    ["featherpad", "gedit", "kate", "leafpad", "mousepad", "pluma", "xed"],
    ["deluge-gtk", "ktorrent", "qbittorrent", "transmission-gtk", "transmission-qt"],
    ["baka-mplayer", "celluloid", "haruna", "kaffeine", "smplayer", "totem", "vlc"]
]

itemsContents_PackageDescriptions = [
    [
        "Lightweight, advanced audio player focused on audio quality",
        "Simple and elegant music player from the KDE project",
        "A modern music player from the GNOME project",
        "Music playback and management application",
        "A music player aimed at audio enthusiasts and music collectors"
    ], [
        "Web browser developed by Google, the open source project behind Google Chrome",
        "Web browser based on QtWebEngine, written in Qt framework",
        "Extensible browser from Mozilla based on Gecko with fast rendering",
        "Web browser based on Qt toolkit and Qt WebEngine",
        "Securely and easily download, verify, install, and launch Tor Browser",
        "An advanced browser made with the power user in mind"
    ], [
        "A popular and easy to use graphical IRC (chat) client",
        "Qt-based IRC client by the KDE project",
        "Multi-protocol instant messaging client with audio support",
        "Simple IRC client by the GNOME project",
        "Official Telegram Desktop client",
        "Instant messaging client using the Telepathy framework"
    ], [
        "Visual Studio Code is a cross-platform, open-source text editor supporting many languages",
        "Small and lightweight IDE with many supported many programming and markup languages",
        "Tool to write and contribute to GNOME-based applications",
        "IDE for Java, Groovy and other programming languages",
        "Feature-full, plugin extensible IDE for C/C++ and other programming languages",
        "IDE for developing with Java, JavaScript, PHP, Python, C/C++, and other languages",
        "Python IDE with support for code analysis, debugging and unit testing",
        "Lightweight, cross-platform C++ integrated development environment with a focus on Qt"
    ], [
        "Mature and feature-rich e-mail client that is part of the GNOME project",
        "Simple desktop mail client built in Vala",
        "Mature and feature-rich email client from the KDE project",
        "Modern communication and collaboration client built with QtQuick",
        "Lightweight and user-friendly GTK email client",
        "Feature-rich email client from Mozilla written in GTK"
    ], [
        "Advanced photography workflow and RAW development application",
        "GNU Image Manipulation Program",
        "Professional vector graphics editor",
        "A simple paint program from the KDE project",
        "Digital painting and image editing software form the KDE project",
        "Simple but powerful image editor originally inspired by PhotoFiltre",
        "Simple drawing and editing program modeled after Paint.NET",
        "A powerful cross-platform raw image processing program"
    ], [
        "An advanced digital photo management application fromt he KDE project",
        "Image viewing and cataloging program from the GNOME project",
        "Lightweight image viewer and manager",
        "A tool to access, organize, and share your photos from the GNOME project",
        "Image viewer and browser from the GNOME project",
        "Fast and easy to use image viewer from the KDE project",
        "Download photos and videos from cameras, memory cards and portable storage devices",
        "Fast and lightweight image viewer from the Xfce project",
        "A digital photo organizer designed for the GNOME desktop environment"
    ], [
        "Dynamic mathematics software with interactive graphics, algebra and spreadsheet",
        "Scientific calculator from the GNOME project",
        "Graphing Calculator from the KDE project",
        "Scientific calculator from the KDE project",
        "A high-level language, primarily intended for numerical computations",
        "Open Source Mathematics Software, alternative to Magma, Maple, Mathematica, and Matlab"
    ], [
        "Disk usage analyzer from the GNOME project",
        "Versatile file searching tool from the XFCE proejct",
        "Disk usage analyzer that creates a map to visualise disk usage",
        "Flatpak is a technology for building and distributing desktop applications",
        "An easy to use virtualization client from the GNOME project",
        "Partition editor for graphically managing your disk partitions",
        "A powerful batch file renamer from the KDE project",
        "A graphical partition manager from the KDE project"
    ], [
        "A set of office applications for productivity and creative usage",
        "Spreadsheet program from the GNOME project",
        "A free and powerful office suite, built with the latest features",
        "A free and powerful office suite, built from the stable maintenance branch"
    ], [
        "Simple multi-page document viewer from the MATE project",
        "A document viewer for multiple document formats from the GNOME project",
        "Multi-platform, fast and feature-rich universal document viewer",
        "A simple document viewer from the X-Apps Project"
    ], [
        "Personal and small-business financial-accounting application",
        "Easy to use finance manager that can analyse your personal finance in detail",
        "Personal finance manager for KDE which operates similarly to MS Money or Quicken",
        "Personal finance manager from the KDE project"
    ], [
        "Desktop client for the open-source password manager",
        "Flexible firewall with a built-in GUI",
        "Uncomplicated way to manage your Linux firewall",
        "Cross-platform community-driven port of Keepass password manager",
        "Application for managing encryption keys and passwords in the KDE Wallet",
        "Application for managing encryption keys and passwords in the GNOME Keyring"
    ], [
        "Minimal plain text editor with support for tabs, printing and syntax highlighting",
        "GTK editor with many features from the GNOME project",
        "Advanced, fully-featured text editor from the KDE project",
        "Simple plain text editor for GTK+ 3",
        "A fast and simple text editor from the Xfce project",
        "Powerful text editor from the MATE project",
        "A small and lightweight text editor from the X-Apps Project"
    ], [
        "User-friendly BitTorrent client written in Python using GTK",
        "Feature-rich BitTorrent client for KDE",
        "An advanced BitTorrent client programmed in C++",
        "Simple and easy-to-use BitTorrent client, GTK version",
        "Simple and easy-to-use BitTorrent client, Qt version"
    ], [
        "A free and open source, cross-platform, libmpv based multimedia player",
        "Simple GTK+ frontend for mpv",
        "Open source media player built with Qt/QML and libmpv",
        "Very versatile media player from the KDE project",
        "Media player with built-in codecs that can play virtually all video and audio formats",
        "Media player (audio and video) from the GNOME project",
        "Middleweight video player with support for a wide variety of audio and video formats"
    ]
]
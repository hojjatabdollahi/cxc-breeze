# Third-party content

Everything else in this repo is (c) the repo author and licensed GPL-3.0-or-later, see `LICENSE`.

| What | Where | From | License |
|---|---|---|---|
| Colors | the `*.Builder` configs under `config/cosmic` | KDE's `BreezeLight.colors` and `BreezeDark.colors` from [plasma/breeze](https://invent.kde.org/plasma/breeze), and Plasma's accent swatches | LGPL-2.0-or-later |
| Breeze and Breeze Dark icons | `data/icons/*.breeze.icons` and `*.breeze-dark.icons` | [frameworks/breeze-icons](https://invent.kde.org/frameworks/breeze-icons) 5.115, as packaged in Ubuntu's `breeze-icon-theme` 4:5.115.0-0ubuntu3 | LGPL-3.0, see `LICENSES/breeze-icons.LGPL.txt`. Symlinks were resolved, `icon-theme.cache` removed, Breeze Dark was merged on top of Breeze so it does not depend on a system theme, and `tools/alias-icons.py` adds copies under the names the COSMIC applets use. |
| Breeze cursors | `data/icons/*.breeze.cursors` (Breeze Dark, the black cursors) and `*.breeze-dark.cursors` (Breeze Light, the white cursors) | `cursors/` in [plasma/breeze](https://invent.kde.org/plasma/breeze), Plasma 6 builds with the `cursors_scalable` SVGs, by Ken Vermette and the KDE VDG | LGPL-3.0-or-later, see `cursors/Breeze/COPYING-ICONS` upstream and Debian's copyright file for breeze. Same text as above. Symlinks were resolved. |
| Hack font | `data/fonts/*.fonts.hack` | [source-foundry/Hack](https://github.com/source-foundry/Hack) v3 | MIT and Bitstream Vera, see `LICENSES/Hack.MIT-Bitstream-Vera.md` |
| Hanabi wallpaper | `data/cosmic/breeze/wallpapers/hanabi.png` and `data/cosmic/breeze-dark/wallpapers/hanabi-dark.png` | Plasma's default wallpaper "Next" by Krystian Zajdel, `wallpapers/Next/contents/images/5120x2880.png` and `images_dark/5120x2880.png` in plasma/breeze | CC-BY-SA-4.0, see `LICENSES/Hanabi-wallpaper.CC-BY-SA-4.0.txt` |

Noto Sans is not bundled. Most distros ship it.

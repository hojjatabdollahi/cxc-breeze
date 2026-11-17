# Third-party content

Everything not listed here is © the repository authors, GPL-3.0-or-later (see `LICENSE`).

| What | Where in the bundle | Origin | License |
|---|---|---|---|
| Colours | `config/cosmic/…breeze.Builder`, `…breeze-dark.Builder` | Values from KDE's `BreezeLight.colors` and `BreezeDark.colors` ([plasma/breeze](https://invent.kde.org/plasma/breeze)) and Plasma's accent swatches | LGPL-2.0-or-later (source schemes) |
| Breeze and Breeze Dark icon themes | `data/icons/…breeze.icons`, `…breeze-dark.icons` | [frameworks/breeze-icons](https://invent.kde.org/frameworks/breeze-icons) 5.115 (Ubuntu `breeze-icon-theme` 4:5.115.0-0ubuntu3) | LGPL-3.0, text in `LICENSES/breeze-icons.LGPL.txt`. Modified: symlinks resolved, `icon-theme.cache` removed, and Breeze Dark merged over Breeze so it no longer inherits from a system theme. |
| Breeze cursors | `data/icons/…breeze.cursors` (Breeze Dark cursors, the black ones), `…breeze-dark.cursors` (Breeze Light cursors, the white ones) | [plasma/breeze](https://invent.kde.org/plasma/breeze) `cursors/`, Plasma 6 builds with the `cursors_scalable` SVGs, by Ken Vermette and the KDE VDG | LGPL-3.0-or-later per `cursors/Breeze/COPYING-ICONS` and Debian's copyright file for breeze; same text as above. Modified: symlinks resolved. |
| Hack font | `data/fonts/…fonts.hack` | [source-foundry/Hack](https://github.com/source-foundry/Hack) v3 | MIT + Bitstream Vera, text in `LICENSES/Hack.MIT-Bitstream-Vera.md` |
| Hanabi wallpaper | `data/cosmic/breeze/wallpapers/hanabi.png`, `data/cosmic/breeze-dark/wallpapers/hanabi-dark.png` | Plasma's default wallpaper ("Next") by Krystian Zajdel, `plasma/breeze` `wallpapers/Next/contents/images/5120x2880.png` and `images_dark/5120x2880.png` | CC-BY-SA-4.0, text in `LICENSES/Hanabi-wallpaper.CC-BY-SA-4.0.txt` |

The UI font is Noto Sans, which is not bundled; it ships with most distributions.

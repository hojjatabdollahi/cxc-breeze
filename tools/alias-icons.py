#!/usr/bin/env python3
"""Copy Breeze's monochrome icons to the names COSMIC's applets and settings ask for.

Breeze keeps them under plain 22px names. The applets look up GNOME-style -symbolic
names and cosmic-applet-* names, and libcosmic checks the Cosmic theme before it
strips suffixes, so without these copies COSMIC's own icons show up instead.
Run it again after updating the icon themes.
"""
import shutil
from pathlib import Path

ALIASES = {
    "network-wireless-signal-excellent-symbolic": "status/22/network-wireless-signal-excellent.svg",
    "network-wireless-signal-good-symbolic": "status/22/network-wireless-signal-good.svg",
    "network-wireless-signal-ok-symbolic": "status/22/network-wireless-signal-ok.svg",
    "network-wireless-signal-weak-symbolic": "status/22/network-wireless-signal-weak.svg",
    "network-wireless-disconnected-symbolic": "status/22/network-wireless-disconnected.svg",
    "network-wireless-acquiring-symbolic": "status/22/network-wireless-acquiring.svg",
    "network-wireless-error-symbolic": "status/22/network-wireless-disconnected.svg",
    "network-wired-disconnected-symbolic": "status/22/network-wired-disconnected.svg",
    "network-vpn-symbolic": "devices/22/network-vpn.svg",
    "bluetooth-symbolic": "status/22/network-bluetooth.svg",
    "cosmic-applet-bluetooth-active-symbolic": "status/22/network-bluetooth-activated.svg",
    "cosmic-applet-bluetooth-disabled-symbolic": "status/22/network-bluetooth.svg",
    "cosmic-applet-notification-symbolic": "actions/22/notifications.svg",
    "cosmic-applet-notification-new-symbolic": "actions/22/notifications.svg",
    "cosmic-applet-notification-disabled-symbolic": "actions/22/notifications-disabled.svg",
    "cosmic-applet-battery-display-brightness-off-symbolic": "actions/22/brightness-low.svg",
    "cosmic-applet-battery-display-brightness-low-symbolic": "actions/22/brightness-low.svg",
    "cosmic-applet-battery-display-brightness-medium-symbolic": "actions/22/brightness-high.svg",
    "cosmic-applet-battery-display-brightness-high-symbolic": "actions/22/brightness-high.svg",
    "display-brightness-symbolic": "actions/22/brightness-high.svg",
    "keyboard-brightness-symbolic": "devices/22/input-keyboard.svg",
    "battery-symbolic": "status/22/battery-100.svg",
    # cosmic-settings nav bar and Desktop sub-pages
    "preferences-network-and-wireless-symbolic": "devices/22/network-wireless.svg",
    "video-display-symbolic": "places/22/user-desktop.svg",
    "preferences-desktop-display-symbolic": "devices/22/monitor.svg",
    "preferences-sound-symbolic": "status/22/audio-volume-high.svg",
    "preferences-power-and-battery-symbolic": "status/22/battery-100.svg",
    "preferences-input-devices-symbolic": "actions/22/dialog-input-devices.svg",
    "preferences-applications-symbolic": "actions/22/application-menu.svg",
    "preferences-time-and-language-symbolic": "actions/22/clock.svg",
    "system-users-symbolic": "actions/22/system-users.svg",
    "preferences-desktop-wallpaper-symbolic": "actions/22/viewimage.svg",
    "preferences-appearance-symbolic": "actions/22/draw-brush.svg",
    "preferences-desktop-theme-symbolic": "actions/22/draw-brush.svg",
    "preferences-window-management-symbolic": "actions/22/window-duplicate.svg",
    "preferences-workspaces-symbolic": "actions/22/virtual-desktops.svg",
    "preferences-wireless-symbolic": "devices/22/network-wireless.svg",
    "preferences-wired-symbolic": "devices/22/network-wired.svg",
    "preferences-vpn-symbolic": "devices/22/network-vpn.svg",
    "preferences-system-time-symbolic": "actions/22/clock.svg",
    "preferences-region-and-language-symbolic": "actions/22/languages.svg",
    # Names COSMIC's own theme defines that Breeze has under another name
    "navbar-open-symbolic": "actions/22/sidebar-collapse.svg",
    "navbar-closed-symbolic": "actions/22/sidebar-expand.svg",
    "application-x-executable-symbolic": "mimetypes/22/application-x-executable.svg",
    "display-symbolic": "devices/22/monitor.svg",
    "laptop-symbolic": "devices/22/computer-laptop.svg",
    "smartphone-symbolic": "devices/22/smartphone.svg",
    "tablet-symbolic": "devices/22/tablet.svg",
    "speaker-symbolic": "actions/22/speaker.svg",
    "audio-card-symbolic": "devices/22/audio-card.svg",
    "audio-headphones-symbolic": "devices/22/audio-headphones.svg",
    "audio-headset-symbolic": "devices/22/audio-headset.svg",
    "audio-volume-overamplified-symbolic": "status/22/audio-volume-high.svg",
    "uninterruptible-power-supply-symbolic": "devices/22/battery-ups.svg",
    "system-log-out-symbolic": "actions/22/system-log-out.svg",
    "system-reboot-symbolic": "actions/22/system-reboot.svg",
    "system-suspend-symbolic": "actions/22/system-suspend.svg",
    "airplane-mode-symbolic": "status/22/network-flightmode-on.svg",
    "airplane-mode-disabled-symbolic": "status/22/network-flightmode-off.svg",
    "connection-secure-symbolic": "status/22/security-high.svg",
    "notification-symbolic": "actions/22/notifications.svg",
    "notification-new-symbolic": "actions/22/notifications.svg",
    "notification-disabled-symbolic": "actions/22/notifications-disabled.svg",
    "pin-symbolic": "actions/22/pin.svg",
    "window-stack-symbolic": "actions/22/window-duplicate.svg",
    "window-swap-symbolic": "actions/22/exchange-positions.svg",
    "window-pop-out-symbolic": "actions/22/view-fullscreen.svg",
    # cosmic-viewer's drawing tools
    "insert-line-symbolic": "actions/22/draw-line.svg",
    "insert-ellipse-symbolic": "actions/22/draw-ellipse.svg",
    "insert-rectangle-symbolic": "actions/22/draw-rectangle.svg",
    "insert-polygon-symbolic": "actions/22/draw-polygon.svg",
    "insert-star-symbolic": "actions/22/draw-star.svg",
    "insert-arrow-symbolic": "actions/22/draw-arrow.svg",
    "insert-drawing-symbolic": "actions/22/draw-freehand.svg",
    "pencil-symbolic": "actions/22/document-edit.svg",
    "text-highlight-symbolic": "actions/22/draw-highlight.svg",
    "stroke-width-symbolic": "actions/22/format-stroke-color.svg",
    "view-fit-symbolic": "actions/22/zoom-fit-best.svg",
    "view-actual-size-symbolic": "actions/22/zoom-original.svg",
    "markup-symbolic": "actions/22/draw-brush.svg",
    "ratios-symbolic": "actions/22/ratiocrop.svg",
    # Nearest Breeze glyphs for the rest
    "application-default": "mimetypes/64/application-x-executable.svg",
    "web-browser": "actions/22/globe.svg",
    "web-browser-symbolic": "actions/22/globe.svg",
    "grip-lines-symbolic": "actions/22/handle-sort.svg",
    "software-update-available-symbolic": "status/22/update-high.svg",
    "preferences-default-applications-symbolic": "actions/22/kt-restore-defaults.svg",
    "preferences-startup-applications-symbolic": "actions/22/system-run.svg",
    "input-gaming-symbolic": "devices/22/input-gamepad.svg",
    "scanner-symbolic": "actions/22/document-scan.svg",
    "multimedia-equalizer-symbolic": "actions/22/view-media-equalizer.svg",
    "accessories-text-editor-symbolic": "actions/22/document-edit.svg",
    "text-x-generic-symbolic": "actions/22/edit-select-text.svg",
    "audio-x-generic-symbolic": "actions/22/view-media-track.svg",
    "video-x-generic-symbolic": "devices/22/camera-video.svg",
    "audio-card-usb-symbolic": "devices/22/audio-card.svg",
    "bluetooth-active-symbolic": "status/22/network-bluetooth-activated.svg",
    "bluetooth-disabled-symbolic": "status/22/network-bluetooth.svg",
    "application-menu-symbolic": "actions/22/application-menu.svg",
}
# Second names for the drawn icons in tools/icons.
DRAWN_ALIASES = {
    "applications-accessibility-symbolic": "preferences-desktop-accessibility-symbolic",
}
# The battery applet's steps, rounded to Breeze's tens. Breeze has no charge-limit variant.
for level in (0, 5, 10, 20, 35, 50, 65, 80, 90, 100):
    tens = f"{(level + 5) // 10 * 10:03}"
    for limited in ("", "-limited") if level < 90 else ("",):
        for charging in ("", "-charging"):
            ALIASES[f"cosmic-applet-battery-level-{level}{limited}{charging}-symbolic"] = f"status/22/battery-{tens}{charging}.svg"

for theme in sorted((Path(__file__).resolve().parent.parent / "data/icons").glob("*.icons")):
    for name, source in ALIASES.items():
        shutil.copyfile(theme / source, theme / "status/symbolic" / f"{name}.svg")
    # Monochrome versions drawn here for names Breeze only has coloured icons for.
    extra = list((Path(__file__).resolve().parent / "icons").glob("*.svg"))
    for icon in extra:
        shutil.copyfile(icon, theme / "status/symbolic" / icon.name)
    for name, drawn in DRAWN_ALIASES.items():
        shutil.copyfile(theme / "status/symbolic" / f"{drawn}.svg", theme / "status/symbolic" / f"{name}.svg")
    print(f"{theme.name}: {len(ALIASES)} aliases, {len(extra)} drawn")

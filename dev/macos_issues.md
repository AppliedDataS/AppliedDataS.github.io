
# turn off the startup chime
## macOS Ventura or later
 1. Choose Apple menu  > System Settings.
 2. Click Sound in the sidebar.
 3. Turn “Play sound on startup” on or off.
## macOS Monterey or macOS Big Sur
 1. Choose Apple menu  > System Preferences.
 2. Click Sound.
 3. In the Sound Effects pane, use the “Play sound on startup” setting to turn the startup sound on or off.
## On any version of macOS
On the terminal utility run the command
```
sudo nvram StartupMute=%01
```
>You need to have sudo rights, i.e. either you are an administrator or your user name is on the `/etc/sudoers` file.  
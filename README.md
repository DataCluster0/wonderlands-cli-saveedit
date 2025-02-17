# Wonderlands Port of BL3 Commandline Savegame/Profile Editor

This project is a commandline Python-based Borderlands 3 Savegame
and Profile Editor.  It's a companion to the very similar
[CLI editor for BL2/TPS](https://github.com/apocalyptech/borderlands2),
and provides some very similar functionality.  It can be used
to level up your characters, unlock Mayhem modes early in the
game, unlock TVHM, add SDUs, unlock equipment slots, and more.

This editor has only been tested on PC Savegames -- other platforms'
savegames are not supported at the moment.

Please keep the following in mind:

- This app does not have any graphical interface.  You must be
  on a commandline in order to use it.
- The app has only very limited item-editing capability at the
  moment, which is restricted to:
  - Item Levels can be changed
  - Mayhem Level can be set on items
- It does not offer any direct ability to alter Guardian Rank status.
- While I have not experienced any data loss with the app,
  **take backups of your savegames before using this**, and
  keep in mind that it could end up corrupting your saves.  If
  you do encounter any data loss problems, please contact me
  and I'll try to at least fix whatever bug caused it.

# Table of Contents

- [Wonderlands Port of BL3 Commandline Savegame/Profile Editor](#wonderlands-port-of-bl3-commandline-savegameprofile-editor)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
    - [Upgrading](#upgrading)
    - [Notes for People Using Windows](#notes-for-people-using-windows)
    - [Running from Github](#running-from-github)
    - [Finding Savegames](#finding-savegames)
- [Editor Usage](#editor-usage)
- [TODO](#todo)
- [Credits](#credits)
- [License](#license)
- [Other Utilities](#other-utilities)
- [Changelog](#changelog)

# Installation

This editor requires [Python 3](https://www.python.org/), and has been
tested on 3.7, 3.8, 3.9, and 3.10.  It also requires the [protobuf package](https://pypi.org/project/protobuf/).

The easiest way to install this app is via `pip`/`pip3`.  Once Python 3 is
installed, you should be able to run this to install the app:

    pip3 install bl3-cli-saveedit

Once installed, there should be a few new commandline utilities available
to you.  The main editor is `bl3-save-edit`, and you can see its possible
arguments with `-h`/`--help`:

    bl3-save-edit -h

There's also a `bl3-save-info` utility which just shows some information
about a specified savefile.  You can see its possible arguments with
`-h`/`--help` as well:

    bl3-save-info -h

If you've got a raw savegame protobuf file that you've hand-edited (or
otherwise processed) that you'd like to import into an existing savegame,
you can do that with `bl3-save-import-protobuf`:

    bl3-save-import-protobuf -h

Alternatively, if you've got a savegame exported as JSON that you'd like
to import into an existing savegame, you can do that with
`bl3-save-import-json`:

    bl3-save-import-json -h

Finally, there's a utility which I'd used to generate my
[BL3 Savegame Archive Page](http://apocalyptech.com/games/bl-saves/bl3.php).
This one won't be useful to anyone but me, but you can view its arguments
as well, if you like:

    bl3-process-archive-saves -h

There are also profile-specific versions of most of those commands, which
can be used to edit the main BL3 `profile.sav`:

    bl3-profile-edit -h
    bl3-profile-info -h
    bl3-profile-import-protobuf -h
    bl3-profile-import-json -h

### Upgrading

When a new version is available, you can update using `pip3` like so:

    pip3 install --upgrade bl3-cli-saveedit

You can check your current version by running any of the apps with the
`-V`/`--version` argument:

    bl3-save-info --version

### Notes for People Using Windows

This is a command-line utility, which means there's no graphical interface,
and you'll have to run it from either a Windows `cmd.exe` prompt, or presumably
running through PowerShell should work, too.  The first step is to
install Python:

- The recommended way is to [install Python from python.org](https://www.python.org/downloads/windows/).
  Grab what's available in the 3.x series (at time of writing, that's 3.9.4),
  and when it's installing, make sure to check the checkbox which says something
  like "add to PATH", so that you can run Python from the commandline directly.
- If you're on Windows 10, you can apparently just type `python3` into a command
  prompt to be taken to the Windows store, where you can install Python with
  just one click.  I've heard reports that this method does *not* provide the
  ability to add Python to your system PATH, though, so it's possible that
  running it would be more complicated.

When it's installed, test that you can run it from the commandline.  Open up
either `cmd.exe` or PowerShell, and make sure that you see something like this
when you run `python -V`:

    C:\> python -V
    Python 3.9.4

If that works, you can then run the `pip3 install bl3-cli-saveedit` command
as mentioned above, and use the commandline scripts to edit to your heart's
content.

### Running from Github

Alternatively, if you want to download or run the Github version of
the app: clone the repository and then install `protobuf` (you can
use `pip3 install -r requirements.txt` to do so, though a `pip3 install protobuf`
will also work just fine).

You can then run the scripts directly from the Github checkout, though
you'll have to use a slightly different syntax.  For instance, rather than
running `bl3-save-edit -h` to get help for the main savegame editor, you
would run:

    python -m bl3save.cli_edit -h

The equivalents for each of the commands are listed in their individual
README files, linked below.

### Finding Savegames

This app doesn't actually know *where* your savegames or profiles are located.
When you give it a filename, it'll expect that the file lives in your "current"
directory, unless the filename includes all its path information.  When launching
a `cmd.exe` on Windows, for instance, you'll probably start out in your home
directory (`C:\Users\username`), but your savegames will actually live in a
directory more like `C:\Users\username\My Documents\My Games\Borderlands 3\Saved\SaveGames\<numbers>\`.
The easiest way to run the utilities is to just use `cd` to go into the dir
where your saves are (or otherwise launch your commandline in the directory you
want).  Otherwise, you could copy the save into your main user dir (and then
copy back after editing), or even specify the full paths with the filenames.

# Editor Usage

For instructions on using the Savegame portions of the editor, see
[README-saves.md](https://github.com/apocalyptech/bl3-cli-saveedit/blob/master/README-saves.md).

FOr instructions on using the Profile portions of the editor, see
[README-profile.md](https://github.com/apocalyptech/bl3-cli-saveedit/blob/master/README-profile.md).

# TODO

- Would anyone appreciate an option to *delete* Fabricators?  Hm.
- Would be nice to have some anointment-setting functions in here.
- Did we want a function to *clear* Vault Card progress?
- PS4 Support (for already-unlocked saves, anyway)
- If we fail to read a savefile or profile, might be nice to *actually* check
  if it's the other of profile-or-savefile, and give a more helpful message in
  those cases.
- Something a bit more Enum-like for various things in `__init__.py`; I
  know that's not very Pythonic, but when dealing with extra-Python data
  formats, one must sometimes make exceptions.
- Unit tests?

# Credits

The encryption/decryption stanzas in `BL3Save.__init__` and `BL3Save.save_to`
were [helpfully provided by Gibbed](https://twitter.com/gibbed/status/1246863435868049410?s=19)
(rick 'at' gibbed 'dot' us), so many thanks for that!  The protobuf definitions
are also provided by Gibbed, from his
[Borderlands3Protos](https://github.com/gibbed/Borderlands3Protos) repo,
and used with permission.  Gibbed also kindly provided the exact hashing
mechanism used to work with weapon skins and trinkets.

The rest of the savegame format was gleaned from 13xforever/Ilya's
`gvas-converter` project: https://github.com/13xforever/gvas-converter

Many thanks also to Baysix, who endured an awful lot of basic questions about
pulling apart item serial numbers.  Without their help, we wouldn't have
item level editing (or nice item names in the output)!

Basically what I'm saying is that anything remotely "hard" in here is all thanks
to lots of other folks.  I'm just pasting together all their stuff.  Thanks, all!

# License

All code in this project is licensed under the
[zlib/libpng license](https://opensource.org/licenses/Zlib).  A copy is
provided in [COPYING.txt](COPYING.txt).

# Other Utilities

Various BL3 Savegame/Profile editors have been popping up, ever since Gibbed
released the encryption details.  Here's a few which could be more to your
liking, if you didn't want to use this one for whatever reason:

- [FromDarkHell's BL3 Save/Profile Editor](https://github.com/FromDarkHell/BL3SaveEditor) -
  Written in C#, has EXE downloads for ease of use on Windows.
- [Zak's Borderlands 3 Saver Editor](https://github.com/ZakisM/bl3_save_edit) - Written
  in Rust, and is cross-platform.  Edits both saves and profiles.
- [Raptor's Editor](https://bl3.swiss.dev/) - This is a web-fronted editor,
  though it uses a [local executable](https://github.com/cfi2017/bl3-save/releases)
  to do all the work.  Sourcecode is available, and it works on Windows, Mac,
  and Linux.  Coded in [Go](https://golang.org/).
- [HackerSmaker's CSave Editor](https://github.com/HackerSmacker/CSave) - Cross-platform
  commandline editor written in C.  Has a terminal (ncurses) UI on UNIX-like OSes.

A couple others exist but as of July 2021, are out of date and not really great
for use on newer saves.  Here they are, though, in case they get updated without
me noticing:

- [sandsmark's borderlands3-save-editor](https://github.com/sandsmark/borderlands3-save-editor) -
  Written in C++ with Qt for GUI.  Is still in development.  Native downloads
  for Windows, but should compile fine on other platforms.

In Memoriam: Baysix, the author of the original web-based editor at bl3editor.com,
passed away in early 2021, and that editor is now permanently offline.  RIP!

# Changelog

**v1.0.0**
 - Broken Port to Wonderlands (json works)
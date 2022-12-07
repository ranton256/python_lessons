
Introduction to Linux
=====================

What is Linux?
--------------

Linux is an open source operating system similar to Unix based around the Linux kernel originally created by Linus Torvalds.  Linux is available in many different distributions, which are basically different flavors of the system put together by different groups.  Many of the other parts of a typical Linux distribution besides the kernel are provided by or at least use the same license as the GNU project.  GNU is a recursive(refers to itself) acronym for "GNU's Not Unix".

Users and Logging In
--------------------

On Linux each user has a separate account, and users must login before using the system, whether accessing it locally or remotely. This is typically done using a username and password.  There are other options for authenticating to the system, especially over SSH, but for now let's keep it simple.

The shell
---------

In Linux (and Unix) commands to tell the system what to do are entered through a shell.  Which shell you use is configurable, but the most common shell today is [Bash](http://www.gnu.org/software/bash/) from GNU, which stands for Bourne again shell. It is an expanded version of the Bourne shell, thus "Bourne again".

Inside bash or a similar shell, you will have a prompt which is where you enter your commands; in other words it prompts you for your command to input.

The first commands we are going to learn are actually commands for getting help. A command can be followed by options and arguments as part of the command line. Hitting the return key at the end of the line causes the command to run when you are finished typing it. As long as you have not pressed return yet you can move around with the arrow keys or use backspace to correct any mistakes in your command.

Try these commands out at the prompt.

```bash
 ls -l
 echo "Hello"
```

Your Home Directory
-------------------

Each user in Linux has a home directory. A directory is like a folder in a graphical operating system. It's just part of the hierarchy or tree of files and directories(folders) which can hold files or other directories.  Usually your home directory will be located at `/home/yourusername` where yourusername will be whatever your login username is.  Also, a path is just a way of specifying a location for a file or directory in the `file system` which is just a way of referring to all the files and things on the computer (more or less).

Ownership and Permissions
-------------------------

In Linux (and Unix) files and directories have owners, groups, and permissions.  The permissions control who can see that the files exist, read or access the files, and who can modify the files.  The permissions system also controls which files or directories are executable. If a file is executable it means you can run it (or try) as a program.  If you have execute permissions for a directory it means you are allowed to navigate inside that directory.

Working Directory
-----------------

In Linux you have what is called a current directory or working directory.  This is where you are in a kind of way.  You can refer to files inside the current directory without using their entire path.

You change directories with the `cd` command (change directory). With no arguments it will take you to your home directory or given a path it will take you to that directory.  The special value `..` refers to the parent of the current directory. So `cd ..` takes you one directory higher in the tree of directories.  The command `pwd` tells you what your current directory is (it stands for print working directory).

Some Basic Commands
-------------------

### Listing Files

The `ls` command is used for listing files.  If you want more information try `ls -l` and to make sure you see everything try `ls -Fal`.

### Making Directories

You can make a new directory with the `mkdir` command.

```bash
 mkdir stuff
 mkdir junk
```

You can remove a directory as long as it's empty with `rmdir`.

```bash
 rmdir junk
```

Why don't you try changing to the stuff directory now? Try these commands:

```bash
 cd stuff
 pwd
 ls
 touch something
 ls -l
```

What happened?

A Brief Diversion
-----------------

Type this into your prompt, the little marks are backticks and depending on your keyboard are probably the key to the left of the number 1.

```bash
 cowsay `fortune -s`
```

The fortune command outputs a random saying, some wise, some absurd.  Adding the "-s" just makes it choose a short saying.  The backticks around a command let you send its output on the command line as arguments to another command. In this case that command is `cowsay` which does just what it sounds like.

Getting Help
------------

There are a lot of ways to get some help when you don't know or can't remember how to do something.  Try these out:

```bash
 man man
 info bash
 ls --help
 man -k files
```

Moving Files
------------

If you want to rename or relocate a file or directory, you use the `mv` command. But pay attention, because it can do different things depending on what kind of argument you give it.  

* `mv oldname newname` - As long as `newname` does not already exist, this command will rename the file oldname to newname, BUT if newname exists and is a directory, it will move oldname inside newname where it will still be named oldname. This is true including when oldname is actually a directory itself.

* `mv somefile somedir` - Again, if somedir is a directory it will move somefile into somedir, as in `somefile/somedir`.

Copying Files
-------------

Copying files is done with the `cp` command. Just like `mv` it takes an old name and a new name, and just like `mv` it acts differently if the destination is an existing directory, by putting the destination inside of it instead of using it as a new name.

```bash
 cp oldname newname
 cp myfile newdir
```

Deleting Files
--------------

You can delete a file with the **rm** command. Be sure to use caution with rm. It also takes additional options that allow you to do things like delete all files and directories recursively under a directory.

```bash
 touch killme
 ls
 rm killme
 ls
```

Viewing Files
-------------

You can view the contents of a text file by using the cat, more, or less commands. The > and >> symbols in the example below redirect command output to a file. You'll learn more about those later.

```bash
 echo "Line1" > some.txt
 echo "Line2" >> some.txt
 cat some.txt
 more some.txt
 less some.txt
```

You can also send the output of one command into another command, like more using a pipe, by using the `|` symbol.  Try this out:

 ls --help | less

It's a lot easier to use that way than when it flies off the screen isn't it?  Also note that depending on your terminal setup you can usually use the mouse wheel or Shift + PageUP to view things that already scrolled off the screen.

Editing Files
-------------

Of course sometimes you want to edit a file, not just jam things onto the end of it.  A good editor for text files for beginners is **nano**. It has simple commands and shows the most basic ones at the bottom of the screen to help you. Control key + 'o' saves and Control key + 'x' exits(quits) the program.

```bash
 nano some.txt
```

Check Your Spelling
-------------------

The aspell command for Linux lets you spell check words. Run this command then type in words spelled correctly or otherwise.

```bash
 aspell -a
```

If the word is spelled correctly, aspell will print an asterisk; otherwise it will suggest words you may have meant.

When you are finished, hold down the Control key and press 'D'.

You can interactively spell check and correct an entire text file with the `-c` option.

```bash
 echo "The quick broun fox jumped over the fince." > myfile.txt
 aspell -c myfile.txt
```

Wrap up
-------

That is probably enough for our first lesson. Feel free to explore the shell and commands on your own

<!-- TODO: add all appropriate copyrights. -->

More Information
----------------

* <http://www.linuxfoundation.org/what-is-linux>
* <http://www.gnu.org/>
* <http://www.unixtutorial.org/basic-unix-commands/>

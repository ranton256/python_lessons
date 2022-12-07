<!-- CONTEXT:
title: Computer Concepts
-->

Why Learn to Program?
=====================

Computers are becoming more and more pervasive and powerful.  Microcontrollers
which are basically miniature computers are present in more and more everyday
things from microwaves to automobiles. 

Programming is fun! You get immediate feedback when you get something new
working.  This is why when I was a kid learning to program I loved working on
graphics, and why as an adult I find it rewarding to work on user interfaces.

Learning to program also gives you a deeper understanding of how computer work
and builds skills that are useful when using complicated software for other
purposes as well, not just writing it.

Programming and developing software also requires a very different type of
thought than many other things which makes it an interesting mental exercise.
It is closest to mathematics just by being quite abstract in a similar way,
but at the same time, most programming is still very different than math.

Computer Concepts
=================

It's time to learn some basics about how computer hardware works to
help you understand how to develop programs for them.

Memory
------

Every computer has memory which it uses to store information. Computers store
information as groups of ones or zeroes which form binary numbers. Binary is a
number system similar to the decimal system, but instead of being base 10 as
in decimal numbers, binary numbers are base 2.  That means that when they add
to more than 1, you have to carry. It also means that the value of each digits
place is twice the value of the place to its right, instead of ten times as
much.

There are two basic types of computer memory, RAM and ROM.  

RAM stands for random access memory, and this type of memory is temporary and
changeable.  RAM can be written to and read from repeatedly. The values are
temporary and only last until they are overwritten or power is turned off and
all the values are lost.  Also the random access part refers to the ability to
retrieve values from any position in the RAM at will as opposed to some other
computer storage methods, like magnetic disks for example, which require
seeking to the correct place.

ROM stands for read only memory.  This type of memory can be read from in a
way similar to RAM, but it has two important differences.  It keeps its
contents when power is turned off, and it cannot be written to except
initially.  Actually, this is not entirely true of some type of ROM which can
be programmed(written) repeatedly, but it is a special, slow process still
very different from that in RAM.

Processors
----------

The part of the computer responsible for executing instructions from programs
and making decisions and processing data is called the CPU which stands for
central processing unit.  In modern computers the CPU is a single
microprocessor chip.  Earlier computers had CPU's made of many discreet
components instead of just a single chip.  Today, many devices have
microcontrollers in them which contain a microprocessor as well as built-in
input/output peripherals, which we will discuss shortly.  

The CPU, sometimes just called the processor, handles executing all the
machine code instructions that make up a program. Each instruction tells the
CPU to do a certain operation with certain operands.  For example, an
instruction might tell the CPU to load a value from a specific location in
memory, and the next instruction might add that value to another.

These days computers have processors with multiple cores, which means they are
basically multiple CPU's in the same physical package.

Input and Output
----------------

In order to be of any use, a computer must be able to input and output data.
What is data?f Data is a collection of values or variables. Data has a similar
but slightly different meaning than information.  The difference is that
information is something a person could consume or use to make a decision.
Data is the raw values that must be processed, aggregated, or grouped to
actually turn it into information.  For example, all of the answers everyone
in the United States provided during the most recent census would be data, but
the statistics calculated from them such as the average household income would
be information.

Common types of computer input/output peripherals include keyboards, mice,
monitors, printers, wired or wireless network connections, sound hardware for 
recording or playback, and storage devices such as magnetic, optical or flash
disks.  We will talk about storage separately in a moment.  Many peripherals
are connected over special buses such as USB, which stands for universal
serial bus. USB is used for connecting devices such as keyboards, mice, portable
storage devices, phones, cameras, printers and digital headphones.  Computer
interface standards(buses) include other standards such as firewire (IEEE
1394), and SATA (serial ATA). There are also several standards for connecting
monitors and displays such as DVI, HDMI, and DisplayPort.

Network adapters such as wired Ethernet adapters or wireless WiFi
adapters are another important type of peripheral.  These allow connection to
local are networks (LANs) for sharing data with nearby computers as well as
allowing computers to collect to the Internet over broadband connections or
dedicated Internet connections typically found at businesses and universities.

Storage
-------

Storage devices, which technically include the memory we already discussed
also include slower types used for more permanent storage that can store
greater amounts of data.  Memory is known as primary storage.  Secondary
storage devices are not accessible directly by the CPU, but must be accessed
via input/output channels.  

The most common type of secondary storage for computers is the hard disk
drive.  Hard disks have rapidly rotating metal platters where tiny areas are
magnetized to record the bits stored.  Flash drives have more in common with
ROM chips than hard disks. They are much faster than hard disks, but they have
limitations on the number of time that they can be written to that limit their
service life, whereas a hard disk drive will fail eventually, but eventually
can often be a very long time with no fixed bound.

Optical discs provide another type of storage. CD-ROM's, DVD's and BluRay
discs are all types of optical discs. The mechanisms are part of the drive,
but the media where the data is stored is removable. This type of storage is
very permanent provided it is not physically damaged, but it is significantly
slower to wrote than magnetic storage.  Many types of optical discs can also 
only be written once.


Data Units
----------

We should define some units used for describing sizes of storage or data.
* One bit is a single binary digit.
* Eight bits form a byte.

Additionally, processors typically have a native size known as a word which is
basically the amount of memory that can be retrieved in one memory access
operation and stored in one register inside the CPU.  In typical modern
computers this is either 32 or 64 bits.

* 1024 bytes is a kilobytes. This value comes from 2^10, 2 raised to the 10th power,
in other words this is ten number 2's multiplied together. It is the largest
number you can hold with 10 binary digits plus one.
* 1024 * 1024 or 1048576 bytes or 2^20 is a megabyte.
* 1024 * 1024 * 1024 or 1073741824 or 2^30 is a gigabyte.

Sometimes people use megabyte to mean 1,000,000 bytes and gigabyte to mean
1,000,000,000 bytes. This is usually because they are selling hard drives.

* 1024 bits is a kilobit
* 1024 * 1024 is a megabit
* 1024 * 1024 * 1024 is a gigabit

Units such as kilobits and megabits are typically used when describing network
bandwidth speeds.


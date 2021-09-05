# be-mayhem
So you want to do multi-platform asm development and cannot stand GNU make(1) ?
## How it works
In your main .asm file, the first line and only the first line should start with `;MHM`. This makes it liable to be parsed by be-mayhem
### Be-Mayhem line syntax
- `;MHM` - signified a be-mayhem command line and *MUST* be the first line in your .asm file
- assembler - choose one from the list
- file extension - cannot be blank
- list of options - keep in mind that -L is *ALWAYS* on
### Be-Mayhem command line options
optional arguments:
  `-h`, `--help`            show this help message and exit
  `-i` INPUTDIR, `--inputdir` INPUTDIR
                        top-level directory to scan for asm
### Prerequisites
- Python3
- vasm suite in `$PATH`
## The rest - FAQ
### But is it secure?
It has not been extensively security-tested - recommendations for improvement on the security stance, more than welcome!
### How can I contribute?
Open issue or fork and make PR. Standard CoC applies.
### But this is not nearly as mature as ...
I know, I know ...
### LICENSE
Why, GPL of course!

# a-zsh-a-day

Do you like the **ZSH sheel**? Yes, you - and everybody - do.

Do you like the **Oh My ZSH**? Yes, you - and everyone - do.

![Alt text](https://i.ibb.co/JjtFD0b/ohmyzsh-themes.gif)

There're hundred of different [themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes) to choose. One is better than other. You can use a fantastic theme with **Oh My ZSH**.

But, but... Have you ever thought about use a different theme a day? Every day is a different theme. You will never get sick of your theme, because tomorrow you will use a new one -- **AUTOMATICALLY**.

## How does it works?
`zsh-day` uses the [Anacron job scheduler](https://en.wikipedia.org/wiki/anacron) to executes the `zsh-day` which edits the `~/.zshrc` file, which contains the theme definition. So, every day the `zsh-day` runs and changes the theme's name.

Annnd...**Voilà**. Every day your shell will look another shell. Don't you like the theme of day? Don't worry about it. Tomorrow it will look better... I hope :sweat_smile:

## Installation
- Take a look if `anacron` is installed. If it isn't, install it with your package manager. Probably your **UNIX** system already has the `anacron` installed. If your system - I know about `TinyCore` and `Slitaz` - doesn't have the *anacron* available, you can use the `cron` with some limitations. To do it, see the Wiki.
- Clone this repository in your home directory:
```bash
git clone https://github.com/danielventurini/a-zsh-a-day/
cd a-zsh-a-day/
```
- Install it (the executable is called `zsh-day`):
```bash
make
make install    # try with super
```

## Use
*Anacron* executes `zsh-day` automatically, but you can execute with useful arguments. Type `zsh-day --help` and take a look.

If you run `zsh-day` without arguments, it will change to next theme.

## Oh My ZSH similar
The *Oh My ZSH* has a [similar configuration](https://github.com/ohmyzsh/ohmyzsh#selecting-a-theme) that allows your terminal change to a random theme each time you open a terminal. I don't like it. I prefer to use a theme by a hole day and change it the other day. But, for you know, and if you prefer, *Oh My ZSH* has its own function to change to a random theme.

## Uninstall
```bash
make remove     # try with super
```

# Anki Flashcards

This directory contains sample project for building Anki vocabulary flashcards.

## Initial setup

- install Docker
- install Visual Studio Code
- copy contents of this directory to your workspace
- initialize your git repository and install LFS if you want to use binary files in your flashcards

Open workspace directory in Visual Studio Code, reopen in dev container.

Press `Ctrl+Shift+B` to start the build.

If everything is set up correctly, docker image with build tools should be automatically downloaded
from DockerHub and your build should run.

## Importing flashcards to Anki

Install [Anki](https://apps.ankiweb.net/#download) and build the project.

If project has built successfully, you will find your `*.apkg` file in the `./dist` directory.
The name of the output file can be changed in `jdp-apkg.toml`, the output directory can be changed in `Taskfile.yml`.

In Anki, go to menu `File -> Import` and import the `*.apkg` file that you have built.
Anki will show you a summary of what data has been imported to the deck.
It will also import note type and templates used for this note type, according to the definition in your `jdp-apkg.toml` file.

After import, you can start learning your deck and synchronize it to anki web, from where it can be synchronized to your mobile device.

## Working with the project

TODO

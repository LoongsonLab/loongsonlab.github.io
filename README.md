# Website for the Loongson Lab

Deployed at https://loongsonlab.github.io/.

The setup is modified from https://cmudig.github.io. Thanks to `Data Interaction Group at CMU`.

## Run

Install Jekyll dependencies with `bundle`. To start this page, run `bundle exec jekyll serve --livereload`.

## Run with Docker

```
docker run \
  --rm
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 -p 35729:35729 \
  -it jekyll/jekyll \
  jekyll serve --livereload
```

## Add Content

To add specific content, follow the README guides in the corresponding directories:

* [Add a person](_people)
* [Add a publication](_publications)
* [Add a post](_posts)
* [Add a course](_courses)
* [Add a research area](_research)

!!! warning
    Also, this is a multi-language website. So you will need to create Markdown files for each language.
    If you only have the energy to maintain one language, then please **DO NOT** create "another language" file.
    The site will redirect other languages pages to the maintained language pages automatically.

## General Header

```md
layout: default (Please not modified)
permalink: /
lang: zh/en (Language)
construct: true (Page under construction, optional)
info: (Information bar, optional)
  - ...
  - ...
warning: (Warning bar, optional)
  - ...
  - ...
```
